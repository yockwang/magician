import pymongo
import random

except_input = ["yock", "Teds", "Tux", "Leave3310", "Momo"]
except_input_seat = ["A","B","C","D","E"]
except_input_HP = ["6","6","6","6","6"]
except_input_score = [0,0,0,0,0]

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.magician
collection = db.player_status
for player_name, seat, hp, score in zip(except_input, except_input_seat, except_input_HP, except_input_score):
    existing_player = collection.find_one({"name": player_name})
    if not existing_player:
        player_status = {"name": player_name, "group": except_input, "seat": seat, "HP": hp, "score": score}
        collection.insert_one(player_status)

paired = list(zip(except_input,except_input_seat,except_input_HP,except_input_score))

randomplayer = (random.shuffle(except_input))

#print(except_input)

stone = [
    "magician1",
    "magician2","magician2",
    "magician3","magician3","magician3",
    "magician4","magician4","magician4","magician4",
    "magician5","magician5","magician5","magician5","magician5",
    "magician6","magician6","magician6","magician6","magician6","magician6",
    "magician7","magician7","magician7","magician7","magician7","magician7","magician7",
    "magician8","magician8","magician8","magician8","magician8","magician8","magician8","magician8",
]

#print("Original stone list:", stone)

# 随机洗牌
random.shuffle(stone)

# 分配石头
assigned_stones = {}
for player in except_input:
    assigned_stones[player] = stone[:5]
    stone = stone[5:]
#print(assigned_stones)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.magician
collection = db.player_status

for player, stones in assigned_stones.items():
    existing_player = collection.find_one({"name": player})
    if existing_player:
        player_status = {"hold_stone":stones}
        collection.update_one({"name": player}, {"$set": player_status})

all_player_names = []
cursor = collection.find({"group":"yock"})
for player_doc in cursor:
    player_name = player_doc["name"]
    all_player_names.append(player_name)
print(all_player_names)
#print("Assigned stones to players:")
#for player, stones in assigned_stones.items():
#    print(f"{player}: {stones}")

#print("Remaining stones:", stone)