# Generated from Grammar.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx:GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printExpr.
    def visitPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assign.
    def visitAssign(self, ctx:GrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#blank.
    def visitBlank(self, ctx:GrammarParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ExpFlo.
    def visitExpFlo(self, ctx:GrammarParser.ExpFloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parens.
    def visitParens(self, ctx:GrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#dec.
    def visitDec(self, ctx:GrammarParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#OpIn.
    def visitOpIn(self, ctx:GrammarParser.OpInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#MulDiv.
    def visitMulDiv(self, ctx:GrammarParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AddSub.
    def visitAddSub(self, ctx:GrammarParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Index.
    def visitIndex(self, ctx:GrammarParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#String.
    def visitString(self, ctx:GrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#int.
    def visitInt(self, ctx:GrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Not.
    def visitNot(self, ctx:GrammarParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Bool.
    def visitBool(self, ctx:GrammarParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Comparators.
    def visitComparators(self, ctx:GrammarParser.ComparatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#List.
    def visitList(self, ctx:GrammarParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#id.
    def visitId(self, ctx:GrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AndOr.
    def visitAndOr(self, ctx:GrammarParser.AndOrContext):
        return self.visitChildren(ctx)



del GrammarParser