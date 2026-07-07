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
        4,1,6,21,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,19,0,6,1,0,0,0,2,
        14,1,0,0,0,4,16,1,0,0,0,6,7,3,4,2,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,
        5,1,0,0,10,11,5,3,0,0,11,15,3,2,1,0,12,15,5,1,0,0,13,15,5,2,0,0,
        14,9,1,0,0,0,14,12,1,0,0,0,14,13,1,0,0,0,15,3,1,0,0,0,16,17,5,1,
        0,0,17,18,5,3,0,0,18,19,5,2,0,0,19,5,1,0,0,0,1,14
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "ID", "NUM", "IGUAL", "MAS", "MENOS", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_expr2 = 2

    ruleNames =  [ "root", "expr", "expr2" ]

    EOF = Token.EOF
    ID=1
    NUM=2
    IGUAL=3
    MAS=4
    MENOS=5
    WS=6

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

        def expr2(self):
            return self.getTypedRuleContext(ExprParser.Expr2Context,0)


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
            self.expr2()
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

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def IGUAL(self):
            return self.getToken(ExprParser.IGUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 14
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(ExprParser.ID)
                self.state = 10
                self.match(ExprParser.IGUAL)
                self.state = 11
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(ExprParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def IGUAL(self):
            return self.getToken(ExprParser.IGUAL, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr2




    def expr2(self):

        localctx = ExprParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(ExprParser.ID)
            self.state = 17
            self.match(ExprParser.IGUAL)
            self.state = 18
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





