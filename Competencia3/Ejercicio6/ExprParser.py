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
        4,1,4,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,0,1,2,4,0,2,4,6,0,1,1,0,2,3,30,0,8,1,0,0,
        0,2,11,1,0,0,0,4,25,1,0,0,0,6,27,1,0,0,0,8,9,3,6,3,0,9,10,5,0,0,
        1,10,1,1,0,0,0,11,12,6,1,-1,0,12,13,5,1,0,0,13,22,1,0,0,0,14,15,
        10,2,0,0,15,16,3,4,2,0,16,17,3,2,1,0,17,18,3,4,2,0,18,19,3,2,1,3,
        19,21,1,0,0,0,20,14,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,
        0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,26,7,0,0,0,26,5,1,0,0,0,27,28,
        5,1,0,0,28,29,5,2,0,0,29,30,5,1,0,0,30,31,5,3,0,0,31,32,5,1,0,0,
        32,7,1,0,0,0,1,22
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "NUM", "MAS", "POR", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_op = 2
    RULE_expr2 = 3

    ruleNames =  [ "root", "expr", "op", "expr2" ]

    EOF = Token.EOF
    NUM=1
    MAS=2
    POR=3
    WS=4

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
            self.state = 8
            self.expr2()
            self.state = 9
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

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.OpContext)
            else:
                return self.getTypedRuleContext(ExprParser.OpContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(ExprParser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.op()
                    self.state = 16
                    self.expr(0)
                    self.state = 17
                    self.op()
                    self.state = 18
                    self.expr(3) 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)

        def POR(self):
            return self.getToken(ExprParser.POR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_op




    def op(self):

        localctx = ExprParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUM)
            else:
                return self.getToken(ExprParser.NUM, i)

        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)

        def POR(self):
            return self.getToken(ExprParser.POR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr2




    def expr2(self):

        localctx = ExprParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ExprParser.NUM)
            self.state = 28
            self.match(ExprParser.MAS)
            self.state = 29
            self.match(ExprParser.NUM)
            self.state = 30
            self.match(ExprParser.POR)
            self.state = 31
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




