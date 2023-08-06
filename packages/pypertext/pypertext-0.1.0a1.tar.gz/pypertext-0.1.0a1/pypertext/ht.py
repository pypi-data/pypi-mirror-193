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

import types
import typing as t
import os
from pypertext import utils
from pypertext.element import Element
from pypertext.common import get_current_app
from pypertext.trigger_api import TriggerAPI


class Div(Element):
    """A div tag."""

    tag = "div"


class Header(Element):
    """A header tag."""

    tag = "header"


class Nav(Element):
    """A nav tag."""

    tag = "nav"


class Dl(Element):
    """A dl tag."""

    tag = "dl"


class Dt(Element):
    """A dt tag."""

    tag = "dt"


class Dd(Element):
    """A dd tag."""

    tag = "dd"


class Pre(Element):
    """A pre tag."""

    tag = "pre"


class Strong(Element):
    """A strong tag."""

    tag = "strong"


class P(Element):
    """A p tag."""

    tag = "p"


class Hr(Element):
    """A hr tag."""

    tag = "hr"


class Span(Element):
    """A span tag."""

    tag = "span"


class H1(Element):
    """A h1 tag."""

    tag = "h1"


class H2(Element):
    """A h2 tag."""

    tag = "h1"


class H3(Element):
    """A h3 tag."""

    tag = "h3"


class Br(Element):
    """A br tag."""

    tag = "br"


class Code(Element):
    """A code tag."""

    tag = "code"


class Ul(Element):
    """A ul tag."""

    tag = "ul"


class Ol(Element):
    """A ol tag."""

    tag = "ol"


class Li(Element):
    """A li tag."""

    tag = "li"


class A(Element):
    """An anchor tag."""

    tag = "a"


class Label(Element):
    """An label tag."""

    tag = "label"


