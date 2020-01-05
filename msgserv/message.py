from .db import cursor, commit
from .user import User
from datetime import datetime


class Message:

    def __init__(self):
        """
        Atrybuty każdego obiektu wiadomości:
        id (int)
        from_user (User)
        to_user (User)
        date_sent (datetime)
        contents (str)
        """
        self.__id = -1
        self.from_user = None
        self.to_user = None
        self.__date_sent = None
        self.contents = ""

    @property
    def id(self):
        return self.__id

    def save_to_db(self):
        """Zapisuje wiadomość do bazy"""
        c = cursor()
        if self.id == -1:
            self.__date_sent = datetime.now()
            # TODO insert to tabeli messages
            # TODO z pobraniem id wstawionego wiersza
            # TODO ustawienie self.__id na id wstawionego wiersza
            pass
        else:
            # TODO update w tabeli messages
            pass
        c.close()
        commit()

    def delete(self):
        """Usuwa wiadomość z bazy"""
        c = cursor()
        # TODO usunąć wiersz z messages dla danego id
        c.close()
        commit()

    @classmethod
    def from_row(cls, row):
        """
        Tworzy obiekt Message na podstawie tupli
        :param row: tupla (id, from_id, to_id, date_sent, contents)
        :return: nowy obiekt Message
        """
        if row:
            msg_id, from_id, to_id, date_sent, contents = row
            msg = cls()
            msg.__id = msg_id
            msg.from_user = User.by_id(from_id)
            msg.to_user = User.by_id(to_id)
            msg.__date_sent = date_sent
            msg.contents = contents
            return msg
        else:
            return None

    @classmethod
    def by_id(cls, msg_id):
        c = cursor()
        # TODO select z tabeli messages dla danego id
        msg = None  # TODO utworzyć tutaj obiekt za pomocą _from_row
        c.close()
        return msg

    @classmethod
    def all_to(cls, user):
        """
        Pobiera wszystkie wiadomości, których adresatem jest dany user
        :param user: obiekt klasy User (adresat wiadomości)
        :return: lista obiektów Message
        """
        c = cursor()
        res = []
        # TODO pobrać z tabeli messages wszystkie wiadomości do użytkownika user
        # TODO (sortowanie pobieranych wiadomości malejąco po dacie wysłania)
        # TODO dla każdej z tych wiadomości utworzyć obiekt Message (przez _from_row)
        # TODO dodać utworzony obiekt do listy res
        c.close()
        return res
