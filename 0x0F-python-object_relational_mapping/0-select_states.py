#!/usr/bin/python3
"""Lists all states from a database"""

import MySQLdb
import sys


def list_states(username, password, database):
    """lists states and order them by id"""
    try:
        connection = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)
        cursor = connection.cursor()

        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
