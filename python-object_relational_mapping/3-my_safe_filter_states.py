#!/usr/bin/python3
"""
Module for filtering states by user input (safe from SQL injection)
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and filter states by name safely
    """
    # Validate 4 arguments
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    try:
        # Connect to MySQL database
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        # Create cursor and execute safe query with parameters
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id", 
            (sys.argv[4],)
        )

        # Display results
        for row in cursor.fetchall():
            print(row)

        # Close connections
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
