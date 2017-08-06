# python3

from flask import Flask, render_template, request

import employee_headcount as Headcount
import employee_salary as Salary
from data import employees as database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/averages', methods=['GET'])
def averages():
    employees = database.all_employees
    return Salary.average_current_salaries_as_json(employees)


@app.route('/headcount_over_time', methods=['GET'])
def headcount_over_time():
    dept = request.args.get('department', '')
    employees = database.all_employees
    return Headcount.monthly_headcount_as_json(employees, dept)


if __name__ == '__main__':
    app.run(debug=True)
