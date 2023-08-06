# Copyright (c) Asif Rahman. (2021-2023)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""FastAPI application."""

import os
import types
import typing as t
import logging
import copy
import datetime
import json
import sqlite3
import cloudpickle
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from starlette_session import SessionMiddleware, ISessionBackend
import contextvars

from pypertext import config, ht, utils
from pypertext.trigger_api import TriggerAPI
from pypertext.plugins import pm
from pypertext.interface import Interface
from pypertext.common import (
    get_current_app,
    set_current_app,
)

logging.getLogger("uvicorn").setLevel(logging.WARNING)
logging.getLogger("multipart").setLevel(logging.WARNING)

log = logging.getLogger(__name__)

request_global = contextvars.ContextVar(
    "request_global", default=types.SimpleNamespace()
)
"""A context variable to store the current request object."""


def g():
    """Returns the current request object."""
    return request_global.get().request


class SqliteSessionBackend(ISessionBackend):
    """Session backend that uses SQLite to store session data.

    By default, this uses cloudpickle to serialize the session data, so any
    Python object can be stored in the session table as long as it can be pickled.
    This is useful for storing complex objects like numpy arrays.

    Warning:
        This is not a secure session backend if you use the default cloudpickle
        serializer. It is intended for use in data science/machine learning
        applications and mostly for prototyping. Users can store arbitrary data
        in the session, so it is not suitable for production use. Developers
        should be very careful with what types of objects they store in the
        session.

        Change the `session_serializer` config to `config.session_serializer = "json"` to
        use the json serializer instead. This will only allow for storing
        simple data types like strings, numbers, lists, and dictionaries and is
        much more secure.
    """

    def __init__(self):
        self.expire = config.session_expires
        self.db = sqlite3.connect(config.session_db_file)
        self.db.execute("PRAGMA journal_mode=WAL")
        # check if table exists, if not create it
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{config.session_table_name}';"
        )
        if cursor.fetchone() is None:
            cursor.execute(
                # store as blob to allow for pickling using cloudpickle
                f"CREATE TABLE {config.session_table_name} (key TEXT, value BLOB, exp timestamp)"
            )
            # set index on key
            cursor.execute(
                f"CREATE UNIQUE INDEX {config.session_table_name}_key ON {config.session_table_name} (key)"
            )
            self.db.commit()
        else:
            # clear expired sessions on server startup
            cursor.execute(
                f"DELETE FROM {config.session_table_name} WHERE exp < ?",
                (datetime.datetime.now(),),
            )
            self.db.commit()
        cursor.close()

    async def get(self, key: str, **kwargs: dict) -> t.Optional[dict]:
        log.debug("Session get: %s", key)
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT value FROM {config.session_table_name} WHERE key = ?", (key,)
        )
        result = cursor.fetchone()
        if result is None:
            return None
        if config.session_serializer == "json":
            return json.loads(result[0])
        else:
            return cloudpickle.loads(result[0])

    async def set(
        self, key: str, value: dict, exp: t.Optional[int] = None, **kwargs: dict
    ) -> t.Optional[str]:
        # rolling expiration time - a users current session is extended each time
        # they make a request
        exp = exp if exp is not None else self.expire
        expire = datetime.datetime.now() + datetime.timedelta(seconds=exp)
        log.debug("Session set: %s", key)
        cursor = self.db.cursor()
        if config.session_serializer == "json":
            serialized_data = json.dumps(value)
        else:
            serialized_data = cloudpickle.dumps(value)
        cursor.execute(
            # use "INSERT OR REPLACE" to allow for updating the expiration time
            # without having to delete the row first, this enables rolling expiration
            f"INSERT OR REPLACE INTO {config.session_table_name} (key, value, exp) VALUES (?, ?, ?)",
            (key, serialized_data, expire),
        )
        self.db.commit()
        return key

    async def delete(self, key: str, **kwargs: dict) -> t.Any:
        cursor = self.db.cursor()
        cursor.execute(f"DELETE FROM {config.session_table_name} WHERE key = ?", (key,))
        self.db.commit()


def component(data: t.Any, key: t.Optional[str] = None) -> t.Any:
    processors = pm.hook.register_processor_classes()
    if processors is not None:
        if len(processors) > 0:
            processors = list(utils.flatten(processors))
            for processor in processors:
                if processor.is_valid_type(data):
                    return processor(data=data, key=key).get_element()
    return data


