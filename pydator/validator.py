from pydator.rules import RULES
from pydator.exceptions import ValidationError


class Validator:
    def __init__(self, data, rules, custom_messages=None):
        self.data = data
        self.rules = rules
        self.errors = {}
        self.custom_messages = custom_messages or {}

    def add_rule(self, field, rules):
        self.rules[field] = rules

    def validate(self):
        self.errors = {}
        for field, field_rules in self.rules.items():
            value = self.data.get(field)
            for rule in field_rules:
                rule_name, *params = rule.split(":")
                params = params[0].split(",") if params else []
                rule_instance = RULES.get(rule_name)

                if rule_instance:
                    is_valid, default_message = rule_instance(value, *params)
                    if not is_valid:
                        custom_message = self.custom_messages.get(f"{field}.{rule_name}", default_message)
                        self.errors.setdefault(field, []).append(custom_message)
        return not bool(self.errors)

    def fails(self):
        return not self.validate()

    def get_errors(self):
        return self.errors
