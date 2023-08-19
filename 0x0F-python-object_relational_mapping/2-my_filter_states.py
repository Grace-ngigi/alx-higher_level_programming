#!/usr/bin/python3
"""Prints valus in the states table"""

import sys
import MySQLdb


def display_values(username, password, database, state):
    """takes an arg and display values in the states table"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE\
                       BINARY '{}' ORDER BY states.id ASC".format(state))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    display_values(username, password, database, state)
