# Generated from SpacialTurtle.g4 by ANTLR 4.13.2
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
        4,1,17,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,57,
        8,6,10,6,12,6,60,9,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,9,10,1,0,14,15,71,0,
        23,1,0,0,0,2,31,1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,0,8,48,1,0,0,0,10,
        50,1,0,0,0,12,53,1,0,0,0,14,63,1,0,0,0,16,65,1,0,0,0,18,70,1,0,0,
        0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,
        32,3,4,2,0,29,32,3,16,8,0,30,32,3,12,6,0,31,28,1,0,0,0,31,29,1,0,
        0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,38,3,6,3,0,34,38,3,8,4,0,35,38,
        3,10,5,0,36,38,3,14,7,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,
        0,37,36,1,0,0,0,38,5,1,0,0,0,39,40,5,4,0,0,40,41,3,18,9,0,41,7,1,
        0,0,0,42,43,5,5,0,0,43,49,3,18,9,0,44,45,5,6,0,0,45,49,3,18,9,0,
        46,47,5,7,0,0,47,49,3,18,9,0,48,42,1,0,0,0,48,44,1,0,0,0,48,46,1,
        0,0,0,49,9,1,0,0,0,50,51,5,8,0,0,51,52,7,0,0,0,52,11,1,0,0,0,53,
        54,5,11,0,0,54,58,5,1,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,60,1,0,
        0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,
        5,2,0,0,62,13,1,0,0,0,63,64,5,12,0,0,64,15,1,0,0,0,65,66,5,13,0,
        0,66,67,5,14,0,0,67,68,5,3,0,0,68,69,3,18,9,0,69,17,1,0,0,0,70,71,
        7,1,0,0,71,19,1,0,0,0,5,23,31,37,48,58
    ]

class SpacialTurtleParser ( Parser ):

    grammarFileName = "SpacialTurtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "'move'", "'turnX'", 
                     "'turnY'", "'turnZ'", "'pen'", "'up'", "'down'", "'face'", 
                     "'export'", "'let'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MOVE", "TURNX", "TURNY", "TURNZ", "PEN", "UP", "DOWN", 
                      "FACE", "EXPORT", "LET", "ID", "NUMBER", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_command = 2
    RULE_moveCmd = 3
    RULE_turnCmd = 4
    RULE_penCmd = 5
    RULE_faceBlock = 6
    RULE_exportCmd = 7
    RULE_letInstr = 8
    RULE_value = 9

    ruleNames =  [ "program", "statement", "command", "moveCmd", "turnCmd", 
                   "penCmd", "faceBlock", "exportCmd", "letInstr", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    MOVE=4
    TURNX=5
    TURNY=6
    TURNZ=7
    PEN=8
    UP=9
    DOWN=10
    FACE=11
    EXPORT=12
    LET=13
    ID=14
    NUMBER=15
    COMMENT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SpacialTurtleParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.StatementContext,i)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SpacialTurtleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14832) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(SpacialTurtleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(SpacialTurtleParser.CommandContext,0)


        def letInstr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.LetInstrContext,0)


        def faceBlock(self):
            return self.getTypedRuleContext(SpacialTurtleParser.FaceBlockContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SpacialTurtleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.command()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.letInstr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.faceBlock()
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


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveCmd(self):
            return self.getTypedRuleContext(SpacialTurtleParser.MoveCmdContext,0)


        def turnCmd(self):
            return self.getTypedRuleContext(SpacialTurtleParser.TurnCmdContext,0)


        def penCmd(self):
            return self.getTypedRuleContext(SpacialTurtleParser.PenCmdContext,0)


        def exportCmd(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExportCmdContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = SpacialTurtleParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.moveCmd()
                pass
            elif token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.turnCmd()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.penCmd()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.exportCmd()
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


    class MoveCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(SpacialTurtleParser.MOVE, 0)

        def value(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ValueContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_moveCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveCmd" ):
                listener.enterMoveCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveCmd" ):
                listener.exitMoveCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCmd" ):
                return visitor.visitMoveCmd(self)
            else:
                return visitor.visitChildren(self)




    def moveCmd(self):

        localctx = SpacialTurtleParser.MoveCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_moveCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(SpacialTurtleParser.MOVE)
            self.state = 40
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TurnCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURNX(self):
            return self.getToken(SpacialTurtleParser.TURNX, 0)

        def value(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ValueContext,0)


        def TURNY(self):
            return self.getToken(SpacialTurtleParser.TURNY, 0)

        def TURNZ(self):
            return self.getToken(SpacialTurtleParser.TURNZ, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_turnCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurnCmd" ):
                listener.enterTurnCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurnCmd" ):
                listener.exitTurnCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTurnCmd" ):
                return visitor.visitTurnCmd(self)
            else:
                return visitor.visitChildren(self)




    def turnCmd(self):

        localctx = SpacialTurtleParser.TurnCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_turnCmd)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(SpacialTurtleParser.TURNX)
                self.state = 43
                self.value()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(SpacialTurtleParser.TURNY)
                self.state = 45
                self.value()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(SpacialTurtleParser.TURNZ)
                self.state = 47
                self.value()
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


    class PenCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PEN(self):
            return self.getToken(SpacialTurtleParser.PEN, 0)

        def UP(self):
            return self.getToken(SpacialTurtleParser.UP, 0)

        def DOWN(self):
            return self.getToken(SpacialTurtleParser.DOWN, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_penCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenCmd" ):
                listener.enterPenCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenCmd" ):
                listener.exitPenCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCmd" ):
                return visitor.visitPenCmd(self)
            else:
                return visitor.visitChildren(self)




    def penCmd(self):

        localctx = SpacialTurtleParser.PenCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_penCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SpacialTurtleParser.PEN)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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


    class FaceBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACE(self):
            return self.getToken(SpacialTurtleParser.FACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.StatementContext,i)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_faceBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaceBlock" ):
                listener.enterFaceBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaceBlock" ):
                listener.exitFaceBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFaceBlock" ):
                return visitor.visitFaceBlock(self)
            else:
                return visitor.visitChildren(self)




    def faceBlock(self):

        localctx = SpacialTurtleParser.FaceBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_faceBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(SpacialTurtleParser.FACE)
            self.state = 54
            self.match(SpacialTurtleParser.T__0)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14832) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(SpacialTurtleParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT(self):
            return self.getToken(SpacialTurtleParser.EXPORT, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_exportCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportCmd" ):
                listener.enterExportCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportCmd" ):
                listener.exitExportCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportCmd" ):
                return visitor.visitExportCmd(self)
            else:
                return visitor.visitChildren(self)




    def exportCmd(self):

        localctx = SpacialTurtleParser.ExportCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exportCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SpacialTurtleParser.EXPORT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(SpacialTurtleParser.LET, 0)

        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ValueContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_letInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetInstr" ):
                listener.enterLetInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetInstr" ):
                listener.exitLetInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetInstr" ):
                return visitor.visitLetInstr(self)
            else:
                return visitor.visitChildren(self)




    def letInstr(self):

        localctx = SpacialTurtleParser.LetInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_letInstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(SpacialTurtleParser.LET)
            self.state = 66
            self.match(SpacialTurtleParser.ID)
            self.state = 67
            self.match(SpacialTurtleParser.T__2)
            self.state = 68
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SpacialTurtleParser.NUMBER, 0)

        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = SpacialTurtleParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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





