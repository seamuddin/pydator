from pydator.base_rule import BaseRule


class RequiredRule(BaseRule):
    def __call__(self, value, *args):
        if value is None or (isinstance(value, str) and not value.strip()):
            return False, self.message("required")
        return True, None

    def message(self, field, *args):
        return "This field is required."
