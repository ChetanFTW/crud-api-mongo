from flask import Blueprint, request, jsonify, abort
from bson.errors import InvalidId
from .services import UserService
from .schemas import UserSchema

users_bp = Blueprint('users', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_bp.route('', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify(users_schema.dump(users)), 200

@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = UserService.get_user_by_id(user_id)
    except InvalidId:
        abort(400, description="Invalid user ID format")
    if not user:
        abort(404, description="User not found")
    return jsonify(user_schema.dump(user)), 200

@users_bp.route('', methods=['POST'])
def create_user():
    json_data = request.get_json()
    if not json_data:
        abort(400, description="No input data provided")
    errors = user_schema.validate(json_data)
    if errors:
        return jsonify(errors), 422
    user = UserService.create_user(json_data)
    return jsonify(user_schema.dump(user)), 201

@users_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    json_data = request.get_json()
    if not json_data:
        abort(400, description="No input data provided")
    errors = user_schema.validate(json_data, partial=True)  # Partial update allowed
    if errors:
        return jsonify(errors), 422
    try:
        updated_user = UserService.update_user(user_id, json_data)
    except InvalidId:
        abort(400, description="Invalid user ID format")
    if not updated_user:
        abort(404, description="User not found or no changes made")
    return jsonify(user_schema.dump(updated_user)), 200

@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        deleted = UserService.delete_user(user_id)
    except InvalidId:
        abort(400, description="Invalid user ID format")
    if not deleted:
        abort(404, description="User not found")
    return '', 204
