from pydator.base_rule import BaseRule


class FloatRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, float):
            return False, self.message("float")
        return True, None

    def message(self, field, *args):
        return "Must be a float."
