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
        4,1,52,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,82,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,3,1,3,1,
        3,3,3,99,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,116,8,5,1,6,1,6,1,6,1,7,1,7,1,7,5,7,124,8,7,10,7,12,
        7,127,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,137,8,9,1,10,1,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,5,13,149,8,13,10,13,12,13,
        152,9,13,1,13,1,13,3,13,156,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,3,14,165,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,
        16,3,16,177,8,16,1,16,1,16,3,16,181,8,16,1,16,1,16,3,16,185,8,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,194,8,17,1,17,1,17,1,17,
        5,17,199,8,17,10,17,12,17,202,9,17,1,17,1,17,1,18,1,18,3,18,208,
        8,18,1,19,1,19,1,19,5,19,213,8,19,10,19,12,19,216,9,19,1,20,1,20,
        1,20,1,20,3,20,222,8,20,1,21,1,21,1,21,1,21,1,21,5,21,229,8,21,10,
        21,12,21,232,9,21,3,21,234,8,21,1,21,1,21,1,22,1,22,1,23,1,23,1,
        23,5,23,243,8,23,10,23,12,23,246,9,23,1,24,1,24,1,24,5,24,251,8,
        24,10,24,12,24,254,9,24,1,25,1,25,1,25,3,25,259,8,25,1,26,1,26,1,
        26,5,26,264,8,26,10,26,12,26,267,9,26,1,27,1,27,1,27,5,27,272,8,
        27,10,27,12,27,275,9,27,1,28,1,28,1,28,3,28,280,8,28,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,
        29,297,8,29,1,30,1,30,1,30,1,30,1,30,5,30,304,8,30,10,30,12,30,307,
        9,30,3,30,309,8,30,1,30,1,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,
        6,1,0,14,15,1,0,20,23,1,0,35,40,1,0,41,42,1,0,43,44,2,0,34,34,41,
        42,339,0,65,1,0,0,0,2,81,1,0,0,0,4,92,1,0,0,0,6,98,1,0,0,0,8,100,
        1,0,0,0,10,115,1,0,0,0,12,117,1,0,0,0,14,120,1,0,0,0,16,130,1,0,
        0,0,18,132,1,0,0,0,20,138,1,0,0,0,22,140,1,0,0,0,24,144,1,0,0,0,
        26,155,1,0,0,0,28,157,1,0,0,0,30,166,1,0,0,0,32,172,1,0,0,0,34,189,
        1,0,0,0,36,205,1,0,0,0,38,209,1,0,0,0,40,221,1,0,0,0,42,223,1,0,
        0,0,44,237,1,0,0,0,46,239,1,0,0,0,48,247,1,0,0,0,50,255,1,0,0,0,
        52,260,1,0,0,0,54,268,1,0,0,0,56,279,1,0,0,0,58,296,1,0,0,0,60,298,
        1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,
        0,0,70,82,3,6,3,0,71,82,3,18,9,0,72,82,3,22,11,0,73,82,3,14,7,0,
        74,82,3,28,14,0,75,82,3,30,15,0,76,82,3,32,16,0,77,82,3,34,17,0,
        78,82,3,36,18,0,79,82,3,42,21,0,80,82,3,24,12,0,81,70,1,0,0,0,81,
        71,1,0,0,0,81,72,1,0,0,0,81,73,1,0,0,0,81,74,1,0,0,0,81,75,1,0,0,
        0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,
        1,0,0,0,82,3,1,0,0,0,83,93,3,6,3,0,84,93,3,18,9,0,85,93,3,22,11,
        0,86,93,3,28,14,0,87,93,3,30,15,0,88,93,3,32,16,0,89,93,3,36,18,
        0,90,93,3,42,21,0,91,93,3,24,12,0,92,83,1,0,0,0,92,84,1,0,0,0,92,
        85,1,0,0,0,92,86,1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,
        0,92,90,1,0,0,0,92,91,1,0,0,0,93,5,1,0,0,0,94,99,3,8,4,0,95,99,3,
        10,5,0,96,99,3,12,6,0,97,99,3,16,8,0,98,94,1,0,0,0,98,95,1,0,0,0,
        98,96,1,0,0,0,98,97,1,0,0,0,99,7,1,0,0,0,100,101,5,6,0,0,101,102,
        3,44,22,0,102,9,1,0,0,0,103,104,5,7,0,0,104,116,3,44,22,0,105,106,
        5,8,0,0,106,116,3,44,22,0,107,108,5,9,0,0,108,116,3,44,22,0,109,
        110,5,10,0,0,110,116,3,44,22,0,111,112,5,11,0,0,112,116,3,44,22,
        0,113,114,5,12,0,0,114,116,3,44,22,0,115,103,1,0,0,0,115,105,1,0,
        0,0,115,107,1,0,0,0,115,109,1,0,0,0,115,111,1,0,0,0,115,113,1,0,
        0,0,116,11,1,0,0,0,117,118,5,13,0,0,118,119,7,0,0,0,119,13,1,0,0,
        0,120,121,5,16,0,0,121,125,5,1,0,0,122,124,3,4,2,0,123,122,1,0,0,
        0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,
        0,127,125,1,0,0,0,128,129,5,2,0,0,129,15,1,0,0,0,130,131,5,17,0,
        0,131,17,1,0,0,0,132,133,3,20,10,0,133,136,5,48,0,0,134,135,5,3,
        0,0,135,137,3,44,22,0,136,134,1,0,0,0,136,137,1,0,0,0,137,19,1,0,
        0,0,138,139,7,1,0,0,139,21,1,0,0,0,140,141,3,40,20,0,141,142,5,3,
        0,0,142,143,3,44,22,0,143,23,1,0,0,0,144,145,3,44,22,0,145,25,1,
        0,0,0,146,150,5,1,0,0,147,149,3,2,1,0,148,147,1,0,0,0,149,152,1,
        0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,
        0,0,0,153,156,5,2,0,0,154,156,3,2,1,0,155,146,1,0,0,0,155,154,1,
        0,0,0,156,27,1,0,0,0,157,158,5,24,0,0,158,159,5,45,0,0,159,160,3,
        44,22,0,160,161,5,46,0,0,161,164,3,26,13,0,162,163,5,25,0,0,163,
        165,3,26,13,0,164,162,1,0,0,0,164,165,1,0,0,0,165,29,1,0,0,0,166,
        167,5,26,0,0,167,168,5,45,0,0,168,169,3,44,22,0,169,170,5,46,0,0,
        170,171,3,26,13,0,171,31,1,0,0,0,172,173,5,27,0,0,173,176,5,45,0,
        0,174,177,3,18,9,0,175,177,3,22,11,0,176,174,1,0,0,0,176,175,1,0,
        0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,180,5,4,0,0,179,181,3,44,
        22,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,184,5,4,
        0,0,183,185,3,22,11,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,
        0,0,0,186,187,5,46,0,0,187,188,3,26,13,0,188,33,1,0,0,0,189,190,
        5,28,0,0,190,191,5,48,0,0,191,193,5,45,0,0,192,194,3,38,19,0,193,
        192,1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,196,5,46,0,0,196,
        200,5,1,0,0,197,199,3,2,1,0,198,197,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,1,0,0,0,203,
        204,5,2,0,0,204,35,1,0,0,0,205,207,5,29,0,0,206,208,3,44,22,0,207,
        206,1,0,0,0,207,208,1,0,0,0,208,37,1,0,0,0,209,214,5,48,0,0,210,
        211,5,47,0,0,211,213,5,48,0,0,212,210,1,0,0,0,213,216,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,39,1,0,0,0,216,214,1,0,0,0,217,218,
        5,19,0,0,218,219,5,5,0,0,219,222,3,40,20,0,220,222,5,48,0,0,221,
        217,1,0,0,0,221,220,1,0,0,0,222,41,1,0,0,0,223,224,5,18,0,0,224,
        233,5,45,0,0,225,230,3,44,22,0,226,227,5,47,0,0,227,229,3,44,22,
        0,228,226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,
        0,231,234,1,0,0,0,232,230,1,0,0,0,233,225,1,0,0,0,233,234,1,0,0,
        0,234,235,1,0,0,0,235,236,5,46,0,0,236,43,1,0,0,0,237,238,3,46,23,
        0,238,45,1,0,0,0,239,244,3,48,24,0,240,241,5,33,0,0,241,243,3,48,
        24,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,
        0,0,245,47,1,0,0,0,246,244,1,0,0,0,247,252,3,50,25,0,248,249,5,32,
        0,0,249,251,3,50,25,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,1,
        0,0,0,252,253,1,0,0,0,253,49,1,0,0,0,254,252,1,0,0,0,255,258,3,52,
        26,0,256,257,7,2,0,0,257,259,3,52,26,0,258,256,1,0,0,0,258,259,1,
        0,0,0,259,51,1,0,0,0,260,265,3,54,27,0,261,262,7,3,0,0,262,264,3,
        54,27,0,263,261,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,53,1,0,0,0,267,265,1,0,0,0,268,273,3,56,28,0,269,270,
        7,4,0,0,270,272,3,56,28,0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,55,1,0,0,0,275,273,1,0,0,0,276,277,7,
        5,0,0,277,280,3,56,28,0,278,280,3,58,29,0,279,276,1,0,0,0,279,278,
        1,0,0,0,280,57,1,0,0,0,281,297,5,49,0,0,282,297,3,40,20,0,283,297,
        5,30,0,0,284,297,5,31,0,0,285,297,5,52,0,0,286,287,5,45,0,0,287,
        288,3,44,22,0,288,289,5,46,0,0,289,297,1,0,0,0,290,297,3,60,30,0,
        291,292,3,20,10,0,292,293,5,45,0,0,293,294,3,44,22,0,294,295,5,46,
        0,0,295,297,1,0,0,0,296,281,1,0,0,0,296,282,1,0,0,0,296,283,1,0,
        0,0,296,284,1,0,0,0,296,285,1,0,0,0,296,286,1,0,0,0,296,290,1,0,
        0,0,296,291,1,0,0,0,297,59,1,0,0,0,298,299,5,48,0,0,299,308,5,45,
        0,0,300,305,3,44,22,0,301,302,5,47,0,0,302,304,3,44,22,0,303,301,
        1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,309,
        1,0,0,0,307,305,1,0,0,0,308,300,1,0,0,0,308,309,1,0,0,0,309,310,
        1,0,0,0,310,311,5,46,0,0,311,61,1,0,0,0,29,65,81,92,98,115,125,136,
        150,155,164,176,180,184,193,200,207,214,221,230,233,244,252,258,
        265,273,279,296,305,308
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
                     "'string'", "'if'", "'else'", "'while'", "'for'", "'func'", 
                     "'return'", "'true'", "'false'", "'and'", "'or'", "'not'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MOVE", "TURNX", "TURNY", 
                      "TURNZ", "GTURNX", "GTURNY", "GTURNZ", "PEN", "UP", 
                      "DOWN", "FACE", "EXPORT", "PRINT", "PARENT", "INT_K", 
                      "FLOAT_K", "BOOL_K", "STRING_K", "IF", "ELSE", "WHILE", 
                      "FOR", "FUNC", "RETURN", "TRUE", "FALSE", "AND", "OR", 
                      "NOT", "EQ", "NEQ", "LT", "GT", "LE", "GE", "PLUS", 
                      "MINUS", "MUL", "DIV", "LPAREN", "RPAREN", "COMMA", 
                      "ID", "NUMBER", "COMMENT", "WS", "STRING" ]

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
    RULE_logicalOrExpr = 23
    RULE_logicalAndExpr = 24
    RULE_comparisonExpr = 25
    RULE_additiveExpr = 26
    RULE_multiplicativeExpr = 27
    RULE_unaryExpr = 28
    RULE_primaryExpr = 29
    RULE_funcCall = 30

    ruleNames =  [ "program", "statement", "faceStatement", "command", "moveCmd", 
                   "turnCmd", "penCmd", "faceBlock", "exportCmd", "declaration", 
                   "varType", "assignStmt", "exprStmt", "block", "ifStmt", 
                   "whileStmt", "forStmt", "funcDef", "returnStmt", "paramList", 
                   "variableRef", "printStmt", "expr", "logicalOrExpr", 
                   "logicalAndExpr", "comparisonExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "funcCall" ]

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
    STRING_K=23
    IF=24
    ELSE=25
    WHILE=26
    FOR=27
    FUNC=28
    RETURN=29
    TRUE=30
    FALSE=31
    AND=32
    OR=33
    NOT=34
    EQ=35
    NEQ=36
    LT=37
    GT=38
    LE=39
    GE=40
    PLUS=41
    MINUS=42
    MUL=43
    DIV=44
    LPAREN=45
    RPAREN=46
    COMMA=47
    ID=48
    NUMBER=49
    COMMENT=50
    WS=51
    STRING=52

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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389827440590784) != 0):
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.faceBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.funcDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.returnStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 79
                self.printStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 80
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.printStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 91
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.moveCmd()
                pass
            elif token in [7, 8, 9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.turnCmd()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.penCmd()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
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
            self.state = 100
            self.match(SpacialTurtleParser.MOVE)
            self.state = 101
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
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(SpacialTurtleParser.TURNX)
                self.state = 104
                self.expr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(SpacialTurtleParser.TURNY)
                self.state = 106
                self.expr()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.match(SpacialTurtleParser.TURNZ)
                self.state = 108
                self.expr()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.match(SpacialTurtleParser.GTURNX)
                self.state = 110
                self.expr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.match(SpacialTurtleParser.GTURNY)
                self.state = 112
                self.expr()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.match(SpacialTurtleParser.GTURNZ)
                self.state = 114
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
            self.state = 117
            self.match(SpacialTurtleParser.PEN)
            self.state = 118
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
            self.state = 120
            self.match(SpacialTurtleParser.FACE)
            self.state = 121
            self.match(SpacialTurtleParser.T__0)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389827172089792) != 0):
                self.state = 122
                self.faceStatement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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
            self.state = 130
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
            self.state = 132
            self.varType()
            self.state = 133
            self.match(SpacialTurtleParser.ID)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 134
                self.match(SpacialTurtleParser.T__2)
                self.state = 135
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

        def STRING_K(self):
            return self.getToken(SpacialTurtleParser.STRING_K, 0)

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
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
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
            self.state = 140
            self.variableRef()
            self.state = 141
            self.match(SpacialTurtleParser.T__2)
            self.state = 142
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
            self.state = 144
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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(SpacialTurtleParser.T__0)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389827440590784) != 0):
                    self.state = 147
                    self.statement()
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 153
                self.match(SpacialTurtleParser.T__1)
                pass
            elif token in [6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 34, 41, 42, 45, 48, 49, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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
            self.state = 157
            self.match(SpacialTurtleParser.IF)
            self.state = 158
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 159
            self.expr()
            self.state = 160
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 161
            self.block()
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(SpacialTurtleParser.ELSE)
                self.state = 163
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
            self.state = 166
            self.match(SpacialTurtleParser.WHILE)
            self.state = 167
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 168
            self.expr()
            self.state = 169
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 170
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
            self.state = 172
            self.match(SpacialTurtleParser.FOR)
            self.state = 173
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23]:
                self.state = 174
                self.declaration()
                pass
            elif token in [19, 48]:
                self.state = 175
                self.assignStmt()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 178
            self.match(SpacialTurtleParser.T__3)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389826416705536) != 0):
                self.state = 179
                self.expr()


            self.state = 182
            self.match(SpacialTurtleParser.T__3)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19 or _la==48:
                self.state = 183
                self.assignStmt()


            self.state = 186
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 187
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
            self.state = 189
            self.match(SpacialTurtleParser.FUNC)
            self.state = 190
            self.match(SpacialTurtleParser.ID)
            self.state = 191
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 192
                self.paramList()


            self.state = 195
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 196
            self.match(SpacialTurtleParser.T__0)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389827440590784) != 0):
                self.state = 197
                self.statement()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
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
            self.state = 205
            self.match(SpacialTurtleParser.RETURN)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 206
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
            self.state = 209
            self.match(SpacialTurtleParser.ID)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 210
                self.match(SpacialTurtleParser.COMMA)
                self.state = 211
                self.match(SpacialTurtleParser.ID)
                self.state = 216
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
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(SpacialTurtleParser.PARENT)
                self.state = 218
                self.match(SpacialTurtleParser.T__4)
                self.state = 219
                self.variableRef()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SpacialTurtleParser.PRINT)
            self.state = 224
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389826416705536) != 0):
                self.state = 225
                self.expr()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 226
                    self.match(SpacialTurtleParser.COMMA)
                    self.state = 227
                    self.expr()
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 235
            self.match(SpacialTurtleParser.RPAREN)
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

        def logicalOrExpr(self):
            return self.getTypedRuleContext(SpacialTurtleParser.LogicalOrExprContext,0)


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
            self.state = 237
            self.logicalOrExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.LogicalAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.OR)
            else:
                return self.getToken(SpacialTurtleParser.OR, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_logicalOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpr" ):
                listener.enterLogicalOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpr" ):
                listener.exitLogicalOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpr(self):

        localctx = SpacialTurtleParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.logicalAndExpr()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 240
                self.match(SpacialTurtleParser.OR)
                self.state = 241
                self.logicalAndExpr()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_logicalAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpr" ):
                listener.enterLogicalAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpr" ):
                listener.exitLogicalAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpr(self):

        localctx = SpacialTurtleParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.comparisonExpr()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 248
                self.match(SpacialTurtleParser.AND)
                self.state = 249
                self.comparisonExpr()
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
        self.enterRule(localctx, 50, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.additiveExpr()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0):
                self.state = 256
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
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
        self.enterRule(localctx, 52, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.multiplicativeExpr()
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 261
                    _la = self._input.LA(1)
                    if not(_la==41 or _la==42):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 262
                    self.multiplicativeExpr() 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.unaryExpr()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43 or _la==44:
                self.state = 269
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 270
                self.unaryExpr()
                self.state = 275
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
        self.enterRule(localctx, 56, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6614249635840) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self.unaryExpr()
                pass
            elif token in [19, 20, 21, 22, 23, 30, 31, 45, 48, 49, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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

        def STRING(self):
            return self.getToken(SpacialTurtleParser.STRING, 0)

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
        self.enterRule(localctx, 58, self.RULE_primaryExpr)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(SpacialTurtleParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.variableRef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(SpacialTurtleParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.match(SpacialTurtleParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.match(SpacialTurtleParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 286
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(SpacialTurtleParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 290
                self.funcCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 291
                self.varType()
                self.state = 292
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 293
                self.expr()
                self.state = 294
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
        self.enterRule(localctx, 60, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(SpacialTurtleParser.ID)
            self.state = 299
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5389826416705536) != 0):
                self.state = 300
                self.expr()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==47:
                    self.state = 301
                    self.match(SpacialTurtleParser.COMMA)
                    self.state = 302
                    self.expr()
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 310
            self.match(SpacialTurtleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





