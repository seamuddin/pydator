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

RULES = {
    "required": RequiredRule(),
    "string": StringRule(),
    "number": NumberRule(),
    "min": MinRule(),
    "max": MaxRule(),
    "email": EmailRule(),
    "boolean": BooleanRule(),
    "in": InRule(),
    "regex": RegexRule(),
    "date": DateRule(),
    "float": FloatRule(),
    "url": UrlRule(),
    "integer": IntegerRule(),
    "contains": ContainsRule(),
}
