from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pdfplumber
import os

# 1. Configurar Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. Acessar a página de Login
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)

    # 3. Fazer Login
    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("123")
    driver.find_element(By.ID, "btn-entrar").click()
    time.sleep(2)

    # 4. Clicar no botão de Relatório para baixar
    # O download geralmente vai para a pasta Downloads do seu Windows
    driver.find_element(By.ID, "btn-relatorio").click()
    print("Download solicitado...")
    time.sleep(5) # Espera o download concluir

    # 5. Ler o PDF com pdfplumber
    # Ajuste o caminho para onde o seu Chrome baixa arquivos
    caminho_pdf = os.path.expanduser("~/Downloads/relatorio_docetti.pdf")
    
    if os.path.exists(caminho_pdf):
        with pdfplumber.open(caminho_pdf) as pdf:
            primeira_pagina = pdf.pages[0]
            texto = primeira_pagina.extract_text()
            print("\n--- Conteúdo do PDF ---")
            print(texto)
    else:
        print("Arquivo PDF não encontrado na pasta de Downloads.")

finally:
    driver.quit()