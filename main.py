from flask import Flask, jsonify, make_response, request, render_template, redirect
from flask_cors import CORS

from Repository.QuestionDAO import QuestionDAO
from Repository.AdminUserDAO import AdminUserDAO

from Service.QuestionService import QuestionService

import settings

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/hello')
def hello():
    return jsonify({'message': 'hello'})


## エンドポイント
@app.route('/start', methods=['GET', 'POST'])
def start():
    instance = QuestionDAO()
    game_id = instance.get_game_id()
    return jsonify({'game_id': game_id})


@app.route('/question', methods=['GET', 'POST'])
def question():
    if not request.json:
        return make_response('', 400)

    body = request.json
    game_id = body['game_id']

    if not game_id:
        return make_response('auth error', 400)
    question_id = body['question_id']
    instance = QuestionDAO()
    response = instance.find_question(question_id)
    return jsonify(response)


@app.route('/question/answer', methods=['GET', 'POST'])
def question_answer():
    if not request.json:
        return make_response('not json', 402)

    body = request.json
    game_id = body['game_id']

    if not game_id:
        return make_response('auth error', 400)
    question_id = body['question_id']
    result = body['result']

    if result not in [0, 1]:
        return make_response('"result" is 0 or 1.', 401)
    instance = QuestionDAO()
    try:
        response = instance.insert_answer(game_id, question_id, result)
        return jsonify({'message': 'OK'})
    except:
        return jsonify({'message': 'ERROR'})


@app.route('/result', methods=['GET', 'POST'])
def result():
    if not request.json:
        return make_response('not json', 402)

    body = request.json
    game_id = body['game_id']

    if not game_id:
        return make_response('auth error', 401)

    instance = QuestionService()
    result_circle_list = instance.calc_point(game_id)
    return jsonify({'ranking': result_circle_list})


@app.route('/end', methods=['GET', 'POST'])
def end():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    if not game_id:
        return make_response('auth error', 400)
    instance = QuestionDAO()
    try:
        response = instance.deleat_gameid(game_id)
        return jsonify({'message': 'OK'})
    except:
        return jsonify({'message': 'ERROR'})


if __name__ == '__main__':
    app.run()
