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


    # Enter a parse tree produced by SpacialTurtleParser#letInstr.
    def enterLetInstr(self, ctx:SpacialTurtleParser.LetInstrContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#letInstr.
    def exitLetInstr(self, ctx:SpacialTurtleParser.LetInstrContext):
        pass


    # Enter a parse tree produced by SpacialTurtleParser#value.
    def enterValue(self, ctx:SpacialTurtleParser.ValueContext):
        pass

    # Exit a parse tree produced by SpacialTurtleParser#value.
    def exitValue(self, ctx:SpacialTurtleParser.ValueContext):
        pass



del SpacialTurtleParser