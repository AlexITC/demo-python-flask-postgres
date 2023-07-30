from http import HTTPStatus

from flask import Blueprint, jsonify, request

from models.Task import Task

page = Blueprint('tasks', __name__)


@page.get('/')
def get_tasks():
    tasks = Task.all()
    return jsonify([task.serialize() for task in tasks]), HTTPStatus.OK


@page.get('/<uuid:task_id>')
def get_task(task_id):
    task = Task.get(task_id)
    return jsonify(task.serialize()), HTTPStatus.FOUND


@page.put('/<uuid:task_id>')
def update_task(task_id):
    data = request.json
    task = Task.update(task_id, data)
    return jsonify(task.serialize()), HTTPStatus.ACCEPTED


@page.delete('/<uuid:task_id>')
def delete_task(task_id):
    task = Task.delete(task_id)
    return jsonify(task.serialize()), HTTPStatus.ACCEPTED
