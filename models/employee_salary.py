from collections import defaultdict

import pandas as pd


def average_current_salaries(employees_list):
    """
    Compute the average current salaries in the data set employees_list.
    Return an object mapping department name to mean salary by gender, as a
    dictionary.

    Parameters
    ----------
    employees_list - A list of dictionaries, each including the keys
                      `date`, `dept`, `employee`, `salary`, and `gender`.

    Example result:
    --------------
    {
      'Design': {'male': 64000, 'female': 95000},
      'Engineering': {'male': 33000.67, 'female': 22000.33}
    }
    """
    # data frame for all employees
    df = pd.DataFrame(employees_list)
    df['date'] = pd.to_datetime(df['date'])

    # sort by employees and date, keeping only the most recent entry
    # for a given employee
    df = df.sort_values(
        ['employee', 'date'], ascending=[True, False]).drop_duplicates(
            subset='employee', keep='first')

    # compute mean salary for each department, grouped by gender
    df = df[['dept', 'salary', 'gender']].groupby(['dept',
                                                   'gender']).agg('mean')

    mean_salaries = defaultdict(dict)
    for ((dept, gender), mean_salary) in df['salary'].to_dict().items():
        mean_salaries[dept][gender] = round(mean_salary, 2)

    return dict(mean_salaries)
