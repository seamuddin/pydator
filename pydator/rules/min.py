from pydator.base_rule import BaseRule


class MinRule(BaseRule):
    def __call__(self, value, *args):
        min_val = int(args[0])  # Get min_val from *args
        if not isinstance(value, (int, float)):
            return False, self.message("value_type_error")
        if value < min_val:
            return False, self.message("min_value", min_val)
        return True, None

    def message(self, field, *args):
        if field == "value_type_error":
            return "Value must be a number."
        if field == "min_value":
            return f"Minimum value is {args[0]}."
        return "Validation error."
