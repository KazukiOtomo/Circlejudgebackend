"""
質問の内容を管理するクラス
"""
import sqlite3

class QuestionDAO:
    def __init__(self):
        print(" ")

    def insert(self, question):  # question:質問内容
        # 接続。なければDBを作成する。
        conn = sqlite3.connect('sample.db')
        # カーソルを取得
        c = conn.cursor()
        # Insert実行
        c.execute(f"INSERT INTO question_list (question) VALUES ('{question}')")
        # コミット
        conn.commit()
        # コネクションをクローズ
        conn.close()

    def findAll(self):
        conn = sqlite3.connect('sample.db')
        c = conn.cursor()
        c.execute("SELECT * FROM question_list")
        conn.commit()
        print(c.fetchone())
        print(type(c.fetchone()))
        conn.close()

instance = QuestionDAO()
instance.findAll()
