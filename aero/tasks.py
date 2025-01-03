import pandas as pd
from celery import shared_task

from .models import Cadastros
from entrada.models import EntradasAero
from saida.models import SaidasAero


@shared_task
def importar_registros_task(arquivo, tipo_importacao):
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
