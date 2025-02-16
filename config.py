import os

from dotenv import load_dotenv

ENVIRONMENT = os.getenv("ENVIRONMENT", default="prod")
if ENVIRONMENT == "prod":
    load_dotenv(".env", verbose=True)
else:
    load_dotenv(".env.dev", verbose=True)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

API_URL = os.getenv('API_URL')
GEO_API_URL = os.getenv('GEO_API_URL')
COUNTRIES = os.getenv('COUNTRIES').split(',')
THRESHOLD = os.getenv('THRESHOLD')

DATE_FORMAT = "%Y-%m-%d"

RPDM_LOG_RECIPIENTS = os.getenv('RPDM_LOG_RECIPIENTS')

GMAIL_HOST = os.getenv('GMAIL_HOST')
GMAIL_PORT = os.getenv('GMAIL_PORT')
GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
GMAIL_PROTOCOL = os.getenv('GMAIL_PROTOCOL')

DAYS_TO_FETCH = int(os.getenv('DAYS_TO_FETCH'))

FILE_RESOURCES_PATH = "file_resources"

RUN_IN_PARALLEL = os.getenv('RUN_IN_PARALLEL', default="False").lower() in ['true', '1', 't', 'y', 'yes']
