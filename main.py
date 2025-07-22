import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

# # Tables: employee details, sales records, product information, office locations
# conn1 = sqlite3.connect("data.sqlite")
# employee_data = pd.read_sql("""SELECT * FROM employees;""",conn1)
# print("* Employee Table:")
# print(employee_data)

# conn2 = sqlite3.connect("data.sqlite")
# office_data = pd.read_sql("""SELECT * FROM offices;""",conn2)
# print("* Office Table:")
# print(office_data)

# conn3 = sqlite3.connect("data.sqlite")
# customer_data = pd.read_sql("""SELECT * FROM customers;""",conn3)
# print("* Customer Table:")
# print(customer_data)

# conn4 = sqlite3.connect("data.sqlite")
# product_data = pd.read_sql("""SELECT * FROM products;""",conn4)
# print("* Products Table:")
# print(product_data)

# conn5 = sqlite3.connect("data.sqlite")
# orders_data = pd.read_sql("""SELECT * FROM orders;""",conn5)
# print("* Order Table:")
# print(orders_data)

# conn6 = sqlite3.connect("data.sqlite")
# order_details_data = pd.read_sql("""SELECT * FROM orderdetails;""",conn6)
# print("* Order Details Table:")
# print(order_details_data)

# 1. Select the names of all employees in Boston.
q = """
SELECT firstName, lastName
FROM employees
JOIN offices
    USING(officeCode)
WHERE city = 'Boston'
;
"""
employee_boston = pd.read_sql(q, conn)
print(employee_boston)

# 2. Are there any offices that have zero employees?
q = """
SELECT
    o.officeCode,
    o.city,
    COUNT(e.employeeNumber) AS n_employees
FROM offices AS o
LEFT JOIN employees AS e
    USING(officeCode)
GROUP BY officeCode
HAVING n_employees = 0
;
"""
employees_none = pd.read_sql(q, conn)
print(employees_none)

# 3. How many customers are there per office?
q = """
SELECT
    o.officeCode,
    o.city,
    COUNT(c.customerNumber) AS n_customers
FROM offices AS o
JOIN employees AS e
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY officeCode
;
"""
customers_per_office = pd.read_sql(q, conn)
print(customers_per_office)

# 4. Display the names of every individual product that each employee has sold as a dataframe.
q = """
SELECT firstName, lastName, productName
FROM employees AS e
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
JOIN products
    USING(productCode)
;
"""
products_sold = pd.read_sql(q, conn)
print(products_sold)

# 5. Display the number of products each employee has sold.
# Alphabetize the results by employee last name.
# Use the quantityOrdered column from orderDetails.
# Think about how to group the data when some employees might have the same first or last name.
q = """
SELECT firstName, lastName, SUM(quantityOrdered) as total_products_sold
FROM employees AS e
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
GROUP BY firstName, lastName
ORDER BY lastName
;
"""
num_products_sold = pd.read_sql(q, conn)
print(num_products_sold)


# 6. Display the names of employees who have sold more than 200 different products.
q = """
SELECT firstName, lastName, COUNT(productCode) as different_products_sold
FROM employees AS e
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
GROUP BY firstName, lastName
HAVING different_products_sold > 200
ORDER BY lastName
;
"""
pd.read_sql(q, conn)
print()

conn.close()
