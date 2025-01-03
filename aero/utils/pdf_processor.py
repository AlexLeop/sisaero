import tabula
import pandas as pd
from aero.models import Cadastros


class ProcessarPDF:
    def __init__(self, arquivo, paginas="all"):
        self.arquivo = arquivo
        self.paginas = paginas

    def processar_tabelas(self):
        # Lê o PDF e extrai as tabelas
        dfs = tabula.read_pdf(
            self.arquivo,
            pages=self.paginas,
            pandas_options={'header': None},
            multiple_tables=True,
        )
        if not dfs or len(dfs) == 0:
            raise ValueError("Nenhuma tabela foi encontrada no PDF.")

        resultados = []
        for df in dfs:
            # Ajusta o cabeçalho das tabelas
            df.columns = df.iloc[0]
            df = df[1:]  # Remove a linha duplicada que serve de cabeçalho
            df = df.reset_index(drop=True)

            # Processa cada linha do DataFrame
            for _, row in df.iterrows():
                ordem = row.get("N° Ordem", "").strip()
                nome = row.get("Nome", "").strip()
                dt_inat = self._formatar_data(row.get("Dt. Inat.", ""))
                dt_nasc = self._formatar_data(row.get("Dt. Nasc.", ""))
                endereco = row.get("Endereço", "").strip()
                telefone = row.get("Telefone", "").strip()

                # Salva os dados no banco de dados
                cadastro = Cadastros.objects.create(
                    ordem=ordem,
                    nome=nome,
                    dt_inat=dt_inat,
                    dt_nasc=dt_nasc,
                    endereco=endereco,
                    telefone=telefone,
                )
                resultados.append(cadastro)

        return resultados

    def _formatar_data(self, data):
        """
        Formata a data no padrão YYYY-MM-DD.
        """
        try:
            return pd.to_datetime(data, dayfirst=True).date() if data else None
        except Exception:
            return None
