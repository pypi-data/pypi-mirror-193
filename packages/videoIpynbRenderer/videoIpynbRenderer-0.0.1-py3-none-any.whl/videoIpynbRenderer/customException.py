class InvalidUrlException(Exception):
    def __init__(self, message: str = "URL is invalid"):
        super().__init__(message)
