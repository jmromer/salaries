import pandas as pd


def average_current_salaries_as_json(employees_list):
    """
    Compute the average current salaries in the data set employees_list.
    Return an object mapping department name to mean salary, as JSON.

    employees_list - An array of dictionaries, each including the keys
                      `date`, `employee`, `salary`, and `dept`.
    """
    # data frame for all employees
    df = pd.DataFrame(employees_list)
    df['date'] = pd.to_datetime(df['date'])

    # sort by employees and date, keeping only the most recent entry
    # for a given employee
    uniques_df = df.sort_values(
        ['employee', 'date'], ascending=[True, False]).drop_duplicates(
            subset='employee', keep='first')

    # compute mean salary for each department
    avg_salaries = uniques_df[['dept', 'salary']].groupby('dept').agg('mean')

    # return json mapping department name to mean salary
    return avg_salaries['salary'].to_json()
