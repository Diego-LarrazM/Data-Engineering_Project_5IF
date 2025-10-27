FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN mkdir data

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget gzip && \
    pip install --no-cache-dir -r ./config/requirements.txt

# Download and extract directly accesible IMDB data files

VOLUME /app/data

CMD python ./scripts/main.py
# CMD ["sh", "-c", "\
#     for file in $IMDB_FILES_TO_DOWNLOAD; do \
#     wget -O /app/data/$file https://datasets.imdbws.com/$file && \
#     gzip -d /app/data/$file; \
#     done && \
#     python ./scripts/main.py"]


# docker build -t ingestion/scrapper -f DockerETL_Images\Ingestion\Scrapper\Dockerfile DockerETL_Images\Ingestion\Scrapper
# docker run --name Ingestion_Scrapper --network IngestionNet -v ./data:/app/data --rm --env-file .env ingestion/scrapper 