import pandas as pd


def average_current_salaries(employees_list):
    """
    Compute the average current salaries in the data set employees_list.
    Return an object mapping department name to mean salary, as a
    dictionary.

    Parameters
    ----------
    employees_list - A list of dictionaries, each including the keys
                      `date`, `employee`, `salary`, and `dept`.

    Example result:
    --------------
    {
      'Design': 64000,
      'Engineering': 70000
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

    # compute mean salary for each department
    df = df[['dept', 'salary']].groupby('dept').agg('mean')

    # dict mapping department name to mean salary
    mean_salaries = {
        dept: float(mean_salary)
        for (dept, mean_salary) in df['salary'].to_dict().items()
    }

    return mean_salaries
