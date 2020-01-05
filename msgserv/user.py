from .db import cursor, commit
from .clcrypto import password_hash, check_password


class User:

    def __init__(self):
        self.__id = -1
        self.name = ""
        self.__hashed_pass = ""

    @property
    def id(self):
        return self.__id

    @property
    def password(self):
        """Zwraca zahashowane hasło"""
        return self.__hashed_pass

    @password.setter
    def password(self, new_pass_plain):
        """
        Ustawia nowe hasło, hashując je.

        :param new_pass_plain: nowe hasło (czysty tekst)
        :return: None
        """
        self.__hashed_pass = password_hash(new_pass_plain)

    def password_valid(self, pwd):
        """
        Sprawdza, czy dane hasło jest poprawne.

        :param pwd: hasło do sprawdzenia (czysty tekst)
        :return: True jeżeli hasło jest poprawne, False jeżeli nie
        """
        return check_password(pwd, self.password)

    def save_to_db(self):
        """Zapisuje obiekt użytkownika do bazy"""
        c = cursor()
        if self.id == -1:
            # TODO insert do tabeli users
            # TODO z pobraniem id wstawionego wiersza
            # TODO ustawienie self.__id na id wstawionego wiersza
            pass
        else:
            # TODO update w tabeli users
            pass
        c.close()
        commit()

    def delete(self):
        """Usuwa użytkownika z bazy"""
        c = cursor()
        # TODO delete z tabeli users
        c.close()
        commit()

    @classmethod
    def _from_row(cls, row):
        """
        Tworzy obiekt User na podstawie tupli.

        :param row: tupla (id, name, hashed_password)
        :return: nowy obiekt User
        """
        if row:
            user_id, name, hashed_pwd = row
            u = cls()
            u.__id = user_id
            u.name = name
            u.__hashed_pass = hashed_pwd
            return u
        else:
            return None

    @classmethod
    def by_id(cls, user_id):
        c = cursor()
        # TODO select z tabeli users dla danego id
        user = None  # TODO utworzyć tutaj obiekt za pomocą _from_row
        c.close()
        return user

    @classmethod
    def by_name(cls, name):
        c = cursor()
        # TODO select z tabeli users dla danego name
        user = None  # TODO utworzyć tutaj obiekt za pomocą _from_row
        c.close()
        return user

    @classmethod
    def all(cls):
        c = cursor()
        # TODO pobrać wszystkie wiersze z tabeli users
        res = []
        # TODO iterować po kursorze i dołączać nowe obiekty User do res (tworzyć je za pomocą _from_row)
        c.close()
        return res
