from termcolor import colored


class OtherMessanger:
    @staticmethod
    def receive_message(message, color, name, surname):
        print(colored("Messanger\n", color))
