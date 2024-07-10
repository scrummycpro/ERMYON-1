#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <folder_name>"
    exit 1
fi

# Assign the argument to a variable
folder_name=$1

# Iterate through each Markdown file in the specified folder
for file in "${folder_name}"/*.md; do
    if [ -f "$file" ]; then
        # Get file name without extension
        base_name=$(basename "$file" .md)
        
        # Convert Markdown to HTML using Pandoc
        output_file="${folder_name}/${base_name}_$(date +%s).html"
        pandoc "${file}" -o "${output_file}"

        # Display message indicating conversion
        echo "Converted: ${file} -> ${output_file}"
    fi
done

echo "Conversion completed."

