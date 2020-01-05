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
            sql = 'INSERT INTO users(name, hashed_password) VALUES (%s, %s) RETURNING id'
            c.execute(sql, (self.name, self.__hashed_pass))
            self.__id, = c.fetchone()
        else:
            sql = """
            UPDATE users
            SET name = %s, hashed_password = %s
            WHERE id = %s
            """
            c.execute(sql, (self.name, self.__hashed_pass, self.id))
        c.close()
        commit()

    def delete(self):
        """Usuwa użytkownika z bazy"""
        c = cursor()
        sql = """
        DELETE FROM users 
        WHERE id = %s
        """
        c.execute(sql, (self.id,))
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
        sql = """
        SELECT id, name, hashed_password FROM users WHERE id = %s
        """
        c.execute(sql, (user_id,))

        user = cls._from_row(c.fetchone())
        c.close()
        return user

    @classmethod
    def by_name(cls, name):
        c = cursor()
        sql = """
        SELECT id, name, hashed_password FROM users WHERE name = %s
        """
        c.execute(sql, (name,))
        user = cls._from_row(c.fetchone())
        c.close()
        return user

    @classmethod
    def all(cls):
        c = cursor()
        sql = 'SELECT id, name, hashed_password FROM users'
        c.execute(sql)
        res = []
        for row in c.fetchall():
            res.append(cls._from_row(row))
        c.close()
        return res
