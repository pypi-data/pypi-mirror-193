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
"""FastAPI endpoints for HTMX trigger API."""
import logging
import typing as t
import json
import inspect
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pypertext.utils import flatten
from pypertext import config

log = logging.getLogger(__name__)


class TriggerAPI:
    """FastAPI endpoints for HTMX trigger API.

    The Element class (and elsewhere) has to register functions with the
    TriggerAPI class. The FastAPI app is then configured to use the endpoints.

    This class should be instantiated while the FastAPI app is being created.
    """

    endpoints = {}
    """A dictionary of functions to be used as FastAPI endpoints."""
    api_path: str = config.trigger_api_path
    """The path to use for the FastAPI endpoints."""
    response_triggers: t.List[str] = []
    """A list of trigger events to be sent to the client in HX-Trigger header."""

    def __init__(self, app: FastAPI) -> None:
        self.app = app
        self.configure_app()
        self.in_htmx_request_ctx: bool = False

    def get_endpoint(self, name: str) -> t.Callable:
        """Get an endpoint by name."""
        if name in self.endpoints:
            return self.endpoints.get(name)
        else:
            raise ValueError(f"Endpoint {name} does not exist.")

    async def trigger_api_endpoint(self, name: str, request: Request) -> HTMLResponse:
        """The FastAPI endpoint for HTMX trigger API.

        Receives a POST request from the client with the name of the endpoint
        to call. The function attached to the endpoint is called and the
        response is returned to the client.

        - Send a 404 response if the endpoint function does not exist.
        - Send a 204 response if the endpoint function returns None.
        - Send a 500 response if the endpoint function raises an exception.
        - Send a 200 response if the endpoint function returns a string or an
            Element object. Element objects are rendered to HTML before being
            sent to the client.
        - Sends a HX-Trigger header with a JSON object containing the trigger
            events. Trigger events are cleared before calling the endpoint 
            function, allowing the function to add new trigger events using
            `TriggerAPI.add_triggers()`. Trigger events are cleared after the
            response is sent to the client.

        Args:
            name (str): The name of the endpoint to call. This is passed as a
                query parameter to the endpoint: `/api/trigger/?name=<name>`.
            request (Request): The FastAPI request object.
        
        Returns:
            (HTMLResponse): The response to send to the client.
        """
        log.debug(f"Triggering {name} FastAPI endpoint")

        if not self.has_endpoint(name):
            raise HTTPException(status_code=404, detail="Endpoint not found")

        status_code: int = 200
        headers: t.Mapping[str, str] = {}
        self.in_htmx_request_ctx = "hx-request" in request.headers

        try:
            endpoint_func = self.get_endpoint(name)

            # inspect the function signature and pass the request and form
            # data to the function if it accepts those arguments.
            sig = inspect.signature(endpoint_func).parameters
            kwargs = {}
            if "form_data" in sig:
                form_data = await request.form()
                kwargs["form_data"] = form_data
            if "form" in sig:
                form = await request.form()
                kwargs["form"] = form
            if "request" in sig:
                kwargs["request"] = request

            result = endpoint_func(**kwargs)

            if result is None:
                status_code = 204
        except Exception as e:
            log.exception(e)
            result = None
            status_code = 500

        log.debug(f"{name} triggers: {TriggerAPI.response_triggers}")
        if len(TriggerAPI.response_triggers) > 0:
            headers["HX-Trigger"] = json.dumps(
                {t: 1 for t in TriggerAPI.response_triggers}
            )

        # TODO: use plugins to process the output of an API endpoint before
        # returning it to the client.
        if hasattr(result, "is_element"):
            log.debug(f"Endpoint result is an Element. Rendering...")
            result = result.render()

        if isinstance(result, str):
            log.debug(f"Endpoint result is a string.")
            result = result.encode("utf-8")
            headers["Content-Type"] = "text/html; charset=utf-8"

        response = HTMLResponse(result, status_code=status_code, headers=headers)

        # empty the list of triggers and reset the htmx_request flag
        TriggerAPI.response_triggers = []
        self.in_htmx_request_ctx = False

        return response

    def configure_app(self):
        """Configure FastAPI to list all endpoints (`/api/trigger/list`)
        and to use the trigger API endpoint (`/api/trigger/?name=<name>`).
        """
        def _list_endpoints() -> JSONResponse:
            l = list(self.endpoints.keys())
            return JSONResponse(l)

        self.app.add_api_route(
            self.api_path + "list",
            _list_endpoints,
            methods=["GET"],
        )
        self.app.add_api_route(
            self.api_path,
            self.trigger_api_endpoint,
            methods=["POST"],
        )

    @classmethod
    def add_endpoint(cls, fn: t.Callable, name: t.Optional[str] = None):
        """Add function as an endpoint so it can be called with
        `/api/trigger/?name=<name>`.

        Args:
            fn (Callable): The function to add as an endpoint.
            name (str, optional): The name to use for the endpoint. Defaults to
                the function name.
        """
        name = name or fn.__name__
        cls.endpoints[name] = fn
        log.debug(f"Added {name} to endpoints.")

    @classmethod
    def has_endpoint(cls, fn: t.Union[str, t.Callable]) -> bool:
        """Check if a function is registered as a FastAPI endpoint."""
        name = fn.__name__ if callable(fn) else fn
        return name in cls.endpoints

    @classmethod
    def remove_endpoint(cls, fn: t.Union[str, t.Callable]):
        """Remove a trigger API endpoint from the FastAPI app.

        Args:
            app (FastAPI): The FastAPI app.
            fn (str or Callable): The function or name of the function to remove.
        """
        name = fn.__name__ if callable(fn) else fn
        if name in cls.endpoints:
            del cls.endpoints[name]

    @classmethod
    def add_triggers(cls, events: t.Union[str, t.List[str]]):
        """Add an event to the list of events to be triggered using the 
        HX-Trigger header.
        
        Args:
            events (str or list): The event or list of events to trigger.
        """
        if isinstance(events, str):
            events = [events]
        if callable(events):
            events = [events]
        for e in flatten(events):
            if callable(e):
                e = e.__name__
            if e not in cls.response_triggers:
                cls.response_triggers.append(e)
        log.debug(f"Setting trigger events: {cls.response_triggers}")
