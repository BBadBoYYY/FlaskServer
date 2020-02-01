# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 下午5:06
# @Author  : Hui
# @File    : app.py

from flask import Flask,jsonify


app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries django',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python flask',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=False)