#!/usr/bin/python3
"""filter cities"""

import sys
import MySQLdb


def display_values(username, password, database, state):
    """takes a state arg and list cities safe from SQL injections"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
        cursor = conn.cursor()
        cursor.execute("SELECT cities.name\
                       FROM cities LEFT JOIN states\
                       ON states.id = cities.state_id\
                       WHERE states.name = %s\
                       ORDER BY cities.id ASC", (state,))
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
