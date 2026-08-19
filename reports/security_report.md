# CRM Security Risk Assessment



## Executive Summary



This project evaluates the security posture of a simulated CRM environment. The assessment focuses on multi-factor authentication (MFA), administrative privileges, and least-privilege access controls.



The analysis identified three users without MFA and one user with potentially excessive administrative privileges.



Overall MFA compliance was 70%.



The highest-risk account was U007, a Sales Representative with both MFA disabled and administrative privileges enabled. This account received a risk score of 100 under the project's custom scoring model.



## Scope



The assessment analyzed a simulated CRM user dataset containing:



- User role information

- Department

- Access level

- MFA status

- Administrative privileges



No real customer or employee information was used.



## Security Findings



### Finding 1 - Missing MFA



Three of ten simulated users did not have MFA enabled:



- U003 - David Smith

- U007 - Michael Wilson

- U009 - Robert Anderson



MFA compliance was 70%.



### Finding 2 - Excessive Administrative Privileges



U007 - Michael Wilson, a Sales Representative, had administrative privileges.



This appears inconsistent with the user's role and represents a potential least-privilege violation.



### Finding 3 - High-Risk Account



U007 received a risk score of 100 because:



- MFA was disabled.

- Administrative privileges were enabled.



## Risk Assessment



| Finding | Severity | Recommendation |

|---|---|---|

| Missing MFA | Medium | Enable MFA |

| Excessive privileges | High | Remove unnecessary administrative privileges |

| Combined issue | High | Remediate both controls |



### Risk Scoring Model



- 0 points - No detected issue

- 50 points - Missing MFA

- 100 points - Missing MFA plus excessive administrative privileges



This is a simplified portfolio scoring model and is not an official industry risk-rating framework.



## Recommendations



1. Enable MFA for all CRM users.

2. Remove unnecessary administrative privileges.

3. Conduct periodic access reviews.

4. Monitor privileged accounts.

5. Establish an access-control approval process.



## Conclusion



The assessment demonstrates how Python and Pandas can be used to identify authentication and access-control weaknesses.



The analysis identified missing MFA, excessive privileges, and a high-risk account.



The project demonstrates practical application of Python, Pandas, least privilege, access-control analysis, security risk assessment, and GitHub.


