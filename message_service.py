#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

dsn = "host={} dbname={} user={} password={}".format("localhost", "messagedb", "postgres", "meowmeow")

def send_message(dsc, id, message, recipient):
    print("Sending message...")
    try:
        cur = dsc.cursor()
        pg_insert_query = """ INSERT INTO messages (ID, MESSAGE, RECIPIENT) VALUES (%s,%s,%s)"""
        record_to_insert = (id, message, recipient)
        cur.execute(pg_insert_query, record_to_insert)
        dsc.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into messages table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into messages table", error)

    finally: 
        cur.close()

def read_message():
    try:
        print("")
    except():
        print("")
    finally:
        print("")


def list_messages(dsc):
    print("Listing messages...")
    try:
        cur = dsc.cursor()
        cur.execute("SELECT * FROM messages;")
        for record in cur:
            print(record)

    except (Exception, psycopg2.Error) as error:
        print("Failed to read records from messages table", error)

    finally:
        cur.close()
    

def delete():
    try:
        print("")
    except():
        print("")
    finally:
        print("")


def connect(dsn):
    print("Connecting to DB.")
    try:
        dsc = psycopg2.connect(dsn)
    except (Exception, psycopg2.Error) as error:
        print("Failed to connect to database!")
    finally:
        print("DB connection opened.")
        return dsc

def disconnect(dsc):
    print("Disconnecting from DB.")
    if dsc:
        dsc.close()
        print("DB connection is closed.")

   
def main():
    dsc = connect(dsn)
    list_messages(dsc)
    # send_message(dsc, 5, "This is a test message1.", "Kosmo Kramer")
    # send_message(dsc, 6, "This is a test send1.", "kk@gmail.com")
    # send_message(dsc, 7, "This is a test communication1.", "1234567890")
    # send_message(dsc, 8, "This is a test action1.", "user_name_kosmo78")
    # list_messages(dsc)
    disconnect(dsc)



if __name__ == "__main__":
    main()
