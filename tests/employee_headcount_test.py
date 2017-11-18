from models import employee_headcount as Headcount
from nose.tools import assert_equal


class Test_monthly_headcounts(object):
    def test_correctly_counts_employees_per_month(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-01',
            'employee': 3,
            'salary': 10,
            'dept': 'Engineering'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 10,
            'dept': 'Engineering'
        }]

        headcount = Headcount.monthly_headcounts(employees)

        expected = {
            'data': [{
                'month': '2015-01-01',
                'headcount': 2
            }, {
                'month': '2015-02-01',
                'headcount': 3
            }]
        }
        assert_equal(headcount, expected)

    def test_does_not_count_duplicates_within_a_month(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-15',
            'employee': 2,
            'salary': 10,
            'dept': 'Design'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 10,
            'dept': 'Engineering'
        }]

        headcount = Headcount.monthly_headcounts(employees)

        expected = {
            'data': [{
                'month': '2015-01-01',
                'headcount': 1
            }, {
                'month': '2015-02-01',
                'headcount': 2
            }]
        }
        assert_equal(headcount, expected)

    def test_filters_search_by_department_if_provided(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-15',
            'employee': 2,
            'salary': 10,
            'dept': 'Design'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 10,
            'dept': 'Engineering'
        }]

        headcount = Headcount.monthly_headcounts(employees, 'design')

        expected = {'data': [{'month': '2015-02-01', 'headcount': 1}]}
        assert_equal(headcount, expected)

    def test_counts_only_most_recent_entry_for_an_employee_within_month(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-15',
            'employee': 2,
            'salary': 10,
            'dept': 'Design'
        }, {
            'date': '2015-02-15',
            'employee': 3,
            'salary': 10,
            'dept': 'Engineering'
        }]

        headcount = Headcount.monthly_headcounts(employees, 'engineering')

        expected = {'data': [{'month': '2015-02-01', 'headcount': 1}]}
        assert_equal(headcount, expected)

    def test_returns_an_empty_data_set_if_dept_name_unrecognized(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 10,
            'dept': 'Engineering'
        }]

        headcount = Headcount.monthly_headcounts(employees, 'animal husbandry')

        assert_equal(headcount, {'data': []})
