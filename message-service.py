#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

dsn = "host={} dbname={} user={} password={}".format("localhost", "messagedb", "postgres", "meowmeow")

def test_connect():
    try:
        connection = psycopg2.connect(dsn)
        cur = connection.cursor()

        postgres_insert_query = """ INSERT INTO messages (ID, MESSAGE, RECIPIENT) VALUES (%s,%s,%s)"""
        record_to_insert = (1, 'This is a test message.', 'Kosmo Kramer')
        cur.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into messages table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into messages table", error)

    finally: 
        # closing database connection.
        if connection:
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
def main():
    print("Message service")
    test_connect()


if __name__ == "__main__":
    main()
