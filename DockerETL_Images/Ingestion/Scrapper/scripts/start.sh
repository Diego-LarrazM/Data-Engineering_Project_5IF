#!/bin/sh
set -e

mkdir -p "$DATA_FILE_DIRECTORY"

echo "\n[Downloading] IMDB datasets from $IMDB_DATA_URL"
echo "[Saving files] to $DATA_FILE_DIRECTORY\n"

if [ -z "$IMDB_FILES_TO_DOWNLOAD" ]; then
    raise "No files specified for download. Please set IMDB_FILES_TO_DOWNLOAD in the .env file."
fi

for file in $IMDB_FILES_TO_DOWNLOAD; do
    echo "[Processing $file]"
    if [ -f "$DATA_FILE_DIRECTORY$file" ]; then
        echo "[Skipping] $DATA_FILE_DIRECTORY$file already exists.\n"
        continue
    fi
    wget -O "$DATA_FILE_DIRECTORY$file.tsv.gz" "$IMDB_DATA_URL$file.tsv.gz"
    gzip -d "$DATA_FILE_DIRECTORY$file.tsv.gz"
    mv "$DATA_FILE_DIRECTORY$file.tsv" "$DATA_FILE_DIRECTORY$file"

done

echo "\nAll files downloaded and decompressed successfully.\n"
exec python ./scripts/main.py
