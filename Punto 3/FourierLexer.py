# FourierLexer.py
from antlr4 import *

class FourierLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    WS = 18

    channelNames = [DEFAULT_CHANNEL]
    modeNames = [DEFAULT_MODE]

    literalNames = [ "<INVALID>", "'F'", "'='", "'P'", "'rectangular'", "'triangular'", "'dirac'", "'signum'", "'cos'", "'sin'" ]
    symbolicNames = [ "<INVALID>", "ID", "INT", "FLOAT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", "WS" ]

    def __init__(self, input:CharStream):
        super().__init__(input)
