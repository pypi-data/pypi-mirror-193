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

"""Command line interface"""

import typer
from pathlib import Path
from pypertext import config

HEADER = """
 __       __   ___  __  ___  ___     ___ 
|__) \ / |__) |__  |__)  |  |__  \_/  |  
|     |  |    |___ |  \  |  |___ / \  |  

"""

cli = typer.Typer(add_completion=False)


@cli.command()
def start(
    file: Path,
    app: str = "app",
    open_browser: bool = False,
    reload: bool = True,
    host: str = config.host,
    port: int = config.port,
    workers: int = 1,
    log_level: str = "warning",
):
    """Start a Pypertext web server"""
    if file is not None:
        if not file.exists():
            typer.secho(f"File {file} does not exist", err=True, fg=typer.colors.RED)
            raise typer.Exit(1)

    typer.echo(HEADER)

    import sys
    import os
    from rich.console import Console
    from rich.table import Table
    import pypertext
    import inspect

    # check if address is already in use
    if not reload:  # only check if reload is disabled
        if pypertext.utils.is_address_in_use(host, port):
            typer.secho(
                f"Address {host}:{port} is already in use", err=True, fg=typer.colors.RED
            )
            # look for another port
            port = pypertext.utils.get_open_port(config.port, config.port + 100)
            typer.secho(f"Using port {port} instead", err=True, fg=typer.colors.YELLOW)

    # Watched directories
    file_dir = file.parent.absolute()
    pypertext_dir = Path(inspect.getfile(pypertext)).parent

    run_args = [
        sys.executable,
        "-m",
        "uvicorn",
        "--workers",
        str(workers),
        "--port",
        str(port),
        "--host",
        host,
        "--loop",
        "asyncio",
        "--lifespan",
        "on",
        "--log-level",
        log_level,
        "--reload-dir",
        f'"{file_dir}"',
        "--reload-dir",
        f'"{pypertext_dir}"',
    ]

    if reload:
        run_args.append("--reload")
        # Disable interactive mode of the reload flag is set. uvicorn monitors
        # files for changes and restarts the worker
        config.interactive = False

    # File to app path
    path = os.path.normpath(file)
    path = path.replace("/", ".")
    path = path.replace("\\", ".")
    filename = os.path.splitext(path)[0]

    # use path.module.app if we don't want a factory, otherwise use path.module
    # which calls the __call__ method and creates a new FastAPI instance
    app_path = f"{filename}:{app}"
    # run_args += ["--factory", app_path]  # app factory
    run_args += [app_path]  # app instance

    # Print startup info
    console = Console()
    table = Table("Name", "Setting", title="Server settings")
    table.add_row("Host", f"http://{host}:{port}")
    table.add_row("Workers", str(workers))
    table.add_row("Log Level", log_level)
    table.add_row("App", app_path)
    console.print(table)

    if open_browser:
        pypertext.utils.open_browser(f"http://{host}:{port}")

    # Run command
    cmd = " ".join(run_args)
    os.system(cmd)


if __name__ == "__main__":
    cli()
