from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)

USUARIO_AUTENTICADO = True

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods = ['GET','POST'])
def login():
    global USUARIO_AUTENTICADO

    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'senha':
            USUARIO_AUTENTICADO = True
            return redirect (url_for('comerciantes'))
    else:
        return render_template('login.html', mensagem= 'Usuário ou senha incorretos!')
 
@app.route('/comerciantes')
def comerciantes():
    global USUARIO_AUTENTICADO

    if not USUARIO_AUTENTICADO:
        return redirect (url_for('login'))
    return render_template('comerciantes.html', imagem_fundo = 'VenBarato.jpg')   

@app.route('/consumidores')
def clientes():
    return render_template('clientes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')





app.config['HOST'] ='localhost'
app.config['PORT'] = 4000
app.config['DEBUG'] = True



if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
    #app.run(host=HOST, port=PORT, debug=DEBUG)