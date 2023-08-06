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
import typing as t
from pypertext.element import Element


class BaseProcessor:
    """Base class to transform data into an Element.
    
    Args:
        data (t.Any): The input data.
        key (str): A unique key identifying the input.
    """

    def __init__(self, data: t.Any, key: t.Optional[str]):
        self.data = data
        """The input data."""
        self.key = key
        """A unique key identifying the input."""

    @classmethod
    def is_valid_type(self, data: t.Any) -> bool:
        """Check if the data is of the correct type to be handled by this processor.

        This is a class method, so it can be called without instantiating the processor.
        
        Args:
            data (t.Any): The data to check.
        
        Returns:
            (bool): True if the data is of the correct type to be handled by this processor.
        """
        raise NotImplementedError

    def get_element(self) -> t.Union[str, Element]:
        """Process the data and return an Element or a string.
        
        Returns:
            (str | Element): Output of the processor. Usually an Element.
        """
        raise NotImplementedError
