# fourier_transform.py
from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser

def main():
    # Cambia 'expresion.txt' por el nombre de tu archivo
    with open('expresion.txt', 'r') as file:
        input_stream = InputStream(file.read())
        
    lexer = FourierLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierParser(stream)

    tree = parser.program()  # Llama a la regla inicial
    print(tree.toStringTree(recog=parser))  # Muestra el árbol de análisis

if __name__ == "__main__":
    main()
