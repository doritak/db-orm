import os
from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# # Cargar las variables desde el archivo .env
# from dotenv import load_dotenv
# load_dotenv()

# Crear el motor y base de datos
DATABASE_NAME = "Ferreteria"
USERNAME = "root"        # Cambiar por tu usuario de MySQL
PASSWORD = os.getenv("DB_PASSWORD")  # Recupera la contraseña desde las variables de entorno
HOST = "localhost"
PORT = "3306"

if not PASSWORD:
    raise ValueError("La contraseña no está configurada en las variables de entorno.")


# Crear un motor inicial sin base de datos específica
server_engine = create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}", echo=True)

# Base de modelos
Base = declarative_base()

# Modelo de la tabla proveedores
class Proveedor(Base):
    __tablename__ = "proveedores"
    
    rut = Column(String(12), primary_key=True)  # Clave primaria, RUT
    dv = Column(String(1), primary_key=True)
    nombre_proveedor = Column(String(100), nullable=False)
    razon_social = Column(String(150), nullable=False)
    nombre_vendedor = Column(String(100))
    direccion_proveedor = Column(String(200))
    correo_vendedor = Column(String(100))
    telefono_vendedor = Column(String(15))
    forma_pago = Column(String(50))
    dias_vencimiento = Column(Integer)
    banco = Column(String(50))
    nro_cuenta_bancaria = Column(String(50))
    correo_pago = Column(String(100))
    
    def __repr__(self):
        return f"<Proveedor(rut={self.rut,"-",self.dv}, nombre_proveedor={self.nombre_proveedor})>"
    
    
# Crear la base de datos y las tablas
def create_database():
    # Crear conexión al servidor MySQL
    with server_engine.connect() as connection:
        # Crear la base de datos si no existe
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))
        #connection.execute(text(f"USE {DATABASE_NAME}"))
    
    # Crear las tablas
    db_engine = create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}", echo=True)
    Base.metadata.create_all(db_engine)

if __name__ == "__main__":
    create_database()