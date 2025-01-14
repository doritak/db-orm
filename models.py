import os
from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base

# # Cargar las variables desde el archivo .env
# from dotenv import load_dotenv
# load_dotenv()

# Crear el motor y base de datos
DATABASE_NAME = "ferreteria"
USERNAME = "root"        # Cambiar por tu usuario de MySQL
PASSWORD = os.getenv("DB_PASSWORD")  # Recupera la contraseña desde las variables de entorno
HOST = "localhost"
PORT = "3306"

if not PASSWORD:
    raise ValueError("La contraseña no está configurada en las variables de entorno.")


# Crear un motor inicial sin base de datos específica
engine = create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}", echo=True)

# Base de modelos
Base = declarative_base()

# Modelo de la tabla proveedores
class Proveedor(Base):
    __tablename__ = "proveedores"
    
    rut = Column(String(12), primary_key=True)  # Clave primaria, RUT
    nombre_proveedor = Column(String(120), nullable=False)
    vencimiento = Column(Integer)
    nombre_corto = Column(String(100))
    nombre_vendedor = Column(String(100))
    telefono_vendedor = Column(String(60))
    correo_vendedor = Column(String(120))
    correo_vendedor2 = Column(String(120))
    correo_pago = Column(String(120))
    tipo_flete = Column(String(120))
    transporte = Column(String(120))
    
    def __init__(self, rut, nombre_proveedor, vencimiento, nombre_corto, nombre_vendedor, telefono_vendedor, correo_vendedor, correo_vendedor2, correo_pago, tipo_flete, transporte):
        self.rut = rut
        self.nombre_proveedor = nombre_proveedor
        self.vencimiento = vencimiento
        self.nombre_corto = nombre_corto
        self.nombre_vendedor = nombre_vendedor
        self.telefono_vendedor = telefono_vendedor
        self.correo_vendedor = correo_vendedor
        self.correo_vendedor2 = correo_vendedor2
        self.correo_pago = correo_pago
        self.tipo_flete = tipo_flete
        self.transporte = transporte
    
    def __repr__(self):
        return f"<Proveedor(rut={self.rut,"-",self.dv}, nombre_proveedor={self.nombre_proveedor})>"
    
    
# Crear la base de datos y las tablas
def create_database():
    # Crear conexión al servidor MySQL
    with engine.connect() as connection:
        # Crear la base de datos si no existe
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))
        connection.execute(text(f"USE {DATABASE_NAME}"))
    
    # Crear las tablas
    db_engine = create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}", echo=True)
    Base.metadata.create_all(db_engine)
    
    


    
    
if __name__ == "__main__":
    create_database()
    