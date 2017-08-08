from models import employee_salary as Salary


class Test_average_current_salaries(object):
    def test_correctly_computes_avg_salary_by_dept(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 15,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-01',
            'employee': 4,
            'salary': 20,
            'dept': 'Engineering'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 35,
            'dept': 'Design'
        }, {
            'date': '2015-02-01',
            'employee': 5,
            'salary': 25,
            'dept': 'Design'
        }]
        mean_salaries = Salary.average_current_salaries(employees)

        expected = {'Engineering': 17.5, 'Design': 30}
        assert expected == mean_salaries, '\nActual: %s\nExpected: %s' % (
            mean_salaries, expected)

    def test_only_counts_an_employees_current_position(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 15,
            'dept': 'Engineering'
        }, {
            'date': '2015-01-15',
            'employee': 2,
            'salary': 20,
            'dept': 'Design'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 35,
            'dept': 'Design'
        }, {
            'date': '2015-02-15',
            'employee': 3,
            'salary': 25,
            'dept': 'Sales'
        }]
        mean_salaries = Salary.average_current_salaries(employees)

        expected = {'Design': 20, 'Sales': 25}
        assert expected == mean_salaries, '\nActual: %s\nExpected: %s' % (
            mean_salaries, expected)
