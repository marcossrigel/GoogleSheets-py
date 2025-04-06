from oauth2client.service_account import ServiceAccountCredentials
from cryptography.fernet import Fernet
import webbrowser
import datetime
import time
import os
import gspread

def descriptografar_credencial(caminho_cripto, caminho_temp, caminho_chave):
    key = b'Aih-llrMvRwkzDEJMQV8edVzRuaOCycAEK9hwroVVgY='
    fernet = Fernet(key)
    with open(caminho_cripto, 'rb') as arquivo_criptografado:
        criptografado = arquivo_criptografado.read()
    descriptografado = fernet.decrypt(criptografado)
    with open(caminho_temp, 'wb') as arquivo_temp:
        arquivo_temp.write(descriptografado)

    return caminho_temp

def conectar_google_sheets(caminho_credencial_temp):
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(caminho_credencial_temp, scopes)
    return gspread.authorize(creds)


def enviar_mensagens(planilha):
    dados = planilha.get_all_records()
    cabecalho = planilha.row_values(1)
    coluna_status_index = cabecalho.index('Status') + 1
    data_atual = datetime.date.today().strftime('%d/%m/%Y')

    for i, linha in enumerate(dados, start=2):
        if linha.get('Data') == data_atual and linha.get('Status') == '':
            nome = linha.get('Nome')
            telefone = linha.get('Telefone')
            mensagem = f'Olá {nome}, esta é uma mensagem automática :)'
            webbrowser.open(f'https://web.whatsapp.com/send?phone={telefone}&text={mensagem}')
            time.sleep(5)
            planilha.update_cell(i, coluna_status_index, 'Enviado')


def main():
    caminho_cripto = 'formulariosolicitacaopagamento-0127aa11a88d.json'
    caminho_chave = 'chave.key'
    caminho_temp = 'credenciais_temp.json'

    try:
        credencial_temp = descriptografar_credencial(caminho_cripto, caminho_temp, caminho_chave)
        client = conectar_google_sheets(credencial_temp)

        planilha_completa = client.open(
            title='Planilha Teste - GoogleSheetPython',
            folder_id='1LJvfZ4QtUpJoi03guWZLAiktIbdHiL8z'
        )
        planilha = planilha_completa.get_worksheet(0)
        enviar_mensagens(planilha)

    finally:
        if os.path.exists(caminho_temp):
            os.remove(caminho_temp)

if __name__ == '__main__':
    main()
