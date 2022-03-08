import psycopg2
from psycopg2.extras import DictCursor

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from settings import settings

def do_sql(sql):
    con = settings().connect()
    with con.cursor() as cur:
        con.cursor().execute(sql)
    con.commit()

def read_sql_file(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
        return s

def main():
    dir_name = os.path.dirname(__file__)
    path = dir_name + "/do_sql.sql"
    sql = read_sql_file(path)
    try:
        do_sql(sql)
        print("sqlを正常に実行しました。")
    except Exception as e:
        print("エラー \n " + str(e))

if __name__ == "__main__":
    main()