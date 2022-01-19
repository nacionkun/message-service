# message-service

MessagingService in Python

## provision postgresql container

docker run --name pg-container -p 5432:5432 -e POSTGRES_PASSWORD=meowmeow -d postgres

## manual connect to db container

psql -h localhost -p 5432 -U postgres -d messagedb

## create db and messages table

postgres=# CREATE DATABASE messagedb;
CREATE DATABASE
postgres=#\q

CREATE TABLE messages (
	id serial PRIMARY KEY,
	message VARCHAR ( 50 ) UNIQUE NOT NULL,
	recipient VARCHAR ( 50 ) NOT NULL
);

## verify table

SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';

SELECT
   id,
   message,
   recipient
FROM
   messages;


