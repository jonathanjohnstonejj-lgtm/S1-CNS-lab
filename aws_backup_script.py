"""
Demo backup script for CNS secret detection testing.

NOTE:
All credentials below are FAKE and for testing purposes only.
"""

import boto3

# Fake credentials for testing secret detection
AWS_ACCESS_KEY_ID = "AKIAU5LH5ROW2YR5AOA6"
AWS_SECRET_ACCESS_KEY = "aWoy9swh5qDnRv7hGbea9XKO5bxkRNUtcVAYEIc5"

# Fake database configuration
DB_HOST = "prod-database.company.internal"
DB_USER = "backup_admin"
DB_PASSWORD = "Password123!"

# Fake API key
API_KEY = "sk-demo-1234567890abcdef1234567890"

BUCKET_NAME = "company-backups"


def backup_data():
    print("Connecting to AWS...")
    print(f"Uploading backup to {BUCKET_NAME}")


if __name__ == "__main__":
    backup_data()