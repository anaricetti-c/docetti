from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/site/dashboard.html")

time.sleep(2)

# pega todas as linhas da tabela (tbody)
linhas = driver.find_elements(By.CSS_SELECTOR, "#tabela-encomendas tbody tr")

print("=== PEDIDOS ===")

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    
    cliente = colunas[1].text   # segunda coluna (Cliente)
    valor = colunas[5].text     # sexta coluna (Valor)

    print(f"Cliente: {cliente} | Valor: {valor}")

input("Pressione ENTER para fechar...")
driver.quit()