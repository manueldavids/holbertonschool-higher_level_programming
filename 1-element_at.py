def element_at(my_list, idx):
    """
    Recupera un elemento de una lista dado su índice.

    Args:
        my_list (list): La lista de la que queremos recuperar el elemento.
        idx (int): El índice del elemento.

    Returns:
        El elemento en el índice dado, o None si el índice no es válido.
    """
    # Verificar si el índice es negativo o fuera del rango de la lista
    if idx < 0 or idx >= len(my_list):
        return None
    # Devolver el elemento en el índice válido
    return my_list[idx]
