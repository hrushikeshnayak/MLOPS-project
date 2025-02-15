import os
from datetime import date
from dotenv import load_dotenv
load_dotenv()


MODEL_FILE_NAME = "model.pkl"
db_name = "US_visa"

collection_name = "Visa_data"

MONGODB_URL_KEY = os.getenv("collection_URL")

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2