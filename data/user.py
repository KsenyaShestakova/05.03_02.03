import datetime
import sqlalchemy
from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.orm import relation

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=True)
    modified_date = Column(DateTime, nullable=True)

    jobs_ = relation('Jobs', back_populates='team_leader_instance')