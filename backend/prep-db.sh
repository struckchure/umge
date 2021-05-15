#!/bin/sh

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql postgresql-contrib

# set db

psql \
-c CREATE DATABASE umge_db; \
	CREATE USER ${POSTGRES_USER} WITH PASSWORD ${POSTGRES_USER_PASSWORD}; \
	ALTER ROLE ${POSTGRES_USER} SET client_encoding TO 'utf8'; \
	ALTER ROLE ${POSTGRES_USER} SET default_transaction_isolation TO 'read committed'; \
	ALTER ROLE ${POSTGRES_USER} SET timezone TO 'UTC'; \
	GRANT ALL PRIVILEGES ON DATABASE myproject TO ${POSTGRES_USER}; \
