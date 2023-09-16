from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP

Base = declarative_base()

class Odds(Base):
    __tablename__ = "odds"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sports = Column(String)
    time_created = Column(TIMESTAMP)