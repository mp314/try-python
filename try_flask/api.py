#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Testing microserver/API"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    ''''Return 404 if todo doesn't exist'''
    if todo_id not in TODOS:
        abort(404, message=f"Todo {todo_id} doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('task')


# Class:Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    '''Todo-class'''
    def get(self, todo_id):
        '''Get todo by id'''
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        '''Delete todo by id'''
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        '''New todo'''
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    '''Todolist class'''
    def get(self):
        '''Get todolist'''
        return TODOS

    def post(self):
        '''Add new'''
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = f'todo{todo_id}'
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
