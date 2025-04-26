from pydator.base_rule import BaseRule


class MaxRule(BaseRule):
    def __call__(self, value, *args):
        if not args:
            return False, self.message("max")

        max_val = int(args[0])
        if isinstance(value, (str, list)) and len(value) > max_val:
            return False, self.message("max", max_val)
        if isinstance(value, (int, float)) and value > max_val:
            return False, self.message("max", max_val)
        return True, None

    def message(self, field, *args):
        if args:
            return f"Maximum value/length is {args[0]}."
        return "Maximum value/length exceeded."
