#!/usr/bin/python3
"""List all cities from the db"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """lists all cities from the db"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
        cursor = conn.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name\
                       FROM cities LEFT JOIN states\
                       ON states.id = cities.state_id\
                       ORDER BY cities.id ASC")
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
    list_cities(username, password, database)
