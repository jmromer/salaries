import pandas as pd


def monthly_headcounts(employees_list, department=None):
    """
    Calculate monthly head counts from the data set `employees_list`.
    Return a list of records within a dictionary nested under "data".

    If a department is specified, calculate monthly head counts only for that
    department.

    Parameters:
    ----------
    employees_list - A list of dictionaries, each including the keys
                     `date`, `dept`, `employee`, `salary`, and `gender`.

    department - An optional department name, as a String

    Example result:
    --------------
    {
      'data': [
        {'month': '2015-05-01', 'headcount': 5},
        {'month': '2015-06-01', 'headcount': 6}
      ]
    }
    """
    # yapf: disable
    df = (pd
          .DataFrame(employees_list)
          .pipe(date_to_datetime)
          .pipe(add_month_from_date)
          .pipe(sort_by_month_keeping_latest)
          .pipe(restrict_search_to_department, department)
          .pipe(map_months_to_employee_headcounts))
    # yapf: enable

    # convert to a list of records
    headcounts_list = df.to_dict(orient='records')
    return {'data': headcounts_list}


def map_months_to_employee_headcounts(df):
    """Map months to employee counts."""
    df.copy()
    df = df[['month', 'employee']].groupby('month').agg('count')
    df.rename(columns={'employee': 'headcount'}, inplace=True)
    df.insert(0, 'month', [time.strftime('%Y-%m-%d') for time in df.index])
    return df


def date_to_datetime(df):
    """Convert date string to datetime object."""
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    return df


def add_month_from_date(df):
    """Add 'month' column with month-truncated date."""
    df = df.copy()
    df['month'] = df['date'].apply(lambda date: date.replace(day=1))
    return df


def sort_by_month_keeping_latest(df):
    """
    Sort by month and keep only the last entry for a given employee within
    the month (for cases where an employee transitions between departments
    within the month).
    """
    df = df.copy()
    df = df.sort_values('date', ascending=True)
    df = df.drop_duplicates(subset=['month', 'employee'], keep='last')
    return df


def restrict_search_to_department(df, department=None):
    """
    Limit search to a particular department if a department is provided
    """
    if department is None:
        return df
    df = df.copy()
    department_name = department.lower()
    df['dept'] = df['dept'].apply(lambda name: name.lower())
    df = df[df.dept == department_name]
    return df
