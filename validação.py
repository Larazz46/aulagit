def validar_numero(entrada):
    """Valida se a entrada fornecida é um número.
    
    Args:
        entrada (str): O valor inserido pelo usuário.
    
    Returns:
        int or None: O número convertido ou None se inválido.
    """
    try:
        return int(entrada)
    except ValueError:
        return None
