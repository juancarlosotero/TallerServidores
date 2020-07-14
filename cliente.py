from sqlalchemy import create_engine
from connector import *

# DATA INSERT
autor_1 = Asistencia('Juan','Pedro Ramirez','FullStack')
autor_2 = Asistencia('Andres','Roberto Hernandez','Matematicas')
autor_3 = Asistencia('Manuel','Raul Ortiz','Logica')
autor_4 = Asistencia('pedro',' garcia','istoria')
autor_5 = Asistencia('pedro zuares','jose garcia','etica')
autor_6 = Asistencia('pedro zuares','jose garcia','dibujo')
autor_7 = Asistencia('pedro zuares','jose garcia','geografia')
autor_8 = Asistencia('pedro zuares','jose garcia','ingles')

lista_autores = (autor_1, autor_2, autor_3, autor_4, autor_5,autor_6, autor_7, autor_8) 
session.add_all(lista_autores) 
session.commit()