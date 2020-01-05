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
    return User.by_name(user_name)


def check_password(user, password):
    user = User.by_name(user)
    return user.password_valid(password)



def add_new_user(user_name, password):
    if len(password) < 8:
        return print("Password must be at least 8 characters !!!")
    user = User()
    user.name = user_name
    user.password = password
    user.save_to_db()
    return print('New User was added. :)')


def change_password(user, new_password):
    if len(new_password) < 8:
        return print("Password must be at least 8 characters !!!")
    user.password = new_password
    user.save_to_db()
    return print('User password was changed')


def delete_user(user):
    user.delete()
    return print(f'User on name: {user.name}, was deleted')


def list_users():
    print('User list:')
    for u in User.all():
        print(u.name+'\n')
    return


def choose_action(args):
    user = load_user_data(args.user)

    if not user:
        return add_new_user(args.user, args.password)

    if not check_password(args.user, args.password):
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
