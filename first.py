import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db  = client['starwars']

#character_name= db.characters.find({},{"height":1,"mass":1,"_id":0})
#avg_female = db.characters.aggregate([{"$match":{"gender":"female"}},{"$group":{"_id":"$gender", "avg_height":{"$avg":"$height"}}}])


########## here we are removing all the unknow values in height and mass  #########################
#db.characters.update_many({"height":"unknown"},{"$unset":{"height":""}})
#db.characters.update_many({"mass":"unknown"},{"$unset":{"mass":""}})


############ set height field to int version of original###########################
#db.characters.update_many({},[{"$set": {"height":{"$toInt": "$height"}}}])


# sort out the comma problem
#db.characters.update_one({"mass":"1,358"}, {"$set": {"mass": "1358"}})

# convert mass to double
#db.characters.update_many({},[{"$set": {"mass":{"$toDouble": "$mass"}}}])


all_character= db.characters.find({},{"height":1,"mass":1,"_id":0})


for character in all_character:
  print(character)













#character_name= db.characters.find({"gender":"female"},{"height":1,"mass":1,"_id":0})
# for person in character_name:
#   print(person)

###############################################################################################
# 1) Find the height of Darth Vader, only return results for the name and the height.
# character_name= db.characters.find({"name":"Darth Vader"},{"name":1,"height":1,"_id":0})
# for person in character_name:
#   print(person)


# 2) Find all characters with yellow eyes, only return results for the names of the characters.
# character_name= db.characters.find({"eye_color":"yellow"},{"name":1,"_id":0})

# 3) Find male characters. Limit your results to only show the first 3.
# character_name= db.characters.find({"gender":"male"},{"name":1,"gender":1,"_id":0}).limit(3)


# 4) Find the names of all the humans whose homeworld is Alderaan.
# character_name= db.characters.find({"species.name":"Human","homeworld.name":"Alderaan"},{"name":1,"_id":0})


###########using and for Q4 ##################
#Alderaan = db.characters.find({
#     "$and":[
#         {"species.name": "Human"},
#         {"homeworld.name": "Alderaan"}]},
#         {"name":1, "_id": 0})
# for a in Alderaan:
#     print(a)

#################################################################

# characters = db.characters.find({})
# character_name= db.characters.find({"species.name":"Droid"},{"name":1,"species.name":1,"_id":0})
# for person in character_name:
#   print(person)


##################################################################
#mycol = mydb["customers"]
# mydict = [{ "name": "solmaz", "address": "hammond st" },
#           { "name": "nahid", "address": "98 phillips st" }]
# x = mycol.insert_many(mydict)

# mycol.delete_many(mydict)
# x = mycol.insert_one(mydict)

# print(x.inserted_id)
# for x in mycol.find():
#   print(x)