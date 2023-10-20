import pymongo

class warehouse_repository:
    def __init__(self,Number_of_magic_stones):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.warehouse
        self.Number_of_magic_stone = Number_of_magic_stones

        self.collection.insert_one(Number_of_magic_stones)