import pandas as pd
import pyautogui
import webbrowser
import time
import re
from datetime import datetime

url = 'https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv'

df = pd.read_csv(url, usecols=['Nome', 'Telefone', 'Data'])
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')
hoje = pd.to_datetime(datetime.today().date())

df_hoje = df[df['Data'] == hoje]

for _, row in df_hoje.iterrows():
    nome = row['Nome']
    numero = re.sub(r'\D', '', row['Telefone'])
    webbrowser.open(f'https://web.whatsapp.com/send?phone={numero}&text=Olá {nome}, esta é uma mensagem automática :)')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
