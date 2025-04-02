import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv')

resultado = df[df['ID'] == 1]

telefone = resultado['Telefone'].values[0]
nome = resultado['Nome'].values[0]
print(f"Telefone {nome}: {telefone}")

