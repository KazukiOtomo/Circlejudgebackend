import unittest

from flask import jsonify

import main
import json


class Test(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get(self):
        response = self.app.get('/hello')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['message'] == 'hello'

    # def test_post(self):
    #     params = {'game_id': 1, 'question_id': 1}
    #     rv = self.app.post('/question', json={
    #         'game_id': 1, 'question_id': 1
    #     })
    #     json_data = rv.get_json()
    #     print(json_data)
    #     assert json_data == None

    def test_question(self):
        # send data as POST form to endpoint
        sent = {'game_id': 1, 'question_id': 1}
        result = self.app.post(
            '/question',
            data=sent
        )
        # check result from server with expected data
        print(result.data)

    # 回答(result)が0,1以外の時に401エラーが出せればOK
    def test_question_bad(self):
        sent = json.dumps({'game_id': 1, 'question_id': 1, 'result': 2})
        result = self.app.post(
            'question/answer',
            data=sent,
            content_type='application/json'
        )
        print(result.status_code)
        assert result.status_code == 401

    def test_start(self):
        # send data as POST form to endpoint
        sent = {'game_id': 1}
        result = self.app.post(
            '/start',
            data=sent
        )
        # check result from server with expected data
        print(result.data)


if __name__ == '__main__':
    unittest.main()
