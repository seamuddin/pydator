from pydator.base_rule import BaseRule


class IntegerRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, int):
            return False, self.message("integer")
        return True, None

    def message(self, field, *args):
        return "Must be an integer."
