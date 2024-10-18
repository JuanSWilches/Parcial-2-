import sys
from antlr4 import *
from objiterableLexer import objiterableLexer
from objiterableParser import objiterableParser

class FuncionesMatematicas:
    def __init__(self):
        self.funciones = {
            "cuadrado": lambda x: x ** 2,
            "doble": lambda x: x * 2,
            "par": lambda x: x % 2 == 0,
            "impar": lambda x: x % 2 != 0,
            "multiple": lambda x: x % 3 == 0,
            "raiz": lambda x: x ** 0.5,
            "incrementar": lambda x, n=1: x + n,
            "decrementar": lambda x, n=1: x - n,
            "absoluto": lambda x: x
        }

    def obtener_funcion(self, nombre_funcion):
        return self.funciones.get(nombre_funcion, lambda x: x)

class OperacionesAvanzadas:
    def calcular_rango(self, numeros):
        return max(numeros) - min(numeros) if numeros else 0

    def suma(self, numeros):
        return sum(numeros)

class ManejadorOperaciones(ParseTreeListener):
    def __init__(self):
        self.operaciones = FuncionesMatematicas()
        self.operaciones_avanzadas = OperacionesAvanzadas()

    def extraer_iterable(self, ctx):
        if ctx.listExpression():
            return [int(elemento.getText()) for elemento in ctx.listExpression().itemList().item()]
        elif ctx.tupleExpression():
            return [int(elemento.getText()) for elemento in ctx.tupleExpression().itemList().item()]
        elif ctx.functionIdentifier():
            return [ctx.functionIdentifier().getText()]
        return []

    def ejecutar_operacion(self, ctx, tipo):
        funcion = ctx.functionCall().getText()
        iterable = self.extraer_iterable(ctx.iterableValue())

        if tipo == "map":
            resultado = list(map(self.operaciones.obtener_funcion(funcion), iterable))
        else:  # tipo == "filter"
            resultado = list(filter(self.operaciones.obtener_funcion(funcion), iterable))

        accion = "MAPA" if tipo == "map" else "FILTRO"
        print(f"{accion}: Función '{funcion}' aplicada a {iterable} produce {resultado}")

    def enterMappingStatement(self, ctx: objiterableParser.MappingStatementContext):
        self.ejecutar_operacion(ctx, "map")

    def enterFilteringStatement(self, ctx: objiterableParser.FilteringStatementContext):
        self.ejecutar_operacion(ctx, "filter")

def principal(argv):
    if len(argv) < 2:
        print("Uso: python funciones.py <archivo_de_entrada>")
        return
    
    print("Iniciando el programa...")
    
    try:
        flujo_entrada = FileStream(argv[1])
        lexer = objiterableLexer(flujo_entrada)
        stream = CommonTokenStream(lexer)
        parser = objiterableParser(stream)
        arbol = parser.program()

        print("Análisis sintáctico completado. Procesando el árbol de análisis...")
        
        escucha = ManejadorOperaciones()
        caminante = ParseTreeWalker()
        caminante.walk(escucha, arbol)

        print("El procesamiento ha finalizado.")

    except FileNotFoundError:
        print(f"Error: El archivo '{argv[1]}' no se pudo encontrar.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == '__main__':
    principal(sys.argv)

