# Generated from SpacialTurtle.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SpacialTurtleParser import SpacialTurtleParser
else:
    from SpacialTurtleParser import SpacialTurtleParser

# This class defines a complete listener for a parse tree produced by SpacialTurtleParser.
class SpacialTurtleListener(ParseTreeListener):

    # Enter a parse tree produced by SpacialTurtleParser#program.
    def enterProgram(self, ctx:SpacialTurtleParser.ProgramContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#program.
    def exitProgram(self, ctx:SpacialTurtleParser.ProgramContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#statement.
    def enterStatement(self, ctx:SpacialTurtleParser.StatementContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#statement.
    def exitStatement(self, ctx:SpacialTurtleParser.StatementContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#faceStatement.
    def enterFaceStatement(self, ctx:SpacialTurtleParser.FaceStatementContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#faceStatement.
    def exitFaceStatement(self, ctx:SpacialTurtleParser.FaceStatementContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#command.
    def enterCommand(self, ctx:SpacialTurtleParser.CommandContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#command.
    def exitCommand(self, ctx:SpacialTurtleParser.CommandContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#moveCmd.
    def enterMoveCmd(self, ctx:SpacialTurtleParser.MoveCmdContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#moveCmd.
    def exitMoveCmd(self, ctx:SpacialTurtleParser.MoveCmdContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#turnCmd.
    def enterTurnCmd(self, ctx:SpacialTurtleParser.TurnCmdContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#turnCmd.
    def exitTurnCmd(self, ctx:SpacialTurtleParser.TurnCmdContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#penCmd.
    def enterPenCmd(self, ctx:SpacialTurtleParser.PenCmdContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#penCmd.
    def exitPenCmd(self, ctx:SpacialTurtleParser.PenCmdContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#faceBlock.
    def enterFaceBlock(self, ctx:SpacialTurtleParser.FaceBlockContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#faceBlock.
    def exitFaceBlock(self, ctx:SpacialTurtleParser.FaceBlockContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#exportCmd.
    def enterExportCmd(self, ctx:SpacialTurtleParser.ExportCmdContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#exportCmd.
    def exitExportCmd(self, ctx:SpacialTurtleParser.ExportCmdContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#declaration.
    def enterDeclaration(self, ctx:SpacialTurtleParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#declaration.
    def exitDeclaration(self, ctx:SpacialTurtleParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#varType.
    def enterVarType(self, ctx:SpacialTurtleParser.VarTypeContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#varType.
    def exitVarType(self, ctx:SpacialTurtleParser.VarTypeContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#assignStmt.
    def enterAssignStmt(self, ctx:SpacialTurtleParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#assignStmt.
    def exitAssignStmt(self, ctx:SpacialTurtleParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#exprStmt.
    def enterExprStmt(self, ctx:SpacialTurtleParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#exprStmt.
    def exitExprStmt(self, ctx:SpacialTurtleParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#block.
    def enterBlock(self, ctx:SpacialTurtleParser.BlockContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#block.
    def exitBlock(self, ctx:SpacialTurtleParser.BlockContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#ifStmt.
    def enterIfStmt(self, ctx:SpacialTurtleParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#ifStmt.
    def exitIfStmt(self, ctx:SpacialTurtleParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#whileStmt.
    def enterWhileStmt(self, ctx:SpacialTurtleParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#whileStmt.
    def exitWhileStmt(self, ctx:SpacialTurtleParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#forStmt.
    def enterForStmt(self, ctx:SpacialTurtleParser.ForStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#forStmt.
    def exitForStmt(self, ctx:SpacialTurtleParser.ForStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#funcDef.
    def enterFuncDef(self, ctx:SpacialTurtleParser.FuncDefContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#funcDef.
    def exitFuncDef(self, ctx:SpacialTurtleParser.FuncDefContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#returnStmt.
    def enterReturnStmt(self, ctx:SpacialTurtleParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#returnStmt.
    def exitReturnStmt(self, ctx:SpacialTurtleParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#paramList.
    def enterParamList(self, ctx:SpacialTurtleParser.ParamListContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#paramList.
    def exitParamList(self, ctx:SpacialTurtleParser.ParamListContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#variableRef.
    def enterVariableRef(self, ctx:SpacialTurtleParser.VariableRefContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#variableRef.
    def exitVariableRef(self, ctx:SpacialTurtleParser.VariableRefContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#printStmt.
    def enterPrintStmt(self, ctx:SpacialTurtleParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#printStmt.
    def exitPrintStmt(self, ctx:SpacialTurtleParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#expr.
    def enterExpr(self, ctx:SpacialTurtleParser.ExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#expr.
    def exitExpr(self, ctx:SpacialTurtleParser.ExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:SpacialTurtleParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:SpacialTurtleParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:SpacialTurtleParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:SpacialTurtleParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:SpacialTurtleParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:SpacialTurtleParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:SpacialTurtleParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:SpacialTurtleParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:SpacialTurtleParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:SpacialTurtleParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#unaryExpr.
    def enterUnaryExpr(self, ctx:SpacialTurtleParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#unaryExpr.
    def exitUnaryExpr(self, ctx:SpacialTurtleParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:SpacialTurtleParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:SpacialTurtleParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#funcCall.
    def enterFuncCall(self, ctx:SpacialTurtleParser.FuncCallContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#funcCall.
    def exitFuncCall(self, ctx:SpacialTurtleParser.FuncCallContext):
        pass



del SpacialTurtleParser