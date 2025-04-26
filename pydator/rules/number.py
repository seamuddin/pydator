from pydator.base_rule import BaseRule


class NumberRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, (int, float)):
            return False, self.message("number")
        return True, None

    def message(self, field, *args):
        return "Must be a number."
