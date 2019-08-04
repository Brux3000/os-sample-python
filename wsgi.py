#!flask
from flask import Flask, jsonify

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


@apppplication.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    application.run()
