from datetime import datetime
from pydator.base_rule import BaseRule


class DateRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("date")
        try:
            datetime.fromisoformat(value)
            return True, None
        except ValueError:
            return False, self.message("date")

    def message(self, field, *args):
        return "Invalid date format. Expected ISO format (YYYY-MM-DD)."
