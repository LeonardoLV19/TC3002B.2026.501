# Generated from RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete generic visitor for a parse tree produced by RaraLangParser.

class RaraLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RaraLangParser#prog.
    def visitProg(self, ctx:RaraLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#printStmt.
    def visitPrintStmt(self, ctx:RaraLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#assignStmt.
    def visitAssignStmt(self, ctx:RaraLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#neg.
    def visitNeg(self, ctx:RaraLangParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#based.
    def visitBased(self, ctx:RaraLangParser.BasedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#paren.
    def visitParen(self, ctx:RaraLangParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#string.
    def visitString(self, ctx:RaraLangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#var.
    def visitVar(self, ctx:RaraLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#addSub.
    def visitAddSub(self, ctx:RaraLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#int.
    def visitInt(self, ctx:RaraLangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#mulDiv.
    def visitMulDiv(self, ctx:RaraLangParser.MulDivContext):
        return self.visitChildren(ctx)



del RaraLangParser