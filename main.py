from flask import Flask, render_template, request, url_for, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'fatec-jahu-2026'


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login ():

    if request.method == 'POST':
        login = request.form.get('login', '').strip()
        senha = request.form.get('senha', '').strip()
        erros = []

        if not login:
            erros.append("O CPF é necessário")

        if not senha:
            erros.append('É necessário inserir a senha')

        if erros:
            for erro in erros:
                flash(erro, 'danger')
                return render_template('login.html')
            
        # Validação simples de login:

        if login == "12345678900" and senha == "12345":
            return redirect(url_for('dashboard'))
        else:
            flash(f"Usuário ou senha incorretos!")
            return render_template('login.html')
        
    return render_template('login.html')           

@app.route('/dashboard')
def dashboard ():
    return render_template ('dashboard.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro ():

    if request.method == 'POST':

        #Tabela 1: dados pessoais.

        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        celular = request.form.get('celular', '').strip()
        nasc = request.form.get('nasc', '').strip()
        cpf = request.form.get('cpf', '').strip()
        acesso = request.form.get('acesso', '').strip()
        cep = request.form.get('cep', '').strip()
        endereco = request.form.get('endereco', '').strip()
        numero = request.form.get('numero', '').strip()
        complemento = request.form.get('complemento', '').strip()
        cidade = request.form.get('cidade', '').strip()
        estado = request.form.get('estado', '').strip()

        #Tabela 2: histórico de doações.
        
        doacao = request.form.get('doacao', '').strip()
        local = request.form.get('local', '').strip()
        fator = request.form.get('fator', '').strip()
        tsanguineo = request.form.get('tsanguineo', '').strip()

        #Tabela 3: histórico médico.

        doenca = request.form.get('doenca', '').strip()
        cirurgia = request.form.get('cirurgia', '').strip()
        estetico = request.form.get('estetico', '').strip()
        sexo = request.form.get('sexo', '').strip()

        erros = []

        if not nome:
            erros.append("O CPF é necessário")
        if not email:
            erros.append('É necessário inserir o e-mail')
        if not celular:
            erros.append('É necessário inserir um telefpne')
        if not cpf:
            erros.append('É necessário inserir o CPF')
        if not nasc:
            erros.append('É necessário inserir a data de nascimento')
        if not acesso:
            erros.append('É necessário definir o nível de acesso')
        if not doacao:
            erros.append('É necessário informar a última doação')
        if not fator:
            erros.append('É necessário informar o fator')
        if not tsanguineo:
            erros.append('É necessário informar o tipo sanguíneo')
        if not doenca:
            erros.append('É necessário informar doença ou não')
        if not cirurgia:
            erros.append('É necessário informar se fez cirurgias')
        if not estetico:
            erros.append('É necessário informar se fez procedimentos')

        if erros:
            for erro in erros:
                flash(erro, 'danger')
                return render_template ('cadastro.html', 
                                        nome=nome, email=email, celular=celular, nasc=nasc, cpf=cpf,
                                        acesso=acesso, cep=cep, endereco=endereco, numero=numero,
                                        complemento=complemento, cidade=cidade, estado=estado,
                                        doacao=doacao, local=local, fator=fator, tsanguineo=tsanguineo,
                                        doenca=doenca, cirurgia=cirurgia, estetico=estetico, sexo=sexo
                                        )
        flash(f'Cadastro realizado com sucesso! Consulte no menu Listagem.') 
    return render_template ('cadastro.html')

@app.route('/listagem', methods=['GET', 'POST'])
def listagem ():
   
  return render_template('listagem.html')

if __name__ == '__main__':
    app.run(debug=True)