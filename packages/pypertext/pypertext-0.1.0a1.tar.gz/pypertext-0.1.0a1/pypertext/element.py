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

"""The Element class which is a base class for all HTML elements."""

__all__ = [
    "Element",
    "get_current_element_context",
    "render_element",
    "render_document",
    "elm",
]

import typing as t
import threading
import logging
import json
from numbers import Number
from collections import defaultdict, namedtuple
from pypertext.plugins import pm
from pypertext.trigger_api import TriggerAPI
from pypertext.common import get_current_app
from pypertext import utils

# Type definition for element attributes
AttrsLike = t.Dict[str, t.Union[str, Number, bool, t.Callable]]

log = logging.getLogger(__name__)

_HTMX_CDN_URL = "https://unpkg.com/htmx.org@1.8.4"


def _get_thread_context():
    context = [threading.current_thread()]
    return hash(tuple(context))


class Element:
    """Base class for all HTML elements.

    Element is a generic definition of an HTML element including attributes and
    children. This class is a container for the tag name, a dictionary of
    attributes, and a list of children.

    Classes that inheirt from `Element` can optionally define the `preprocess()`
    method which can modify the `attrs` and `children` attributes before being
    rendered.

    Args:
        *args: children
        **kwargs: attributes

    Attributes:
        tag (str): tag name of the element
        attributes (AttrsLike): dict of element attrs
        children (List[str|Element]): list of children elements
    """

    _frame = namedtuple("frame", ["element", "items", "used"])  # context manager
    _with_contexts = defaultdict(list)  # stack of frames
    is_element = True  # flag to identify elements using hasattr
    tag: str = "div"
    """The tag name of this element."""

    def __init__(self, *args, **kwargs) -> None:
        self.attrs: t.Dict[str, str] = {}
        """Dict of element attributes."""
        self.children: t.List[str | Element] = []
        """List of children elements."""
        self.parent = None
        # don't render this element if visible is False, default is True
        self.visible = True
        # add children and attrs
        if args:
            self.add(*args)
        self.attrs.update(kwargs)
        self._ctx = None
        self._add_to_ctx()

    def _add_to_ctx(self):
        """Add this element to the current context"""
        stack = Element._with_contexts.get(_get_thread_context())
        if stack:
            self._ctx = stack[-1]
            stack[-1].items.append(self)

    def __enter__(self):
        """Enter a context for this element"""
        stack = Element._with_contexts[_get_thread_context()]
        stack.append(Element._frame(element=self, items=[], used=set()))
        return self

    def __exit__(self, type, value, traceback):
        """Exit a context for this element"""
        thread_id = _get_thread_context()
        stack = Element._with_contexts[thread_id]
        frame = stack.pop()
        for item in frame.items:
            # skip used items
            if item in frame.used:
                continue
            # add to parent
            self.add(item)
            if not stack:
                if thread_id in Element._with_contexts:
                    del Element._with_contexts[thread_id]

    def add(self, *args):
        """Add children to this element.

        Args:
            *args: children elements
        """
        for obj in args:
            # None
            if obj is None:
                continue
            # Number
            if isinstance(obj, Number):
                obj = str(obj)
            # String
            if isinstance(obj, str):
                self.children.append(obj)
            # Element
            elif isinstance(obj, Element):
                stack = Element._with_contexts.get(_get_thread_context())
                if stack:
                    stack[-1].used.add(obj)
                self.children.append(obj)
                obj.parent = self
            # Renderable as an element-like object, e.g. Element, str, etc.
            elif hasattr(obj, "get_element"):
                log.debug("Adding %r as a child with get_element", obj)
                self.children.append(obj.get_element)
            # Iterable
            elif hasattr(obj, "__iter__"):
                for subobj in obj:
                    self.add(subobj)
            # Function or method
            elif callable(obj):
                # function is evaluated when rendered
                self.children.append(obj)
            # Unknown
            else:
                raise ValueError(
                    "%r not an Element or string. Failed to add type %s as a child."
                    % (obj, type(obj))
                )
        if len(args) == 1:
            return args[0]
        return args

    def append(self, *args):
        """Add children to this element.

        Args:
            *args: children elements
        """
        return self.add(*args)

    def __iadd__(self, other):
        """Add children to this element with += operator"""
        self.add(other)
        return self

    def __add__(self, other):
        """Add children to this element with + operator"""
        return self.add(other)

    def __iter__(self):
        """Iterate over the element children"""
        return self.children.__iter__()

    def set_attrs(self, **kwargs):
        """Set an attribute on this element"""
        self.attrs.update(kwargs)

    def print_tree(self, indent=0):
        """Print the tree of elements"""
        tag = "" + self.tag
        if "id" in self.attrs:
            tag += "#" + self.attrs["id"]
        for c in ["class_", "classes", "classname"]:
            if c in self.attrs:
                tag += "." + self.attrs[c].replace(" ", ".")
        print("  " * indent + tag)
        for child in self.children:
            if isinstance(child, Element):
                child.print_tree(indent + 1)
            else:
                print("  " * (indent + 1) + child)

    def htmx(
        self,
        fn: t.Union[str, t.Callable],
        event: t.Union[str, None] = None,
        from_selector: t.Union[str, None] = None,
        target: t.Union[str, None] = None,
        on_load: t.Optional[bool] = None,
        outer: t.Optional[bool] = None,
        inner: t.Optional[bool] = None,
        swap: str = "innerHTML",
        delay_seconds: t.Union[int, str, None] = None,
        throttle_seconds: t.Union[int, None] = None,
        poll_seconds: t.Union[int, None] = None,
        api_route: str = TriggerAPI.api_path,
    ) -> None:
        """Build htmx attributes for this element.

        This is provided as a convenience method for building htmx attributes
        but it is not required to use htmx. You can build the attributes yourself.

        Args:
            fn (Union[str, Callable]): function or name of function
                that will be called when the event is triggered
            event (Union[str, None], optional): event name. Defaults to None.
            from_selector (Union[str, None], optional): selector for the
                hx-trigger attribute. Defaults to None.
            target (Union[str, None], optional): selector for the hx-target
                attribute. Defaults to None.
            on_load (bool, optional): if True, set the hx-trigger attribute
                to "load". Defaults to None.
            outer (bool, optional): if True, set the hx-swap attribute to "outerHTML".
                Defaults to False.
            inner (bool, optional): if True, set the hx-swap attribute to "innerHTML".
                Defaults to False.
            swap (str, optional): value for the hx-swap attribute. Defaults to "none".
                If either `outer` or `inner` is True, then this value will be ignored.
            delay_seconds (Union[int, None], optional): seconds to delay the
                request after it's triggered. Defaults to None.
            throttle_seconds (Union[int, None], optional): seconds to throttle
                the request before making another request. Defaults to None.
            poll_seconds (Union[int, None], optional): poll the server every
                at this interval. Defaults to None.

        Examples:
        ```python
        from pypertext import Div, Button
        # Create a button that will call the `my_func` function when clicked
        btn1 = Button("Click me!").htmx("my_func", event="click")
        btn2 = Button("Click me!", hx_trigger="click from:body", hx_swap="none")
        # btn1 and btn2 are equivalent
        ```
        """
        if callable(fn):
            # Register the function as an endpoint: /api/trigger/<fn>
            # NOTE: we could have used `if not TriggerAPI.has_endpoint(fn)` to
            # check if the function is already registered, but this would not work
            # with interactive development environments like Jupyter Notebook
            # where the user modifies the function and then re-runs the cell.
            # So instead we just register the function every time.
            current_app = get_current_app()
            if current_app is not None:
                current_app._trigger_api.add_endpoint(fn)
        name = fn.__name__ if callable(fn) else fn
        hx_post = f"{api_route}?name={name}"
        hx_attrs = dict(
            hx_post=hx_post,
        )
        # create hx-trigger
        hx_trigger = []
        if event:
            _trigger = "" + event
            if ("from:" not in event) & (from_selector is not None):
                _trigger = _trigger + f" from:{from_selector}"
            if delay_seconds:
                _trigger = _trigger + f" delay:{delay_seconds}s"
            if throttle_seconds:
                _trigger = _trigger + f" throttle:{throttle_seconds}s"
            hx_trigger.append(_trigger)
        # polling
        if poll_seconds:
            hx_trigger.append(f"every {poll_seconds}s")
        # swap, does not swap element content with the response by default
        if outer is not None:
            if outer:
                hx_swap = "outerHTML"
        elif inner is not None:
            if inner:
                hx_swap = "innerHTML"
        else:
            hx_swap = swap
        if hx_swap:
            hx_attrs["hx_swap"] = hx_swap
        # target
        if target:
            hx_attrs["hx_target"] = target
        # build hx_trigger
        if len(hx_trigger) > 0:
            _hx_trigger = ", ".join(hx_trigger)
            hx_attrs["hx_trigger"] = _hx_trigger
        # on_load
        if on_load is not None:
            if on_load:
                hx_attrs["hx_trigger"] = ", ".join(
                    ["load", hx_attrs.get("hx_trigger", "")]
                )
        # use data- attributes as hx-vals
        hx_vals = {}
        for k, v in self.attrs.items():
            if k.startswith("data_"):
                n = k[5:]
                hx_vals[n] = v
        if len(hx_vals) > 0:
            hx_attrs["hx_vals"] = json.dumps(hx_vals)

        self.attrs.update(hx_attrs)

    def on_event(self, event: str, fn: t.Callable, **kwargs) -> "Element":
        """Call `fn` when `event` is triggered.

        Args:
            event (str): event name
            fn (t.Callable): function to call
            **kwargs: keyword arguments to pass to `htmx`

        Returns:
            (Element): self
        """
        self.htmx(
            fn,
            event=event,
            from_selector=kwargs.pop("from_selector", "body"),
            **kwargs,
        )
        return self

    def on_change(self, fn: t.Callable, **kwargs) -> "Element":
        """Call `fn` when the `keyup changed` event fires on the element.

        Args:
            fn (t.Callable): function to call
            **kwargs: keyword arguments to pass to `htmx`

        Returns:
            (Element): self
        """
        self.htmx(
            fn,
            event="keyup changed",
            delay=kwargs.pop("delay", "500ms"),
            **kwargs,
        )
        return self

    def on_click(self, fn: t.Callable, **kwargs) -> "Element":
        """Call `fn` when the `click` event fires on the element."""
        self.htmx(
            fn,
            event="click",
            **kwargs,
        )
        return self

    def preprocess(self) -> None:
        """Preprocess the element before it is rendered. Tags that implement
        this method can modify the element before it is rendered."""
        raise NotImplementedError

    def get_element(self) -> t.Union[t.Dict[str, t.Any], None]:
        """Create a dictionary of the element's tag, attrs, and children.

        If the `preprocess` method is defined, then it will be called while
        generating the dictionary. The output of `preprocess` can be any valid
        children like an ElementTag, string, or an instance of Element.

        Returns:
            (dict): dictionary with keys `tag`, `attrs`, and `children`
        """
        # if this element is not visible then return None
        if not self.visible:
            return None

        try:
            self.preprocess()
        except NotImplementedError:
            pass

        # Plugins implementing preprocess_element can modify the
        # element before it is rendered. This is useful for adding attributes
        # or children to the element and is similar to the `preprocess` method.
        # Plugins modify the element after the `preprocess` method is called.
        hooks = pm.hook.preprocess_element(element=self)
        if hooks:
            for hook in hooks:
                hook()

        return {
            "tag": self.tag,
            "attrs": self.attrs,
            "children": self.children,
        }

    def render(self) -> str:
        """Render this tag to html string.

        Returns:
            (str): html string
        """
        return render_element(self.get_element())

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> "Element":
        """Add children and attrs to the element.

        Args:
            *args: children
            **kwargs: attrs

        Example:
        ```python
        div = Div("Hello", id="my-div")
        div("World", class_="my-class")
        print(div.render())  # <div id="my-div" class="my-class">Hello World</div>
        ```
        """
        self.attrs.update(kwargs)
        self.children.extend(list(args))

    def __str__(self) -> str:
        return self.render()