class App(FastAPI):
    """Extension of the FastAPI application class with additional methods to
    render UI components and manage session state."""

    def __init__(self, **kwargs):
        # pass all keyword arguments to the FastAPI constructor
        super().__init__(**kwargs)
        self.interface = Interface()
        self._session_backend: SqliteSessionBackend = SqliteSessionBackend()
        self._trigger_api: t.Union[TriggerAPI, None] = None
        self._state_model = None
        self._custom_homepage: t.Union[t.Callable, None] = None

    @utils.decorator_with_options
    def custom_homepage(self, fn: t.Callable) -> t.Callable:
        """Replace the default homepage with a custom function."""
        self._custom_homepage = fn

    def set_state(self, *, state: t.Dict[str, t.Any] = None, **kwargs):
        """Sets the state of the application by updating the session data.

        Args:
            state (dict): A dictionary of state values.
        """
        q = state or {}
        q.update(kwargs)
        namespace = request_global.get()
        namespace.request.session.update(q)

    def get_state(
        self, key: t.Optional[str] = None, default: t.Optional[t.Any] = None
    ) -> t.Any:
        """Returns a deep copy of the data.

        Args:
            key (str): The key of the data to return. If None, returns all data.
            default (any): The default value to return if the key is not found.
        """
        namespace = request_global.get()
        if namespace is None or (not hasattr(namespace, "request")):
            return default
        if key is not None:
            return copy.deepcopy(namespace.request.session.get(key, default))
        return copy.deepcopy(namespace.request.session)

    def ui(self, component: t.Any, key: t.Optional[str] = None):
        """Add an Element or string to the UI.

        Args:
            component (Any): An Element or string to be rendered.
            key (str): A unique key for the component. If not provided, a random
                key will be generated.
        """
        self.interface.add_component(component, key=key)

    @staticmethod
    def create_app(
        *args,
        **kwargs,
    ) -> "App":
        """Creates the FastAPI application.
        
        Args:
            *args: Positional arguments to pass to the FastAPI constructor.
            **kwargs: Keyword arguments to pass to the FastAPI constructor.
        """
        app = App(
            *args,
            default_response_class=kwargs.pop("default_response_class", HTMLResponse),
            **kwargs,
        )
        # The session middleware reads/writes a signed cookie to the client and
        # calls the session backend to get/set the session data into request.session.
        # NOTE: the session backend creates SQLite database connection in separate
        # threads.
        app.add_middleware(
            SessionMiddleware,
            secret_key=os.urandom(32),
            cookie_name=config.cookie_name,
            backend_type="custom",
            max_age=config.session_expires,
            custom_session_backend=app._session_backend,
        )
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @app.middleware("http")
        async def init_requestvars(request: Request, call_next):
            """Sets the current request object in a context variable.
            Users can then access the current request object using `g()` outside
            of the view function.
            """
            initial_g = types.SimpleNamespace(request=request)
            request_global.set(initial_g)
            response = await call_next(request)
            return response

        app._trigger_api = TriggerAPI(app)

        def robots_txt() -> str:
            """Returns a robots.txt file."""
            return "User-agent: *\nDisallow: /"

        def clear_sessions() -> HTMLResponse:
            """Removed expired sessions from the database."""
            db = sqlite3.connect(config.session_db_file)
            cursor = db.cursor()
            cursor.execute(
                f"DELETE FROM {config.session_table_name} WHERE exp < ?",
                (datetime.datetime.now(),),
            )
            db.commit()
            cursor.close()
            db.close()

        def index() -> HTMLResponse:
            """Renders a page from a collection of blocks."""
            # User can override the homepage with a custom function.
            if app._custom_homepage is not None:
                doc = app._custom_homepage(app)
            else:
                doc = app.interface.homepage()
            return HTMLResponse(doc)

        # Add routes
        app.add_api_route(
            "/robots.txt",
            robots_txt,
            response_class=PlainTextResponse,
            methods=["GET"],
            include_in_schema=False,
        )
        app.add_api_route("/", index, methods=["GET"], include_in_schema=True)
        app.add_api_route(
            "/sessions/clear", clear_sessions, methods=["GET"], include_in_schema=True
        )

        return app

    def display_inline(self) -> None:
        """Displays the application inline in a Jupyter notebook."""
        try:
            from IPython.display import HTML, display  # type: ignore

            local_url = "http://{}:{}/".format(config.host, config.port)
            with ht.Div() as el:
                ht.IFrame(src=local_url, width=config.width, height=config.height)
            display(HTML(el.render()))
        except ImportError:
            log.debug("Could not import IPython.display. Inline display not available.")
            pass

    def trigger(self, event: str):
        """Trigger an event in the app.

        Args:
            event (str): The name of the event to trigger.
        """
        current_app = get_current_app()
        if current_app is not None:
            current_app._trigger_api.add_triggers(event)


def create_app(
    *args: t.Any,
    ui_components: t.Optional[t.Mapping[str, t.Any]] = None,
    **kwargs: t.Any,
) -> App:
    """Return an ASGI application. This is the entry point for the ASGI server.

    Args:
        *args: Positional arguments to pass to FastAPI
        ui_components: A dictionary of ui_components to add to the app.
        homepage: A function to use as the homepage. Must return an HTML string.
        **kwargs: Keyword arguments to pass to FastAPI

    Returns:
        (App): An ASGI application, instance of FastAPI.
    """
    current_app = get_current_app()
    if current_app is None:
        log.info("Creating FastAPI app")
        current_app = App.create_app(*args, ui_components=ui_components, **kwargs)
    else:
        log.info("Returning existing FastAPI app")
        current_app.interface.reset_components()
    set_current_app(current_app)
    return current_app


__all__ = [
    name
    for name, thing in globals().items()
    if not (name.startswith("_") or isinstance(thing, types.ModuleType))
]
