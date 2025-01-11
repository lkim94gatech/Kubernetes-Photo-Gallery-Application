import os

# Bucket configuration
BUCKET_NAME = os.getenv("BUCKET_NAME")
ACCESS_KEY_USERNAME = os.getenv("ACCESS_KEY")
SECRET_KEY_PASSWORD = os.getenv("SECRET_KEY")
STORAGE_HOST = os.getenv("STORAGE_HOST")
STORAGE_HOST_PORT = os.getenv("STORAGE_HOST_PORT")
STORAGE_HOST_EXT = os.getenv("STORAGE_HOST_EXT")
STORAGE_PORT_EXT = os.getenv("STORAGE_PORT_EXT")

# MySQL Configuration
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT"))
DB_TABLE = os.getenv("DB_TABLE")
