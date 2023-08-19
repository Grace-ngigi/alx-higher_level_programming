#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the query to retrieve states sorted by id
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
