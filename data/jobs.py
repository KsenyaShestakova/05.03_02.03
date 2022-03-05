import datetime
import sqlalchemy
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Column
from sqlalchemy.orm import relation

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(ForeignKey('users.id'), nullable=False)
    job = Column(String(1000), nullable=False)
    work_size = Column(Integer, nullable=True)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, nullable=True)

    team_leader_instance = relation('User')