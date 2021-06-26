from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from consts import db_name

base_dir = os.path.abspath(os.path.dirname(__file__))
local_db_url = "sqlite:///" + os.path.join(base_dir, db_name)

engine = create_engine(local_db_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()

