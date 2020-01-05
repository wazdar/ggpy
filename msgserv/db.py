import psycopg2

cnx = None


def connection():
    global cnx
    if not cnx:
        cnx = psycopg2.connect(
            dbname="msg_db",
            user="postgres",
            password="coderslab",
            host="localhost"
        )
    return cnx


def cursor():
    return connection().cursor()


def commit():
    return connection().commit()


def close():
    global cnx
    connection().close()
    cnx = None
