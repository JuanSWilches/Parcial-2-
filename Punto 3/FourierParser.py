# FourierParser.py
from antlr4 import *
from FourierLexer import FourierLexer

class FourierParser(Parser):
    # Definición de las reglas de la gramática
    RULE_program = 0
    RULE_statement = 1
    RULE_functionStatement = 2
    RULE_pulseStatement = 3
    RULE_pulseType = 4
    RULE_expression = 5

    ruleNames = [
        "program", "statement", "functionStatement", 
        "pulseStatement", "pulseType", "expression"
    ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self._ctx = None

    def program(self):
        # Regla de inicio del programa
        localctx = self._ctx = self.createContext()
        self.enterRule(localctx, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            while True:
                if self._input.LA(1) in [FourierLexer.ID, FourierLexer.T__0, FourierLexer.T__2]:
                    self.statement()
                else:
                    break
        finally:
            self.exitRule()

    def statement(self):
        # Procesa una declaración que puede ser de función o pulso
        localctx = self._ctx
        self.enterRule(localctx, self.RULE_statement)
        try:
            if self._input.LA(1) == FourierLexer.T__0:  # 'F'
                self.functionStatement()
            elif self._input.LA(1) == FourierLexer.T__2:  # 'P'
                self.pulseStatement()
            else:
                raise RecognitionException("Expected function or pulse statement")
        finally:
            self.exitRule()

    def functionStatement(self):
        # Regla para analizar las declaraciones de función
        localctx = self._ctx
        self.enterRule(localctx, self.RULE_functionStatement)
        try:
            self.match(FourierLexer.T__0)  # 'F'
            self.match(FourierLexer.T__1)  # '='
            self.expression()
            self.match(FourierLexer.T__1)  # '='
            self.expression()
        finally:
            self.exitRule()

    def pulseStatement(self):
        # Regla para analizar las declaraciones de pulsos
        localctx = self._ctx
        self.enterRule(localctx, self.RULE_pulseStatement)
        try:
            self.match(FourierLexer.T__2)  # 'P'
            self.match(FourierLexer.T__1)  # '='
            self.pulseType()
        finally:
            self.exitRule()

    def pulseType(self):
        # Regla para analizar los tipos de pulso
        localctx = self._ctx
        self.enterRule(localctx, self.RULE_pulseType)
        try:
            if self._input.LA(1) in [
                FourierLexer.T__3, FourierLexer.T__4, 
                FourierLexer.T__5, FourierLexer.T__6, 
                FourierLexer.T__7, FourierLexer.T__8
            ]:
                self.match(self._input.LA(1))
            else:
                raise RecognitionException("Expected pulse type")
        finally:
            self.exitRule()

    def expression(self):
        # Regla para analizar expresiones (ID, INT, FLOAT)
        localctx = self._ctx
        self.enterRule(localctx, self.RULE_expression)
        try:
            if self._input.LA(1) == FourierLexer.ID:
                self.match(FourierLexer.ID)
            elif self._input.LA(1) == FourierLexer.INT:
                self.match(FourierLexer.INT)
            elif self._input.LA(1) == FourierLexer.FLOAT:
                self.match(FourierLexer.FLOAT)
            else:
                raise RecognitionException("Expected an expression")
        finally:
            self.exitRule()