def get_current_element_context(default=None):
    """Get the current element context. This should only be used inside
    the `with` statement of an Element.

    Args:
        default (any): default value to return if no context is found

    Returns:
        (Element): current element

    Raises:
        ValueError: if no context is found and `default` is not provided
    """
    h = _get_thread_context()
    # ctx has type Element._frame, a namedtuple with fields element, items, and used
    ctx = Element._with_contexts.get(h, None)
    if ctx:
        return ctx[-1].element
    if default is None:
        raise ValueError("No current context. Use this only inside `with` statement.")
    return default


def render_element(element: t.Union[t.Dict[str, t.Any], Element]) -> str:
    """Render an element dictionary to string.

    - Elements without a tag are treated as div
    - Attributes with None values are ignored
    - Attributes class_, classname, classes, c, and klass are set to class attribute
    - Attributes for_ is set to for attribute
    - If a prop value has double quotes then it is wrapped in single quotes,
        otherwise it is wrapped in double quotes
    - If a child has the `is_element` attribute then assume it is an Element
        and call its `render` method
    - If a child is a callable function then call it and treat the output as
        a string

    Args:
        element (dict): A dictionary with keys `tag`, `attrs`, and `children`.
            Children can be a string, an element dict, or a list including
            instances of Element, strings, or callable functions that return an
            Element.

    Returns:
        (str): html representation of the element

    Example:

    ```python
    element = {
        "tag": "div",
        "attrs": {"id": "my-div"},
        "children": [
            "Hello",
            {"tag": "span", "attrs": {"class": "my-span"}, "children": ["World"]},
        ],
    }
    html = render_element(element)
    print(html)  # <div id="my-div">Hello<span class="my-span">World</span></div>
    ```
    """
    if utils.is_function(element) or utils.is_method(element):
        element = element()

    # get_element is a special method that can be implemented by classes and
    # should return an Element or a dictionary with keys `tag`, `attrs`, and `children`
    if hasattr(element, "get_element"):
        element = element.get_element()

    if element is None:
        return ""

    if isinstance(element, (str, Number, bool)):
        return str(element)

    if isinstance(element, Element):
        element = element.get_element()

    # self-closing tags
    # fmt: off
    sct: t.Mapping[str, bool] = {
        k: True for k in [
            "meta", "link", "img", "br", "hr", "input", "area", 
            "base", "col", "embed", "command", "keygen", "param", "source", 
            "track", "wbr"
        ]
    }
    # fmt: on
    try:
        tag: str = element.get("tag", "div")  # default to div
        attrs: AttrsLike = element.get("attrs", {})
        children: t.Any = element.get("children", [])
    except AttributeError:
        raise TypeError(
            "element must be a dict, got type %s: %r" % (type(element), element)
        )
    # children is a dict containing an element-like structure (tag, attrs, children)
    if isinstance(children, dict):
        if "tag" in children:
            children = [children]
    _attrs: t.List[t.Any] = []
    attrs_str: str = ""
    if attrs is not None:
        for k, v in attrs.items():
            # "classname", "class_", "classes", "klass" attrs are converted to "class"
            if k in ["classname", "class_", "classes", "klass", "cl", "cls", "c"]:
                k = "class"
            if k == "for_":
                k = "for"
            # prop keys with underscores are converted to dashes
            k = k.replace("_", "-")
            # evaluate values that are callable functions
            if utils.is_function(v) or utils.is_method(v):
                v = v()
            if isinstance(v, bool):
                # boolean value only adds the key if True
                if v:
                    _attrs.append(k)
            else:
                if v is None:
                    # None value is skipped
                    continue
                # all other value types converted to string
                if not isinstance(v, str):
                    v = str(v)
                # handle the case where value contains double quotes by using
                # single quotes
                if '"' in v:
                    _attrs.append(f"{k}='{v}'")
                else:
                    _attrs.append(f'{k}="{v}"')
        attrs_str = " ".join(_attrs)
    # if attrs is not empty, prepend a space
    if len(attrs_str) > 0:
        attrs_str = " " + attrs_str
    if tag in sct:
        # self-closing tags have no children
        return f"<{tag}{attrs_str}/>"
    else:
        innerHTML: str = ""
        if children is None:
            innerHTML = ""
        elif isinstance(children, (str, Number, bool)):
            innerHTML = str(children)
        elif isinstance(children, Element):  # Element class instance
            try:
                innerHTML = children.render()
            except:
                pass
        elif isinstance(children, Element):  # Element class instance
            try:
                innerHTML = children.render()
            except:
                pass
        elif hasattr(
            children, "get_element"
        ):  # Any class instance with a get_element method
            try:
                innerHTML = children.get_element()
            except:
                pass
        elif callable(children):
            innerHTML += str(children())
        elif isinstance(children, (list, tuple)):
            for child in children:
                innerHTML += render_element(child)
        return f"<{tag}{attrs_str}>{innerHTML}</{tag}>"


