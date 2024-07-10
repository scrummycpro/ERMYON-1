#!/bin/bash
## Example: bash chron-query.sh "science" "chemistry"
## Search for the word "science" in the "chemistry" table
### You can find the table names by running sqlite3 responses.db ".schema"
### Create a static webpage with the search results: bash chron-query.sh "science" chemistry > testdoc.md && pandoc testdoc.md -o testdoc.html

# Function to display usage
usage() {
    echo "Usage: $0 [-j] <search_term> <table_name>"
    echo "  -j      Output results in JSON format"
    exit 1
}

# Initialize json variable
json=false

# Parse command-line options
while getopts "j" option; do
    case "$option" in
        j) json=true ;;
        *) usage ;;
    esac
done

# Shift to the next argument after processing options
shift $((OPTIND - 1))

# Validate input arguments
if [ $# -lt 2 ]; then
    usage
fi

# Assign input arguments to variables
search_term="$1"
table_name="$2"

# Determine output format
if [ "$json" = true ]; then
    # Execute SQLite query and format output as JSON
    sqlite3 responses.db "SELECT response FROM $table_name WHERE response LIKE '%$search_term%';" -json| jq -s '{ responses: . }'
else
    # Execute SQLite query to select response
    sqlite3 responses.db "SELECT response FROM $table_name WHERE response LIKE '%$search_term%';"
fi
