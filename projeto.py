import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1p5GkS4ngPcai_U8p2rOKnj3_kiefYYv383L6oevaNmM/export?format=csv'

df = pd.read_csv(url)

df.head()
