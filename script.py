from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os

file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
scopes = [
  "https://spreadsheets.google.com/feeds",
  "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
  filename=file,
  scopes=scopes
  )
client = gspread.authorize(creds)
print(client)

planilha_completa = client.open(
    title="", 
    folder_id=""
)