# ==========================================
# PART 1: CONNECTING TO THE DATA
# ==========================================

# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Add code below and run file to see data from employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# ==========================================
# PART 2: BASIC SELECT FILTERING
# ==========================================

# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
# Select last name before employee number
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)


# ==========================================
# PART 3: ALIASING IN SELECT
# ==========================================

# STEP 4
# Rename employeeNumber column as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)


# ==========================================
# PART 4: CASE FUNCTION
# ==========================================

# STEP 5
# Use CASE to bin job titles into Executive vs Not Executive
df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN jobTitle = 'President' 
              OR jobTitle = 'VP Sales' 
              OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# ==========================================
# PART 5: BUILT-IN FUNCTIONS - STRINGS
# ==========================================

# STEP 6
# Select the first name and the length of the first name
df_name_length = pd.read_sql("""
    SELECT firstName, LENGTH(firstName) AS name_length 
    FROM employees
""", conn)

# STEP 7
# Select the job title and a shortened 5-character version of it
df_short_title = pd.read_sql("""
    SELECT jobTitle, SUBSTR(jobTitle, 1, 5) AS short_title 
    FROM employees
""", conn)


# ==========================================
# PART 6: BUILT-IN FUNCTIONS - NUMERICS
# ==========================================

# Add the code below and run the file to see order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Find total amount by summing rounded total prices
# FIX: Sum the columns directly in SQL so we can return a Series with an integer index [0]
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_sum
    FROM orderDetails
""", conn)['total_sum']

# STEP 9
# Break out order dates into day, month, and year columns
# FIX: Shifted SQLite SUBSTR indices to properly parse YYYY-MM-DD
df_day_month_year = pd.read_sql("""
    SELECT 
        orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)
