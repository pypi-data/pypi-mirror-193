from dataclasses import dataclass
from typing import List

from flake8.formatting.default import Default
from flake8.options.manager import OptionManager
from flake8.violation import Violation


class Formatter(Default):
    def format(self, error: Violation):
        custom_error = self.get_custom_error(error.code)
        if custom_error:
            # interpolate the original error message in case it is specified in
            # the custom message.
            custom_text = custom_error.text.format(original_message=error.text)
            new_error = Violation(
                error.code,
                error.filename,
                error.line_number,
                error.column_number,
                custom_text,
                error.physical_line,
            )
            return super().format(new_error)
        else:
            return super().format(error)

    def get_custom_error(self, code: str) -> "CustomError":
        for custom_error in self.custom_errors:
            if code.startswith(custom_error.code):
                return custom_error

    def after_init(self):
        error_messages = self.options.error_messages
        if not error_messages:
            msgs = []
        elif isinstance(error_messages, str):
            # parsed from the config file, so we need to convert it to a list
            # flake8 does not support parsing values containing spaces from config
            # files
            msgs = [
                line.strip()
                for line in error_messages.splitlines()
                if line.strip()
            ]
        else:
            # when parsed from the command line, the value is already a list
            msgs = error_messages

        # split the error code from the custom error message
        errors = []
        for msg in msgs:
            code = msg.split()[0]
            text = msg.replace(code, "", 1).strip()
            errors.append(CustomError(code, text))

        self.custom_errors: List[CustomError] = errors


class Plugin:
    name = "flake8-custom-error-messages"
    version = "0.1.1"

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        return  # because the package doesn't add any rules
        # yield added so python considers the run method as returning a generator
        # even though it's unreachable
        yield  # noqa

    @classmethod
    def add_options(cls, options_manager: OptionManager):
        options_manager.add_option(
            "--custom-error-messages",
            dest="error_messages",
            type=str,
            parse_from_config=True,
            help=(
                "Specify a custom error message for an error code. The message "
                "should start with the error code in question followed by a "
                "space and then the custom message."
            ),
            metavar="MSG",
            nargs="+",
        )


@dataclass
class CustomError:
    code: str
    text: str
