#!/usr/bin/python3
"""Lists states from db"""
import sys
import MySQLdb


def list_states(username, password, database):
    """list only states with a name starting with N"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM states WHERE name
        LIKE BINARY 'N%' ORDER BY id ASC""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
