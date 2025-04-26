from pydator.base_rule import BaseRule


class StringRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("string")
        return True, None

    def message(self, field, *args):
        return "Must be a string."
