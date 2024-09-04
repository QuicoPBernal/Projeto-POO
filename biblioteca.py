class Livro:

  def __init__(self, titulo, autor, id, status="Disponível"):
      self.titulo = titulo
      self.autor = autor
      self.id = id
      self.status = status

  def emprestar(self):

      if self.status == "Disponível":
          self.status = "Emprestado"
          print(f"O livro '{self.titulo}' foi emprestado.")
      else:
          print(f"O livro '{self.titulo}' já está emprestado.")

  def devolver(self):

      if self.status == "Emprestado":
          self.status = "Disponível"
          print(f"O livro '{self.titulo}' foi devolvido.")
      else:
          print(f"O livro '{self.titulo}' já está disponível.")

  def __str__(self):

      return f"Título: {self.titulo}\nAutor: {self.autor}\nID: {self.id}\nStatus: {self.status}"


class Membro:

  def __init__(self, nome, numero_membro, livros_emprestados=[]):
      self.nome = nome
      self.numero_membro = numero_membro
      self.livros_emprestados = livros_emprestados

  def emprestar_livro(self, livro):

      if livro.status == "Disponível":
          self.livros_emprestados.append(livro)
          livro.emprestar()
          print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
      else:
          print(f"O livro '{livro.titulo}' não está disponível.")

  def devolver_livro(self, livro):

      if livro in self.livros_emprestados:
          self.livros_emprestados.remove(livro)
          livro.devolver()
          print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
      else:
          print(f"{self.nome} não está emprestando o livro '{livro.titulo}'.")

  def __str__(self):

      return f"Nome: {self.nome}\nNúmero de Membro: {self.numero_membro}\nLivros Emprestados: {', '.join([livro.titulo for livro in self.livros_emprestados])}"


class Biblioteca:

  def __init__(self):
      self.catalogo = []
      self.membros = []

  def adicionar_livro(self, livro):

      self.catalogo.append(livro)
      print(f"O livro '{livro.titulo}' foi adicionado ao catálogo.")

  def adicionar_membro(self, membro):

      self.membros.append(membro)
      print(f"{membro.nome} foi adicionado à biblioteca.")

  def encontrar_livro(self, titulo_ou_id):

      for livro in self.catalogo:
          if livro.titulo == titulo_ou_id or livro.id == titulo_ou_id:
              return livro
      return None

  def emprestar_livro(self, titulo_ou_id, numero_membro):

      livro = self.encontrar_livro(titulo_ou_id)
      membro = self.encontrar_membro(numero_membro)
      if livro and membro:
          membro.emprestar_livro(livro)
      else:
          print("Livro ou membro não encontrado.")

  def devolver_livro(self, titulo_ou_id, numero_membro):

      livro = self.encontrar_livro(titulo_ou_id)
      membro = self.encontrar_membro(numero_membro)
      if livro and membro:
          membro.devolver_livro(livro)
      else:
          print("Livro ou membro não encontrado.")

  def encontrar_membro(self, numero_membro):

      for membro in self.membros:
          if membro.numero_membro == numero_membro:
              return membro
      return None

  def listar_livros(self):

      if self.catalogo:
          for livro in self.catalogo:
              print(livro)
              print("-" * 20)
      else:
          print("O catálogo está vazio.")

  def listar_membros(self):

      if self.membros:
          for membro in self.membros:
              print(membro)
              print("-" * 20)
      else:
          print("Não há membros cadastrados.")



def main():

    biblioteca = Biblioteca()

    while True:
        print("\nBem-vindo à Biblioteca!")
        print("1. Adicionar Livro")
        print("2. Adicionar Membro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Pesquisar Livro")
        print("6. Listar Livros")
        print("7. Listar Membros")
        print("8. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            id = input("Digite o ID do livro: ")
            livro = Livro(titulo, autor, id)
            biblioteca.adicionar_livro(livro)

        elif opcao == '2':
            nome = input("Digite o nome do membro: ")
            numero_membro = input("Digite o número do membro: ")
            membro = Membro(nome, numero_membro)
            biblioteca.adicionar_membro(membro)

        elif opcao == '3':
            titulo_ou_id = input("Digite o título ou ID do livro: ")
            numero_membro = input("Digite o número do membro: ")
            biblioteca.emprestar_livro(titulo_ou_id, numero_membro)

        elif opcao == '4':
            titulo_ou_id = input("Digite o título ou ID do livro: ")
            numero_membro = input("Digite o número do membro: ")
            biblioteca.devolver_livro(titulo_ou_id, numero_membro)

        elif opcao == '5':
            titulo_ou_id = input("Digite o título ou ID do livro: ")
            livro = biblioteca.encontrar_livro(titulo_ou_id)
            if livro:
                print(livro)
            else:
                print("Livro não encontrado.")

        elif opcao == '6':
            biblioteca.listar_livros()

        elif opcao == '7':
            biblioteca.listar_membros()

        elif opcao == '8':
            print("Saindo da biblioteca...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
