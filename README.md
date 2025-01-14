# Python y DB MySql con ORM de SqlAlchemy

Crear una base de datos MySql con sqlalchemy (ORM) para poder realizar ejercicios:

- Generar la base de datos con DATABASE_NAME y la gestionar la contraseña por sistema PASSWORD = os.getenv("DB_PASSWORD")
- Crear el motor de conexión create_engine
- Definir las tabals con Base.metadata.create_all
- Configurar la sesión con sessionmaker
- Realizar operaciones CRUD con la sessión bajo SQLAlchemy (ORM)
- Cerrar sessión
