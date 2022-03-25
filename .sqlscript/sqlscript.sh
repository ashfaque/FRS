#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE frsdb;
    GRANT ALL PRIVILEGES ON DATABASE frsdb TO root;
EOSQL