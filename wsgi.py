#!flask
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

application = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy Groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@application.route("/")
def hello():
    return "Hello World BRUNELLO!"


@application.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@application.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@application.route('/masks', methods=['POST'])
def masks_task():
    return "Mask Task  BRUNELLO!"

@application.route('/tasks', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': u'Milk_Pizza', 
        'done': False
    }
    tasks.append(task)
    return "End Post Procedure"

#    if not request.json or not 'title' in request.json:
#         abort(400)
#    task = {
#        'id': tasks[-1]['id'] + 1,
#        'title': request.json['title'],
#        'description': request.json.get('description', ""),
#        'done': False
#    }
#    tasks.append(task)
#    return jsonify({'task': task})


@application.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@application.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == "__main__":
    application.run()
