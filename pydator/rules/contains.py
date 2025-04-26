from pydator.base_rule import BaseRule


class ContainsRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("contains")

        substring = args[0] if args else ""
        if substring not in value:
            return False, self.message("contains", substring)
        return True, None

    def message(self, field, *args):
        return f"Must contain '{args[0]}'."