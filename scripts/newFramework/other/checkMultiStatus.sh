#!/bin/bash

# Check if directories are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 [directory1] [directory2] ..."
    exit 1
fi

# Iterate over the directories
for dir in "$@"; do
    # Check if directory exists
    if [ -d "$dir" ]; then
        echo "Running command in $dir"
        # Run your command here
        # Example: listing files in the directory
        # ls "$dir"
        crab status -d "$dir"
    else
        echo "Directory '$dir' not found"
    fi
done
