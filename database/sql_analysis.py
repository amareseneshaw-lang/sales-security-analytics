import sqlite3

connection = sqlite3.connect("database/sales_security.db")
cursor = connection.cursor()

print("=== SQL SALES ANALYSIS ===")

cursor.execute("""
    SELECT SUM(Sales_Amount)
    FROM sales
""")

total_sales = cursor.fetchone()[0]
print(f"Total Sales Value: ${total_sales:,.2f}")

cursor.execute("""
    SELECT SUM(Sales_Amount)
    FROM sales
    WHERE Deal_Stage = 'Closed Won'
""")

closed_won = cursor.fetchone()[0]
print(f"Closed-Won Revenue: ${closed_won:,.2f}")

cursor.execute("""
    SELECT
        Sales_Rep,
        SUM(Sales_Amount) AS Closed_Won_Revenue
    FROM sales
    WHERE Deal_Stage = 'Closed Won'
    GROUP BY Sales_Rep
    ORDER BY Closed_Won_Revenue DESC
""")

print("\n=== CLOSED-WON REVENUE BY SALES REP ===")

for rep, revenue in cursor.fetchall():
    print(f"{rep}: ${revenue:,.2f}")

cursor.execute("""
    SELECT User_ID, Employee_Name, Role
    FROM users
    WHERE MFA_Enabled = 'No'
""")

print("\n=== USERS WITHOUT MFA - SQL ===")

for user_id, name, role in cursor.fetchall():
    print(f"{user_id}: {name} - {role}")

cursor.execute("""
    SELECT User_ID, Employee_Name, Role
    FROM users
    WHERE Admin_Privileges = 'Yes'
      AND Role NOT LIKE '%Administrator%'
""")

print("\n=== POTENTIAL EXCESSIVE PRIVILEGE - SQL ===")

for user_id, name, role in cursor.fetchall():
    print(f"{user_id}: {name} - {role}")
# Calculate security risk scores using SQL
cursor.execute("""
    SELECT
        User_ID,
        Employee_Name,
        Role,
        MFA_Enabled,
        Admin_Privileges,
        CASE
            WHEN MFA_Enabled = 'No'
                 AND Admin_Privileges = 'Yes'
                 AND Role NOT LIKE '%Administrator%'
                THEN 100
            WHEN MFA_Enabled = 'No'
                THEN 50
            WHEN Admin_Privileges = 'Yes'
                 AND Role NOT LIKE '%Administrator%'
                THEN 50
            ELSE 0
        END AS Risk_Score
    FROM users
    ORDER BY Risk_Score DESC
""")

print("\n=== SQL SECURITY RISK SCORES ===")

for row in cursor.fetchall():
    print(row)

connection.close()