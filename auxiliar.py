import pywhatkit
import datetime
import time

hora_atual = datetime.datetime.now()
numero_da_hora = hora_atual.hour
numero_do_minuto = hora_atual.minute
minuto_mais_1 = numero_do_minuto + 1

if minuto_mais_1 == 60:
    minuto_mais_1 = 0

pywhatkit.sendwhatmsg("+558994994977", "Ola Rhuaan, Esta é uma mensagem programada", numero_da_hora, minuto_mais_1)




