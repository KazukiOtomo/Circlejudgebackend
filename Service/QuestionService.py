"""
採点・提案する処理の実装クラス
"""
import numpy

from Repository import QuestionDAO


class calc_point:
    def __init__(self):
        print("")

    """
    DAOクラスの物を切り分け
    """

    def sample(self):
        game_id = '314b8c3b-7dc3-479a-906d-8be9a8bcda4b'
        instance = QuestionDAO.QuestionDAO()
        # TODO：sample.dbへの相対パスを指定する
        db_path = './../Repository/sample.db'

        answer_dict = instance.find_answer(game_id, db_path)
        pointList = [0, 0, 0, 0, 0, 0, 0, 0]
        number_of_answer = len(answer_dict)

        for i in range(0, number_of_answer):
            answerList = answer_dict.pop(0)
            question_id = answerList.get("question_id")
            answer = answerList.get("answer")

            pointRuleIncetance = instance.find_point_rule(question_id, db_path)
            pointRuleList = pointRuleIncetance.pop(0)
            for j in range(1, 9):
                cicle_id = "cicle_" + str(j)
                if (pointRuleList.get(cicle_id) == answer):
                    print("true")
                    tmp = pointList[j - 1]
                    pointList[j - 1] = tmp + 1
                else:
                    print("false")

        # 元の得点リスト
        print(pointList)
        point_array = numpy.array(pointList)
        sort_point_array = numpy.sort(point_array)[::-1]

        # ソート後の得点リスト
        print(sort_point_array)
        sort_point_array = numpy.argsort(point_array)[::-1]

        # ソート前におけるインデックス番号
        print(sort_point_array)


"""
テスト用
"""
if __name__ == "__main__":
    instance_calc_point = calc_point()
    instance_calc_point.sample()
