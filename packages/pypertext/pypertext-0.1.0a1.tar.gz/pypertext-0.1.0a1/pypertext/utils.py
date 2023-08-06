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

"""Utility functions."""

import types
import typing as t
import sys
import os
import logging
import random
import string
import subprocess
import functools
import inspect

log = logging.getLogger(__name__)


def setup_logging(
    level: t.Union[str, int] = logging.INFO, logfile: t.Optional[os.PathLike] = None
):
    """Setup logging for the current process.

    Args:
        level (int): The logging level. Defaults to logging.INFO.
        logfile (str): The path to the log file. If None, the log will be
            printed to stdout only.
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper())
    handlers = [logging.StreamHandler()]
    if logfile:
        handlers.append(logging.FileHandler(logfile))
    logging.basicConfig(
        level=level,
        format="%(levelname)s|%(asctime)s|%(name)s|%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
    )


def get_fqn(the_type: type) -> str:
    """Get module.type_name for a given type."""
    return f"{the_type.__module__}.{the_type.__qualname__}"


def get_fqn_type(obj: object) -> str:
    """Get module.type_name for a given object."""
    return get_fqn(type(obj))


def is_type(obj, fqn_type_pattern):
    """Check if an object is of a given type."""
    return type(obj).__module__ + "." + type(obj).__name__ == fqn_type_pattern


def is_function(x: object):
    """Return True if x is a function."""
    return isinstance(x, types.FunctionType)


def is_method(obj: object) -> bool:
    """Check if `obj` is a method."""
    return inspect.ismethod(obj) or inspect.isfunction(obj)


def is_iterable(obj: object):
    try:
        iter(obj)  # type: ignore[call-overload]
    except TypeError:
        return False
    return True


def is_sequence(seq: t.Any) -> bool:
    """True if input looks like a sequence."""
    if isinstance(seq, str):
        return False
    try:
        len(seq)
    except Exception:
        return False
    return True


def decorator_with_options(dec_fun: t.Callable) -> t.Callable:
    """Makes it possible for function to be used with and without arguments"""

    @functools.wraps(dec_fun)
    def wrapper(*args, **kwargs):
        # Note: if the def_fun is a method, then args will contain the object the method is bound to.
        if args and inspect.isfunction(args[-1]):
            # The decorator is invoked with a function as its first argument
            # Call the decorator function directly
            return dec_fun(*args, **kwargs)
        else:
            # The function is called with arguments
            # bind those arguments to the function and decorate the next token
            # args is only nonempty if it's the object the method is bound to
            return functools.partial(dec_fun, *args, **kwargs)

    return wrapper


def is_executable_in_path(name):
    """Check if executable is in OS path."""
    from distutils.spawn import find_executable

    return find_executable(name) is not None


def random_id(k=8):
    """Generate a random ID of length k. The first character is always a letter."""
    a = random.choice(string.ascii_lowercase)
    return a + "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(k - 1)
    )


def str_escape(data: str, quote: bool = True) -> str:
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    if quote:
        data = data.replace('"', "&quot;")
    return data


def open_browser(url):
    """Open a web browser pointing to a given URL.

    We use this function instead of Python's `webbrowser` module because this
    way we can capture stdout/stderr to avoid polluting the terminal with the
    browser's messages. For example, Chrome always prints things like "Created
    new window in existing browser session".

    Args:
        url (str): The URL. Must include the protocol.
    """
    # Treat Windows separately because:
    # 1. /dev/null doesn't exist.
    # 2. subprocess.Popen(['start', url]) doesn't actually pop up the
    #    browser even though 'start url' works from the command prompt.
    # Fun!
    # Also, use webbrowser if we are on Linux and xdg-open is not installed.
    #
    # We don't use the webbrowser module on Linux and Mac because some browsers
    # (Chrome) always print "Opening in existing browser session" to
    # the terminal, which is spammy and annoying. So instead we start the
    # browser ourselves and send all its output to /dev/null.

    import platform

    _system = platform.system()
    IS_WINDOWS = _system == "Windows"
    IS_DARWIN = _system == "Darwin"
    IS_LINUX_OR_BSD = (_system == "Linux") or ("BSD" in _system)

    if IS_WINDOWS:
        _open_browser_with_webbrowser(url)
        return
    if IS_LINUX_OR_BSD:
        if is_executable_in_path("xdg-open"):
            _open_browser_with_command("xdg-open", url)
            return
        _open_browser_with_webbrowser(url)
        return
    if IS_DARWIN:
        _open_browser_with_command("open", url)
        return

    raise Exception('Cannot open browser in platform "%s"' % platform.system())


def _open_browser_with_webbrowser(url):
    import webbrowser

    webbrowser.open(url)


def _open_browser_with_command(command, url):
    cmd_line = [command, url]
    with open(os.devnull, "w") as devnull:
        subprocess.Popen(cmd_line, stdout=devnull, stderr=subprocess.STDOUT)


def in_repl():
    """Return True if running in the Python REPL."""
    import inspect

    root_frame = inspect.stack()[-1]
    filename = root_frame[1]  # 1 is the filename field in this tuple.

    if filename.endswith(os.path.join("bin", "ipython")):
        return True

    # <stdin> is what the basic Python REPL calls the root frame's
    # filename, and <string> is what iPython sometimes calls it.
    if filename in ("<stdin>", "<string>"):
        return True

    return False


def ipython_shell():
    """Same as `get_ipython` but returns `False` if not in IPython"""
    try:
        return get_ipython()  # type: ignore
    except NameError:
        return False


def in_ipython():
    """Check if code is running in some kind of IPython environment"""
    return bool(ipython_shell())


def in_colab():
    """Check if the code is running in Google Colaboratory"""
    return "google.colab" in sys.modules


def in_jupyter():
    """Check if the code is running in a jupyter notebook"""
    if not in_ipython():
        return False
    return ipython_shell().__class__.__name__ == "ZMQInteractiveShell"


def in_notebook():
    "Check if the code is running in a jupyter notebook"
    return in_colab() or in_jupyter()


IN_REPL, IN_IPYTHON, IN_JUPYTER, IN_COLAB, IN_NOTEBOOK = (
    in_repl(),
    in_ipython(),
    in_jupyter(),
    in_colab(),
    in_notebook(),
)

def is_address_in_use(host: str, port: int) -> bool:
    """Check if a port is already in use.

    Args:
        host (str): Host address.
        port (int): Port number.

    Returns:
        (bool): True if the port is in use, False otherwise.
    """
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host, port))
    except OSError:
        return True
    finally:
        sock.close()
    return False


def get_open_port(host: str, initial: int, final: int) -> int:
    """Gets the first open port in range.

    Args:
        host (str): host address
        initial (int): initial port
        final: final (exclusive) port

    Returns:
        port (int): the first open port in the range
    """
    import socket

    for port in range(initial, final):
        try:
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.close()
            return port
        except OSError:
            pass
    raise OSError(
        f"All ports from {initial} to {final-1} are in use. Please close a port."
    )


def flatten(x) -> t.Iterable:
    def iselement(e):
        return not (hasattr(e, "__iter__") and not isinstance(e, str))

    for el in x:
        if iselement(el):
            yield el
        else:
            yield from flatten(el)


__all__ = [
    name
    for name, thing in globals().items()
    if not (name.startswith("_") or isinstance(thing, types.ModuleType))
]
