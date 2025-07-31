#!/bin/bash

# Check for argument
if [ -z "$1" ]; then
  echo "Usage: $0 <DirectoryName>"
  exit 1
fi

dirname="$1"
pyfile="${1}.py"

# Create directory and data subdir
mkdir -p "$dirname/data"

# Create (or touch) Python file
touch "$dirname/$pyfile"

echo "Created directory: $dirname"
echo "Created subdirectory: $dirname/data"
echo "Created Python file: $dirname/$pyfile"
