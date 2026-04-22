# Generated from SpacialTurtle.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from typing import Dict, Any, List

def serializedATN():
    return [
        4,1,50,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,3,3,97,
        8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,114,8,5,1,6,1,6,1,6,1,7,1,7,1,7,5,7,122,8,7,10,7,12,7,125,9,
        7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,10,1,11,1,11,
        1,11,1,11,1,12,1,12,1,13,1,13,5,13,147,8,13,10,13,12,13,150,9,13,
        1,13,1,13,3,13,154,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        163,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,
        175,8,16,1,16,1,16,3,16,179,8,16,1,16,1,16,3,16,183,8,16,1,16,1,
        16,1,16,1,17,1,17,1,17,1,17,3,17,192,8,17,1,17,1,17,1,17,5,17,197,
        8,17,10,17,12,17,200,9,17,1,17,1,17,1,18,1,18,3,18,206,8,18,1,19,
        1,19,1,19,5,19,211,8,19,10,19,12,19,214,9,19,1,20,1,20,1,20,1,20,
        3,20,220,8,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,5,23,230,8,
        23,10,23,12,23,233,9,23,1,24,1,24,1,24,3,24,238,8,24,1,25,1,25,1,
        25,5,25,243,8,25,10,25,12,25,246,9,25,1,26,1,26,1,26,5,26,251,8,
        26,10,26,12,26,254,9,26,1,27,1,27,1,27,3,27,259,8,27,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,275,
        8,28,1,29,1,29,1,29,1,29,1,29,5,29,282,8,29,10,29,12,29,285,9,29,
        3,29,287,8,29,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,7,1,0,
        14,15,1,0,20,22,1,0,31,32,1,0,34,39,1,0,40,41,1,0,42,43,2,0,33,33,
        40,41,314,0,63,1,0,0,0,2,79,1,0,0,0,4,90,1,0,0,0,6,96,1,0,0,0,8,
        98,1,0,0,0,10,113,1,0,0,0,12,115,1,0,0,0,14,118,1,0,0,0,16,128,1,
        0,0,0,18,130,1,0,0,0,20,136,1,0,0,0,22,138,1,0,0,0,24,142,1,0,0,
        0,26,153,1,0,0,0,28,155,1,0,0,0,30,164,1,0,0,0,32,170,1,0,0,0,34,
        187,1,0,0,0,36,203,1,0,0,0,38,207,1,0,0,0,40,219,1,0,0,0,42,221,
        1,0,0,0,44,224,1,0,0,0,46,226,1,0,0,0,48,234,1,0,0,0,50,239,1,0,
        0,0,52,247,1,0,0,0,54,258,1,0,0,0,56,274,1,0,0,0,58,276,1,0,0,0,
        60,62,3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,
        0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,
        80,3,6,3,0,69,80,3,18,9,0,70,80,3,22,11,0,71,80,3,14,7,0,72,80,3,
        28,14,0,73,80,3,30,15,0,74,80,3,32,16,0,75,80,3,34,17,0,76,80,3,
        36,18,0,77,80,3,42,21,0,78,80,3,24,12,0,79,68,1,0,0,0,79,69,1,0,
        0,0,79,70,1,0,0,0,79,71,1,0,0,0,79,72,1,0,0,0,79,73,1,0,0,0,79,74,
        1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,
        80,3,1,0,0,0,81,91,3,6,3,0,82,91,3,18,9,0,83,91,3,22,11,0,84,91,
        3,28,14,0,85,91,3,30,15,0,86,91,3,32,16,0,87,91,3,36,18,0,88,91,
        3,42,21,0,89,91,3,24,12,0,90,81,1,0,0,0,90,82,1,0,0,0,90,83,1,0,
        0,0,90,84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,1,0,0,0,90,88,
        1,0,0,0,90,89,1,0,0,0,91,5,1,0,0,0,92,97,3,8,4,0,93,97,3,10,5,0,
        94,97,3,12,6,0,95,97,3,16,8,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,
        1,0,0,0,96,95,1,0,0,0,97,7,1,0,0,0,98,99,5,6,0,0,99,100,3,44,22,
        0,100,9,1,0,0,0,101,102,5,7,0,0,102,114,3,44,22,0,103,104,5,8,0,
        0,104,114,3,44,22,0,105,106,5,9,0,0,106,114,3,44,22,0,107,108,5,
        10,0,0,108,114,3,44,22,0,109,110,5,11,0,0,110,114,3,44,22,0,111,
        112,5,12,0,0,112,114,3,44,22,0,113,101,1,0,0,0,113,103,1,0,0,0,113,
        105,1,0,0,0,113,107,1,0,0,0,113,109,1,0,0,0,113,111,1,0,0,0,114,
        11,1,0,0,0,115,116,5,13,0,0,116,117,7,0,0,0,117,13,1,0,0,0,118,119,
        5,16,0,0,119,123,5,1,0,0,120,122,3,4,2,0,121,120,1,0,0,0,122,125,
        1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,
        1,0,0,0,126,127,5,2,0,0,127,15,1,0,0,0,128,129,5,17,0,0,129,17,1,
        0,0,0,130,131,3,20,10,0,131,134,5,47,0,0,132,133,5,3,0,0,133,135,
        3,44,22,0,134,132,1,0,0,0,134,135,1,0,0,0,135,19,1,0,0,0,136,137,
        7,1,0,0,137,21,1,0,0,0,138,139,3,40,20,0,139,140,5,3,0,0,140,141,
        3,44,22,0,141,23,1,0,0,0,142,143,3,44,22,0,143,25,1,0,0,0,144,148,
        5,1,0,0,145,147,3,2,1,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,154,
        5,2,0,0,152,154,3,2,1,0,153,144,1,0,0,0,153,152,1,0,0,0,154,27,1,
        0,0,0,155,156,5,23,0,0,156,157,5,44,0,0,157,158,3,44,22,0,158,159,
        5,45,0,0,159,162,3,26,13,0,160,161,5,24,0,0,161,163,3,26,13,0,162,
        160,1,0,0,0,162,163,1,0,0,0,163,29,1,0,0,0,164,165,5,25,0,0,165,
        166,5,44,0,0,166,167,3,44,22,0,167,168,5,45,0,0,168,169,3,26,13,
        0,169,31,1,0,0,0,170,171,5,26,0,0,171,174,5,44,0,0,172,175,3,18,
        9,0,173,175,3,22,11,0,174,172,1,0,0,0,174,173,1,0,0,0,174,175,1,
        0,0,0,175,176,1,0,0,0,176,178,5,4,0,0,177,179,3,44,22,0,178,177,
        1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,5,4,0,0,181,183,
        3,22,11,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,185,
        5,45,0,0,185,186,3,26,13,0,186,33,1,0,0,0,187,188,5,27,0,0,188,189,
        5,47,0,0,189,191,5,44,0,0,190,192,3,38,19,0,191,190,1,0,0,0,191,
        192,1,0,0,0,192,193,1,0,0,0,193,194,5,45,0,0,194,198,5,1,0,0,195,
        197,3,2,1,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,
        199,1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,5,2,0,0,202,
        35,1,0,0,0,203,205,5,28,0,0,204,206,3,44,22,0,205,204,1,0,0,0,205,
        206,1,0,0,0,206,37,1,0,0,0,207,212,5,47,0,0,208,209,5,46,0,0,209,
        211,5,47,0,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,
        213,1,0,0,0,213,39,1,0,0,0,214,212,1,0,0,0,215,216,5,19,0,0,216,
        217,5,5,0,0,217,220,3,40,20,0,218,220,5,47,0,0,219,215,1,0,0,0,219,
        218,1,0,0,0,220,41,1,0,0,0,221,222,5,18,0,0,222,223,3,44,22,0,223,
        43,1,0,0,0,224,225,3,46,23,0,225,45,1,0,0,0,226,231,3,48,24,0,227,
        228,7,2,0,0,228,230,3,48,24,0,229,227,1,0,0,0,230,233,1,0,0,0,231,
        229,1,0,0,0,231,232,1,0,0,0,232,47,1,0,0,0,233,231,1,0,0,0,234,237,
        3,50,25,0,235,236,7,3,0,0,236,238,3,50,25,0,237,235,1,0,0,0,237,
        238,1,0,0,0,238,49,1,0,0,0,239,244,3,52,26,0,240,241,7,4,0,0,241,
        243,3,52,26,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
        245,1,0,0,0,245,51,1,0,0,0,246,244,1,0,0,0,247,252,3,54,27,0,248,
        249,7,5,0,0,249,251,3,54,27,0,250,248,1,0,0,0,251,254,1,0,0,0,252,
        250,1,0,0,0,252,253,1,0,0,0,253,53,1,0,0,0,254,252,1,0,0,0,255,256,
        7,6,0,0,256,259,3,54,27,0,257,259,3,56,28,0,258,255,1,0,0,0,258,
        257,1,0,0,0,259,55,1,0,0,0,260,275,5,48,0,0,261,275,3,40,20,0,262,
        275,5,29,0,0,263,275,5,30,0,0,264,265,5,44,0,0,265,266,3,44,22,0,
        266,267,5,45,0,0,267,275,1,0,0,0,268,275,3,58,29,0,269,270,3,20,
        10,0,270,271,5,44,0,0,271,272,3,44,22,0,272,273,5,45,0,0,273,275,
        1,0,0,0,274,260,1,0,0,0,274,261,1,0,0,0,274,262,1,0,0,0,274,263,
        1,0,0,0,274,264,1,0,0,0,274,268,1,0,0,0,274,269,1,0,0,0,275,57,1,
        0,0,0,276,277,5,47,0,0,277,286,5,44,0,0,278,283,3,44,22,0,279,280,
        5,46,0,0,280,282,3,44,22,0,281,279,1,0,0,0,282,285,1,0,0,0,283,281,
        1,0,0,0,283,284,1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,286,278,
        1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,5,45,0,0,289,59,
        1,0,0,0,26,63,79,90,96,113,123,134,148,153,162,174,178,182,191,198,
        205,212,219,231,237,244,252,258,274,283,286
    ]

