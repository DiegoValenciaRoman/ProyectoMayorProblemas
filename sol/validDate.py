import datetime
dia = 10
mes = 12
ano = 2021
correctDate = None
try:
    newDate = datetime.datetime(ano,mes,dia)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))
