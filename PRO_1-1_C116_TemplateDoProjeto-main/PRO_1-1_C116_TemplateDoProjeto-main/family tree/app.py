# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Gabriel" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/flask2")
def pai():
    nome = "Charles" # escreva seu nome
    idade = "50" # escreva sua idade
# defina a rota para a página da mãe
@app.route("/flask3")
def mae():
    nome = "Silvana" # escreva seu nome
    idade = "49" # escreva sua idade

# defina a rota para a página do amigo
@app.route("/flask4")
def amigo():
    nome = "Bruno" # escreva seu nome
    idade = "13" # escreva sua idade

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
