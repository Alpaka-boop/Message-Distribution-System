from src.Addressee import Addressee
from src.Message import Message, MessageImportanceLevel


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
    def filter_messages(message_list: list[Message], importance_level: MessageImportanceLevel) -> list[Message]:
        if importance_level is None:
            return message_list
        filtered_message_list = []
        for message in message_list:
            if message.get_importance_level() == importance_level:
                filtered_message_list.append(message)

        return filtered_message_list

    def send_message_to_group(self, message: Message, group: list[Addressee], importance_level=None):
        message_list = self.filter_messages([message], importance_level)
        if not message_list:
            return
        for addressee in group:
            addressee.receive_message(message_list[0])

    def send_message(self, message: Message, addressee: Addressee, importance_level=None):
        message_list = self.filter_messages([message], importance_level)
        if not message_list:
            return
        addressee.receive_message(message_list[0])
