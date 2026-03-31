from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Iniciar o Navegador
driver = webdriver.Chrome()

try:
    # 2. Acessar a página de login local
    driver.get("http://127.0.0.1:5000/") # Porta padrão do Flask
    time.sleep(2)

    # 3. Preencher formulário de login (baseado no index.html)
    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("123")
    
    # Clica no botão "Entrar" (usando a classe CSS definida no style.css)
    driver.find_element(By.CLASS_NAME, "btn-entrar").click()
    time.sleep(2)

    # 4. Extrair os dados da página confidencial (dashboard)
    print("=== EXTRAINDO DADOS CONFIDENCIAIS ===")
    
    # Localiza as linhas da tabela
    linhas = driver.find_elements(By.CSS_SELECTOR, "#tabela-encomendas tbody tr")

    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        # Pega o texto de cada coluna relevante
        cliente = colunas[1].text
        entrega = colunas[2].text
        valor = colunas[5].text
        
        print(f"Cliente: {cliente} | Entrega: {entrega} | Valor: {valor}")

finally:
    # Mantém aberto por uns segundos para conferência e fecha
    time.sleep(5)
    driver.quit()