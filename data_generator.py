import pandas as pd
import numpy as np

def generate_mock_data():
    np.random.seed(42)
    n_records = 1500

    towers = ['Infrastructure', 'Application Support', 'HR Shared Services', 'Finance Operations', 'Customer Success']

    categories = {
        'Infrastructure': ['L1 Password Reset', 'Server Provisioning', 'Access Access/IAM', 'Network Troubleshooting', 'Status Meetings'],
        'Application Support': ['Bug Fixing', 'Deployment Support', 'Database Querying', 'Code Review', 'Daily Standup'],
        'HR Shared Services': ['Onboarding Admin', 'Payroll Inquiries', 'Leave Processing', 'Benefits Review', 'Sync Meetings'],
        'Finance Operations': ['Invoice Matching', 'Expense Auditing', 'Vendor Setup', 'Monthly Closing', 'Team Alignments'],
        'Customer Success': ['Ticket Escalation', 'CRM Data Entry', 'Onboarding Calls', 'Retention Strategy', 'Review Meetings']
    }

    data = []
    for _ in range(n_records):
        tower = np.random.choice(towers)
        category = np.random.choice(categories[tower])

        is_meeting = 'Meeting' in category or 'Standup' in category or 'Alignment' in category or 'Sync' in category
        task_type = 'Meeting' if is_meeting else 'Ops Ticket'

        hours = np.random.exponential(scale=3.5) if not is_meeting else np.random.uniform(0.5, 2.0)
        hours = max(0.5, round(hours, 1))

        data.append({
            'Tower': tower,
            'Category': category,
            'Task_Type': task_type,
            'Hours_Spent': hours,
            'Complexity': np.random.choice(['Low', 'Medium', 'High'], p=[0.5, 0.3, 0.2])
        })

    df = pd.DataFrame(data)
    df.to_csv('synthetic_data.csv', index=False)
    return df

if __name__ == "__main__":
    generate_mock_data()
    print("Synthetic data generated successfully!")