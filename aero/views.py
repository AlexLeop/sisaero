from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from entrada.models import EntradasAero
from saida.models import SaidasAero
from .models import Cadastros
from .utils.pdf_processor import ProcessarPDF
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import pandas as pd
from django.contrib import messages
from .tasks import importar_registros_task  # Importa a tarefa Celery


def importar_registros(arquivo, tipo_importacao):
    extensao = arquivo.name.split(".")[-1].lower()

    # Verificação de formato de arquivo
    if extensao == "csv":
        df = pd.read_csv(arquivo)
    elif extensao in ["xls", "xlsx"]:
        df = pd.read_excel(arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado.")

    if tipo_importacao == "cadastro":
        for _, row in df.iterrows():
            Cadastros.objects.update_or_create(
                cpf_pessoa=row["CPF"],
                matricula=row["Matrícula"],
                defaults={
                    "nome_pessoa": row["Nome"],
                    "posto": row["Posto"],
                    "data_admissao": row["Dt. Admissão"],
                    "data_termino": row["Dt. Término"],
                    "banco": row["Banco"],
                    "agencia": row["Agência"],
                    "tipo_conta": row["Tip Conta"],
                    "numero_conta": row["Nº Conta"],
                    "proventos": row["Proventos"],
                    "descontos": row["Descontos"],
                    "liquido": row["Líquido"],
                    "sigla_uo": row["Sigla UO"],
                },
            )

    elif tipo_importacao == "entrada":
        for _, row in df.iterrows():
            cadastro = Cadastros.objects.get(matricula=row["Matrícula"])  # Associando com o cadastro
            EntradasAero.objects.create(
                cadastro=cadastro,
                org=row["ORG"],
                matricula=row["Matrícula"],
                nome=row["Nome"],
                un_org=row["Und. Organizacional"],
                cargo=row["Cargo"],
                ind_parcs_pg=row["Índice de Parcelas Pagas"],
                valor=row["Valor"],
                caixas=row["Caixas"],
            )

    elif tipo_importacao == "saida":
        for _, row in df.iterrows():
            cadastro = Cadastros.objects.get(matricula=row["Matrícula"])  # Associando com o cadastro
            SaidasAero.objects.create(
                cadastro=cadastro,
                org=row["ORG"],
                matricula=row["Matrícula"],
                nome=row["Nome"],
                un_org=row["Und. Organizacional"],
                cargo=row["Cargo"],
                ind_parcs_pg=row["Índice de Parcelas Pagas"],
                valor=row["Valor"],
                caixas=row["Caixas"],
            )

@login_required
def cadastros_list(request):
    if request.method == "POST" and request.FILES.get("arquivo"):
        arquivo = request.FILES["arquivo"]
        tipo_importacao = request.POST.get("tipo_importacao")  # Obtém o tipo de importação selecionado

        try:
            # Chama a tarefa Celery de importação em segundo plano
            importar_registros_task.apply_async(args=[arquivo, tipo_importacao])
            messages.success(request, "A importação está em andamento!")
        except Exception as e:
            messages.error(request, f"Erro ao iniciar a importação: {e}")
            return redirect("cadastros_list")

        return redirect("cadastros_list")

    # Requisição GET - Listagem de cadastros
    cadastros = Cadastros.objects.prefetch_related("entradas", "saidas").all()
    return render(request, "aero/cadastros_list.html", {"cadastros": cadastros})


class ImportarPDFView(TemplateView):
    template_name = 'aero/importar_pdf.html'

    def post(self, request):
        if 'arquivo' not in request.FILES:
            return JsonResponse({'error': 'Arquivo não enviado'}, status=400)

        arquivo = request.FILES['arquivo']
        caminho_arquivo = f'/tmp/{arquivo.name}'
        with open(caminho_arquivo, 'wb+') as destino:
            for chunk in arquivo.chunks():
                destino.write(chunk)

        try:
            processor = ProcessarPDF(caminho_arquivo)
            resultados = processor.processar_tabelas()
            return JsonResponse({
                'message': 'Importação concluída com sucesso!',
                'registros': len(resultados),
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        finally:
            os.remove(caminho_arquivo)


def custom_logout(request):
    logout(request)
    return redirect('login')
