from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import random
import os

app = Flask(__name__)

# CHAVE SECRETA: Sem isso, o servidor dá erro ao tentar usar 'session'
app.secret_key = 'docetti_12345'

USER_DATA = {"usuario": "admin", "senha": "123"}

@app.route('/')
def index():
    # Gera o captcha
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    session['captcha_res'] = str(n1 + n2)
    pergunta_texto = f"Quanto é {n1} + {n2}?"
    
    # Se o login falhar, podemos passar uma mensagem de erro aqui
    erro = request.args.get('erro')
    
    return render_template('index.html', pergunta=pergunta_texto, erro=erro)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    captcha_usuario = request.form.get('captcha')

    # Validação do Captcha (Exercício 1)
    if captcha_usuario != session.get('captcha_res'):
        return redirect(url_for('index', erro="Captcha incorreto!"))

    # Validação de Usuário e Senha
    if usuario == USER_DATA['usuario'] and senha == USER_DATA['senha']:
        # Redireciona para a FUNÇÃO dashboard_page
        return redirect(url_for('dashboard_page'))
    else:
        return redirect(url_for('index', erro="Usuário ou senha incorretos!"))

@app.route('/dashboard')
def dashboard_page():
    # Certifique-se que o arquivo dashboard.html existe na pasta templates
    return render_template('dashboard.html')

@app.route('/relatorio_docetti.pdf')
def download_file():
    return send_from_directory('static', 'relatorio_docetti.pdf')

if __name__ == '__main__':
    app.run(debug=True)
