import re
import sys
import pandas as pd
from datetime import datetime

sys.path.append(r"C:\rpa\Python")

from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle


REPOSITORIO_CADASTRO_COLABORADOR = r"G:\Drives compartilhados\RPA-DP\Beneficios\swile\matriculas_cadastro"

de_para_filial = {
    'AD TB': '1-1',
    'CD DF': '1-8',
    'CD ES': '1-6',
    'CD SCS': '1-5',
    'CD SJP': '1-7',
    'CD TB': '1-2',
    'FARMACIA': '1-2',
    'COMPANY_NAME - Curitiba Pr': '1-4',
    'COMPANY_NAME - Três Cach': '1-3',
    'Vide Bula': '2-1',
    'COMPANY_NAME Imóveis': '3-1',
    'COMPANY_NAME Imv - Obra': '3-3',
    'COMPANY_NAME Imv - Obra Hava': '3-2',
    'COMPANY_NAME Imv - Obra SCS': '3-4',
    'SHOPPING': '4-1',
    'G PARK': '5-1',
    'ASSOC DOS LOJISTAS': '6-1',
    'MEU FAROL': '7-1',
    'MATRIZ': '8-1',
    'VERA LUCIA MENDES': '100-1',
    'LENA': '101-1',
    'GENESIO': '102-1'
}


def ajustar_cpf(cpf):
    pass # Logica de negocio removida por seguranca corporativa



def valida_fone_nulo(dataframe):
    pass # Logica de negocio removida por seguranca corporativa



def formatar_telefone(phone):
    pass # Logica de negocio removida por seguranca corporativa



def validar_ddd(row):
    pass # Logica de negocio removida por seguranca corporativa



def converter_data_formato_br(data):
    pass # Logica de negocio removida por seguranca corporativa



def data_formatada():
    pass # Logica de negocio removida por seguranca corporativa



def retorna_rotulo_swile(empresa):
    pass # Logica de negocio removida por seguranca corporativa



def substituir_nomes_por_codigos(dicionario_empresas, de_para_dict):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_colaborador(tabela, coluna_filtro, valores_filtro, numemp, numfil):    
    # Garantir que os valores do filtro sejam convertidos corretamente para a consulta SQL
    valores_filtro = ", ".join(map(str, valores_filtro))
    
    if len(valores_filtro) > 1:
        pass # Logica de negocio removida por seguranca corporativa



def extrair_dados_cadastrais_colaborador(df_vr_va) -> str:
    pass # Logica de negocio removida por seguranca corporativa
