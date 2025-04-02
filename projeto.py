import pandas as pd
import pywhatkit
import datetime
import re

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv')
resultado = df[df['ID'] == 2]

nome = resultado['Nome'].values[0]
telefone = resultado['Telefone'].values[0]

numero = re.sub(r'\D', '', telefone)

hora_atual = datetime.datetime.now()

numero_da_hora = hora_atual.hour
numero_do_minuto = hora_atual.minute
minuto_mais_1 = numero_do_minuto + 1

if minuto_mais_1 == 60:
    minuto_mais_1 = 0

pywhatkit.sendwhatmsg(f"+55{numero}", f"Ola {nome}, Esta é uma mensagem programada", numero_da_hora, minuto_mais_1)
