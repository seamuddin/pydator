
class ValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("Validation failed.")
