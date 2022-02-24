"""
Adminを管理するクラス
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
        c.execute("select name from sqlite_master where type = 'table' ORDER BY name ASC")
        result_dict = c.fetchall()
        table_name_list = []
        for data in result_dict:
            if 'sqlite_' not in data['name']: 
                table_name_list.append(data['name'])
        conn.close()
        return table_name_list

    
    def get_table_col_info(self, table_name, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        c.execute(f"PRAGMA table_info('{table_name}')")
        result_dict = c.fetchall()
        return result_dict

    
    def get_table_create_sql(self, table_name, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        c.execute(f"select * from sqlite_master where type = 'table' and name='{table_name}'")
        result_dict = c.fetchall()
        return result_dict


    # dict_factoryの定義
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d