from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Scan(Base):

    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)

    target = Column(String)

    result = Column(String)