def render_document(
    body: t.List = [],
    *,
    title: t.Union[str, None] = None,
    head: t.List[dict] = [],
    use_htmx: bool = True,
    body_class: str = "",
) -> str:
    """Render a full html document.

    Args:
        children (list): list of children elements
        title (str): title of the document
        head (list): list of elements to include in the head
        use_htmx (bool): if True, import htmx and sweetalert2

    Returns:
        str: html document
    """
    _head = [
        dict(tag="meta", attrs={"charset": "utf-8"}),
        dict(
            tag="meta",
            attrs={
                "name": "viewport",
                "content": "width=device-width, initial-scale=1",
            },
        ),
        dict(tag="meta", attrs={"http-equiv": "X-UA-Compatible", "content": "IE=edge"}),
    ]
    if use_htmx:
        htmx_scripts = [
            dict(tag="script", attrs={"src": _HTMX_CDN_URL}),
        ]
        _head.extend(htmx_scripts)

    if title:
        _head.append(dict(tag="title", children=title))
    if isinstance(head, dict):
        head = [head]
    _head.extend(head)
    container = [
        dict(tag="head", children=_head),
        dict(tag="body", children=body, attrs={"class": body_class}),
    ]
    html = ["<!DOCTYPE html>"]
    html.append("<html>")
    for elem in container:
        html.append(render_element(elem))
    html.append("</html>")
    return "".join(html)


def elm(tag: str, *args: t.Any, **kwargs: t.Any) -> Element:
    """Create an Element instance.

    Args:
        tag (str): tag name
        *args: children
        **kwargs: attributes

    Returns:
        Element: Element instance
    """
    el = Element(*args, **kwargs)
    el.tag = tag
    return el
