from pydator.base_rule import BaseRule


class InRule(BaseRule):
    def __call__(self, value, *args):
        if value not in args:
            return False, self.message("in", *args)
        return True, None

    def message(self, field, *args):
        return f"Value must be one of: {', '.join(args)}."