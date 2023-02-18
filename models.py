from base_model import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    DateTime,
    DECIMAL,
    Table,
    Boolean,
    UniqueConstraint, Enum,
    ARRAY, text, bindparam
)


class Person(Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    second_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    employment_date = Column(Date)
    salary = Column(DECIMAL)
    boss_id = Column(
        Integer,
        ForeignKey("person.id", name="person_position_fkey", ondelete="SET NULL"),
    )
