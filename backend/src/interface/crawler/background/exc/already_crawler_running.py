from .ERR_CODE import ERR_CODE


class AlreadyCrawlerRunningException(Exception):
    """
    Exception raised when a crawler is already running.
    """

    def __init__(self, message: str = "Crawler is already running."):
        super().__init__(message)
        self.code = f"{ERR_CODE}001"
        self.message = message
