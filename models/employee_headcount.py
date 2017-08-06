import json

import pandas as pd


def monthly_headcount_as_json(employees_list, department=None):
    """
    Calculate monthly head counts from the data set employees_list.
    Return a list of records as JSON.

    If a department is specified, calculate monthly head counts only for that
    department.

    Parameters:
    ----------
    employees_list - A list of dictionaries, each including the keys
                     `date`, `employee`, `salary`, and `dept`.

    department - An optional department name, as a String

    Example JSON:
    ------------
    {
      "data": [
        {"month": "2015-05-01",
        "headcount": 5},
        {"month": "2015-06-01",
        "headcount": 6},
        ...
      ]
    }
    """
    # data frame for all employees
    df = pd.DataFrame(employees_list)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].apply(lambda x: x.replace(day=1))

    # limit search to a particular department if a department is provided
    if department:
        department_name = department.lower()
        df['dept'] = df['dept'].apply(lambda x: x.lower())
        df = df[df.dept == department_name]

    # sort by month and keep only the last entry for a given employee within
    # the month (for cases where an employee transitions between departments
    # within the month).
    sorted_uniques_df = df.sort_values(
        'month', ascending=True).drop_duplicates(
            subset=['month', 'employee'], keep='last')

    # map months to employee counts
    headcounts_df = sorted_uniques_df[['month', 'employee'
                                       ]].groupby('month').agg('count')

    # rename employee count column to 'headcount'
    headcounts_df.rename(columns={'employee': 'headcount'}, inplace=True)

    # insert months as a column of strings in first position
    headcounts_df.insert(0, 'month', [
        time.strftime('%Y-%m-%d') for time in headcounts_df.index
    ])

    # convert to a list of records
    headcounts_dict = headcounts_df.to_dict(orient='records')

    return json.dumps({'data': headcounts_dict})
