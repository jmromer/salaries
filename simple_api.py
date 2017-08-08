from flask import Flask, jsonify, render_template, request

from data import database as db
from models import employee_headcount as Headcount
from models import employee_salary as Salary

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/salaries', methods=['GET'])
def salaries():
    return jsonify(db.employees)


@app.route('/averages', methods=['GET'])
def averages():
    employees = db.employees
    return Salary.average_current_salaries_as_json(employees)


@app.route('/headcount_over_time', methods=['GET'])
def headcount_over_time():
    dept = request.args.get('department', '')
    headcounts = Headcount.monthly_headcounts(db.employees, dept)
    return jsonify(headcounts)


if __name__ == '__main__':
    app.run(debug=True)
