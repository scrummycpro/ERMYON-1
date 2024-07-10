#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <table_name>"
    exit 1
fi

# Assign the argument to a variable
table_name=$1

# Create folder if it doesn't exist
folder_name="${table_name}_folder"
mkdir -p "${folder_name}"

# SQLite query to select a random id and its corresponding response
query="SELECT id, response FROM ${table_name} WHERE id = (SELECT id FROM ${table_name} ORDER BY RANDOM() LIMIT 1);"

# Execute the query using sqlite3 and save output to a file
output_file="${folder_name}/${table_name}.md"
echo "# Random Response from Table '${table_name}'" > "${output_file}"
sqlite3 -batch responses.db "${query}" >> "${output_file}"

# Display message indicating where the file is saved
echo "Result saved to: ${output_file}"

