from flask import Flask, render_template, jsonify, make_response, request
import requests
import json
import os

from Repository.QuestionDAO import QuestionDAO

app = Flask(__name__)


@app.route('/hello')
def hello():
    return jsonify({'message': 'hello'})


## エンドポイント
@app.route('/start', methods=['GET','POST'])
def start():
    instance = QuestionDAO()
    game_id = instance.get_game_id()
    return jsonify({'game_id': game_id})


@app.route('/question', methods=['GET','POST'])
def question():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    if not game_id:
        return make_response('auth error', 400)
    question_id = body['question_id']
    instance = QuestionDAO()
    game_id = instance.find_question(question_id)
    return jsonify({'game_id': game_id, 'question_id': question_id})
# curl -X POST -H "Content-Type: application/json" -d '{"question_id":"abfb4da9-fcdb-4951-943f-5d483b079e57", "game_id":"1"}' http://localhost:5000/question

@app.route('/question/answer', methods=['GET','POST'])
def question_answer():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    question_id = body['question_id']
    result = body['result']
    return jsonify({'game_id': game_id, 'question_id': question_id, 'result': result})


@app.route('/result', methods=['GET','POST'])
def result():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    return jsonify({'game_id': game_id})

@app.route('/end', methods=['GET','POST'])
def end():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    return jsonify({'game_id': game_id})


if __name__ == '__main__':
    app.run()
