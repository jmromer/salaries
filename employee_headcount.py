import json

import pandas as pd


def monthly_headcount_as_json(employees_list, department=None):
    # data frame for all employees
    df = pd.DataFrame(employees_list)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].apply(lambda x: x.replace(day=1))

    # sort by month and keep only the last entry for a given employee within
    # the month (for cases where an employee transitions to another department
    # within the month).
    sorted_uniques_df = df.sort_values(
        'month', ascending=True).drop_duplicates(
            subset=['month', 'employee'], keep='last')

    # map months to employee counts
    headcounts_df = sorted_uniques_df[['month', 'employee'
                                       ]].groupby('month').agg('count')

    # rename employee count column to 'headcount'
    headcounts_df.rename(columns={'employee': 'headcount'}, inplace=True)

    # insert months as a string column in first position
    headcounts_df.insert(0, 'month', [
        time.strftime('%Y-%m-%d') for time in headcounts_df.index
    ])

    return json.dumps({'data': headcounts_df.to_dict(orient='records')})
