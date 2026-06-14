import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import pandas as pd
import sys
import time

from extrairDadosCadastrais import extrair_dados_cadastrais_colaborador
from acessaSiteSwile import acessar_site_swile

sys.path.append(r'C:\rpa\Python')

from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets
from Classes.Postgres.Postgres.ConectaPG import ConectaPG


def consulta_admissoes():    
    try:
        pass # Logica de negocio removida por seguranca corporativa

        

def insert_postgres(matriculas, status, data_execucao):
    pass # Logica de negocio removida por seguranca corporativa



def get_data_atual():
    pass # Logica de negocio removida por seguranca corporativa



def reativar_colaborador(driver, cpf):

    pass # Logica de negocio removida por seguranca corporativa



def baixar_e_procurar_novo_arquivo(driver, caminho_pasta):
    pass # Logica de negocio removida por seguranca corporativa



def cadastra_colaborador_swile(driver, arquivo, pasta_download):
    pass # Logica de negocio removida por seguranca corporativa

    def remove_caracter_cpf(cpf):
        pass # Logica de negocio removida por seguranca corporativa
