from http import HTTPStatus

from flask import Blueprint, jsonify, request

from models.Task import Task
from models.User import User

page = Blueprint('users', __name__)


@page.get('/')
def get_users():
    users = User.all()
    return jsonify([user.serialize() for user in users]), HTTPStatus.OK


@page.get('/<uuid:user_id>')
def get_user(user_id):
    user = User.get(user_id)
    return jsonify(user.serialize()), HTTPStatus.FOUND


@page.post('/')
def create_user():
    data = request.json
    try:
        user = User.create(data)
        return jsonify(user.serialize()), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'message': f'Missing arguments {e}'}), HTTPStatus.CONFLICT


@page.put('/<uuid:user_id>')
def update_user(user_id):
    data = request.json
    user = User.update(user_id, data)
    return jsonify(user.serialize()), HTTPStatus.ACCEPTED


@page.delete('/<uuid:user_id>')
def delete_user(user_id):
    user = User.delete(user_id)
    return jsonify(user.serialize()), HTTPStatus.ACCEPTED


@page.get('/<uuid:user_id>/tasks')
def get_user_tasks(user_id):
    tasks = Task.get_by_user(user_id)
    return jsonify([task.serialize() for task in tasks]), HTTPStatus.OK


@page.post('/<uuid:user_id>/tasks')
def create_user_task(user_id):
    data = request.json
    try:
        task = Task.create(user_id, data)
        return jsonify(task.serialize()), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'message': f'Missing arguments {e}'}), HTTPStatus.CONFLICT
