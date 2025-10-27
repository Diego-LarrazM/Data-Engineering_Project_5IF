from pymongo import MongoClient, AsyncMongoClient
from urllib.parse import quote_plus
import ast
import os

class Extractor:

    HOST = os.environ.get("MONGO_HOST_NAME")
    PORT = int(os.environ.get("MONGO_PORT"))
    USERNAME = os.environ.get("MONGO_USERNAME")
    PASSWORD = os.environ.get("MONGO_PASSWORD")
    MONGO_DB = os.environ.get("MONGO_DB")
    DATA_DIR = os.environ.get("DATA_FILE_DIRECTORY")
    
    def __init__(self, host=HOST, port=PORT, username=USERNAME, password=PASSWORD):
        credentials = ""
        if username and password:
            credentials = f"{quote_plus(username)}:{quote_plus(password)}@"
        self.client = MongoClient(host = f"mongodb://{credentials}{host}:{port}/") #or AsyncMongoClient for async operations
        self.db = self.client[self.MONGO_DB]
        if not os.path.exists(self.DATA_DIR):
            raise Exception(f"Data directory {self.DATA_DIR} does not exist.")
        print(self.client.list_database_names())

    # def extract_IMDB_data(self, filename = "imdb_data.txt"): or whatever extension
    # def extract_games_metacritic_data(self, filename = "games_metac_data.txt"):
    # def extract_filmTvReviews_data(self, filename = "ftv_reviews_data.txt"):

    def insert_data(self, collection_name, filename):
        collection = self.db[collection_name]
        with open(f"{self.DATA_DIR}{filename}", "r", encoding="utf-8") as file:
            data = file.readlines()
            documents = [ast.literal_eval(line) for line in data]
            collection.insert_many(documents)