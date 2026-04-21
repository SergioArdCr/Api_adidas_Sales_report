from sqlalchemy import Column, Integer, String
from app.db.database import Base
from pydantic import BaseModel

class Usuario(Base):
    __tablename__ = "usuarios"
    id       = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)   # aquí va el hash, nunca el texto plano

class UsuarioCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str