class SpacialTurtleParser ( Parser ):

    grammarFileName = "SpacialTurtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "';'", "'::'", "'move'", 
                     "'turnX'", "'turnY'", "'turnZ'", "'gturnX'", "'gturnY'", 
                     "'gturnZ'", "'pen'", "'up'", "'down'", "'face'", "'export'", 
                     "'print'", "'parent'", "'int'", "'float'", "'bool'", 
                     "'if'", "'else'", "'while'", "'for'", "'func'", "'return'", 
                     "'true'", "'false'", "'and'", "'or'", "'not'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MOVE", "TURNX", "TURNY", 
                      "TURNZ", "GTURNX", "GTURNY", "GTURNZ", "PEN", "UP", 
                      "DOWN", "FACE", "EXPORT", "PRINT", "PARENT", "INT_K", 
                      "FLOAT_K", "BOOL_K", "IF", "ELSE", "WHILE", "FOR", 
                      "FUNC", "RETURN", "TRUE", "FALSE", "AND", "OR", "NOT", 
                      "EQ", "NEQ", "LT", "GT", "LE", "GE", "PLUS", "MINUS", 
                      "MUL", "DIV", "LPAREN", "RPAREN", "COMMA", "ID", "NUMBER", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_faceStatement = 2
    RULE_command = 3
    RULE_moveCmd = 4
    RULE_turnCmd = 5
    RULE_penCmd = 6
    RULE_faceBlock = 7
    RULE_exportCmd = 8
    RULE_declaration = 9
    RULE_varType = 10
    RULE_assignStmt = 11
    RULE_exprStmt = 12
    RULE_block = 13
    RULE_ifStmt = 14
    RULE_whileStmt = 15
    RULE_forStmt = 16
    RULE_funcDef = 17
    RULE_returnStmt = 18
    RULE_paramList = 19
    RULE_variableRef = 20
    RULE_printStmt = 21
    RULE_expr = 22
    RULE_logicalExpr = 23
    RULE_comparisonExpr = 24
    RULE_additiveExpr = 25
    RULE_multiplicativeExpr = 26
    RULE_unaryExpr = 27
    RULE_primaryExpr = 28
    RULE_funcCall = 29

    ruleNames =  [ "program", "statement", "faceStatement", "command", "moveCmd", 
                   "turnCmd", "penCmd", "faceBlock", "exportCmd", "declaration", 
                   "varType", "assignStmt", "exprStmt", "block", "ifStmt", 
                   "whileStmt", "forStmt", "funcDef", "returnStmt", "paramList", 
                   "variableRef", "printStmt", "expr", "logicalExpr", "comparisonExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "primaryExpr", 
                   "funcCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    MOVE=6
    TURNX=7
    TURNY=8
    TURNZ=9
    GTURNX=10
    GTURNY=11
    GTURNZ=12
    PEN=13
    UP=14
    DOWN=15
    FACE=16
    EXPORT=17
    PRINT=18
    PARENT=19
    INT_K=20
    FLOAT_K=21
    BOOL_K=22
    IF=23
    ELSE=24
    WHILE=25
    FOR=26
    FUNC=27
    RETURN=28
    TRUE=29
    FALSE=30
    AND=31
    OR=32
    NOT=33
    EQ=34
    NEQ=35
    LT=36
    GT=37
    LE=38
    GE=39
    PLUS=40
    MINUS=41
    MUL=42
    DIV=43
    LPAREN=44
    RPAREN=45
    COMMA=46
    ID=47
    NUMBER=48
    COMMENT=49
    WS=50

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113906585536) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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


        def declaration(self):
            return self.getTypedRuleContext(SpacialTurtleParser.DeclarationContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.AssignStmtContext,0)


        def faceBlock(self):
            return self.getTypedRuleContext(SpacialTurtleParser.FaceBlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ForStmtContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(SpacialTurtleParser.FuncDefContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.PrintStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprStmtContext,0)


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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.faceBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.funcDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.returnStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.printStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.exprStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FaceStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(SpacialTurtleParser.CommandContext,0)


        def declaration(self):
            return self.getTypedRuleContext(SpacialTurtleParser.DeclarationContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ForStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.PrintStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_faceStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFaceStatement" ):
                listener.enterFaceStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFaceStatement" ):
                listener.exitFaceStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFaceStatement" ):
                return visitor.visitFaceStatement(self)
            else:
                return visitor.visitChildren(self)




    def faceStatement(self):

        localctx = SpacialTurtleParser.FaceStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_faceStatement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 87
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 88
                self.printStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.exprStmt()
                pass


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
        self.enterRule(localctx, 6, self.RULE_command)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.moveCmd()
                pass
            elif token in [7, 8, 9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.turnCmd()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.penCmd()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
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

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


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
        self.enterRule(localctx, 8, self.RULE_moveCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SpacialTurtleParser.MOVE)
            self.state = 99
            self.expr()
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

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def TURNY(self):
            return self.getToken(SpacialTurtleParser.TURNY, 0)

        def TURNZ(self):
            return self.getToken(SpacialTurtleParser.TURNZ, 0)

        def GTURNX(self):
            return self.getToken(SpacialTurtleParser.GTURNX, 0)

        def GTURNY(self):
            return self.getToken(SpacialTurtleParser.GTURNY, 0)

        def GTURNZ(self):
            return self.getToken(SpacialTurtleParser.GTURNZ, 0)

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
        self.enterRule(localctx, 10, self.RULE_turnCmd)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(SpacialTurtleParser.TURNX)
                self.state = 102
                self.expr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(SpacialTurtleParser.TURNY)
                self.state = 104
                self.expr()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(SpacialTurtleParser.TURNZ)
                self.state = 106
                self.expr()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(SpacialTurtleParser.GTURNX)
                self.state = 108
                self.expr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.match(SpacialTurtleParser.GTURNY)
                self.state = 110
                self.expr()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 111
                self.match(SpacialTurtleParser.GTURNZ)
                self.state = 112
                self.expr()
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
        self.enterRule(localctx, 12, self.RULE_penCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(SpacialTurtleParser.PEN)
            self.state = 116
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


    class FaceBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACE(self):
            return self.getToken(SpacialTurtleParser.FACE, 0)

        def faceStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.FaceStatementContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.FaceStatementContext,i)


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
        self.enterRule(localctx, 14, self.RULE_faceBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SpacialTurtleParser.FACE)
            self.state = 119
            self.match(SpacialTurtleParser.T__0)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113772302272) != 0):
                self.state = 120
                self.faceStatement()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
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
        self.enterRule(localctx, 16, self.RULE_exportCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(SpacialTurtleParser.EXPORT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VarTypeContext,0)


        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = SpacialTurtleParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.varType()
            self.state = 131
            self.match(SpacialTurtleParser.ID)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 132
                self.match(SpacialTurtleParser.T__2)
                self.state = 133
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_K(self):
            return self.getToken(SpacialTurtleParser.INT_K, 0)

        def FLOAT_K(self):
            return self.getToken(SpacialTurtleParser.FLOAT_K, 0)

        def BOOL_K(self):
            return self.getToken(SpacialTurtleParser.BOOL_K, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_varType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarType" ):
                listener.enterVarType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarType" ):
                listener.exitVarType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = SpacialTurtleParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
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


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableRef(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VariableRefContext,0)


        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_assignStmt

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




    def assignStmt(self):

        localctx = SpacialTurtleParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.variableRef()
            self.state = 139
            self.match(SpacialTurtleParser.T__2)
            self.state = 140
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = SpacialTurtleParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.StatementContext,i)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SpacialTurtleParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(SpacialTurtleParser.T__0)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113906585536) != 0):
                    self.state = 145
                    self.statement()
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 151
                self.match(SpacialTurtleParser.T__1)
                pass
            elif token in [6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 33, 40, 41, 44, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.statement()
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


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SpacialTurtleParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.BlockContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(SpacialTurtleParser.ELSE, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_ifStmt

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




    def ifStmt(self):

        localctx = SpacialTurtleParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SpacialTurtleParser.IF)
            self.state = 156
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 157
            self.expr()
            self.state = 158
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 159
            self.block()
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(SpacialTurtleParser.ELSE)
                self.state = 161
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SpacialTurtleParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SpacialTurtleParser.BlockContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_whileStmt

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




    def whileStmt(self):

        localctx = SpacialTurtleParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(SpacialTurtleParser.WHILE)
            self.state = 165
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 166
            self.expr()
            self.state = 167
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 168
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SpacialTurtleParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SpacialTurtleParser.BlockContext,0)


        def declaration(self):
            return self.getTypedRuleContext(SpacialTurtleParser.DeclarationContext,0)


        def assignStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.AssignStmtContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.AssignStmtContext,i)


        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = SpacialTurtleParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SpacialTurtleParser.FOR)
            self.state = 171
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22]:
                self.state = 172
                self.declaration()
                pass
            elif token in [19, 47]:
                self.state = 173
                self.assignStmt()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 176
            self.match(SpacialTurtleParser.T__3)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113394405376) != 0):
                self.state = 177
                self.expr()


            self.state = 180
            self.match(SpacialTurtleParser.T__3)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19 or _la==47:
                self.state = 181
                self.assignStmt()


            self.state = 184
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 185
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(SpacialTurtleParser.FUNC, 0)

        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.StatementContext,i)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = SpacialTurtleParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(SpacialTurtleParser.FUNC)
            self.state = 188
            self.match(SpacialTurtleParser.ID)
            self.state = 189
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 190
                self.paramList()


            self.state = 193
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 194
            self.match(SpacialTurtleParser.T__0)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113906585536) != 0):
                self.state = 195
                self.statement()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(SpacialTurtleParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SpacialTurtleParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_returnStmt

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




    def returnStmt(self):

        localctx = SpacialTurtleParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(SpacialTurtleParser.RETURN)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 204
                self.expr()


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
                return self.getTokens(SpacialTurtleParser.ID)
            else:
                return self.getToken(SpacialTurtleParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.COMMA)
            else:
                return self.getToken(SpacialTurtleParser.COMMA, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_paramList

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

        localctx = SpacialTurtleParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(SpacialTurtleParser.ID)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 208
                self.match(SpacialTurtleParser.COMMA)
                self.state = 209
                self.match(SpacialTurtleParser.ID)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENT(self):
            return self.getToken(SpacialTurtleParser.PARENT, 0)

        def variableRef(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VariableRefContext,0)


        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_variableRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableRef" ):
                listener.enterVariableRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableRef" ):
                listener.exitVariableRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableRef" ):
                return visitor.visitVariableRef(self)
            else:
                return visitor.visitChildren(self)




    def variableRef(self):

        localctx = SpacialTurtleParser.VariableRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variableRef)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(SpacialTurtleParser.PARENT)
                self.state = 216
                self.match(SpacialTurtleParser.T__4)
                self.state = 217
                self.variableRef()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(SpacialTurtleParser.ID)
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


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(SpacialTurtleParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_printStmt

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




    def printStmt(self):

        localctx = SpacialTurtleParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(SpacialTurtleParser.PRINT)
            self.state = 222
            self.expr()
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

        def logicalExpr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.LogicalExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SpacialTurtleParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.logicalExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.ComparisonExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.ComparisonExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.AND)
            else:
                return self.getToken(SpacialTurtleParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.OR)
            else:
                return self.getToken(SpacialTurtleParser.OR, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_logicalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalExpr(self):

        localctx = SpacialTurtleParser.LogicalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logicalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.comparisonExpr()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.comparisonExpr()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.AdditiveExprContext,i)


        def EQ(self):
            return self.getToken(SpacialTurtleParser.EQ, 0)

        def NEQ(self):
            return self.getToken(SpacialTurtleParser.NEQ, 0)

        def LT(self):
            return self.getToken(SpacialTurtleParser.LT, 0)

        def GT(self):
            return self.getToken(SpacialTurtleParser.GT, 0)

        def LE(self):
            return self.getToken(SpacialTurtleParser.LE, 0)

        def GE(self):
            return self.getToken(SpacialTurtleParser.GE, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_comparisonExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpr(self):

        localctx = SpacialTurtleParser.ComparisonExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.additiveExpr()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0):
                self.state = 235
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 236
                self.additiveExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.PLUS)
            else:
                return self.getToken(SpacialTurtleParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.MINUS)
            else:
                return self.getToken(SpacialTurtleParser.MINUS, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = SpacialTurtleParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.multiplicativeExpr()
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 240
                    _la = self._input.LA(1)
                    if not(_la==40 or _la==41):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.multiplicativeExpr() 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.MUL)
            else:
                return self.getToken(SpacialTurtleParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.DIV)
            else:
                return self.getToken(SpacialTurtleParser.DIV, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = SpacialTurtleParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.unaryExpr()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42 or _la==43:
                self.state = 248
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.unaryExpr()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.UnaryExprContext,0)


        def PLUS(self):
            return self.getToken(SpacialTurtleParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SpacialTurtleParser.MINUS, 0)

        def NOT(self):
            return self.getToken(SpacialTurtleParser.NOT, 0)

        def primaryExpr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = SpacialTurtleParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3307124817920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.unaryExpr()
                pass
            elif token in [19, 20, 21, 22, 29, 30, 44, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.primaryExpr()
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SpacialTurtleParser.NUMBER, 0)

        def variableRef(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VariableRefContext,0)


        def TRUE(self):
            return self.getToken(SpacialTurtleParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SpacialTurtleParser.FALSE, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def funcCall(self):
            return self.getTypedRuleContext(SpacialTurtleParser.FuncCallContext,0)


        def varType(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VarTypeContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = SpacialTurtleParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primaryExpr)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(SpacialTurtleParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.variableRef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.match(SpacialTurtleParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.match(SpacialTurtleParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 265
                self.expr()
                self.state = 266
                self.match(SpacialTurtleParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.funcCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.varType()
                self.state = 270
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 271
                self.expr()
                self.state = 272
                self.match(SpacialTurtleParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SpacialTurtleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SpacialTurtleParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.ExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.COMMA)
            else:
                return self.getToken(SpacialTurtleParser.COMMA, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = SpacialTurtleParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(SpacialTurtleParser.ID)
            self.state = 277
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 443113394405376) != 0):
                self.state = 278
                self.expr()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==46:
                    self.state = 279
                    self.match(SpacialTurtleParser.COMMA)
                    self.state = 280
                    self.expr()
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 288
            self.match(SpacialTurtleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





