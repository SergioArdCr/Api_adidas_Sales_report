from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base
from pydantic import BaseModel

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    region = Column(String)
    state = Column(String)
    product = Column(String)
    price_per_unit = Column("Price per Unit", Float)
    units_sold = Column("Units Sold", Integer)
    total_sales = Column("Total Sales", Float)
    operating_profit = Column("Operating Profit", Float)

class VentaUpdate(BaseModel):
    total_sales: float

class VentaCreate(BaseModel):
    region: str
    state: str
    product: str
    price_per_unit: float
    units_sold: int
    total_sales: float
    operating_profit: float