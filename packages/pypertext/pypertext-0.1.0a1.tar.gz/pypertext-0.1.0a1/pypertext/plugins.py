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

__all__ = ["pm", "hookimpl"]

import typing as t
import importlib
import pluggy
from pypertext import hookspecs

DEFAULT_PLUGINS: t.Tuple[str] = (
    "pypertext.processors.markdown",
    "pypertext.processors.dataframe",
    "pypertext.processors.matplotlib",
)

pm = pluggy.PluginManager("pypertext")
pm.add_hookspecs(hookspecs)

hookimpl = pluggy.HookimplMarker("pypertext")

# Load default plugins
for plugin in DEFAULT_PLUGINS:
    mod = importlib.import_module(plugin)
    pm.register(mod, plugin)
