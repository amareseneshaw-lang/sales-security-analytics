import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("database/sales_security.db")

# Load CSV files
sales = pd.read_csv("data/sales.csv")
users = pd.read_csv("data/users.csv")

# Create database tables
sales.to_sql("sales", connection, if_exists="replace", index=False)
users.to_sql("users", connection, if_exists="replace", index=False)

print("Database created successfully.")
print("Sales records:", len(sales))
print("User records:", len(users))

connection.close()