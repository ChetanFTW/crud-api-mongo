from . import mongo
from bson.objectid import ObjectId
from .models import User

class UserService:
    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        return [User.from_dict(user) for user in users]

    @staticmethod
    def get_user_by_id(user_id):
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return User.from_dict(user)
        return None

    @staticmethod
    def create_user(data):
        result = mongo.db.users.insert_one(data)
        return User.from_dict(mongo.db.users.find_one({'_id': result.inserted_id}))

    @staticmethod
    def update_user(user_id, data):
        result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': data})
        if result.modified_count == 1:
            return UserService.get_user_by_id(user_id)
        return None

    @staticmethod
    def delete_user(user_id):
        result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count == 1
