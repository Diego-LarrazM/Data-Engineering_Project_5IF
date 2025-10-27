from extractor import Extractor



if __name__ == "__main__":
    extractor = Extractor()
    #extractor.extract_IMDB_data()
    #extractor.extract_games_metacritic_data()
    #extractor.extract_filmTvReviews_data()

    # Image Testing
    extractor.insert_data("test_collection", "test.txt")