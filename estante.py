class Item:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluido = False
        self.nota = None

    def concluir(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("A nota precisa ser entre 0 e 10.")
        self.concluido = True
        self.nota = nota

    def detalhes(self):
        return ""

    def __str__(self):
        status = f"concluído, nota {self.nota}" if self.concluido else "pendente"
        return f"{self.titulo} {self.detalhes()} - {status}"


class Livro(Item):
    def __init__(self, titulo, autor):
        super().__init__(titulo)
        self.autor = autor

    def detalhes(self):
        return f"(livro de {self.autor})"


class Serie(Item):
    def __init__(self, titulo, temporadas):
        super().__init__(titulo)
        self.temporadas = temporadas

    def detalhes(self):
        return f"(série, {self.temporadas} temporadas)"


class Estante:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def pendentes(self):
        return [item for item in self.itens if not item.concluido]

    def media_notas(self):
        notas = [item.nota for item in self.itens if item.concluido]
        if not notas:
            return None
        return sum(notas) / len(notas)


def mostrar(itens):
    if not itens:
        print("Nada por aqui.")
    for i, item in enumerate(itens, start=1):
        print(f"{i}. {item}")


def main():
    estante = Estante()
    menu = """
1 - Adicionar livro
2 - Adicionar série
3 - Ver tudo
4 - Ver pendentes
5 - Marcar como concluído
6 - Ver média das notas
0 - Sair
"""
    while True:
        print(menu)
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            estante.adicionar(Livro(titulo, autor))
        elif opcao == "2":
            titulo = input("Título: ")
            temporadas = int(input("Temporadas: "))
            estante.adicionar(Serie(titulo, temporadas))
        elif opcao == "3":
            mostrar(estante.itens)
        elif opcao == "4":
            mostrar(estante.pendentes())
        elif opcao == "5":
            mostrar(estante.itens)
            try:
                numero = int(input("Número do item: "))
                nota = float(input("Nota (0 a 10): "))
                estante.itens[numero - 1].concluir(nota)
            except (ValueError, IndexError) as erro:
                print(f"Não deu certo: {erro}")
        elif opcao == "6":
            media = estante.media_notas()
            print("Nenhum item concluído ainda." if media is None else f"Média: {media:.1f}")
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
