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
import logging
from pypertext.processors.base import BaseProcessor
from pypertext.ht import Div
from pypertext.plugins import hookimpl

logging.getLogger("markdown_it").setLevel(logging.WARNING)


class MarkdownProcessor(BaseProcessor):
    """Processor for Markdown text.

    Renders a string of Markdown formatted text into an HTML div element.
    """

    md = None

    def get_md(self):
        from markdown_it import MarkdownIt

        if not self.md:
            self.md = MarkdownIt()
        return self.md

    @classmethod
    def is_valid_type(cls, data) -> bool:
        return isinstance(data, str)

    def get_element(self):
        md_html = self.get_md().render(self.data)
        return Div(md_html, id=self.key)


@hookimpl
def register_processor_classes():
    return MarkdownProcessor
