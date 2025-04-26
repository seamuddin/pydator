from abc import ABC, abstractmethod


class BaseRule(ABC):
    """
    Base class for all validation rules.
    All custom and built-in rules should inherit from this class.
    """

    @abstractmethod
    def __call__(self, value, *args):
        """
        Validate the given value.

        Should return a tuple: (bool: is_valid, str: error_message)
        """
        pass

    def message(self, field, *args):
        """
        Default error message if validation fails.
        Can be overridden by subclasses for specific error messages.
        """
        return f"Validation error on {field}."
