
class Curso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Campus:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, nome_curso):
        self.cursos.append(Curso(nome_curso))

    def listar_cursos(self):
        return [curso.nome for curso in self.cursos]

    def atualizar_curso(self, indice, novo_nome):
        if 0 <= indice < len(self.cursos):
            self.cursos[indice].nome = novo_nome

    def remover_curso(self, indice):
        if 0 <= indice < len(self.cursos):
            del self.cursos[indice]

