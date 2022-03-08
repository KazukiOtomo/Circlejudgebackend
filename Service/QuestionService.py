"""
採点・提案する処理の実装クラス
"""
import sys
import os

import numpy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Repository.QuestionDAO import QuestionDAO


class QuestionService:
    def __init__(self):
        print("")

    """
    DAOクラスの物を切り分け
    """

    def calc_point(self, game_id):
        instance = QuestionDAO()
        numberOfCircleInstance = instance.get_number_of_circles()
        numberOfCircleList = numberOfCircleInstance.pop(0)
        answer_dict = instance.find_answer(game_id)

        numberOfCircle = numberOfCircleList.get('count')

        pointList = [0] * numberOfCircle
        number_of_answer = len(answer_dict)

        for i in range(0, number_of_answer):
            answerList = answer_dict.pop(0)
            question_id = answerList.get("question_id")
            answer = answerList.get("answer")

            pointRuleIncetance = instance.find_point_rule(question_id)
            pointRuleList = pointRuleIncetance.pop(0)
            for j in range(0, numberOfCircle):
                cicle_id = "cicle_" + str(j + 1)
                if (pointRuleList.get(cicle_id) == answer):
                    # print("true")
                    tmp = pointList[j]
                    pointList[j] = tmp + 1

        for k in range(0, numberOfCircle):
            tmp = pointList[k]
            pointList[k] = (tmp / float(number_of_answer))
            #     print("true")
            #     tmp = pointList[j - 1]
            #     pointList[j - 1] = tmp + 1
            # else:
            #     print("false")

        # 元の得点リスト
        print(pointList)
        point_array = numpy.array(pointList)
        sort_point_array = numpy.sort(point_array)[::-1]

        # ソート後の得点リスト
        print(sort_point_array)
        sort_point_array = numpy.argsort(point_array)[::-1]

        # ソート前におけるインデックス番号
        print(sort_point_array)

        # とりあえずTOP3の出力
        first = instance.get_circle_name(sort_point_array[0])
        second = instance.get_circle_name(sort_point_array[1])
        third = instance.get_circle_name(sort_point_array[2])

        # result(main.py)に返す値(list)
        result_circle_list = []
        for index in sort_point_array:
            result_circle_list.append({'name': instance.get_circle_name(sort_point_array[index])})
        return result_circle_list


if __name__ == "__main__":
    instance = QuestionService()
    instance.calc_point('176ae382-e61c-41db-bc0a-e0233921bc80')
