"""
質問の内容を管理するクラス
"""
import sqlite3
import uuid

class QuestionDAO:
    def __init__(self):
        print(" ")

    """
    最初のみ実行するINSERTメソッド
    @:return game_id
    """

    def get_game_id(self):
        conn = sqlite3.connect('./sample.db')
        c = conn.cursor()
        # UUIDが被らなくなるまでループ
        while(True):
            # UUIDの発行(ランダム)
            game_id = str(uuid.uuid4())
            dupli_flag = c.execute(f"select * from answer_table where game_id = '{game_id}'")
            # SELECE文に引っかからない ＝ dupli_flagはNone
            if dupli_flag.fetchone() == None:
                break
        conn.close()
        return game_id

    """
    2度目以降用のINSERTメソッド
    """

    def insert_answer(self, game_id, question_number, answer_flag):
        conn = sqlite3.connect('sample.db')
        c = conn.cursor()
        c.execute(f"insert into answer_table values ('{game_id}',{question_number},{answer_flag})")
        conn.commit()
        conn.close()

    """
    後に利用するメソッド
    """
    # dict_factoryの定義
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    """
    質問番号から質問内容を引き出すメソッド
    """

    # return dict [ {'question_id': 質問番号, 'question': 質問内容'},{......}]
    def find_question(self, question_number):
        conn = sqlite3.connect('sample.db')
        # row_factoryの変更(dict_factoryに変更)
        conn.row_factory = self.dict_factory

        c = conn.cursor()
        c.execute(f"SELECT * FROM question_list where question_id = {question_number}")

        question_dict = c.fetchall()
        conn.close()
        return question_dict

    """
    引数の　game_idから、answer_tableの内容を検索してソートした後に、辞書型に変換して返す（find_questionを参考にどうぞ）
    @:param game_id
    @:return answer_dict
    """

    def find_answer(self, game_id):
        conn = sqlite3.connect('./sample.db')
        conn.row_factory = self.dict_factory
        c = conn.cursor()

        c.execute(f"SELECT * FROM answer_table where game_id = '{game_id}'")
        answer_dict = c.fetchall()
        conn.close()
        return answer_dict

    """
    引数の　question_idから、point_ruleを検索して、辞書型に変換して返す
    @:param question_id
    @:return answer_dict
    """
    def find_point_rule(self,question_id):
        conn = sqlite3.connect('./sample.db')
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        c.execute(f"SELECT * FROM point_rule where question_id = '{question_id}'")
        answer_dict = c.fetchall()
        conn.close()
        return answer_dict


# 以下開発実験用コード
game_id = '314b8c3b-7dc3-479a-906d-8be9a8bcda4b'
instance = QuestionDAO()
answerInstance = instance.find_answer(game_id)
numberOfAnswer = len(answerInstance)
pointList = [0,0,0,0,0,0,0,0]
for i in range(0,numberOfAnswer):
    answerList = answerInstance.pop(0)
    question_id = answerList.get("question_id")
    answer = answerList.get("answer")
    pointRuleIncetance = instance.find_point_rule(question_id)
    pointRuleList = pointRuleIncetance.pop(0)
    for j in range(1,9):
        cicle_id = "cicle_"+str(j)
        if(pointRuleList.get(cicle_id)==answer):
            print("true")
            tmp = pointList[j-1]
            pointList[j-1] = tmp+1
        else:
            print("false")
print(pointList)