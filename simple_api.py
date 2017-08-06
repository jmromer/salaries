# python3

import pandas as pd
from flask import Flask, jsonify, render_template, request

from data import employees as data

app = Flask(__name__)


def unique_employees(dataframe):
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    return dataframe.sort_values(
        ['employee', 'date'], ascending=[True, False]).drop_duplicates(
            subset='employee', keep='first')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/averages', methods=['GET'])
def averages():
    uniques_df = unique_employees(pd.DataFrame(data.all_employees))
    avg_salaries = uniques_df[['dept', 'salary']].groupby('dept').agg('mean')
    return avg_salaries['salary'].to_json()


@app.route("/headcount_over_time", methods=['GET'])
def headcount_over_time():
    return 'headcount'


if __name__ == '__main__':
    app.run(debug=True)
