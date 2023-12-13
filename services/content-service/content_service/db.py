from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select, insert
import os
from configparser import ConfigParser
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from structs import Odds

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
    

    def start(self):
        self.session_maker = sessionmaker(bind=self.db_engine)

    def write_odds_data(self):
        with self.session_maker() as session:
            statement = insert(Odds).values()
            session.