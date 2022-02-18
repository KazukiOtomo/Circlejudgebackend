import unittest
import main
from flask import Flask, render_template, jsonify, make_response
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

    def test_main(self):
        # send data as POST form to endpoint
        sent = {'game_id': 1, 'question_id': 1}
        result = self.app.post(
            '/question',
            data=sent
        )
        # check result from server with expected data
        print(result.data)

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