import pandas as pd

sheet_id = "1AbCdeFgHiJKLmnopQRStuvWXyZ1234567890"  # Substitua pelo ID real
sheet_name = "Página1"  # Substitua pelo nome real da aba

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)

print(df.head())
