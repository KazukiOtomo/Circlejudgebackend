import sqlite3


# データベース名
dbname = './Repository/sample.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS answer_table")
cur.execute("create table answer_table( game_id varchar(64) , question_id integer NOT NULL , answer boolean NOT NULL , PRIMARY KEY (game_id,question_id) )")

cur.execute("DROP TABLE IF EXISTS question_list")
cur.execute("create table question_list( question_id integer primary key autoincrement , question varchar(64) )")

cur.execute("insert into answer_table values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b',1,true)")
cur.execute("insert into question_list (question) values ('ポケモンコンテストに参加したい')")

conn.commit()

# データベースへのコネクションを閉じる。(必須)
conn.close()