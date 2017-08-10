from models import employee_salary as Salary


class Test_average_current_salaries(object):
    def test_correctly_computes_avg_salary_by_dept(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 15,
            'dept': 'Engineering',
            'gender': 'male'
        }, {
            'date': '2015-01-01',
            'employee': 4,
            'salary': 20,
            'dept': 'Engineering',
            'gender': 'female'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 35,
            'dept': 'Design',
            'gender': 'female'
        }, {
            'date': '2015-02-01',
            'employee': 5,
            'salary': 25,
            'dept': 'Design',
            'gender': 'male'
        }]
        mean_salaries = Salary.average_current_salaries(employees)

        expected = {
            'Engineering': {
                'male': 15,
                'female': 20
            },
            'Design': {
                'male': 25,
                'female': 35
            }
        }
        assert expected == mean_salaries, '\nActual: %s\nExpected: %s' % (
            mean_salaries, expected)

    def test_only_counts_an_employees_current_position(self):
        employees = [{
            'date': '2015-01-01',
            'employee': 2,
            'salary': 15,
            'dept': 'Engineering',
            'gender': 'male'
        }, {
            'date': '2015-01-15',
            'employee': 2,
            'salary': 20,
            'dept': 'Design',
            'gender': 'male'
        }, {
            'date': '2015-02-01',
            'employee': 3,
            'salary': 35,
            'dept': 'Design',
            'gender': 'female'
        }, {
            'date': '2015-02-15',
            'employee': 3,
            'salary': 25,
            'dept': 'Sales',
            'gender': 'female'
        }]
        mean_salaries = Salary.average_current_salaries(employees)

        expected = {'Design': {'male': 20}, 'Sales': {'female': 25}}
        assert expected == mean_salaries, '\nActual: %s\nExpected: %s' % (
            mean_salaries, expected)
