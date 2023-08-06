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
"""Contains common variables and functions used by multiple sub-modules."""
import os
import typing as t
from pathlib import Path
from dataclasses import dataclass
from importlib.resources import files

# Path to module resources folder
resources = files("pypertext") / "resources"

# Instance of FastAPI app
current_app = None

@dataclass
class Config:
    static_dir: os.PathLike = Path.cwd()
    """The directory where static files are stored. Defaults to the current 
    working directory where the script is being run."""
    static_dir_name: str = "static"
    """The name of the static directory to be used in URL paths."""
    stylesheets: t.Optional[t.List[str]] = None
    """Full path to stylesheets or paths relative to the static directory."""
    app_name: str = "Pypertext"
    """Name of the Pyper application. Defaults to Pypertext. This is used in the
    title of the web page. It can also be changed later with `Pyper.set_title`"""
    host: str = "127.0.0.1"
    """Host address to run the server on."""
    port: int = 8700
    """Port to run the server on."""
    interactive: bool = True
    """Interactive mode reloads connected clients when the script is modified."""
    log_level: str = "warning"
    """Logging level. Can be one of the following: debug, info, warning, error,
    critical."""
    workers: int = 1
    """Number of workers to use when running in production mode."""
    daemonize: bool = False
    """Whether to run the server in the background as a daemon."""
    reload: bool = False
    """Whether to reload the server if it already exists."""
    server_task_name: str = "PypertextServer"
    """Name of the server task in asyncio."""
    width: t.Union[str, int] = "100%"
    """Width of the UI in Jupyter Notebook."""
    height: t.Union[str, int] = "500"
    """Height of the UI in Jupyter Notebook."""
    body_class: t.Optional[str] = None
    """CSS class to apply to the body element."""
    session_db_file: os.PathLike = Path.cwd() / "pypertext_sessions.db"
    """Path to the SQLite database file used to store session data."""
    cookie_name: str = "pypertext_session"
    """Name of the cookie used to store the session ID."""
    session_table_name: str = "pypertext_sessions"
    """Name of the table used to store session data in the database."""
    session_expires: int = 60
    """Number of seconds before a session expires."""
    trigger_api_path: str = "/api/trigger/"
    """Path to the trigger API endpoint."""
    session_serializer: str = "cloudpickle" # json or cloudpickle
    """Serializer to use for session data. Can be either json or cloudpickle."""

config = Config()
"""Global configuration settings."""


def set_current_app(app):
    global current_app
    current_app = app

def get_current_app():
    """Returns the FastAPI application."""
    global current_app
    return current_app
