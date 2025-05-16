from sqlalchemy import create_engine #para importar funciones de una dependencia
from sqlalchemy.ext.declarative import declarative_base

#connection string:
#representa la base de datos a conestarse
#depende de la base de datos que se use
#y el puntaje de programacion
SQLALCHEMY_DATABASE_URL= 'mysql+pymysql://root:admin@localhost:3315/py-shopy'

##Crear el objeto de la base de datos
conn = create_engine(SQLALCHEMY_DATABASE_URL)

#importr la clase base para los modelos
Base = declarative_base()

