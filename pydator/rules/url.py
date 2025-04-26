from urllib.parse import urlparse
from pydator.base_rule import BaseRule


class UrlRule(BaseRule):
    def __call__(self, value, *args):
        if not isinstance(value, str):
            return False, self.message("url")
        parsed = urlparse(value)
        if not all([parsed.scheme, parsed.netloc]):
            return False, self.message("url")
        return True, None

    def message(self, field, *args):
        return "Invalid URL format."
