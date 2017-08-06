import json

from models import employee_headcount as Headcount
from nose.tools import assert_equal


class TestEmployeeSalary(object):
    def test_monthly_headcount_as_json(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }]
        expected = {'data': [{'month': '2015-01-01', 'headcount': 1}]}
        headcount = Headcount.monthly_headcount_as_json(employees)
        assert_equal(expected, json.loads(headcount))
