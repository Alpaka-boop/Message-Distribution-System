from src.Addressee import Addressee
from src.Message import Message


class MessageDistributionSys:
    __all_accounts = []

    def add_addressee(self, addressee: Addressee):
        if not self.validate_new_addressee(addressee):
            raise RuntimeError("Invalid addressee\n")
        self.__all_accounts.append(addressee)

    def validate_new_addressee(self, addressee: Addressee):
        try:
            self.__all_accounts.index(addressee)
        except ValueError:
            return True
        return False

    @staticmethod
    def send_message_to_group(message: Message, group: list[Addressee]):
        for addressee in group:
            addressee.receive_message(message)

    @staticmethod
    def filter_messages(message_list: list[Message], importance_level) -> list[Message]:
        filtered_message_list = []
        for message in message_list:
            if message.get_importance_level() == importance_level:
                filtered_message_list.append(message)

        return filtered_message_list
