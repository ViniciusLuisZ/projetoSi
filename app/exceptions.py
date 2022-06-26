from enum import Enum, auto

class ErrorType(Enum):
    """Class that define app error types."""
    RSC_NOT_FOUND = auto()
    INVALID_AMOUNT = auto()
    INVALID_PARTIAL_CANCEL = auto()
    INSUFFICIENT_FUNDS = auto()
    SERVER_ERROR = auto()
    INVALID_INPUT = auto()
    ALREADY_CAPTURED = auto()

class InvalidInput(Exception):
    """Exceção levantada por uma entrada incorreta de valores"""
    def __init__(self, message):
        super().__init__(message)

        self.detail = {
            'type': ErrorType.INVALID_INPUT.name,
            'reason': 'Data validation error',
            'errors': [{'msg': message}]
        }