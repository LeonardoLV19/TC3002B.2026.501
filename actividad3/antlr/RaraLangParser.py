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
        4,1,33,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,2,1,2,1,2,5,2,
        41,8,2,10,2,12,2,44,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,57,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,66,8,3,10,3,12,3,
        69,9,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,86,8,4,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,5,1,5,1,5,5,
        5,112,8,5,10,5,12,5,115,9,5,1,5,0,1,8,6,0,2,4,6,8,10,0,3,1,0,21,
        24,2,0,19,20,25,25,1,0,15,18,133,0,16,1,0,0,0,2,21,1,0,0,0,4,37,
        1,0,0,0,6,73,1,0,0,0,8,92,1,0,0,0,10,108,1,0,0,0,12,15,3,2,1,0,13,
        15,3,6,3,0,14,12,1,0,0,0,14,13,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,
        0,16,17,1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,20,5,0,0,1,20,1,1,
        0,0,0,21,22,5,13,0,0,22,23,5,30,0,0,23,25,5,1,0,0,24,26,3,4,2,0,
        25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,2,0,0,28,32,5,
        3,0,0,29,31,3,6,3,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,
        33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,4,0,0,36,3,1,0,0,
        0,37,42,5,30,0,0,38,39,5,5,0,0,39,41,5,30,0,0,40,38,1,0,0,0,41,44,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,42,1,0,0,0,45,
        46,5,6,0,0,46,74,3,8,4,0,47,48,5,30,0,0,48,49,5,7,0,0,49,74,3,8,
        4,0,50,51,5,8,0,0,51,52,3,8,4,0,52,53,5,9,0,0,53,56,3,6,3,0,54,55,
        5,10,0,0,55,57,3,6,3,0,56,54,1,0,0,0,56,57,1,0,0,0,57,74,1,0,0,0,
        58,59,5,11,0,0,59,60,3,8,4,0,60,61,5,12,0,0,61,62,3,6,3,0,62,74,
        1,0,0,0,63,67,5,3,0,0,64,66,3,6,3,0,65,64,1,0,0,0,66,69,1,0,0,0,
        67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,74,5,
        4,0,0,71,72,5,14,0,0,72,74,3,8,4,0,73,45,1,0,0,0,73,47,1,0,0,0,73,
        50,1,0,0,0,73,58,1,0,0,0,73,63,1,0,0,0,73,71,1,0,0,0,74,7,1,0,0,
        0,75,76,6,4,-1,0,76,77,5,26,0,0,77,93,3,8,4,7,78,79,5,1,0,0,79,80,
        3,8,4,0,80,81,5,2,0,0,81,93,1,0,0,0,82,83,5,30,0,0,83,85,5,1,0,0,
        84,86,3,10,5,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,93,5,
        2,0,0,88,93,5,27,0,0,89,93,5,28,0,0,90,93,5,29,0,0,91,93,5,30,0,
        0,92,75,1,0,0,0,92,78,1,0,0,0,92,82,1,0,0,0,92,88,1,0,0,0,92,89,
        1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,105,1,0,0,0,94,95,10,10,0,
        0,95,96,7,0,0,0,96,104,3,8,4,11,97,98,10,9,0,0,98,99,7,1,0,0,99,
        104,3,8,4,10,100,101,10,8,0,0,101,102,7,2,0,0,102,104,3,8,4,9,103,
        94,1,0,0,0,103,97,1,0,0,0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,
        1,0,0,0,105,106,1,0,0,0,106,9,1,0,0,0,107,105,1,0,0,0,108,113,3,
        8,4,0,109,110,5,5,0,0,110,112,3,8,4,0,111,109,1,0,0,0,112,115,1,
        0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,11,1,0,0,0,115,113,1,0,
        0,0,13,14,16,25,32,42,56,67,73,85,92,103,105,113
    ]

