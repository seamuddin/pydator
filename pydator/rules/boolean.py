from pydator.base_rule import BaseRule


class BooleanRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, bool):
            return False, self.message("boolean")
        return True, None

    def message(self, field, *args):
        return "Must be a boolean."
