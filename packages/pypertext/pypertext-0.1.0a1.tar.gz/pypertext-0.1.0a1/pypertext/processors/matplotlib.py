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
from pypertext import utils
from pypertext.element import Element
from pypertext.plugins import hookimpl

log = logging.getLogger(__name__)


def mpl_png(fig, dpi=150) -> str:
    """Return the base64 encoded png string of a matplotlib figure.

    Args:
        fig: matplotlib figure
        dpi: dpi of the figure, default 150

    Returns:
        str: base64 encoded png string
    """
    import io
    import base64

    f = io.BytesIO()
    fig.savefig(f, dpi=dpi, format="png", bbox_inches="tight")
    f.seek(0)
    b = base64.b64encode(f.getvalue()).decode("utf-8").replace("\n", "")
    return (
        '<img class="mpl-figure-png" align="center" src="data:image/png;base64,%s">' % b
    )


class MatplotlibProcessor(BaseProcessor):
    """Processor for Matplotlib figures."""

    @classmethod
    def is_valid_type(cls, data) -> bool:
        return any([utils.is_type(data, t) for t in ["matplotlib.figure.Figure"]])

    def get_element(self) -> Element:
        el = mpl_png(self.data)
        return el


@hookimpl
def register_processor_classes():
    return MatplotlibProcessor
