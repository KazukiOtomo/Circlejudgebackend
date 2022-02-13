"""
質問の内容を管理するクラス
"""
import sqlite3


class QuestionDAO:
    def __init__(self):
        print(" ")

    # def insert(self, question):  # question:質問内容
    #     # 接続。なければDBを作成する。
    #     conn = sqlite3.connect('sample.db')
    #     # カーソルを取得
    #     c = conn.cursor()
    #     # Insert実行
    #     c.execute(f"INSERT INTO question_list (question) VALUES ('{question}')")
    #     # コミット
    #     conn.commit()
    #     # コネクションをクローズ
    #     conn.close()

    # dict_factoryの定義
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

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


instance = QuestionDAO()
result = instance.find_question(6)
print(result)
