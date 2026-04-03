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


    # Visit a parse tree produced by SpacialTurtleParser#letInstr.
    def visitLetInstr(self, ctx:SpacialTurtleParser.LetInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpacialTurtleParser#value.
    def visitValue(self, ctx:SpacialTurtleParser.ValueContext):
        return self.visitChildren(ctx)



del SpacialTurtleParser