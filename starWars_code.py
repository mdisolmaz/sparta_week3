import requests
import pymongo
from bson.objectid import ObjectId

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["starwars_db"]
characters_collection = db["characters"]
starships_collection = db["starships"]

# Define the function to fetch all the starships from the API
def get_all_starships():
    url = "https://swapi.dev/api/starships/"
    response = requests.get(url)
    return response.json()

# Define the function to replace the "pilots" key with a list of ObjectIDs
def replace_pilots_with_object_ids(starships):
    for starship in starships:
        pilot_urls = starship["pilots"]
        pilot_ids = []
        for url in pilot_urls:
            character = characters_collection.find_one({"url": url})
            if character:
                pilot_ids.append(character["_id"])
        starship["pilots"] = pilot_ids
    return starships

# Define the function to insert the starships into the collection
def insert_starships_into_collection(starships):
    for starship in starships:
        result = starships_collection.insert_one(starship)
        print(f"Inserted starship with ID: {result.inserted_id}")

# Call the functions to retrieve and store the starships
starships_data = get_all_starships()
starships = starships_data["results"]
starships = replace_pilots_with_object_ids(starships)
insert_starships_into_collection(starships)