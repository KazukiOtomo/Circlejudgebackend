"""
質問の内容を管理するクラス
"""
import uuid
import sqlite3

import psycopg2
from psycopg2.extras import DictCursor

from settings import settings


class QuestionDAO:
    def __init__(self):
        print(" ")

    """
    最初のみ実行し、game_idを発行する
    @:return game_id
    @:済
    """

    def get_game_id(self):
        con = settings().connect()

        while (True):
            # UUIDの発行(ランダム)
            game_id = str(uuid.uuid4())

            sql = f"select count (game_id) from answer_table where game_id = '{game_id}'"

            with con.cursor() as cur:
                con.cursor().execute(sql)
                try:
                    cur.fetchone()
                except psycopg2.ProgrammingError:
                    break

        return game_id

    """
    回答内容INSERTメソッド
    @:済
    """

    def insert_answer(self, game_id, question_number, answer_flag):
        con = settings().connect()
        sql = f"insert into answer_table values ('{game_id}',{question_number},{answer_flag})"

        with con.cursor() as cur:
            con.cursor().execute(sql)
        con.commit()

    """
    質問番号から質問内容を引き出すメソッド
    @:済
    """

    # return dict [ {'question_id': 質問番号, 'question': 質問内容'},{......}]
    def find_question(self, question_number):
        con = settings().connect()
        sql = f"SELECT * FROM question_list where question_id = {question_number}"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            question_dict = []
            for row in results:
                question_dict.append(dict(row))

        return question_dict

    """
    引数の　game_idから、answer_tableの内容を検索してソートした後に、辞書型に変換して返す（find_questionを参考にどうぞ）
    @:param game_id
    @:return answer_dict
    @:済
    """

    def find_answer(self, game_id):
        con = settings().connect()

        sql = f"SELECT * FROM answer_table where game_id = '{game_id}'"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            answer_dict = []
            for row in results:
                answer_dict.append(dict(row))

        return answer_dict

    """
    引数の　question_idから、point_ruleを検索して、辞書型に変換して返す
    @:param question_id
    @:return answer_dict
    @:済
    """

    def find_point_rule(self, question_id):
        con = settings().connect()

        sql = f"SELECT * FROM point_rule where question_id = '{question_id}'"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            answer_dict = []
            for row in results:
                answer_dict.append(dict(row))

        return answer_dict

    """
    @:済
    """

    def delete_gameid(self, game_id):
        con = settings().connect()

        sql = f"DELETE FROM answer_table WHERE game_id = '{game_id}'"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
        return 0

    """
    circle_listを検索してレコード数（サークル数）を返す
    @:return answer_dict
    @:済
    """

    def get_number_of_circles(self):
        con = settings().connect()
        sql = f"SELECT COUNT ('circlr_id') FROM circle_list"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            results = cur.fetchall()
            answer_dict = []
            for row in results:
                answer_dict.append(dict(row))

        return answer_dict

    """
    @:済
    """

    def get_circle_name(self, circle_id):
        con = settings().connect()
        sql = f"select circle_name from circle_list where circle_id = {circle_id}"

        with con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            circle_name = cur.fetchone()[0]
        return circle_name


if __name__ == '__main__':
    instance = QuestionDAO()
    result = instance.get_circle_name(3)
    print(result)
