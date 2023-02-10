
import requests
from pymongo import MongoClient

def get_data(url):
    response = requests.get(url)
    return response.json()

def get_all_starships(url):
    starships = []
    while url:
        data = get_data(url)
        starships += data['results']
        url = data['next']
    return starships

def update_pilots(pilots, character_urls):
    characters = []
    for url in character_urls:
        character = get_data(url)
        characters.append(character['name'])
    return characters

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']
    starship2_collection = db['starship3']

    # Get all starships from the API
    url = "https://swapi.dev/api/starships/"
    all_starships = get_all_starships(url)

    # Update the "pilots" key and insert the starships into the new collection "starship2"
    for starship in all_starships:
        if starship.get('pilots'):
            pilots = update_pilots(starship['pilots'], starship['pilots'])
            starship['pilots'] = pilots
        starship2_collection.insert_one(starship)

if __name__ == '__main__':
    main()


##########################################################################
# after we have printed the name we need to get the _id from charcaters and added to pilot

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']
    starship2_collection = db['starship3']
    characters_collection = db['characters']

    # Create a new collection "starships"
    starships_collection = db['starships_final']

    # Loop through starwars.starship2 and find the _id for each name in the "pilots" array
    for starship in starship2_collection.find({}):
        pilots = []
        for name in starship['pilots']:
            character = characters_collection.find_one({'name': name})
            if character:
                pilot = {
                    'name': name,
                    '_id': character['_id']
                }
                pilots.append(pilot)
        if pilots:
            starship['pilots'] = pilots
            starships_collection.insert_one(starship)

if __name__ == '__main__':
    main()
