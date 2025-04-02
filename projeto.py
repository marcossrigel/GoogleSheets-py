import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv'

df = pd.read_csv(url)

id_procurado = 1

resultado = df[df['ID'] == id_procurado]

if not resultado.empty:
    print(resultado.to_string(index=False))
else:
    print("ID não encontrado.")