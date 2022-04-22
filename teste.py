from datetime import datetime, timedelta
import time

date = "2022-01-01T08:44:00"
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

print(f"{year}/{month}/{day}")


import datetime

first_date = datetime.date(year, month, day)
second_date = datetime.date(2015, 12, 16)


data = dict(banco_origem="x",
            agencia_origem="row[1]",
            conta_origem=" ",
            banco_destino="x",
            agencia_destino=""
)

for c in data.values():
    if not c:
        print("Não existe")
    print(c)