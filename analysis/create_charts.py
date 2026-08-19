import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("data/sales.csv")

# Filter to Closed-Won deals
closed_won = df[df["Deal_Stage"] == "Closed Won"]

# Calculate Closed-Won revenue by sales representative
revenue_by_rep = (
    closed_won.groupby("Sales_Rep")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Create the chart
plt.figure(figsize=(9, 6))
revenue_by_rep.plot(kind="bar")

plt.title("Closed-Won Revenue by Sales Representative")
plt.xlabel("Sales Representative")
plt.ylabel("Closed-Won Revenue ($)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig("screenshots/closed_won_by_rep.png", dpi=150)

plt.close()

print("Chart created: screenshots/closed_won_by_rep.png")

import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("data/sales.csv")

# Calculate revenue by product
revenue_by_product = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Create the chart
plt.figure(figsize=(9, 6))
revenue_by_product.plot(kind="bar")

plt.title("Sales Value by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount ($)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

# Save chart
plt.savefig("screenshots/revenue_by_product.png", dpi=150)

plt.close()

print("Chart created: screenshots/revenue_by_product.png")


import pandas as pd
import matplotlib.pyplot as plt

# Load CRM user data
users = pd.read_csv("data/users.csv")

# Count MFA status
mfa_counts = users["MFA_Enabled"].value_counts()

# Create the chart
plt.figure(figsize=(8, 6))
mfa_counts.plot(kind="bar")

plt.title("CRM Multi-Factor Authentication Status")
plt.xlabel("MFA Enabled")
plt.ylabel("Number of Users")
plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
plt.savefig("screenshots/mfa_compliance.png", dpi=150)

plt.close()

print("Chart created: screenshots/mfa_compliance.png")
import pandas as pd
import matplotlib.pyplot as plt

# Load CRM user data
users = pd.read_csv("data/users.csv")


# Calculate security risk score
def calculate_risk(row):
    score = 0

    if row["MFA_Enabled"] == "No":
        score += 50

    if row["Admin_Privileges"] == "Yes" and "Administrator" not in row["Role"]:
        score += 50

    return score


users["Risk_Score"] = users.apply(calculate_risk, axis=1)

# Sort users by risk
risk_data = users.sort_values("Risk_Score", ascending=False)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    risk_data["Employee_Name"],
    risk_data["Risk_Score"]
)

plt.title("CRM User Security Risk Scores")
plt.xlabel("Employee")
plt.ylabel("Risk Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
plt.savefig("screenshots/security_risk_scores.png", dpi=150)

plt.close()

print("Chart created: screenshots/security_risk_scores.png")
