from abc import ABC, abstractmethod


class BaseRule(ABC):
    @abstractmethod
    def __call__(self, value, *args):
        pass

    def message(self, field, *args):
        return "Validation error."
