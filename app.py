from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# o dicionario é definido aqui:
livros = []
detalhes = []

@app.route('/')
def index():
    return redirect(url_for('livros_view'))


@app.route('/livros', methods=['GET', 'POST'])
def livros_view():  # usei um nome diferente para evitar conflito de nomes
    if request.method == 'POST':
        titulo = request.form['titulo']
        livros.append(titulo)
    return render_template('livros.html', livros=livros)

@app.route('/detalhes', methods=['GET', 'POST'])
def detalhes_view():  # usei um nome diferente para evitar conflito de nomes
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']
        detalhes.append({'titulo': titulo, 'autor': autor, 'ano': ano})
    return render_template('detalhes.html', detalhes=detalhes)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')
