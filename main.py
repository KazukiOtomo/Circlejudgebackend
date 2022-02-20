from flask import Flask, jsonify, make_response, request

from Repository.QuestionDAO import QuestionDAO

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({'message': 'hello'})


## エンドポイント
@app.route('/start', methods=['GET','POST'])
def start():
    instance = QuestionDAO()
    db_path = './Repository/sample.db'
    game_id = instance.get_game_id(db_path)
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
    db_path = './Repository/sample.db'
    response = instance.find_question(question_id, db_path)
    return jsonify(response)


@app.route('/question/answer', methods=['GET','POST'])
def question_answer():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    if not game_id:
        return make_response('auth error', 400)
    question_id = body['question_id']
    result = body['result']
    if question_id in [0, 1]:
        return make_response('"question_id" is 0 or 1.', 400)
    instance = QuestionDAO()
    db_path = './Repository/sample.db'
    try:
        response = instance.insert_answer(game_id, question_id, result, db_path)
        return jsonify({'message': 'OK'})
    except:
        return jsonify({'message': 'ERROR'})


@app.route('/result', methods=['GET','POST'])
def result():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    if not game_id:
        return make_response('auth error', 400)
    instance = QuestionDAO()
    db_path = './Repository/sample.db'
    return jsonify({'game_id': game_id})


@app.route('/end', methods=['GET','POST'])
def end():
    if not request.json:
        return make_response('', 400)
    body = request.json
    game_id = body['game_id']
    if not game_id:
        return make_response('auth error', 400)
    instance = QuestionDAO()
    db_path = './Repository/sample.db'
    try:
        response = instance.deleat_gameid(game_id, db_path)
        return jsonify({'message': 'OK'})
    except:
        return jsonify({'message': 'ERROR'})


if __name__ == '__main__':
    app.run()
