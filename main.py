from flask import Flask, jsonify, make_response, request, render_template
from flask_cors import CORS

from Repository.QuestionDAO import QuestionDAO
from Repository.AdminUserDAO import AdminUserDAO

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/hello')
def hello():
    return jsonify({'message': 'hello'})


# admin
@app.route('/admin/login')
def admin_home():
    return render_template('admin/login.html')


@app.route("/admin/home", methods=["POST"])
def admin_posted():
    user_id = request.form["user_id"]
    user_pass = request.form["user_pass"]
    instance = AdminUserDAO()
    db_path = './Repository/sample.db'
    user = instance.find_user(user_id ,user_pass ,db_path)
    if not user:
        message = "認証エラー"
        return render_template('admin/home.html', message=message)
    else:
        message = user['user_id']
        return render_template('admin/home.html', message=message)


@app.route("/admin/sql_result", methods=["POST"])
def admin_sql_result():
    sql = request.form["sql"]
    instance = AdminUserDAO()
    db_path = './Repository/sample.db'
    sql_result = instance.do_sql(sql ,db_path)
    message = sql_result['message']
    result = sql_result['result']
    keys = sql_result['keys']
    is_ok = sql_result['is_ok']
    keys_len = len(keys)
    result_len = len(result)
    return render_template('admin/sql_result.html', message=message, result={'is_ok': is_ok,'result_len': result_len,'keys_len': keys_len}, keys=keys, result_list=result)

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
