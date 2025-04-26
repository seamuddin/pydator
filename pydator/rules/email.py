import re
from pydator.base_rule import BaseRule


class EmailRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("email")
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, value):
            return False, self.message("email")
        return True, None

    def message(self, field, *args):
        return "Invalid email format."
