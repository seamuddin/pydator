import re
from pydator.base_rule import BaseRule


class RegexRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("regex")

        pattern = args[0] if args else ""
        if not re.match(pattern, value):
            return False, self.message("regex", pattern)
        return True, None

    def message(self, field, *args):
        return f"Value does not match the required pattern: {args[0]}"