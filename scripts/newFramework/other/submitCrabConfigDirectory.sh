# !/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "At least one directory is necessary to submit crab configs from."
    exit 1
fi

for dir in "$@"; do
    if [ ! -d "$dir" ]; then
        echo "Directory '$dir' does not exist"
        continue
    fi

    find "$dir" -type f -name "*.py" -exec echo "Submitting crab config on: {}" \; -exec crab submit -c {} \;
done