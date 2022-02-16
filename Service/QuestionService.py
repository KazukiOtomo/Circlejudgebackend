"""
採点・提案する処理の実装クラス
"""
import sqlite3

from Repository import QuestionDAO

instance = QuestionDAO.QuestionDAO()
instance.hello()
print(instance.get_game_id())
# print(instance.find_answer('314b8c3b-7dc3-479a-906d-8be9a8bcda4b'))





