import pandas as pd

# Load the CRM user dataset
users = pd.read_csv("data/users.csv")

print("=== CRM USER SECURITY ASSESSMENT ===")
print(users)

# Find users without Multi-Factor Authentication
mfa_risks = users[users["MFA_Enabled"] == "No"]

print("\n=== USERS WITHOUT MFA ===")
print(mfa_risks[["User_ID", "Employee_Name", "Role"]])

# Find non-administrative users with admin privileges
privilege_risks = users[
    (users["Admin_Privileges"] == "Yes") &
    (~users["Role"].str.contains("Administrator"))
]

print("\n=== POTENTIAL EXCESSIVE PRIVILEGE ===")
print(privilege_risks[["User_ID", "Employee_Name", "Role", "Admin_Privileges"]])

# Calculate security metrics
total_users = len(users)
users_without_mfa = len(mfa_risks)
excessive_privilege_count = len(privilege_risks)

mfa_compliance = ((total_users - users_without_mfa) / total_users) * 100

print("\n=== SECURITY METRICS ===")
print(f"Total users: {total_users}")
print(f"Users without MFA: {users_without_mfa}")
print(f"MFA compliance: {mfa_compliance:.2f}%")
print(f"Potential excessive-privilege accounts: {excessive_privilege_count}")

# Calculate a simple security risk score
def calculate_risk(row):
    score = 0

    if row["MFA_Enabled"] == "No":
        score += 50

    if row["Admin_Privileges"] == "Yes" and "Administrator" not in row["Role"]:
        score += 50

    return score


users["Risk_Score"] = users.apply(calculate_risk, axis=1)

print("\n=== USER RISK SCORES ===")
print(
    users[
        ["User_ID", "Employee_Name", "Role", "MFA_Enabled",
         "Admin_Privileges", "Risk_Score"]
    ].sort_values("Risk_Score", ascending=False)
)