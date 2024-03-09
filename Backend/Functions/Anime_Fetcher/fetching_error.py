

class AnimeFetchingError(Exception):
    __ERROR_MESSAGE = "Could not fetch anime data."

    def __init__(self):
        super().__init__(self.__ERROR_MESSAGE)