# Practice for Join Statements with SQL

## Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

Next, let's set up our code in `main.py`. Import libraries and connect to the database.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')
```

## Practice Queries

1. Select the names (first and last) of all employees in Boston.

2. Are there any offices that have zero employees?

3. How many customers are there per office?

4. Display the names of every individual product that each employee has sold as a dataframe.

5. Display the number of products each employee has sold
- Alphabetize the results by employee last name.
- Use the quantityOrdered column from orderDetails.
- Think about how to group the data when some employees might have the same first or last name.

6.  Display the names of employees who have sold more than 200 different products.