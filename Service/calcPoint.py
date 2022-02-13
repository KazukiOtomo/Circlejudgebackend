import sqlite3

class CalcPoint:
    x = 6
    ranking = []
    def calcPoint(game_id):
        for i in range(1,6):

            # game_idを元にanswer_tableからquestion_idとanswerを取得する


            return

    def checkPointHandlerTable(question_id,answer):
        return

    def searchAnswerTable(game_id):
        corn = sqlite3.connect('sample.db')
        c = corn.cursor()
        c.execute(f"select 'game_id','question_id','answer' from 'answer_table'")