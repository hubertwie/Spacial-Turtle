# Generated from SpacialTurtle.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SpacialTurtleParser import SpacialTurtleParser
else:
    from SpacialTurtleParser import SpacialTurtleParser

# This class defines a complete generic visitor for a parse tree produced by SpacialTurtleParser.

class SpacialTurtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpacialTurtleParser#program.
    def visitProgram(self, ctx:SpacialTurtleParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#statement.
    def visitStatement(self, ctx:SpacialTurtleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#faceStatement.
    def visitFaceStatement(self, ctx:SpacialTurtleParser.FaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#command.
    def visitCommand(self, ctx:SpacialTurtleParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#moveCmd.
    def visitMoveCmd(self, ctx:SpacialTurtleParser.MoveCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#turnCmd.
    def visitTurnCmd(self, ctx:SpacialTurtleParser.TurnCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#penCmd.
    def visitPenCmd(self, ctx:SpacialTurtleParser.PenCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#faceBlock.
    def visitFaceBlock(self, ctx:SpacialTurtleParser.FaceBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#exportCmd.
    def visitExportCmd(self, ctx:SpacialTurtleParser.ExportCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#declaration.
    def visitDeclaration(self, ctx:SpacialTurtleParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#varType.
    def visitVarType(self, ctx:SpacialTurtleParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#assignStmt.
    def visitAssignStmt(self, ctx:SpacialTurtleParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#exprStmt.
    def visitExprStmt(self, ctx:SpacialTurtleParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#block.
    def visitBlock(self, ctx:SpacialTurtleParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#ifStmt.
    def visitIfStmt(self, ctx:SpacialTurtleParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#whileStmt.
    def visitWhileStmt(self, ctx:SpacialTurtleParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#forStmt.
    def visitForStmt(self, ctx:SpacialTurtleParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#funcDef.
    def visitFuncDef(self, ctx:SpacialTurtleParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#returnStmt.
    def visitReturnStmt(self, ctx:SpacialTurtleParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#paramList.
    def visitParamList(self, ctx:SpacialTurtleParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#variableRef.
    def visitVariableRef(self, ctx:SpacialTurtleParser.VariableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#printStmt.
    def visitPrintStmt(self, ctx:SpacialTurtleParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#expr.
    def visitExpr(self, ctx:SpacialTurtleParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#logicalExpr.
    def visitLogicalExpr(self, ctx:SpacialTurtleParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:SpacialTurtleParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:SpacialTurtleParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:SpacialTurtleParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#unaryExpr.
    def visitUnaryExpr(self, ctx:SpacialTurtleParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:SpacialTurtleParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#funcCall.
    def visitFuncCall(self, ctx:SpacialTurtleParser.FuncCallContext):
        return self.visitChildren(ctx)



del SpacialTurtleParser