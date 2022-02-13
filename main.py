from flask import Flask, render_template, jsonify, make_response
import requests
import json
import os

app = Flask(__name__)


@app.route('/hello')
def hello():
    return jsonify({'message': 'hello'})


## エンドポイント
@app.route('/start', methods=['GET','POST'])
def start():
    return jsonify({'message': 'start'})


@app.route('/question', methods=['GET','POST'])
def question():
    if not requests.json:
        return make_response('', 400)
    body = requests.json
    game_id = body['game_id']
    question_id = body['question_id']
    return jsonify({'game_id': game_id, 'question_id': question_id})


@app.route('/hello/answer', methods=['GET','POST'])
def question_answer():
    if not requests.json:
        return make_response('', 400)
    body = requests.json
    game_id = body['game_id']
    question_id = body['question_id']
    result = body['result']
    return jsonify({'game_id': game_id, 'question_id': question_id, 'result': result})


@app.route('/result', methods=['GET','POST'])
def result():
    if not requests.json:
        return make_response('', 400)
    body = requests.json
    game_id = body['game_id']
    return jsonify({'game_id': game_id})

@app.route('/end', methods=['GET','POST'])
def end():
    if not requests.json:
        return make_response('', 400)
    body = requests.json
    game_id = body['game_id']
    return jsonify({'game_id': game_id})


if __name__ == '__main__':
    app.run()