class RaraLangParser ( Parser ):

    grammarFileName = "RaraLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "','", "'print'", 
                     "'<--'", "'if'", "'then'", "'else'", "'while'", "'do'", 
                     "'func'", "'return'", "'=='", "'!='", "'<'", "'>'", 
                     "'+'", "'-'", "'\\u00D7'", "'\\u00F7'", "'\\u229E'", 
                     "'\\u22A0'", "'\\u2248'", "'\\u00B1'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PRINT", "ASSIGN", "IF", 
                      "THEN", "ELSE", "WHILE", "DO", "FUNC", "RETURN", "EQ", 
                      "NEQ", "LT", "GT", "PLUS", "MINUS", "TIMES", "DIVIDE", 
                      "MOD", "DPLS", "AVG", "UNEG", "INT", "BASED_NUMBER", 
                      "STRING", "ID", "NEWLINE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_funcDecl = 1
    RULE_paramList = 2
    RULE_stmt = 3
    RULE_expr = 4
    RULE_argList = 5

    ruleNames =  [ "prog", "funcDecl", "paramList", "stmt", "expr", "argList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    PRINT=6
    ASSIGN=7
    IF=8
    THEN=9
    ELSE=10
    WHILE=11
    DO=12
    FUNC=13
    RETURN=14
    EQ=15
    NEQ=16
    LT=17
    GT=18
    PLUS=19
    MINUS=20
    TIMES=21
    DIVIDE=22
    MOD=23
    DPLS=24
    AVG=25
    UNEG=26
    INT=27
    BASED_NUMBER=28
    STRING=29
    ID=30
    NEWLINE=31
    COMMENT=32
    WS=33

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

        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.FuncDeclContext,i)


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
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073768776) != 0):
                self.state = 14
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 12
                    self.funcDecl()
                    pass
                elif token in [3, 6, 8, 11, 14, 30]:
                    self.state = 13
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(RaraLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(RaraLangParser.FUNC, 0)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(RaraLangParser.ParamListContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StmtContext,i)


        def getRuleIndex(self):
            return RaraLangParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = RaraLangParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(RaraLangParser.FUNC)
            self.state = 22
            self.match(RaraLangParser.ID)
            self.state = 23
            self.match(RaraLangParser.T__0)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 24
                self.paramList()


            self.state = 27
            self.match(RaraLangParser.T__1)
            self.state = 28
            self.match(RaraLangParser.T__2)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073760584) != 0):
                self.state = 29
                self.stmt()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(RaraLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RaraLangParser.ID)
            else:
                return self.getToken(RaraLangParser.ID, i)

        def getRuleIndex(self):
            return RaraLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = RaraLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(RaraLangParser.ID)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 38
                self.match(RaraLangParser.T__4)
                self.state = 39
                self.match(RaraLangParser.ID)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


    class ReturnStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(RaraLangParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = RaraLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = RaraLangParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(RaraLangParser.PRINT)
                self.state = 46
                self.expr(0)
                pass
            elif token in [30]:
                localctx = RaraLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(RaraLangParser.ID)
                self.state = 48
                self.match(RaraLangParser.ASSIGN)
                self.state = 49
                self.expr(0)
                pass
            elif token in [8]:
                localctx = RaraLangParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(RaraLangParser.IF)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(RaraLangParser.THEN)
                self.state = 53
                self.stmt()
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.match(RaraLangParser.ELSE)
                    self.state = 55
                    self.stmt()


                pass
            elif token in [11]:
                localctx = RaraLangParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(RaraLangParser.WHILE)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(RaraLangParser.DO)
                self.state = 61
                self.stmt()
                pass
            elif token in [3]:
                localctx = RaraLangParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(RaraLangParser.T__2)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073760584) != 0):
                    self.state = 64
                    self.stmt()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self.match(RaraLangParser.T__3)
                pass
            elif token in [14]:
                localctx = RaraLangParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.match(RaraLangParser.RETURN)
                self.state = 72
                self.expr(0)
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


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)
        def argList(self):
            return self.getTypedRuleContext(RaraLangParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = RaraLangParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 76
                self.match(RaraLangParser.UNEG)
                self.state = 77
                self.expr(7)
                pass

            elif la_ == 2:
                localctx = RaraLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(RaraLangParser.T__0)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(RaraLangParser.T__1)
                pass

            elif la_ == 3:
                localctx = RaraLangParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(RaraLangParser.ID)
                self.state = 83
                self.match(RaraLangParser.T__0)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374786) != 0):
                    self.state = 84
                    self.argList()


                self.state = 87
                self.match(RaraLangParser.T__1)
                pass

            elif la_ == 4:
                localctx = RaraLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(RaraLangParser.INT)
                pass

            elif la_ == 5:
                localctx = RaraLangParser.BasedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(RaraLangParser.BASED_NUMBER)
                pass

            elif la_ == 6:
                localctx = RaraLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(RaraLangParser.STRING)
                pass

            elif la_ == 7:
                localctx = RaraLangParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(RaraLangParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = RaraLangParser.MulDivContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = RaraLangParser.AddSubContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35127296) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = RaraLangParser.CompareContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(9)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)


        def getRuleIndex(self):
            return RaraLangParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = RaraLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.expr(0)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 109
                self.match(RaraLangParser.T__4)
                self.state = 110
                self.expr(0)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




