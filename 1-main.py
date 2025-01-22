#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

# Lista de ejemplo
my_list = [1, 2, 3, 4, 5]

# Índice a verificar
idx = 3

# Imprimir el resultado
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# Pruebas adicionales
print("Element at index -1 is {}".format(element_at(my_list, -1)))  # None
print("Element at index 10 is {}".format(element_at(my_list, 10)))  # None
print("Element at index 2 is {}".format(element_at(my_list, 2)))  # 3
