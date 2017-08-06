# python3

from flask import Flask, jsonify
from flask import Flask, jsonify, render_template, request

from data import employees

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/averages', methods=['GET'])
def averages():
    return jsonify(employees.all_employees)


@app.route("/headcount_over_time", methods=['GET'])
def headcount_over_time():
    return 'headcount'


if __name__ == '__main__':
    app.run(debug=True)
