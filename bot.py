from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pdfplumber
import os

# 1. Configurações de Pasta
diretorio_projeto = os.getcwd()
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": diretorio_projeto}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Inicializa a variável para evitar o NameError que deu antes
caminho_final = ""

try:
    # 2. Processo de Login e Navegação
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)
    
    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("123")
    driver.find_element(By.CLASS_NAME, "btn-entrar").click()
    
    time.sleep(3) # Aguarda carregar o Dashboard

    # 3. Clique no botão de download
    botoes = driver.find_elements(By.CLASS_NAME, "btn-action")
    for b in botoes:
        if "Relatório" in b.text:
            b.click()
            break
            
    print("Download solicitado...")
    time.sleep(5) # Tempo para o arquivo ser salvo

    # 4. Localização do PDF (Projeto ou Downloads)
    caminho_local = os.path.join(diretorio_projeto, "relatorio_docetti.pdf")
    caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads", "relatorio_docetti.pdf")

    if os.path.exists(caminho_local):
        caminho_final = caminho_local
    elif os.path.exists(caminho_downloads):
        caminho_final = caminho_downloads

    # 5. Leitura e Exibição dos Clientes
    if caminho_final:
        print("\n" + "="*40)
        print("--- LISTA DE CLIENTES E PAGAMENTOS ---")
        print("="*40)
        
        with pdfplumber.open(caminho_final) as pdf:
            pagina = pdf.pages[0]
            tabela = pagina.extract_table()
            
            # O loop percorre a tabela a partir da segunda linha (pula o cabeçalho)
            for linha in tabela[1:]:
                # linha[0] é o Cliente, linha[-1] é o Valor Total
                cliente = linha[0]
                valor = linha[-1]
                print(f"Cliente: {cliente} | Valor Pago: {valor}")
                
        print("="*40)
    else:
        print("Erro: O arquivo 'relatorio_docetti.pdf' não foi localizado.")

finally:
    # driver.quit() # Deixe o navegador aberto para conferir se chegou na tela certa
    print("\nAutomação finalizada.")

# Exemplo de como o bot leria o captcha:
pergunta_texto = driver.find_element(By.CSS_SELECTOR, "label[for='captcha']").text
# Lógica para extrair números e somar...
# driver.find_element(By.NAME, "captcha").send_keys(resultado_calculado)