import pymongo

class warehouse_repository:
    def __init__(self,except_input_name=None,secret_stone=None,stone=None):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.warehouse
        self.secret_stone = secret_stone
        self.stone = stone
        self.gruop = except_input_name

    def set_warehouse_secret_stone(self,secretstone):
        existing_group = self.collection.find_one({"group": self.gruop})
        if not existing_group:
            secret_warehouse_status = {"group":self.gruop, "secret_stone":secretstone}
            self.collection.insert_one(secret_warehouse_status)

    def get_warehouse_secret_stone(self,group):
        cursor = self.collection.find_one({"group":group})
        secret_stone = cursor["secret_stone"]
        return secret_stone


    def set_warehouse_stone(self,last_stone):
        existing_group = self.collection.find_one({"group": self.gruop})
        if existing_group:
            last_warehouse_status = {"last_stone":last_stone}
            self.collection.update_one({"group": self.gruop}, {"$set": last_warehouse_status})

    def get_warehouse_stone(self,group):
        cursor = self.collection.find_one({"group":group})
        last_stone = cursor["last_stone"]
        return last_stone
