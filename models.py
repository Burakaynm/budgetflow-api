from sqlalchemy import Column, Integer, String, Float, Date

from database import Base


class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)


class IncomeModel(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    source = Column(String)
    date = Column(Date)