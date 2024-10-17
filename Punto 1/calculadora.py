import sys
from antlr4 import *
from calnumcomplejosLexer import calnumcomplejosLexer
from calnumcomplejosParser import calnumcomplejosParser

class ManejadorErrores:
    @staticmethod
    def manejar_error(e):
        """Maneja errores específicos."""
        if isinstance(e, ZeroDivisionError):
            print("Error: División por cero.")
        elif isinstance(e, ValueError):
            print("Error: Valor inválido ingresado.")
        else:
            print(f"Error: {e}")

class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def suma(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imaginario + otro.imaginario)

    def resta(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imaginario - otro.imaginario)

    def multiplicacion(self, otro):
        return NumeroComplejo(
            self.real * otro.real - self.imaginario * otro.imaginario,
            self.real * otro.imaginario + self.imaginario * otro.real
        )

    def division(self, otro):
        denom = otro.real ** 2 + otro.imaginario ** 2
        if denom == 0:
            raise ZeroDivisionError("División por cero")
        return NumeroComplejo(
            (self.real * otro.real + self.imaginario * otro.imaginario) / denom,
            (self.imaginario * otro.real - self.real * otro.imaginario) / denom
        )

class Evaluador(ParseTreeListener):
    def enterExpr(self, ctx: calnumcomplejosParser.ExprContext):
        resultado = None
        for i in range(0, len(ctx.children), 2):
            num_complejo = self.extraerNumeroComplejo(ctx.getChild(i))
            if resultado is None:
                resultado = num_complejo
            else:
                operador = ctx.getChild(i-1).getText()
                # Impresión de la operación que se está realizando con paréntesis
                print(f"Realizando operación: ({resultado}) {operador} ({num_complejo})")
                resultado = self.aplicarOperacion(resultado, num_complejo, operador)
        if resultado:
            print(f"Resultado: ({resultado})")

    def extraerNumeroComplejo(self, ctx):
        real = int(ctx.realPart().getText())
        imag = int(ctx.imaginaryPart().getText())
        signo = ctx.sign().getText()
        return NumeroComplejo(real, -imag if signo == '-' else imag)

    def aplicarOperacion(self, total, num_complejo, operador):
        if operador == '+':
            return total.suma(num_complejo)
        elif operador == '-':
            return total.resta(num_complejo)
        elif operador == '*':
            return total.multiplicacion(num_complejo)
        elif operador == '/':
            return total.division(num_complejo)

def main():
    if len(sys.argv) < 2:
        print("Uso: python calculadora.py <archivo>")
        return
    
    flujo_entrada = FileStream(sys.argv[1])
    lexer = calnumcomplejosLexer(flujo_entrada)
    stream = CommonTokenStream(lexer)
    parser = calnumcomplejosParser(stream)
    tree = parser.prog()

    evaluador = Evaluador()
    
    try:
        walker = ParseTreeWalker()
        walker.walk(evaluador, tree)
    except Exception as e:
        ManejadorErrores.manejar_error(e)

if __name__ == '__main__':
    main()

