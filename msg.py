from msgserv import Message, User
import argparse

def parse_args():
    """
    Parsuje parametry z wiersza poleceń.
    :return: obiekt (jak słownik) args, zawierający zdekodowane parametry
    """
    parser = argparse.ArgumentParser(description="User management tool for the messaging system")
    parser.add_argument(
        "-u", "--user",
        help="user name",
        required=True
    )
    parser.add_argument(
        "-p", "--password",
        help="user password (plain text)",
        required=True
    )
    parser.add_argument(
        "-l", "--list",
        help="show all messages for this user",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "-t", "--to",
        help="set the recipient of the message",
        required=False,
    )
    parser.add_argument(
        "-s", "--send",
        help="send a new message to the user specified with -t (--to)",
        required=False
    )
    return parser.parse_args()


def get_user(name, password = None):
    # TODO utworzyć obiekt użytkownika (User) na podstawie nazwy (pobrać z bazy)
    # TODO jeżeli nie ma takiego użytkownika, zwrócić None
    # TODO jeżeli podano password, to sprawdzić, czy hasło jest poprawne
    # TODO jeżeli tak, zwrócić obiekt użytkownika
    # TODO jeżeli nie, zwrócić None
    # TODO jeżeli hasła nie podano, zwrócić obiekt użytkownika
    return None


def msg_list(user):
    # TODO utworzyć listę obiektów komunikatów dla użytkownika (Message)
    # TODO wyświetlić datę i treść każdego komunikatu
    pass


def send_msg(user, contents):
    # TODO utworzyć obiekt wiadomości, wypełnić jego atrybuty
    # TODO zapisać obiekt do bazy
    # TODO wypisać informację o wysłaniu wiadomości
    pass


def choose_action(args):
    user = get_user(args.user, args.password)

    if not user:
        print("Invalid user name or password")
        return

    if args.send:
        if args.to:
            to_user = get_user(args.to)
            if to_user:
                return send_msg(to_user, args.send)
            else:
                print(f"Recipient {args.to} not found")
                return
        else:
            print("Missing recipient name (-t, --to)")
            return


if __name__ == "__main__":
    parsed_args = parse_args()
    choose_action(parsed_args)
