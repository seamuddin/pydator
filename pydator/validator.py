from pydator.base_rule import BaseRule
from pydator.rules.required_rule import RequiredRule
from pydator.rules.string_rule import StringRule
from pydator.rules.number import NumberRule
from pydator.rules.min import MinRule
from pydator.rules.max import MaxRule
from pydator.rules.email import EmailRule
from pydator.rules.boolean import BooleanRule
from pydator.rules.in_rule import InRule
from pydator.rules.regex import RegexRule
from pydator.rules.date import DateRule
from pydator.rules.float_rule import FloatRule
from pydator.rules.url import UrlRule
from pydator.rules.integer import IntegerRule
from pydator.rules.contains import ContainsRule


class Validator:
    RULES = {}

    @staticmethod
    def register_rule(rule_name, rule_instance):
        """Registers a validation rule."""
        if not isinstance(rule_instance, BaseRule):
            raise ValueError("Only rules that inherit BaseRule can be registered.")
        Validator.RULES[rule_name] = rule_instance

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
                rule_instance = Validator.RULES.get(rule_name)

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


Validator.register_rule("required", RequiredRule())
Validator.register_rule("string", StringRule())
Validator.register_rule("number", NumberRule())
Validator.register_rule("min", MinRule())
Validator.register_rule("max", MaxRule())
Validator.register_rule("email", EmailRule())
Validator.register_rule("boolean", BooleanRule())
Validator.register_rule("in", InRule())
Validator.register_rule("regex", RegexRule())
Validator.register_rule("date", DateRule())
Validator.register_rule("float", FloatRule())
Validator.register_rule("url", UrlRule())
Validator.register_rule("integer", IntegerRule())
Validator.register_rule("contains", ContainsRule())
