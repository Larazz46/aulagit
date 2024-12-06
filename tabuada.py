from mensagens import exibir_mensagem_inicial
from validacao import validar_numero
from calculos import gerar_tabuada

def main():
    # Exibe uma mensagem inicial para o usuário
    exibir_mensagem_inicial()

    while True:
        # Solicita ao usuário um número para gerar a tabuada
        entrada = input("Digite um número para gerar a tabuada (ou 'sair' para encerrar): ").strip()

        if entrada.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break

        # Valida se a entrada é um número válido
        numero = validar_numero(entrada)
        if numero is not None:
            # Gera e exibe a tabuada do número
            tabuada = gerar_tabuada(numero)
            print(f"\nTabuada do {numero}:")
            for linha in tabuada:
                print(linha)
            print("\n")
        else:
            print("Entrada inválida. Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
