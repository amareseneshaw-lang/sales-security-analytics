import pandas as pd

# Load the sales dataset
df = pd.read_csv("data/sales.csv")

# Display the first 5 records
print("=== SALES DATA ===")
print(df.head())

# Calculate total sales revenue
total_revenue = df["Sales_Amount"].sum()

print("\n=== TOTAL REVENUE ===")
print(f"${total_revenue:,.2f}")

# Calculate revenue by salesperson
revenue_by_rep = df.groupby("Sales_Rep")["Sales_Amount"].sum().sort_values(ascending=False)

print("\n=== REVENUE BY SALES REP ===")
print(revenue_by_rep)

# Calculate revenue by product
revenue_by_product = df.groupby("Product")["Sales_Amount"].sum().sort_values(ascending=False)

print("\n=== REVENUE BY PRODUCT ===")
print(revenue_by_product)

# Calculate deal conversion rate
total_deals = len(df)
closed_won_deals = len(df[df["Deal_Stage"] == "Closed Won"])

conversion_rate = (closed_won_deals / total_deals) * 100

print("\n=== DEAL CONVERSION RATE ===")
print(f"{conversion_rate:.2f}%")

# Calculate actual closed-won revenue
closed_won_revenue = df[df["Deal_Stage"] == "Closed Won"]["Sales_Amount"].sum()

print("\n=== CLOSED-WON REVENUE ===")
print(f"${closed_won_revenue:,.2f}")

# Calculate closed-won revenue by salesperson
won_revenue_by_rep = (
    df[df["Deal_Stage"] == "Closed Won"]
    .groupby("Sales_Rep")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== CLOSED-WON REVENUE BY SALES REP ===")
print(won_revenue_by_rep)