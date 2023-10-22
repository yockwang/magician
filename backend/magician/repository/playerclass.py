import pymongo


class Player_repository:
    def __init__(self, except_input_name=None,except_input_seat=None,except_input_HP=None,except_input_score=None): #資料內容名稱可以重改
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.player_status
        self.except_input_name = except_input_name
        self.except_input_seat = except_input_seat
        self.except_input_HP = except_input_HP
        self.except_input_score = except_input_score        
        # self.update_player_status()

    # def __init__(self,player):
    #     self.client = pymongo.MongoClient("mongodb://localhost:27017")
    #     self.db = self.client.magician
    #     self.collection = self.db.player_status
    #     self.except_input_name = player
    #     self.gather_status()
        

    def update_player_status(self):
        for player_name, seat, hp, score in zip(self.except_input_name,self.except_input_seat,self.except_input_HP,self.except_input_score):
            existing_player = self.collection.find_one({"name": self.except_input_name})
            if not existing_player:
                player_status = {"name": player_name, "group": self.except_input_name,"seat":seat,"HP":hp,"score":score}
                self.collection.insert_one(player_status)
        #self.get_all_player_names()

    def get_all_player_names(self):
        all_player_names = []
        cursor = self.collection.find({"name": self.except_input_name})
        # for player_doc in cursor:
        #     player_name = player_doc["name"]  # 目前不處裡同名id
        #     all_player_names.append(player_name)
        all_player_names = cursor[0]["group"]
        return all_player_names

    def gather_status(self):
        cursor = self.collection.find({"name": self.except_input_name})
        self.except_input_seat = cursor[0]["seat"]
        self.except_input_HP = cursor[0]["HP"]
        self.except_input_score = cursor[0]["score"]        

    def update_player_hand_stone(self, hand_stone): #set_hand_stone
        existing_player = self.collection.find_one({"name": self.except_input_name})
        if existing_player:
            player_status = {"hand_stone": hand_stone}
            self.collection.update_one({"name": self.except_input_name}, {"$set": player_status})
            return existing_player["name"]
        else:
            return -1
    
    def get_hand_stone(self):
        existing_hand_stone = self.collection.find_one({"name": self.except_input_name})

        return existing_hand_stone["hand_stone"]

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
