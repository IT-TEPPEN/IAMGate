from .ERR_CODE import ERR_CODE


class FailToGetContentException(Exception):
    """
    Exception raised when content acquisition fails.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.code = f"{ERR_CODE}001"
        self.message = message
