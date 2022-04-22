from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from banco.models import Transacao
from django.contrib import auth, messages
from django.conf import settings
import csv
import os
import datetime
def index(request):
    return render(request, "index.html")

def enviar_arquivo(request):
    if request.method == "POST":
        file = request.FILES['file_csv']
        lista_bank = pars_csv(file)
        if not lista_bank:
            messages.error(request, 'Arquivo Vazio')
            return redirect('envia_arquivo')

        try:
            list_bank_updated = list()
            records = lista_bank
            date_record = records[0].split(",")
            date_first = date_record[7]
            if validade_duplicate_transaction(date_first):
                messages.error(request, 'Transações dessa data ja foram importadas no banco')
                return redirect('envia_arquivo')
            for data_bank in lista_bank:
                row = data_bank.split(",")
                data = dict(banco_origem=row[0],
                    agencia_origem=row[1],
                    conta_origem=row[2],
                    banco_destino=row[3],
                    agencia_destino=row[4],
                    conta_destino=row[5],
                    valor_transacao=row[6],
                    data_hora_trasacao=row[7])

                if not validate_date(date_first, data["data_hora_trasacao"]) or not validade_data_transaction(data):
                    print("ALGUNS DADOS PODEM ESTAR EM BRANCO")
                    continue

                banco =Transacao.objects.create(**data)
                banco.save()
                list_bank_updated.append(banco)
        except Exception as err:
            messages.error(request, f'Arquivo Imcompativel {err}')
            return redirect('envia_arquivo')

        dados = consulta_transacoes()
        return render(request, "enviado_sucesso.html", dados)
    else:
        return render(request, "envia-arquivo.html")

def acessa_transacoes(request):
    dados = consulta_transacoes()
    return render(request, "enviado_sucesso.html", dados)

def consulta_transacoes():
    bancos = Transacao.objects.all().order_by('-data_importacao').order_by('-data_importacao', '-data_hora_trasacao')
    dados = {"bancos": bancos}
    return dados


def pars_csv(data):
    file_str = str(data.read())
    if len(file_str)<=3:
        return False
    list = file_str.split("'")
    clear_list = list[1].split("\\n")
    return clear_list

def validate_date(first_date, current_date):
    year_first_date = int(first_date[0:4])
    month_first_date = int(first_date[5:7])
    day_first_date = int(first_date[8:10])

    year_current_date = int(current_date[0:4])
    month_current_date = int(current_date[5:7])
    day_current_date = int(current_date[8:10])

    first_date = datetime.date(year_first_date, month_first_date, day_first_date)
    current_date = datetime.date(year_current_date, month_current_date,day_current_date)
    retorno = True if first_date == current_date else False

    return retorno

def validade_data_transaction(data):
    for blank_data in data.values():
        if not blank_data:
            return False
    return True

def validade_duplicate_transaction(data):


    date = Transacao.objects.filter(data_hora_trasacao=data)

    return True if date else False



