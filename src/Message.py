from enum import Enum


class MessageImportanceLevel(Enum):
    SPAM = 0
    REGULAR = 1
    IMPORTANT = 2


class Message:
    __name = ''
    __body = ''
    __length = 0
    __importance_level = MessageImportanceLevel.SPAM

    def __init__(self, name, body, importance_level):
        self.__name = name
        self.__body = body
        self.__length = len(body)
        self.__importance_level = importance_level

    def get_length(self):
        return self.__length

    def get_body(self):
        return self.__body

    def get_importance_level(self):
        return self.__importance_level
