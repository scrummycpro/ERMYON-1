#!/bin/bash


# Run sqlite3 to fetch schema, grep to extract table names, awk to extract the second column (table name), and execute a script for each table name

sqlite3 responses.db ".schema" | grep -o -w -h "TABLE \w\+" | awk '{print $2}' | xargs -n1 -I% bash cron-get-random-id.sh % &

