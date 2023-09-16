from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
from structs import Odds

def main():
    cfg = configparser.ConfigParser()
    cfg.read("./content_service.cfg")


    Session = sessionmaker(bind=db_engine)
    with Session() as session:
        for instance in session.query(Odds).order_by(Odds.id):
            print(instance.id, instance.sports, instance.time_created)


if __name__ == "__main__":
    main()