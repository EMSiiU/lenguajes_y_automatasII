# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,19,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,5,6,15,0,6,1,0,0,0,2,9,1,
        0,0,0,4,16,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,
        0,0,10,11,5,3,0,0,11,12,3,4,2,0,12,13,5,2,0,0,13,14,3,4,2,0,14,15,
        5,4,0,0,15,3,1,0,0,0,16,17,7,0,0,0,17,5,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'>'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "MAYOR", "PAR1", "PAR2", "IDT", 
                      "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_valor = 2

    ruleNames =  [ "root", "expr", "valor" ]

    EOF = Token.EOF
    IF=1
    MAYOR=2
    PAR1=3
    PAR2=4
    IDT=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def PAR1(self):
            return self.getToken(ExprParser.PAR1, 0)

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValorContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValorContext,i)


        def MAYOR(self):
            return self.getToken(ExprParser.MAYOR, 0)

        def PAR2(self):
            return self.getToken(ExprParser.PAR2, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(ExprParser.IF)
            self.state = 10
            self.match(ExprParser.PAR1)
            self.state = 11
            self.valor()
            self.state = 12
            self.match(ExprParser.MAYOR)
            self.state = 13
            self.valor()
            self.state = 14
            self.match(ExprParser.PAR2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def IDT(self):
            return self.getToken(ExprParser.IDT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_valor




    def valor(self):

        localctx = ExprParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





