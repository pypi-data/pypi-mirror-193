from typing import Callable, Optional

import justpy as jp

from .string_element import StringElement


class Input(StringElement):

    def __init__(self, label: str = None, *,
                 placeholder: str = None, value: str = '', on_change: Optional[Callable] = None):
        """Text Input

        :param label: displayed label for the text input
        :param placeholder: text to show if no value is entered
        :param value: the current value of the text input
        :param on_change: callback to execute when the input is confirmed by leaving the focus
        """
        view = jp.QInput(
            label=label,
            placeholder=placeholder,
            value=value,
            change=self.handle_change,
            disable_input_event=True,
            temp=False,
        )

        super().__init__(view, value=value, on_change=on_change)
