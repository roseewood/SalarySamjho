from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Payslip(Base):
    __tablename__ = "payslips"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    year = Column(String)
    raw_text = Column(String)
    components = Column(JSON)