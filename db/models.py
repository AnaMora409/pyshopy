from .database import Base 
from sqlalchemy import Column,Integer,String,Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer,
                primary_key=True,)
    estado=Column(Boolean)
    fecha_creacion=Column(Date)
    nombre=Column(String(60))
    
    #entidad-proyecto1
class Dueño(Base):
    __tablename__ ="Dueño"
    id = Column(Integer,
                primary_key=True,)
    num_documento=Column(Integer)
    nombre=Column(String(60))
    
    #relacion 1 a muchos con produtos
    Producto = relationship("Producto", 
                           back_populates="categoria")
    
    #entidad-proyecto2
class Producto(Base):
    __tablename__ ="Producto"
    id = Column(Integer,
                primary_key=True,)
    marca=Column(String(60))
    modelo=Column(String(60))
    precio=Column(String(60))
    categoria_id=Column(Integer,
                        ForeignKey("categorias.id"))
    