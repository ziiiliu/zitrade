from sqlalchemy import create_engine
import os
from configparser import ConfigParser
from dotenv import load_dotenv

CONFIG_SECTION = "db"
load_dotenv()

class DBManager:
    def __init__(self, cfg: ConfigParser):
        host = os.environ.get('DB_HOST')
        port = cfg.get(CONFIG_SECTION, "DB_PORT")
        user = cfg.get(CONFIG_SECTION, "DB_USER")
        password = os.environ.get('DB_PASSWORD')
        url = f"postgresql://{user}:{password}@{host}:{port}"
        self.db_engine = create_engine(url=url)
    