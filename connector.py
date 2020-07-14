from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
#DB CONECTION
engine = create_engine( 'mysql+pymysql://root:AC13n19m1!@localhost/asistencia' ) 
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
#TABLES

class Asistencia(Base):
    __tablename__ = 'Asistencia'
    id_asistencia = Column(Integer, primary_key=True)
    clase = Column(String(50), index= True, nullable=False) 
    alumno = Column(String(50))
    curso = Column(String(50))

    def __init__(self, clase, alumno, curso): 
        self.clase = clase
        self.alumno = alumno
        self.curso = curso

    def __repr__(self):
        return unicode(self.clase)

class Alumnos(Base):
    __tablename__ = 'Alumnos'
    id_alumno = Column(Integer, primary_key=True)
    nombre = Column(String(50), index= True, nullable=False) 
    apellido = Column(String(50))
    cedula = Column(String(15))

    def __init__(self, nombre, apellido, cedula): 
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def __repr__(self):
        return unicode(self.nombre)

class Clases(Base):
    __tablename__ = 'Clases'
    id_clase = Column(Integer, primary_key=True)
    clase = Column(String(50), index= True, nullable=False) 
    horario = Column(String(20))
    profesor = Column(String(50))

    def __init__(self, clase, horario, profesor): 
        self.clase = clase
        self.horario = horario
        self.profesor = profesor

    def __repr__(self):
        return unicode(self.clase)

class Cursos(Base):
    __tablename__ = 'Cursos'
    id_curso = Column(Integer, primary_key=True)
    curso = Column(String(50), index= True, nullable=False) 

    def __init__(self, curso): 
        self.curso = curso

    def __repr__(self):
        return unicode(self.curso)


class Profesores(Base):
    __tablename__ = 'Profesores'
    id_profesor = Column(Integer, primary_key=True)
    profesor = Column(String(50), index= True, nullable=False) 

    def __init__(self, curso): 
        self.profesor = profesor

    def __repr__(self):
        return unicode(self.profesor)

class Horarios(Base):
    __tablename__ = 'Horario'
    id_horario = Column(Integer, primary_key=True)
    horario = Column(String(20), index= True, nullable=False) 

    def __init__(self, curso): 
        self.horario = horario

    def __repr__(self):
        return unicode(self.horario)
    
    
Base.metadata.create_all(engine)