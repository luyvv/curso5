from flask import render_template, Flask
app = Flask(__name__)

class Livro:
    def __init__(self, titulo, autor, categoria, ano, editora):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.editora = editora
        self.ativo = False


@app.route("/inicio")
def ola():
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "HarperCollins")
    lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
        
    livro2 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Martin Claret")
    livro3 = Livro("O Alquimista", "Paulo Coelho", "Autoajuda", 1988, "Rocco")

    # lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
    lista = [livro1, livro2, livro3]
    return render_template(
        "lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista
    )

app.run()