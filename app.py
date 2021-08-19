import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# configuração
DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/hello')
def pagina_inicial():
    return "Hello World"
