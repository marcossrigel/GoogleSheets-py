import pandas as pd
import pyautogui
import webbrowser
import re

url = 'https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv'
df = pd.read_csv(url, usecols=['ID', 'Nome', 'Telefone'])

resultado = df.loc[df['ID'] == 4].squeeze()
nome = resultado['Nome']
numero = re.sub(r'\D', '', resultado['Telefone'])

webbrowser.open(f"https://web.whatsapp.com/send?phone={numero}&text=Olá {nome}, esta é uma mensagem automática :)")
pyautogui.press('enter')
