# Generated from RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete listener for a parse tree produced by RaraLangParser.
class RaraLangListener(ParseTreeListener):

    # Enter a parse tree produced by RaraLangParser#prog.
    def enterProg(self, ctx:RaraLangParser.ProgContext):
        pass

    # Exit a parse tree produced by RaraLangParser#prog.
    def exitProg(self, ctx:RaraLangParser.ProgContext):
        pass


    # Enter a parse tree produced by RaraLangParser#funcDecl.
    def enterFuncDecl(self, ctx:RaraLangParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by RaraLangParser#funcDecl.
    def exitFuncDecl(self, ctx:RaraLangParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by RaraLangParser#paramList.
    def enterParamList(self, ctx:RaraLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by RaraLangParser#paramList.
    def exitParamList(self, ctx:RaraLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by RaraLangParser#printStmt.
    def enterPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#printStmt.
    def exitPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#assignStmt.
    def enterAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#assignStmt.
    def exitAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ifStmt.
    def enterIfStmt(self, ctx:RaraLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ifStmt.
    def exitIfStmt(self, ctx:RaraLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#whileStmt.
    def enterWhileStmt(self, ctx:RaraLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#whileStmt.
    def exitWhileStmt(self, ctx:RaraLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#blockStmt.
    def enterBlockStmt(self, ctx:RaraLangParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#blockStmt.
    def exitBlockStmt(self, ctx:RaraLangParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#returnStmt.
    def enterReturnStmt(self, ctx:RaraLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by RaraLangParser#returnStmt.
    def exitReturnStmt(self, ctx:RaraLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by RaraLangParser#call.
    def enterCall(self, ctx:RaraLangParser.CallContext):
        pass

    # Exit a parse tree produced by RaraLangParser#call.
    def exitCall(self, ctx:RaraLangParser.CallContext):
        pass


    # Enter a parse tree produced by RaraLangParser#neg.
    def enterNeg(self, ctx:RaraLangParser.NegContext):
        pass

    # Exit a parse tree produced by RaraLangParser#neg.
    def exitNeg(self, ctx:RaraLangParser.NegContext):
        pass


    # Enter a parse tree produced by RaraLangParser#based.
    def enterBased(self, ctx:RaraLangParser.BasedContext):
        pass

    # Exit a parse tree produced by RaraLangParser#based.
    def exitBased(self, ctx:RaraLangParser.BasedContext):
        pass


    # Enter a parse tree produced by RaraLangParser#paren.
    def enterParen(self, ctx:RaraLangParser.ParenContext):
        pass

    # Exit a parse tree produced by RaraLangParser#paren.
    def exitParen(self, ctx:RaraLangParser.ParenContext):
        pass


    # Enter a parse tree produced by RaraLangParser#compare.
    def enterCompare(self, ctx:RaraLangParser.CompareContext):
        pass

    # Exit a parse tree produced by RaraLangParser#compare.
    def exitCompare(self, ctx:RaraLangParser.CompareContext):
        pass


    # Enter a parse tree produced by RaraLangParser#string.
    def enterString(self, ctx:RaraLangParser.StringContext):
        pass

    # Exit a parse tree produced by RaraLangParser#string.
    def exitString(self, ctx:RaraLangParser.StringContext):
        pass


    # Enter a parse tree produced by RaraLangParser#var.
    def enterVar(self, ctx:RaraLangParser.VarContext):
        pass

    # Exit a parse tree produced by RaraLangParser#var.
    def exitVar(self, ctx:RaraLangParser.VarContext):
        pass


    # Enter a parse tree produced by RaraLangParser#addSub.
    def enterAddSub(self, ctx:RaraLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by RaraLangParser#addSub.
    def exitAddSub(self, ctx:RaraLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by RaraLangParser#int.
    def enterInt(self, ctx:RaraLangParser.IntContext):
        pass

    # Exit a parse tree produced by RaraLangParser#int.
    def exitInt(self, ctx:RaraLangParser.IntContext):
        pass


    # Enter a parse tree produced by RaraLangParser#mulDiv.
    def enterMulDiv(self, ctx:RaraLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by RaraLangParser#mulDiv.
    def exitMulDiv(self, ctx:RaraLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by RaraLangParser#argList.
    def enterArgList(self, ctx:RaraLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by RaraLangParser#argList.
    def exitArgList(self, ctx:RaraLangParser.ArgListContext):
        pass



del RaraLangParser