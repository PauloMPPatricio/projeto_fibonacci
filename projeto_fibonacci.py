""" Projeto Para a seleção de estágio da Target Sistemas
Nome: Paulo Mauricio Pereira Patricio
Estudante: Análise e Desenvolvimento de Sistemas"""


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
    while True:
        try:
            # Solicita que o usuário insira um número inteiro
            numero = int(input("Informe um número inteiro para verificar se pertence à sequência de Fibonacci: "))
            return numero
        except ValueError:
            # Trata o erro de valor caso o usuário não insira um número inteiro
            print("Entrada inválida. Por favor, insira um número inteiro.")


# Função principal para rodar o programa
def main():
    # Chama a função que garante uma entrada válida
    numero = entrada_valida()

    # Cria uma instância da classe Fibonacci
    fibonacci = Fibonacci()

    # Verifica se o número pertence à sequência de Fibonacci
    if fibonacci.pertence_a_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


# Executa o programa principal
if __name__ == "__main__":
    main()
