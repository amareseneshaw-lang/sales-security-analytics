# \# Sales \& Security Analytics

# 

# \## Overview

# 

# A portfolio project combining sales analytics and cybersecurity risk assessment using Python, Pandas, Git, and GitHub.

# 

# The project analyzes simulated sales and CRM user data to identify business performance trends and security risks.

# 

# \## Business Objectives

# 

# \- Analyze sales performance and opportunity value

# \- Identify top-performing sales representatives

# \- Analyze revenue by product

# \- Calculate sales conversion rate

# \- Measure actual Closed-Won revenue

# \- Evaluate CRM security controls

# \- Identify users without MFA

# \- Detect potentially excessive administrative privileges

# \- Assign a simplified security risk score

# 

# \## Sales Analytics

# 

# The sales analysis evaluates:

# 

# \- Total opportunity value

# \- Closed-Won revenue

# \- Revenue by sales representative

# \- Revenue by product

# \- Deal conversion rate

# 

# \### Key Sales Results

# 

# | Metric | Result |

# |---|---:|

# | Total Opportunity Value | $358,500 |

# | Closed-Won Revenue | $245,200 |

# | Conversion Rate | 66.67% |

# | Top Closed-Won Sales Rep | Maria Lopez |

# | Top Product by Opportunity Value | Cybersecurity Package |

# 

# \## Cybersecurity Assessment

# 

# The security assessment evaluates a simulated CRM environment using:

# 

# \- Multi-Factor Authentication (MFA)

# \- Administrative privileges

# \- Least-privilege access

# \- User risk scoring

# 

# \### Key Security Results

# 

# | Security Metric | Result |

# |---|---:|

# | Total Users | 10 |

# | MFA Compliance | 70% |

# | Users Without MFA | 3 |

# | Potential Excessive-Privilege Accounts | 1 |

# | Highest Risk Score | 100 |

# 

# \### Highest-Risk Finding

# 

# U007 - Michael Wilson

# 

# Role: Sales Representative

# 

# Security issues:

# 

# \- MFA disabled

# \- Administrative privileges enabled

# 

# This combination resulted in a risk score of 100 under the project's simplified scoring model.

# 

# \## Recommendations

# 

# 1\. Enable MFA for all CRM users.

# 2\. Remove unnecessary administrative privileges.

# 3\. Conduct periodic access reviews.

# 4\. Monitor privileged accounts.

# 5\. Establish an access-control approval process.

# 

# \## Technologies

# 

# \- Python

# \- Pandas

# \- Git

# \- GitHub

# \- CSV

# \- Markdown

# 

# \## Project Structure

# 

# ```text

# sales-security-analytics/

# ├── analysis/

# │   └── sales\_analysis.py

# ├── data/

# │   ├── sales.csv

# │   └── users.csv

# ├── security/

# │   └── security\_assessment.py

# ├── reports/

# │   └── security\_report.md

# ├── screenshots/

# ├── .gitignore

# └── README.md

