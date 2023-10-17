import os
from pydantic import BaseSettings

class DbConfig(BaseSettings):
    db_host: str = os.environ.get("DB_HOST", "tech_db")
    db_port: int = int(os.environ.get("DB_PORT", 5432))
    db_username: str = os.environ.get("DB_USERNAME", "tech_user")
    db_password: str = os.environ.get("DB_PASSWORD", "tech_password")
    db_database: str = os.environ.get("DB_DATABASE", "tech_db")

db_config = DbConfig()