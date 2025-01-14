import os
import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import Proveedor, create_engine

# establecer los parametros de la base de datos
DATABASE_NAME = "ferreteria"
USERNAME = "root"        # Cambiar por tu usuario de MySQL
PASSWORD = os.getenv("DB_PASSWORD")  # Recupera la contraseña desde las variables de entorno
HOST = "localhost"
PORT = "3306"

engine = create_engine(f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}", echo=False)



def leer_datos_excel(ruta, sheet_name=0):
    df = pd.read_excel(ruta, sheet_name)  # Specify the sheet name or index
    print(df.head())
    return df

def insertar_proveedores(df):
    df["Vencimiento días"] = df["Vencimiento días"].fillna(0).astype(int)
    # Replace NaN values with empty strings
    df = df.fillna('')
    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    # Insertar los datos
    for _, row in df.iterrows():
        proveedor = Proveedor(
            rut=row["RUT"],
            nombre_proveedor=row["Name"],
            vencimiento=row["Vencimiento días"],
            nombre_corto=row["Nombre Corto"],
            nombre_vendedor=row["Nombre vendedor"],
            telefono_vendedor=row["Teléfono - celular"],
            correo_vendedor=row["Mail Vendedor"],
            correo_vendedor2=row["Mail 2do Vendedor"],
            correo_pago=row["Mail Pago"],
            tipo_flete=row["Flete si/no"],
            transporte=row["Transporte"],
        )
        # Agregar a la sesión
        session.add(proveedor)
    # Confirmar los cambios
    session.commit()
    session.close()
    
def eliminar_contenido_tabla(tabla):
    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    # Eliminar el contenido de la tabla
    session.query(tabla).delete()
    # Confirmar los cambios
    session.commit()
    session.close()
    

if __name__ == "__main__":

    df = leer_datos_excel(ruta="datos_excel/Lista_de_Proveeedores.xlsx", sheet_name="lista")
    
    insertar_proveedores(df)
    
    # eliminar_contenido_tabla(Proveedor)