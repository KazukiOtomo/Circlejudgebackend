import os
from os.path import join, dirname

import psycopg2
from dotenv import load_dotenv

"""
DBに接続するための情報
"""
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_USER = os.environ.get("DB_USER")
DB_PORT = os.environ.get("DB_PORT")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_URI = os.environ.get("DB_URI")

# 以下、DB接続確認用テスト
class settings:

    def connect(self):
        con = psycopg2.connect("host=" + DB_HOST +
                               " port=" + DB_PORT +
                               " dbname=" + DB_DATABASE +
                               " user=" + DB_USER +
                               " password=" + DB_PASSWORD)

        return con

    def select_execute(self, con, sql):
        with con.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

        return rows


if __name__ == '__main__':
    con = settings().connect()

    sql = 'select * from admin_table'

    res = settings().select_execute(con, sql)
    for r in res:
        print(r)
