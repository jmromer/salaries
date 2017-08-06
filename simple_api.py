# python3

from flask import Flask, jsonify

from data import employees

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return """
    <h1>Available routes</h1>
    <h2><pre>/averages</pre></h2>
    Returns JSON mapping from a department name to that department's
    average current salary.

    <h2><pre>/headcount_over_time[?department=DEPT_NAME]</pre></h2>
    Returns a headcount grouped by month.
    Accepts an optional query param <code>department</code> to filter the list.
    """


@app.route('/averages', methods=['GET'])
def averages():
    return jsonify(employees.all_employees)


@app.route("/headcount_over_time", methods=['GET'])
def headcount_over_time():
    return 'headcount'


if __name__ == '__main__':
    app.run(debug=True)
