import random
import pymongo

def round_start():
    # Given 目前有5位玩家A、B、C、D、E
    # When 系統確認玩家為A、B、C、D 、E 5名玩家魔法石都有5顆
    # Then 系統回合開始

    # 局初始設置：
    # 1.已洗好魔法石
    # 2.每位玩家已拿5顆魔法石
    # 3.已設定玩家血量
    # 4.已決定第一位玩家
    # 5.從剩餘魔法石取出4顆魔法石作為秘密魔法石
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

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.magician
    collection = db.player_status

    all_player_names = []
    cursor = collection.find({"group":"Yock"})
    for player_doc in cursor:
        player_name = player_doc["name"]
        all_player_names.append(player_name)

    random.shuffle(stone)
    assigned_stones = {}
    for player in all_player_names:
        assigned_stones[player] = stone[:5]
        stone = stone[5:]

    for player, stones in assigned_stones.items():
        existing_player = collection.find_one({"name": player})
        if existing_player:
            player_status = {"hold_stone":stones}
            collection.update_one({"name": player}, {"$set": player_status})
