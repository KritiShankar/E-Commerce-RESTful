import sqlite3
import contextlib

@contextlib.contextmanager
def get_connection_db():
    connection = sqlite3.connect("ecommerce.db")
    try:
        yield connection
    except Exception as e:
        print(e)
        raise Exception("Error: While creating SQLite connection object.")
    finally:
        connection.commit()
        connection.close()