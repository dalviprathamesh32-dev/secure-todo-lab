from sqlalchemy import Boolean , Integer , String , Column
from db import Base

class tasks (Base):
    __tablename__="tasks"

    id = Column (Integer , primary_key=True , autoincrement=True)
    task_name = Column (String , nullable=False)
    urgent = Column (Boolean , default=False)

    