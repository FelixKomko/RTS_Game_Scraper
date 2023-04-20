from pymongo import MongoClient 




class ScrapyRTSPipeline:

    def __init__(self):
        client = MongoClient('-----')
        self.db = client.RTS_games

        
    def process_item(self, item, spider):
        
        collection_RTS_games = self.db[f'{spider.name}']

        if not len(list(self.db[f'{spider.name}'].find({"game_name" : item["game_name"]}))):
            collection_RTS_games.insert_one(item)
        else:
            print(f'This game is already in the database: {item["game_name"]}')

        return item
