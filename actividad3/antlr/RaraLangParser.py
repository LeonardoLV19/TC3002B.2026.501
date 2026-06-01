# Generated from RaraLang.g4 by ANTLR 4.13.2
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
        4,1,30,70,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,3,1,41,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,65,8,2,10,2,12,2,68,9,2,1,2,0,
        1,4,3,0,2,4,0,3,1,0,18,21,2,0,16,17,22,22,1,0,12,15,81,0,9,1,0,0,
        0,2,40,1,0,0,0,4,53,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,
        9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,
        1,13,1,1,0,0,0,14,15,5,5,0,0,15,41,3,4,2,0,16,17,5,27,0,0,17,18,
        5,6,0,0,18,41,3,4,2,0,19,20,5,7,0,0,20,21,3,4,2,0,21,22,5,8,0,0,
        22,25,3,2,1,0,23,24,5,9,0,0,24,26,3,2,1,0,25,23,1,0,0,0,25,26,1,
        0,0,0,26,41,1,0,0,0,27,28,5,10,0,0,28,29,3,4,2,0,29,30,5,11,0,0,
        30,31,3,2,1,0,31,41,1,0,0,0,32,36,5,1,0,0,33,35,3,2,1,0,34,33,1,
        0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,
        36,1,0,0,0,39,41,5,2,0,0,40,14,1,0,0,0,40,16,1,0,0,0,40,19,1,0,0,
        0,40,27,1,0,0,0,40,32,1,0,0,0,41,3,1,0,0,0,42,43,6,2,-1,0,43,44,
        5,23,0,0,44,54,3,4,2,6,45,46,5,3,0,0,46,47,3,4,2,0,47,48,5,4,0,0,
        48,54,1,0,0,0,49,54,5,24,0,0,50,54,5,25,0,0,51,54,5,26,0,0,52,54,
        5,27,0,0,53,42,1,0,0,0,53,45,1,0,0,0,53,49,1,0,0,0,53,50,1,0,0,0,
        53,51,1,0,0,0,53,52,1,0,0,0,54,66,1,0,0,0,55,56,10,9,0,0,56,57,7,
        0,0,0,57,65,3,4,2,10,58,59,10,8,0,0,59,60,7,1,0,0,60,65,3,4,2,9,
        61,62,10,7,0,0,62,63,7,2,0,0,63,65,3,4,2,8,64,55,1,0,0,0,64,58,1,
        0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,
        5,1,0,0,0,68,66,1,0,0,0,7,9,25,36,40,53,64,66
    ]

class RaraLangParser ( Parser ):

    grammarFileName = "RaraLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "'print'", 
                     "'<--'", "'if'", "'then'", "'else'", "'while'", "'do'", 
                     "'=='", "'!='", "'<'", "'>'", "'+'", "'-'", "'\\u00D7'", 
                     "'\\u00F7'", "'\\u229E'", "'\\u22A0'", "'\\u2248'", 
                     "'\\u00B1'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PRINT", "ASSIGN", "IF", "THEN", "ELSE", 
                      "WHILE", "DO", "EQ", "NEQ", "LT", "GT", "PLUS", "MINUS", 
                      "TIMES", "DIVIDE", "MOD", "DPLS", "AVG", "UNEG", "INT", 
                      "BASED_NUMBER", "STRING", "ID", "NEWLINE", "COMMENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PRINT=5
    ASSIGN=6
    IF=7
    THEN=8
    ELSE=9
    WHILE=10
    DO=11
    EQ=12
    NEQ=13
    LT=14
    GT=15
    PLUS=16
    MINUS=17
    TIMES=18
    DIVIDE=19
    MOD=20
    DPLS=21
    AVG=22
    UNEG=23
    INT=24
    BASED_NUMBER=25
    STRING=26
    ID=27
    NEWLINE=28
    COMMENT=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RaraLangParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StmtContext,i)


        def getRuleIndex(self):
            return RaraLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RaraLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134218914) != 0):
                self.state = 6
                self.stmt()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(RaraLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(RaraLangParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(RaraLangParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)

        def DO(self):
            return self.getToken(RaraLangParser.DO, 0)
        def stmt(self):
            return self.getTypedRuleContext(RaraLangParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(RaraLangParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)

        def THEN(self):
            return self.getToken(RaraLangParser.THEN, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(RaraLangParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(RaraLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = RaraLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = RaraLangParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(RaraLangParser.PRINT)
                self.state = 15
                self.expr(0)
                pass
            elif token in [27]:
                localctx = RaraLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(RaraLangParser.ID)
                self.state = 17
                self.match(RaraLangParser.ASSIGN)
                self.state = 18
                self.expr(0)
                pass
            elif token in [7]:
                localctx = RaraLangParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(RaraLangParser.IF)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(RaraLangParser.THEN)
                self.state = 22
                self.stmt()
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.match(RaraLangParser.ELSE)
                    self.state = 24
                    self.stmt()


                pass
            elif token in [10]:
                localctx = RaraLangParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.match(RaraLangParser.WHILE)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(RaraLangParser.DO)
                self.state = 30
                self.stmt()
                pass
            elif token in [1]:
                localctx = RaraLangParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.match(RaraLangParser.T__0)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134218914) != 0):
                    self.state = 33
                    self.stmt()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                self.match(RaraLangParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

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


        def getRuleIndex(self):
            return RaraLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNEG(self):
            return self.getToken(RaraLangParser.UNEG, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class BasedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BASED_NUMBER(self):
            return self.getToken(RaraLangParser.BASED_NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBased" ):
                listener.enterBased(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBased" ):
                listener.exitBased(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBased" ):
                return visitor.visitBased(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(RaraLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(RaraLangParser.NEQ, 0)
        def LT(self):
            return self.getToken(RaraLangParser.LT, 0)
        def GT(self):
            return self.getToken(RaraLangParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(RaraLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(RaraLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RaraLangParser.MINUS, 0)
        def AVG(self):
            return self.getToken(RaraLangParser.AVG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RaraLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(RaraLangParser.TIMES, 0)
        def DIVIDE(self):
            return self.getToken(RaraLangParser.DIVIDE, 0)
        def MOD(self):
            return self.getToken(RaraLangParser.MOD, 0)
        def DPLS(self):
            return self.getToken(RaraLangParser.DPLS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RaraLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = RaraLangParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(RaraLangParser.UNEG)
                self.state = 44
                self.expr(6)
                pass
            elif token in [3]:
                localctx = RaraLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(RaraLangParser.T__2)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(RaraLangParser.T__3)
                pass
            elif token in [24]:
                localctx = RaraLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(RaraLangParser.INT)
                pass
            elif token in [25]:
                localctx = RaraLangParser.BasedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(RaraLangParser.BASED_NUMBER)
                pass
            elif token in [26]:
                localctx = RaraLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(RaraLangParser.STRING)
                pass
            elif token in [27]:
                localctx = RaraLangParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(RaraLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = RaraLangParser.MulDivContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = RaraLangParser.AddSubContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4390912) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = RaraLangParser.CompareContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(8)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




