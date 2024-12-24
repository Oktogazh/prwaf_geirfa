import sqlite3


def your_module_function():
    conn = sqlite3.connect("items.db")
    return conn
