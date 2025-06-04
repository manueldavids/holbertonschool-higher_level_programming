#!/usr/bin/python3
"""
Módulo para leer archivos de texto y mostrar su contenido.
"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
