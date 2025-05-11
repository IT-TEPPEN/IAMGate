from .ERR_CODE import ERR_CODE


class NotRunningCrawlerException(Exception):
    """
    Exception raised when a crawler is already running.
    """

    def __init__(self, message: str = "Crawler is not running."):
        super().__init__(message)
        self.code = f"{ERR_CODE}002"
        self.message = message
