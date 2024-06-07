from bson import ObjectId
from pymongo import MongoClient
import re
from jukebox.Song import Song


class Dao_song():
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.col = MongoClient(connection_string)["jukebox"]["songs"]

    def create(self, room):
        self.col.insert_one(room.__dict__)

    def read_by_id(self, _id):
        song = Song(**self.col.find_one({_id: ObjectId(_id)}))
        return song

    def read_all(self):
        songs = [Song(**song) for song in self.col.find({})]
        return songs

    def read_by_regex(self, regex):
        self.col.find({
            "$or": [
                {"name": {"$regex": re.compile(re.escape(query), re.IGNORECASE)}},
                {"interpret": {"$regex": re.compile(re.escape(query), re.IGNORECASE)}},
                {"album": {"$regex": re.compile(re.escape(query), re.IGNORECASE)}},
                {"genre": {"$regex": re.compile(re.escape(query), re.IGNORECASE)}}
            ]
        })

    def update(self, song):
        self.col.update_one({"_id": song._id}, {"$set": song.__dict__})

    def delete(self, song):
        return self.col.delete_one({"_id": song._id})
