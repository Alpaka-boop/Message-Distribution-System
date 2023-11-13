import sys

from enum import Enum
from src.Message import Message
from src.OtherMessanger import OtherMessanger
from src.MessageDistributionSys import MessageDistributionSys
from termcolor import colored

CONST_MAX_LOG_MES_CHAR_NUM = 100_000_000


class MessagesStatus(Enum):
    DELIVERED = 0
    READ = 1


class Addressee:
    def receive_message(self, message: Message):
        raise RuntimeError("Unrecognised addressee type\n")


class User(MessageDistributionSys, Addressee):
    __name = ''
    __surname = ''
    __nickname = ''

    __logged_messages = []
    __logged_messages_status = []
    __logged_messages_char_num = 0

    def __init__(self, name: str, surname: str, nickname: str, password: str):
        self.__name = name
        self.__surname = surname
        self.__nickname = nickname
        self.__password = password

    def get_nickname(self):
        return self.__nickname

    def log_message(self, message: Message):
        self.__logged_messages.append(message)
        self.__logged_messages_status.append(MessagesStatus.DELIVERED)
        self.__logged_messages_char_num += message.get_length()
        self.check_logged_mess_len()

    def receive_message(self, message: Message):
        self.log_message(message)

    def dump_message_by_end_index(self, index: int):
        if index > 0:
            raise RuntimeError("Index must be negative to dump from end")
        print(self.__logged_messages[index])
        self.mark_message_as_read_by_end_index(index)

    def mark_message_as_read_by_end_index(self, index: int):
        if index > 0:
            raise RuntimeError("Index must be negative to dump from end")
        self.__logged_messages_status[index] = MessagesStatus.READ

    def delete_message_by_end_index(self, index: int):
        if index > 0:
            raise RuntimeError("Index must be negative to dump from end")
        self.__logged_messages_char_num -= self.__logged_messages[index].get_length()
        self.__logged_messages.pop(index)
        self.__logged_messages_status.pop(index)

    def check_logged_mess_len(self):
        while self.__logged_messages_char_num > CONST_MAX_LOG_MES_CHAR_NUM:
            self.__logged_messages_char_num -= self.__logged_messages[0].get_length()
            self.__logged_messages.pop(0)
            self.__logged_messages_status.pop(0)


class MessangerAddressee(MessageDistributionSys, Addressee):
    __addressee_name = ''
    __addressee_surname = ''

    def __init__(self, other_messenger: OtherMessanger, addressee_name, addressee_surname):
        self.__other_messenger = other_messenger
        self.__addressee_name = addressee_name
        self.__addressee_surname = addressee_surname

    def receive_message(self, message: Message, color='white'):
        self.__other_messenger.receive_message(message, color, self.__addressee_name, self.__addressee_surname)


class Display(MessageDistributionSys, Addressee):
    __output_stream = sys.stdout
    __message = ''
    __output_color = 'white'

    def __init__(self, output_stream):
        self.__output_stream = output_stream

    def receive_message(self, message: Message):
        self.__message = message

    def display(self):
        print(colored(self.__message.get_body(), self.__output_color), file=self.__output_stream)

    def clear_display(self):
        self.__message = ''

    def set_color(self, color):
        self.__output_color = color

