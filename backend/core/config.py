from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Setting(BaseSettings):
     api_v1_prefix: str = "/api"
     db_url: str = f"postgresql:///{BASE_DIR}/db.sqlite3"
     #"postgresql://ivlad:050266@localhost:5432/ad_campaign_db"
     db_echo: bool = True
     api_port: int = 8000

settings = Setting()