class Img(Element):
    """An img tag."""

    tag = "img"

    def __init__(self, src, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.attrs["src"] = src


class Script(Element):
    """A script tag."""

    tag = "script"

    def from_file(self, path: os.PathLike) -> None:
        """Loads the JS script from a file."""
        self.attrs["type"] = "text/javascript"
        with open(path, "r") as f:
            content = f.read()
            self.add(content)
        return self


class Style(Element):
    """A style tag."""

    tag = "style"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.attrs["type"] = kwargs.pop("type", "text/css")

    def from_file(self, path: os.PathLike) -> None:
        """Loads the CSS from a file."""
        with open(path, "r") as f:
            content = f.read()
            self.add(content)
        return self


class StylesheetLink(Element):
    """A link tag for a stylesheet.

    Args:
        url (str): url of the stylesheet
    """

    tag = "link"

    def __init__(self, url: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.attrs["rel"] = "stylesheet"
        self.attrs["href"] = url


class Table(Element):
    """A table tag."""

    tag = "table"


class RecordsTable(Element):
    """A table tag from list of dicts."""

    tag = "table"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._records: t.List[t.Dict[str, t.Any]] = []
        self.columns: t.List[str] = []
        self.column_names: t.Dict[str, str] = {}

    def from_records(
        self, records: t.List[dict], column_names: t.Dict[str, str] = {}
    ) -> "RecordsTable":
        """Create a table from a list of dicts.

        Args:
            records (list): list of dicts
            column_names (dict): dict mapping column names to display names. If not
                provided, the column names will be used as the display names.
        """
        self.columns = list(records[0].keys())
        self._records = records
        self.column_names.update(column_names)
        return self

    def set_columns(self, columns: t.List[str]) -> "RecordsTable":
        """Set the table columns.

        Args:
            columns (list): list of column names
        """
        self.columns = columns
        return self

    def rename(self, mapping: dict[str, str]) -> "RecordsTable":
        """Update the column name mapping dict."""
        self.column_names.update(mapping)
        return self

    def add_row(self, row: t.Dict[str, t.Any]) -> "RecordsTable":
        """Add a row to the records.

        Args:
            row (dict): dict with keys matching the column names
        """
        self._records.append(row)
        return self

    def preprocess(self):
        self.children = []
        # create thead
        row_th: t.List[Th] = []
        for h in self.columns:
            name = self.column_names.get(h, h)
            row_th.append(Th(name, scope="col"))
        thead = Thead(Tr(*row_th))
        # create tbody
        tbody = Tbody()
        for record in self._records:
            row_td: t.List[Td] = []
            for h in self.columns:
                row_td.append(Td(record[h]))
            tbody.append(Tr(*row_td))
        self.add(thead, tbody)


class Tr(Element):
    """A tr tag."""

    tag = "tr"


class Td(Element):
    """A td tag."""

    tag = "td"


class Th(Element):
    """A th tag."""

    tag = "th"


class Thead(Element):
    """A thead tag."""

    tag = "thead"


class Tbody(Element):
    """A tbody tag."""

    tag = "tbody"


class Tfoot(Element):
    """A tfoot tag."""

    tag = "tfoot"


class Text(Element):
    """A text node that can be added to a tag.

    Args:
        text (str): The text to add.
        escape (bool): Whether to escape the text. Defaults to True. Replaces
            &, <, >, and " with their HTML entities.
    """

    def __init__(self, text: str, escape: bool = True) -> None:
        super(Text, self).__init__()
        self.escape = escape
        if escape:
            self.text = utils.str_escape(text)
        else:
            self.text = text

    def preprocess(self) -> str:
        self.add(self.text)


class I(Element):
    """An i tag."""

    tag = "i"


class Button(Element):
    """A button tag."""

    tag = "button"


class Input(Element):
    """An input tag."""

    tag = "input"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs["type"] = kwargs.get("type", "text")
        if "name" not in self.attrs:
            raise ValueError("Input must have a name")


class TextArea(Element):
    """A textarea tag."""

    tag = "textarea"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "name" not in self.attrs:
            raise ValueError("Textarea must have a name")


class Select(Element):
    """A select tag."""

    tag = "select"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "name" not in self.attrs:
            raise ValueError("Selet must have a name")


class Checkbox(Element):
    """A checkbox tag."""

    tag = "checkbox"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "name" not in self.attrs:
            raise ValueError("Checkbox must have a name")


class Option(Element):
    """A option tag."""

    tag = "option"


class Main(Element):
    """A main tag."""

    tag = "main"


class Aside(Element):
    """A aside tag."""

    tag = "aside"


class Section(Element):
    """A section tag."""

    tag = "section"


class HXForm(Element):
    """A form tag that uses htmx to submit the form.

    This form can contain many inputs and prioritizes the submit request over
    all input requests. The form must have a submit button.

    Args:
        func (str or callable): The endpoint name. This is usually the name of
            the function that handles the form submission.
    """

    tag = "form"

    def __init__(
        self,
        fn: t.Union[str, t.Callable],
        *args,
        api_path: str = TriggerAPI.api_path,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        # Add the function as an endpoint if it is callable
        if utils.is_function(fn):
            current_app = get_current_app()
            if current_app is not None:
                current_app._trigger_api.add_endpoint(fn)
        name: str = fn.__name__ if callable(fn) else fn
        attrs: t.Dict[str, str] = {
            "method": "POST",
            "hx_post": f"{api_path}?name={name}",
            "hx_sync": "this:replace",
            "hx_swap": "none",
        }
        for k, v in attrs.items():
            if k not in self.attrs:
                self.attrs[k] = v


class IFrame(Element):
    """An iframe tag."""

    tag = "iframe"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        attrs = {
            "frameborder": "0",
            "scrolling": "no",
            "allow": "autoplay; camera; microphone; clipboard-read; clipboard-write;",
        }
        self.attrs.update(attrs)


__all__ = [
    name
    for name, thing in globals().items()
    if not (name.startswith("_") or isinstance(thing, types.ModuleType))
] + ["Element"]
del types
