import json

from nose.tools import assert_equal

from simple_api import app


class TestSimpleAPI(object):
    def setup(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        assert_equal(200, response.status_code)
        assert_equal(True, '<html>' in str(response.data))

    def test_averages(self):
        response = self.app.get('/averages')
        response_json = json.loads(response.data)
        assert_equal(200, response.status_code)
        assert isinstance(response_json, dict)

    def test_headcount_over_time(self):
        response = self.app.get('/headcount_over_time')
        response_json = json.loads(response.data)
        assert_equal(200, response.status_code)
        assert 'data' in response_json, 'results are not within a "data" key'
        assert isinstance(response_json['data'], list)
