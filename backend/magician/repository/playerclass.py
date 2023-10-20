import pymongo


class Player_repository:
    def __init__(self, except_input_name,except_input_seat,except_input_HP,except_input_score):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.player_status
        #self.player_name = player_name  # 目前不處裡同名id
        self.except_input_name = except_input_name
        self.except_input_seat = except_input_seat
        self.except_input_HP = except_input_HP
        self.except_input_score = except_input_score
        self.update_player_status(self.except_input_name,self.except_input_seat,self.except_input_HP,self.except_input_score)

    def update_player_status(self,except_input_name,except_input_seat,except_input_HP,except_input_score):
        for player_name, seat, hp , score in zip(self.except_input_name,self.except_input_seat,self.except_input_HP,self.except_input_score):
            existing_player = self.collection.find_one({"name": player_name})
            if not existing_player:
                player_status = {"name": player_name, "group": self.except_input_name,"seat":seat,"HP":hp,"score":score}
                self.collection.insert_one(player_status)
        #self.get_all_player_names()

    #def get_all_player_names(self):
    #    all_player_names = []
    #    cursor = self.collection.find({"name": self.except_input_name})
    #    # for player_doc in cursor:
    #    #     player_name = player_doc["name"]  # 目前不處裡同名id
    #    #     all_player_names.append(player_name)
    #    all_player_names = cursor[0]["group"]
    #    return all_player_names

    # class PlayerSeat:

    # self.client = pymongo.MongoClient("mongodb://localhost:27017")
    # self.db = self.client.magician
    # self.collection = self.db.player_status
    # #self.player_name = player_name
    # self.player_name = player_seat
    def test(self, player_name, player_seat):
        existing_player = self.collection.find_one({"name": player_name})
        if existing_player:
            player_status = {"seat": player_seat}
            self.collection.update_one({"name": player_name}, {"$set": player_status})
    

    def update_player_hold_stone(except_input_hold_stone,player_seat):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.magician
        collection = db.player_status

        existing_player = collection.find_one({"seat": player_seat})
        if existing_player:
        # 如果已存在相同 'name' 的记录&#xff0c;直接返回已存在的数据
            player_status = {"hold_stone":except_input_hold_stone}
            collection.update_one({"seat": player_seat}, {"$set": player_status})


# def player_status(players_name):
#    client = pymongo.MongoClient("mongodb://localhost:27017")
#    db = client.magician
#    collection = db.player_status
#
#
#    class playername:
#        def name(self):
#            existing_player = collection.find_one({"name": players_name})
#            if not existing_player:
#
#                player_status = {
#                    "name": players_name
#                }
#                collection.update_one({"name": players_name}, {"$set": player_status})
#
#            all_player_names = []
#            cursor = collection.find({})
#            for player_doc in cursor:
#                player_name = player_doc["name"]
#                all_player_names.append(player_name)
#
#            return all_player_names
#
#    class seat:
#        pass
