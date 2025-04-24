# Copyright (c) [2025] [Seam Uddin]
# This file is licensed under the MIT License.

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
                validator_func = RULES.get(rule_name)
                if validator_func:
                    # Adjusted to pass parameters correctly
                    is_valid, default_message = validator_func(value, *params)
                    if not is_valid:
                        custom_message = self.custom_messages.get(f"{field}.{rule_name}", default_message)
                        self.errors.setdefault(field, []).append(custom_message)
        return not bool(self.errors)
