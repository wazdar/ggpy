from msgserv import User
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
        "-n", "--new-pass",
        help="new password for the user (plain text)",
        required=False
    )
    parser.add_argument(
        "-l", "--list",
        help="show the list of users",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "-d", "--delete",
        help="delete the user and all messages related to her/him",
        required=False,
        action="store_true"
    )
    parser.add_argument(
        "-e", "--edit",
        help="edit the user (e.g. set new password)",
        required=False,
        action="store_true"
    )
    return parser.parse_args()


def load_user_data(user_name):
    # TODO utworzyć obiekt User dla podanej nazwy użytkownika (z danmi z bazy)
    # TODO zwrócić ten obiekt lub None jeżeli nie ma takiego użytkownika
    return None


def check_password(user, password):
    # TODO sprawdzić, czy podane hasło jest poprawne dla użytkownika
    # TODO zwrócić True lub False
    pass


def add_new_user(user_name, password):
    # TODO sprawdzić, czy hasło ma minimum 8 znaków (jeżeli nie, wypisać info i nie dodawać użytkownika)
    # TODO dodać nowego użytkownika do bazy (nowy obiekt User, save_to_db)
    # TODO Wypisać informację o dodaniu użytkownika w konsoli
    print(user_name)
    print(password)
    pass


def change_password(user, new_password):
    # TODO sprawdzić, czy nowe hasło ma min. 8 znaków
    # TODO zmienić hasło w obiekcie user, zapisać go do bazy
    # TODO wypisać informację w konsoli
    pass


def delete_user(user):
    # TODO usunąć użytkownika
    # TODO wypisać informację w konsoli
    pass


def list_users():
    # TODO pobrać listę wszystkich użytkowników
    # TODO wyświetlić ich nazwy w konsoli
    pass


def choose_action(args):
    user = load_user_data(args.username)

    if not user:
        return add_new_user(args.username, args.password)

    if not check_password(args.username, args.password):
        print("Invalid password")
        return

    if args.edit:
        if args.new_pass:
            return change_password(user, args.new_pass)
        else:
            print("New password not provided")
            return

    if args.delete:
        return delete_user(user)

    if args.list:
        return list_users()


if __name__ == "__main__":
    parsed_args = parse_args()
    choose_action(parsed_args)
