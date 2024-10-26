"""
Projeto Para a seleção de estágio da Target Sistemas
Nome: Paulo Mauricio Pereira Patricio
Estudante: Análise e Desenvolvimento de Sistemas

Atualize o número da versão aqui
Versão: 1.0.1

Descrição da Versão:
- Melhorada a legibilidade da saída com inclusão de "\n".
- Adicionado "input()" para pausar a tela e permitir melhor leitura dos resultados.
"""


class Fibonacci:
    def __init__(self):
        # Inicia a sequência com os dois primeiros números de Fibonacci
        self.sequencia = [0, 1]

    def gerar_sequencia(self, limite):
        """
        Gera a sequência de Fibonacci até que o último número
        seja maior ou igual ao limite fornecido.
        """
        while self.sequencia[-1] < limite:
            # Adiciona o próximo número da sequência de Fibonacci
            proximo = self.sequencia[-1] + self.sequencia[-2]
            self.sequencia.append(proximo)

    def pertence_a_fibonacci(self, numero):
        """
        Verifica se o número informado pertence à sequência de Fibonacci.
        """
        # Gera a sequência até o número informado ou maior
        self.gerar_sequencia(numero)

        # Verifica se o número está na sequência gerada
        if numero in self.sequencia:
            return True
        else:
            return False


# Função para garantir que o usuário insira um número inteiro
def entrada_valida():
    print("*" * 3 + " Verificador de Fibonacci " + 3 * "*")
    while True:
        try:
            # Solicita que o usuário insira um número inteiro
            numero = int(input("\nInforme um número inteiro para verificar se pertence à sequência de Fibonacci: "))
            return numero
        except ValueError:
            # Trata o erro de valor caso o usuário não insira um número inteiro
            print("\nEntrada inválida. Por favor, insira um número inteiro.")


# Função principal para rodar o programa
def main():
    # Chama a função que garante uma entrada válida
    numero = entrada_valida()

    # Cria uma instância da classe Fibonacci
    fibonacci = Fibonacci()

    # Verifica se o número pertence à sequência de Fibonacci
    if fibonacci.pertence_a_fibonacci(numero):
        print(f"\nO número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"\nO número {numero} NÃO pertence à sequência de Fibonacci.")
    input()


# Executa o programa principal
if __name__ == "__main__":
    main()
