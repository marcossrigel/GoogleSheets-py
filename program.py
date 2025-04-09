import webbrowser
import datetime
import script
import time

cabecalho = script.planilha.row_values(1)
coluna_status_index = cabecalho.index('Status') + 1

data_atual = datetime.date.today().strftime('%d/%m/%Y')

for i, linha in enumerate(script.dados, start=2):
  if linha.get('Data') == data_atual:
    if linha.get('Status') == '':
      webbrowser.open(f'https://web.whatsapp.com/send?phone={linha.get('Telefone')}&text=Olá {linha.get('Nome')}, esta é uma mensagem automática :)')
      time.sleep(7)
      script.planilha.update_cell(i, coluna_status_index, 'Enviado')

