# Definir funções orientadas a objetos em Python envolve a criação de classes e métodos para encapsular comportamentos e dados relacionados.
# Agora, você pode associar um objeto Endereco à classe Pessoa definindo um atributo endereco na classe Pessoa.
class Pessoa:
    # construtor da classe
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    # metodo para exibir informacoes da pessoa
    def exibir_nome_idade(self):
        return f"Olá, meu nome é {self.nome} e minha idade é {self.idade} anos"

    def exibir_endereco(self):
        return self.endereco.exibir_endereco()

# Para criar uma classe chamada Endereco e associá-la à classe Pessoa em Python, você pode usar composição. Composição é um conceito de programação orientada a objetos em que uma classe contém uma instância de outra classe como um de seus atributos. Neste caso, você pode associar um objeto Endereco a cada objeto Pessoa.
# Primeiro, defina a classe Endereco com os atributos relevantes


class Endereco:
    def __init__(self, cidade, rua, cep):
        self.cidade = cidade
        self.rua = rua
        self.cep = cep

    def exibir_endereco(self):
        return f"Endereço: Cidade: {self.cidade}, Rua: {self.rua}, CEP: {self.cep}"


    # criar objetos pessoas. Criei duas instancias da classe pessoa.
endereco1 = Endereco("Porto Alegre", "Canto e Melo", 90830220)
endereco2 = Endereco("Londres", "Santo Antonio", 90830100)

pessoa1 = Pessoa("Bruno", 30, endereco1)
pessoa2 = Pessoa("Carol", 29, endereco2)

# chamar o metodo para exibir informacoes
print(pessoa1.exibir_nome_idade())
print(pessoa1.exibir_endereco())
print(pessoa2.exibir_nome_idade())
print(pessoa2.exibir_endereco())
