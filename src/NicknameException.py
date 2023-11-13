

class NicknameException(Exception):
    __nickname = ''

    def __init__(self, nickname):
        self.__nickname = nickname