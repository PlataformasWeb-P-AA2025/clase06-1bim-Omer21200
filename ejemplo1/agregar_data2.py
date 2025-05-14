import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2  
from configuracion import engine


Session = sessionmaker(bind=engine)
session = Session()

csv_path = "data/saludos_mundo.csv"


with open(csv_path, newline='', encoding='utf-8') as csvfile:
    salud = csv.DictReader(csvfile, delimiter='|')
    for s in salud:
        saludo = Saludo2(
            mensaje=s['saludo'],
            tipo=s['tipo'],
            origen=s['origen']
        )
        session.add(saludo)

# Confirmar las transacciones
session.commit()
