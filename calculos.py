def gerar_tabuada(numero):
    """Gera a tabuada de 1 a 10 para o número fornecido.
    
    Args:
        numero (int): O número para o qual a tabuada será gerada.
    
    Returns:
        list: Uma lista contendo as linhas da tabuada.
    """
    return [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]
