#!/bin/sh
set -e

mkdir -p "$DATA_FILE_DIRECTORY"

for file in $IMDB_FILES_TO_DOWNLOAD; do
    wget -O "$DATA_FILE_DIRECTORY$file" "$IMDB_DATA_URL$file"
    gzip -d "$DATA_FILE_DIRECTORY$file"
done

exec python ./scripts/main.py
