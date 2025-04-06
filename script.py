from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import gspread

file = 'formulariosolicitacaopagamento-0127aa11a88d.json'
scopes = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
  filename=file,
  scopes=scopes
  )
client = gspread.authorize(creds)
#print(client)

planilha_completa = client.open(
    title='Planilha Teste - GoogleSheetPython',
    folder_id='1LJvfZ4QtUpJoi03guWZLAiktIbdHiL8z',
    )

planilha = planilha_completa.get_worksheet(0)
<<<<<<< HEAD
dados = planilha.get_all_records()
=======
dados = planilha.get_all_records()
>>>>>>> 7897b18a4ca9310e7a3613aad21d7136b1ab2600
