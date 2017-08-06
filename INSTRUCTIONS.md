The vast majority of our app involves the user requesting some data that
requires us to do some manipulation on the backend before returning it to the
user. Imagine we have some simple datastructure with columns:

    - Employee ID
    - Salary
    - Effective Date
    - Department

Note that Employee ID is a unique identifier for the individual person. A
person joins the company when their employee ID has its first effective date.
If the same ID has multiple effective dates, that may be a result of getting a
raise, or switching departments within the company.

Assume that the company has no employees other than the ones in the data, and
that no one leaves the company after they join.

Your task is to write a small backend server with two endpoints:

    /averages

and

    /headcount_over_time

The /averages endpoint should accept a GET request and return the *average
current salary* of employees broken down by department, eg

    {
      "Design": 64000,
      "Engineering": 70000
    }

The /headcount_over_time endpoint should accept GET requests along with a
possible parameter 'department'. It should return the headcount of the
organization for each month, possibly filtered by the value of the 'department'
parameter. It should return something like:

    {
      "data": [
        {"month": "2015-05-01",
        "headcount": 5},
        {"month": "2015-06-01",
        "headcount": 6},
        ...
      ]
    }

Please use python for this task, though feel free to use whichever
librarys/frameworks you like. As for the data, pretend the variable
'employee_data' is output from querying the database for all records.

The server should get up and running by just running this file with `python
simple_api.py` from the command-line.
