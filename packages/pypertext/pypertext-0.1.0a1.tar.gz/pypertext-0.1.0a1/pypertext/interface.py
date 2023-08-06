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

"""Interface with UI components."""

import typing as t
from collections import OrderedDict
from pydantic import BaseModel

from pypertext import config, ht, utils
from pypertext.element import render_document
from pypertext.common import resources
from pypertext.plugins import pm
from pypertext.processors.base import BaseProcessor


class Interface():
    """User interface."""
    def __init__(self, state_model: t.Optional[BaseModel]=None) -> None:
        self.ui_components: t.Mapping[str, t.Any] = OrderedDict()
        self.state_model = state_model
        self.stylesheet_file = resources / "pypertext.css"
        self.head = []

        # Register data processors. These are used to process data before it is
        # passed to the view function.
        self._processors: t.List[BaseProcessor] = []
        processors = pm.hook.register_processor_classes()
        if processors is not None:
            if len(processors) > 0:
                self._processors = list(utils.flatten(processors))

    def get_components(self) -> t.Mapping[str, t.Any]:
        """Returns the blocks of elements."""
        if self.ui_components is None:
            raise ValueError("This app does not have any UI components.")
        return list(self.ui_components.values())

    def reset_components(self):
        """Resets the blocks of elements."""
        self.ui_components = OrderedDict()

    def add_component(self, component: t.Any, key: t.Optional[str] = None) -> None:
        """Adds a component to the UI.

        Args:
            component (Any): An Element or string to be rendered.
            key (str): A unique key for the component. If not provided, a random
                key will be generated.
        """
        if key is None:
            key = utils.random_id()

        if self.ui_components is None:
            self.ui_components = OrderedDict()

        # Process the component with the registered processors.
        for processor in self._processors:
            if processor.is_valid_type(component):
                component = processor(data=component, key=key).get_element()
                break

        self.ui_components[key] = component

    def homepage(self) -> str:
        """Renders UI components into an HTML document.

        Returns:
            (str): The HTML document.
        """
        body = self.get_components()
        head = [ht.Style().from_file(self.stylesheet_file)] + self.head
        doc = render_document(body=body, head=head, body_class=config.body_class)
        return doc
