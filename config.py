from dotenv import load_dotenv
import os

load_dotenv()

# ==============================
# ServiceNow Configuration
# ==============================

INSTANCE = os.getenv("SERVICENOW_INSTANCE")
USERNAME = os.getenv("SERVICENOW_USERNAME")
PASSWORD = os.getenv("SERVICENOW_PASSWORD")

# ==============================
# Amazon Bedrock Configuration
# ==============================

AWS_REGION = os.getenv("AWS_REGION", "eu-central-1")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "eu.amazon.nova-2-lite-v1:0")
