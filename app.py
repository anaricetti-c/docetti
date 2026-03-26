from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Configuração simples de usuário/senha
USER_DATA = {"usuario": "admin", "senha": "123"}

@app.route('/')
def index():
    # Página inicial será o formulário de login
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == USER_DATA['usuario'] and senha == USER_DATA['senha']:
        return redirect(url_for('download_page'))
    else:
        return "Usuário ou senha incorretos!", 401

@app.route('/dashboard')
def download_page():
    return render_template('download.html')

@app.route('/relatorio_docetti.pdf')
def download_file():
    # Certifique-se de que o PDF está na pasta 'static'
    return send_from_directory('static', 'relatorio_docetti.pdf')

if __name__ == '__main__':
    app.run(debug=True)