"""
Adminを管理するクラス
"""
from msilib.schema import tables
import sqlite3

from peewee import *
from peewee import IndexMetadata
from playhouse.dataset import DataSet
from playhouse.migrate import migrate

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
            if 'select' in sql or 'SELECT' in sql:
                c.execute(sql)
                result_dict = c.fetchall()
                conn.close()
                # keyを取得
                result_dict_key_list = list(result_dict[0].keys())
                return {'is_ok': True, 'message': f"成功 \n Done : \n {sql}", 'result': result_dict, 'keys': result_dict_key_list}
            else:
                c.execute(sql)
                conn.close()
                return {'is_ok': True, 'message': f"成功 \n Done : \n {sql}", 'result': [], 'keys': []}
        except Exception as e:
            return {'is_ok': False, 'message': f"失敗 \n ERROR : \n {e} \n SQL : {sql}", 'result': [], 'keys': []}


    def get_tables_name(self, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        c.execute("select name from sqlite_master where type = 'table'")
        result_dict = c.fetchall()
        table_name_list = []
        for data in result_dict:
            if 'sqlite_' not in data['name']: 
                table_name_list.append(data['name'])
        conn.close()
        table_name_list.sort()
        return table_name_list

    
    def get_indexes(self, table, db_path):
        dataset = DataSet(db_path)
        return dataset._database.get_indexes(table)

    def get_columns(self, table, db_path):
        dataset = DataSet(db_path)
        return dataset._database.get_columns(table)

    # def get_foreign_keys(self, table, db_path):
    #     dataset = DataSet(db_path)
    #     return dataset._database.get_foreign_keys(table)

    # dict_factoryの定義
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d