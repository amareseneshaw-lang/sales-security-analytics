import pandas as pd
from datetime import datetime

# Load CRM user data
users = pd.read_csv("data/users.csv")

audit_records = []

for _, user in users.iterrows():

    risk_score = 0
    findings = []
    recommendations = []

    # Check MFA
    if user["MFA_Enabled"] == "No":
        risk_score += 50
        findings.append("MFA disabled")
        recommendations.append("Enable MFA")

    # Check excessive privileges
    if (
        user["Admin_Privileges"] == "Yes"
        and "Administrator" not in user["Role"]
    ):
        risk_score += 50
        findings.append("Potential excessive administrative privilege")
        recommendations.append("Review and remove unnecessary admin privileges")

    # Determine risk level
    if risk_score >= 100:
        risk_level = "High"
    elif risk_score >= 50:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # Create audit record
    audit_records.append({
        "Audit_Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User_ID": user["User_ID"],
        "Employee_Name": user["Employee_Name"],
        "Role": user["Role"],
        "Risk_Score": risk_score,
        "Risk_Level": risk_level,
        "Findings": "; ".join(findings) if findings else "No issues detected",
        "Recommendations": "; ".join(recommendations) if recommendations else "No action required"
    })

# Create audit log
audit_log = pd.DataFrame(audit_records)

# Save audit log
audit_log.to_csv("security/audit_log.csv", index=False)

print("=== SECURITY AUDIT LOG GENERATED ===")
print(f"Records created: {len(audit_log)}")
print("File: security/audit_log.csv")