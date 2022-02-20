"""
質問の内容を管理するクラス
"""
import sqlite3


class AdminUserDAO:
    def __init__(self):
        print(" ")

    def find_user(self, user_id, user_pass, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        c.execute(f"SELECT * FROM admin_table where user_id = '{user_id}' AND user_pass = '{user_pass}'")
        user_dict = c.fetchone()
        conn.close()
        return user_dict


    def do_sql(self, sql, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        try:
            c.execute(sql)
            conn.close()
            return f"Done : {sql}"
        except Exception as e:
            return f"ERROR : {e} \n SQL : {sql}"



    # dict_factoryの定義
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d