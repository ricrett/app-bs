from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def login ():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro ():
    return render_template('cadastro.html')

@app.route('/listagem')
def listagem ():
    return render_template('listagem.html')

if __name__ == '__main__':
    app.run(debug=True)