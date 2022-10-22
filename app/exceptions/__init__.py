"""Custom exception classes"""


class OnlyOneValue(Exception):
    def __init__(self, message="Cannot perform Operation on only 1 val"):
        self.message = message
        super().__init__(self.message)
