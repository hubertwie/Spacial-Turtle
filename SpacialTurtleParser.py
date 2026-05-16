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
        4,1,57,339,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,90,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,103,8,2,1,3,1,3,1,3,1,3,3,3,109,8,3,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,126,
        8,5,1,6,1,6,1,6,1,7,1,7,1,7,5,7,134,8,7,10,7,12,7,137,9,7,1,7,1,
        7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,147,8,9,1,10,1,10,1,11,1,11,1,11,1,
        11,1,12,1,12,1,13,1,13,5,13,159,8,13,10,13,12,13,162,9,13,1,13,1,
        13,3,13,166,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,175,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,187,8,16,
        1,16,1,16,3,16,191,8,16,1,16,1,16,3,16,195,8,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,3,17,204,8,17,1,17,1,17,1,17,3,17,209,8,17,1,17,
        1,17,5,17,213,8,17,10,17,12,17,216,9,17,1,17,1,17,1,18,1,18,3,18,
        222,8,18,1,19,1,19,1,19,5,19,227,8,19,10,19,12,19,230,9,19,1,20,
        1,20,1,20,1,20,1,21,1,21,3,21,238,8,21,1,22,1,22,3,22,242,8,22,1,
        23,1,23,1,23,1,23,3,23,248,8,23,1,24,1,24,1,24,1,24,1,24,5,24,255,
        8,24,10,24,12,24,258,9,24,3,24,260,8,24,1,24,1,24,1,25,1,25,1,26,
        1,26,1,26,5,26,269,8,26,10,26,12,26,272,9,26,1,27,1,27,1,27,5,27,
        277,8,27,10,27,12,27,280,9,27,1,28,1,28,1,28,3,28,285,8,28,1,29,
        1,29,1,29,5,29,290,8,29,10,29,12,29,293,9,29,1,30,1,30,1,30,5,30,
        298,8,30,10,30,12,30,301,9,30,1,31,1,31,1,31,3,31,306,8,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,3,32,323,8,32,1,33,1,33,1,33,1,33,1,33,5,33,330,8,33,10,33,
        12,33,333,9,33,3,33,335,8,33,1,33,1,33,1,33,0,0,34,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,0,6,1,0,15,16,1,0,23,26,1,0,38,43,1,0,44,45,1,
        0,46,49,2,0,37,37,44,45,369,0,71,1,0,0,0,2,89,1,0,0,0,4,102,1,0,
        0,0,6,108,1,0,0,0,8,110,1,0,0,0,10,125,1,0,0,0,12,127,1,0,0,0,14,
        130,1,0,0,0,16,140,1,0,0,0,18,142,1,0,0,0,20,148,1,0,0,0,22,150,
        1,0,0,0,24,154,1,0,0,0,26,165,1,0,0,0,28,167,1,0,0,0,30,176,1,0,
        0,0,32,182,1,0,0,0,34,199,1,0,0,0,36,219,1,0,0,0,38,223,1,0,0,0,
        40,231,1,0,0,0,42,235,1,0,0,0,44,239,1,0,0,0,46,247,1,0,0,0,48,249,
        1,0,0,0,50,263,1,0,0,0,52,265,1,0,0,0,54,273,1,0,0,0,56,281,1,0,
        0,0,58,286,1,0,0,0,60,294,1,0,0,0,62,305,1,0,0,0,64,322,1,0,0,0,
        66,324,1,0,0,0,68,70,3,2,1,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,
        0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,0,0,1,75,
        1,1,0,0,0,76,90,3,6,3,0,77,90,3,18,9,0,78,90,3,22,11,0,79,90,3,14,
        7,0,80,90,3,28,14,0,81,90,3,30,15,0,82,90,3,32,16,0,83,90,3,34,17,
        0,84,90,3,36,18,0,85,90,3,48,24,0,86,90,3,24,12,0,87,90,3,42,21,
        0,88,90,3,44,22,0,89,76,1,0,0,0,89,77,1,0,0,0,89,78,1,0,0,0,89,79,
        1,0,0,0,89,80,1,0,0,0,89,81,1,0,0,0,89,82,1,0,0,0,89,83,1,0,0,0,
        89,84,1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,
        0,0,0,90,3,1,0,0,0,91,103,3,6,3,0,92,103,3,18,9,0,93,103,3,22,11,
        0,94,103,3,28,14,0,95,103,3,30,15,0,96,103,3,32,16,0,97,103,3,36,
        18,0,98,103,3,48,24,0,99,103,3,24,12,0,100,103,3,42,21,0,101,103,
        3,44,22,0,102,91,1,0,0,0,102,92,1,0,0,0,102,93,1,0,0,0,102,94,1,
        0,0,0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,
        0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,5,1,0,0,0,104,
        109,3,8,4,0,105,109,3,10,5,0,106,109,3,12,6,0,107,109,3,16,8,0,108,
        104,1,0,0,0,108,105,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,
        7,1,0,0,0,110,111,5,7,0,0,111,112,3,50,25,0,112,9,1,0,0,0,113,114,
        5,8,0,0,114,126,3,50,25,0,115,116,5,9,0,0,116,126,3,50,25,0,117,
        118,5,10,0,0,118,126,3,50,25,0,119,120,5,11,0,0,120,126,3,50,25,
        0,121,122,5,12,0,0,122,126,3,50,25,0,123,124,5,13,0,0,124,126,3,
        50,25,0,125,113,1,0,0,0,125,115,1,0,0,0,125,117,1,0,0,0,125,119,
        1,0,0,0,125,121,1,0,0,0,125,123,1,0,0,0,126,11,1,0,0,0,127,128,5,
        14,0,0,128,129,7,0,0,0,129,13,1,0,0,0,130,131,5,17,0,0,131,135,5,
        1,0,0,132,134,3,4,2,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,
        0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,
        2,0,0,139,15,1,0,0,0,140,141,5,18,0,0,141,17,1,0,0,0,142,143,3,20,
        10,0,143,146,5,53,0,0,144,145,5,3,0,0,145,147,3,50,25,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,19,1,0,0,0,148,149,7,1,0,0,149,21,1,
        0,0,0,150,151,3,46,23,0,151,152,5,3,0,0,152,153,3,50,25,0,153,23,
        1,0,0,0,154,155,3,50,25,0,155,25,1,0,0,0,156,160,5,1,0,0,157,159,
        3,2,1,0,158,157,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,
        1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,166,5,2,0,0,164,166,
        3,2,1,0,165,156,1,0,0,0,165,164,1,0,0,0,166,27,1,0,0,0,167,168,5,
        27,0,0,168,169,5,50,0,0,169,170,3,50,25,0,170,171,5,51,0,0,171,174,
        3,26,13,0,172,173,5,28,0,0,173,175,3,26,13,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,29,1,0,0,0,176,177,5,29,0,0,177,178,5,50,0,0,178,
        179,3,50,25,0,179,180,5,51,0,0,180,181,3,26,13,0,181,31,1,0,0,0,
        182,183,5,30,0,0,183,186,5,50,0,0,184,187,3,18,9,0,185,187,3,22,
        11,0,186,184,1,0,0,0,186,185,1,0,0,0,186,187,1,0,0,0,187,188,1,0,
        0,0,188,190,5,4,0,0,189,191,3,50,25,0,190,189,1,0,0,0,190,191,1,
        0,0,0,191,192,1,0,0,0,192,194,5,4,0,0,193,195,3,22,11,0,194,193,
        1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,197,5,51,0,0,197,198,
        3,26,13,0,198,33,1,0,0,0,199,200,5,31,0,0,200,201,5,53,0,0,201,203,
        5,50,0,0,202,204,3,38,19,0,203,202,1,0,0,0,203,204,1,0,0,0,204,205,
        1,0,0,0,205,208,5,51,0,0,206,207,5,5,0,0,207,209,3,20,10,0,208,206,
        1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,214,5,1,0,0,211,213,
        3,2,1,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,
        1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,2,0,0,218,35,1,
        0,0,0,219,221,5,32,0,0,220,222,3,50,25,0,221,220,1,0,0,0,221,222,
        1,0,0,0,222,37,1,0,0,0,223,228,3,40,20,0,224,225,5,52,0,0,225,227,
        3,40,20,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,
        1,0,0,0,229,39,1,0,0,0,230,228,1,0,0,0,231,232,5,53,0,0,232,233,
        5,5,0,0,233,234,3,20,10,0,234,41,1,0,0,0,235,237,5,20,0,0,236,238,
        5,4,0,0,237,236,1,0,0,0,237,238,1,0,0,0,238,43,1,0,0,0,239,241,5,
        21,0,0,240,242,5,4,0,0,241,240,1,0,0,0,241,242,1,0,0,0,242,45,1,
        0,0,0,243,244,5,22,0,0,244,245,5,6,0,0,245,248,3,46,23,0,246,248,
        5,53,0,0,247,243,1,0,0,0,247,246,1,0,0,0,248,47,1,0,0,0,249,250,
        5,19,0,0,250,259,5,50,0,0,251,256,3,50,25,0,252,253,5,52,0,0,253,
        255,3,50,25,0,254,252,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,
        257,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,259,251,1,0,0,0,259,
        260,1,0,0,0,260,261,1,0,0,0,261,262,5,51,0,0,262,49,1,0,0,0,263,
        264,3,52,26,0,264,51,1,0,0,0,265,270,3,54,27,0,266,267,5,36,0,0,
        267,269,3,54,27,0,268,266,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,
        0,270,271,1,0,0,0,271,53,1,0,0,0,272,270,1,0,0,0,273,278,3,56,28,
        0,274,275,5,35,0,0,275,277,3,56,28,0,276,274,1,0,0,0,277,280,1,0,
        0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,55,1,0,0,0,280,278,1,0,0,
        0,281,284,3,58,29,0,282,283,7,2,0,0,283,285,3,58,29,0,284,282,1,
        0,0,0,284,285,1,0,0,0,285,57,1,0,0,0,286,291,3,60,30,0,287,288,7,
        3,0,0,288,290,3,60,30,0,289,287,1,0,0,0,290,293,1,0,0,0,291,289,
        1,0,0,0,291,292,1,0,0,0,292,59,1,0,0,0,293,291,1,0,0,0,294,299,3,
        62,31,0,295,296,7,4,0,0,296,298,3,62,31,0,297,295,1,0,0,0,298,301,
        1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,61,1,0,0,0,301,299,1,
        0,0,0,302,303,7,5,0,0,303,306,3,62,31,0,304,306,3,64,32,0,305,302,
        1,0,0,0,305,304,1,0,0,0,306,63,1,0,0,0,307,323,5,54,0,0,308,323,
        3,66,33,0,309,323,3,46,23,0,310,323,5,33,0,0,311,323,5,34,0,0,312,
        323,5,57,0,0,313,314,5,50,0,0,314,315,3,50,25,0,315,316,5,51,0,0,
        316,323,1,0,0,0,317,318,3,20,10,0,318,319,5,50,0,0,319,320,3,50,
        25,0,320,321,5,51,0,0,321,323,1,0,0,0,322,307,1,0,0,0,322,308,1,
        0,0,0,322,309,1,0,0,0,322,310,1,0,0,0,322,311,1,0,0,0,322,312,1,
        0,0,0,322,313,1,0,0,0,322,317,1,0,0,0,323,65,1,0,0,0,324,325,5,53,
        0,0,325,334,5,50,0,0,326,331,3,50,25,0,327,328,5,52,0,0,328,330,
        3,50,25,0,329,327,1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,
        1,0,0,0,332,335,1,0,0,0,333,331,1,0,0,0,334,326,1,0,0,0,334,335,
        1,0,0,0,335,336,1,0,0,0,336,337,5,51,0,0,337,67,1,0,0,0,32,71,89,
        102,108,125,135,146,160,165,174,186,190,194,203,208,214,221,228,
        237,241,247,256,259,270,278,284,291,299,305,322,331,334
    ]

class SpacialTurtleParser ( Parser ):

    grammarFileName = "SpacialTurtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "';'", "':'", "'::'", 
                     "'move'", "'turnX'", "'turnY'", "'turnZ'", "'gturnX'", 
                     "'gturnY'", "'gturnZ'", "'pen'", "'up'", "'down'", 
                     "'face'", "'export'", "'print'", "'break'", "'continue'", 
                     "'parent'", "'int'", "'float'", "'bool'", "'string'", 
                     "'if'", "'else'", "'while'", "'for'", "'func'", "'return'", 
                     "'true'", "'false'", "'and'", "'or'", "'not'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'//'", "'%'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MOVE", "TURNX", 
                      "TURNY", "TURNZ", "GTURNX", "GTURNY", "GTURNZ", "PEN", 
                      "UP", "DOWN", "FACE", "EXPORT", "PRINT", "BREAK", 
                      "CONTINUE", "PARENT", "INT_K", "FLOAT_K", "BOOL_K", 
                      "STRING_K", "IF", "ELSE", "WHILE", "FOR", "FUNC", 
                      "RETURN", "TRUE", "FALSE", "AND", "OR", "NOT", "EQ", 
                      "NEQ", "LT", "GT", "LE", "GE", "PLUS", "MINUS", "MUL", 
                      "DIV", "IDIV", "MOD", "LPAREN", "RPAREN", "COMMA", 
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
    RULE_typedParamList = 19
    RULE_paramWithType = 20
    RULE_breakStmt = 21
    RULE_continueStmt = 22
    RULE_variableRef = 23
    RULE_printStmt = 24
    RULE_expr = 25
    RULE_logicalOrExpr = 26
    RULE_logicalAndExpr = 27
    RULE_comparisonExpr = 28
    RULE_additiveExpr = 29
    RULE_multiplicativeExpr = 30
    RULE_unaryExpr = 31
    RULE_primaryExpr = 32
    RULE_funcCall = 33

    ruleNames =  [ "program", "statement", "faceStatement", "command", "moveCmd", 
                   "turnCmd", "penCmd", "faceBlock", "exportCmd", "declaration", 
                   "varType", "assignStmt", "exprStmt", "block", "ifStmt", 
                   "whileStmt", "forStmt", "funcDef", "returnStmt", "typedParamList", 
                   "paramWithType", "breakStmt", "continueStmt", "variableRef", 
                   "printStmt", "expr", "logicalOrExpr", "logicalAndExpr", 
                   "comparisonExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "funcCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MOVE=7
    TURNX=8
    TURNY=9
    TURNZ=10
    GTURNX=11
    GTURNY=12
    GTURNZ=13
    PEN=14
    UP=15
    DOWN=16
    FACE=17
    EXPORT=18
    PRINT=19
    BREAK=20
    CONTINUE=21
    PARENT=22
    INT_K=23
    FLOAT_K=24
    BOOL_K=25
    STRING_K=26
    IF=27
    ELSE=28
    WHILE=29
    FOR=30
    FUNC=31
    RETURN=32
    TRUE=33
    FALSE=34
    AND=35
    OR=36
    NOT=37
    EQ=38
    NEQ=39
    LT=40
    GT=41
    LE=42
    GE=43
    PLUS=44
    MINUS=45
    MUL=46
    DIV=47
    IDIV=48
    MOD=49
    LPAREN=50
    RPAREN=51
    COMMA=52
    ID=53
    NUMBER=54
    COMMENT=55
    WS=56
    STRING=57

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
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315633835212672) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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


        def breakStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ContinueStmtContext,0)


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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.faceBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.funcDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.returnStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.printStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.exprStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 87
                self.breakStmt()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 88
                self.continueStmt()
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


        def breakStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(SpacialTurtleParser.ContinueStmtContext,0)


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
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.command()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 98
                self.printStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 99
                self.exprStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 100
                self.breakStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 101
                self.continueStmt()
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
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.moveCmd()
                pass
            elif token in [8, 9, 10, 11, 12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.turnCmd()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.penCmd()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
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
            self.state = 110
            self.match(SpacialTurtleParser.MOVE)
            self.state = 111
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
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(SpacialTurtleParser.TURNX)
                self.state = 114
                self.expr()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(SpacialTurtleParser.TURNY)
                self.state = 116
                self.expr()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(SpacialTurtleParser.TURNZ)
                self.state = 118
                self.expr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(SpacialTurtleParser.GTURNX)
                self.state = 120
                self.expr()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.match(SpacialTurtleParser.GTURNY)
                self.state = 122
                self.expr()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.match(SpacialTurtleParser.GTURNZ)
                self.state = 124
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
            self.state = 127
            self.match(SpacialTurtleParser.PEN)
            self.state = 128
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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
            self.state = 130
            self.match(SpacialTurtleParser.FACE)
            self.state = 131
            self.match(SpacialTurtleParser.T__0)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315631687597952) != 0):
                self.state = 132
                self.faceStatement()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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
            self.state = 140
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
            self.state = 142
            self.varType()
            self.state = 143
            self.match(SpacialTurtleParser.ID)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 144
                self.match(SpacialTurtleParser.T__2)
                self.state = 145
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
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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
            self.state = 150
            self.variableRef()
            self.state = 151
            self.match(SpacialTurtleParser.T__2)
            self.state = 152
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
            self.state = 154
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
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(SpacialTurtleParser.T__0)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315633835212672) != 0):
                    self.state = 157
                    self.statement()
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 163
                self.match(SpacialTurtleParser.T__1)
                pass
            elif token in [7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 37, 44, 45, 50, 53, 54, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
            self.state = 167
            self.match(SpacialTurtleParser.IF)
            self.state = 168
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 169
            self.expr()
            self.state = 170
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 171
            self.block()
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 172
                self.match(SpacialTurtleParser.ELSE)
                self.state = 173
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
            self.state = 176
            self.match(SpacialTurtleParser.WHILE)
            self.state = 177
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 178
            self.expr()
            self.state = 179
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 180
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
            self.state = 182
            self.match(SpacialTurtleParser.FOR)
            self.state = 183
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 26]:
                self.state = 184
                self.declaration()
                pass
            elif token in [22, 53]:
                self.state = 185
                self.assignStmt()
                pass
            elif token in [4]:
                pass
            else:
                pass
            self.state = 188
            self.match(SpacialTurtleParser.T__3)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315625643835392) != 0):
                self.state = 189
                self.expr()


            self.state = 192
            self.match(SpacialTurtleParser.T__3)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==53:
                self.state = 193
                self.assignStmt()


            self.state = 196
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 197
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

        def typedParamList(self):
            return self.getTypedRuleContext(SpacialTurtleParser.TypedParamListContext,0)


        def varType(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VarTypeContext,0)


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
            self.state = 199
            self.match(SpacialTurtleParser.FUNC)
            self.state = 200
            self.match(SpacialTurtleParser.ID)
            self.state = 201
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 202
                self.typedParamList()


            self.state = 205
            self.match(SpacialTurtleParser.RPAREN)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 206
                self.match(SpacialTurtleParser.T__4)
                self.state = 207
                self.varType()


            self.state = 210
            self.match(SpacialTurtleParser.T__0)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315633835212672) != 0):
                self.state = 211
                self.statement()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
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
            self.state = 219
            self.match(SpacialTurtleParser.RETURN)
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 220
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramWithType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpacialTurtleParser.ParamWithTypeContext)
            else:
                return self.getTypedRuleContext(SpacialTurtleParser.ParamWithTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.COMMA)
            else:
                return self.getToken(SpacialTurtleParser.COMMA, i)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_typedParamList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedParamList" ):
                listener.enterTypedParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedParamList" ):
                listener.exitTypedParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedParamList" ):
                return visitor.visitTypedParamList(self)
            else:
                return visitor.visitChildren(self)




    def typedParamList(self):

        localctx = SpacialTurtleParser.TypedParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typedParamList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.paramWithType()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 224
                self.match(SpacialTurtleParser.COMMA)
                self.state = 225
                self.paramWithType()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamWithTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpacialTurtleParser.ID, 0)

        def varType(self):
            return self.getTypedRuleContext(SpacialTurtleParser.VarTypeContext,0)


        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_paramWithType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamWithType" ):
                listener.enterParamWithType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamWithType" ):
                listener.exitParamWithType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamWithType" ):
                return visitor.visitParamWithType(self)
            else:
                return visitor.visitChildren(self)




    def paramWithType(self):

        localctx = SpacialTurtleParser.ParamWithTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramWithType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(SpacialTurtleParser.ID)
            self.state = 232
            self.match(SpacialTurtleParser.T__4)
            self.state = 233
            self.varType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SpacialTurtleParser.BREAK, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = SpacialTurtleParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_breakStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(SpacialTurtleParser.BREAK)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 236
                self.match(SpacialTurtleParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(SpacialTurtleParser.CONTINUE, 0)

        def getRuleIndex(self):
            return SpacialTurtleParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = SpacialTurtleParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continueStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(SpacialTurtleParser.CONTINUE)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 240
                self.match(SpacialTurtleParser.T__3)


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
        self.enterRule(localctx, 46, self.RULE_variableRef)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(SpacialTurtleParser.PARENT)
                self.state = 244
                self.match(SpacialTurtleParser.T__5)
                self.state = 245
                self.variableRef()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
        self.enterRule(localctx, 48, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(SpacialTurtleParser.PRINT)
            self.state = 250
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315625643835392) != 0):
                self.state = 251
                self.expr()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 252
                    self.match(SpacialTurtleParser.COMMA)
                    self.state = 253
                    self.expr()
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 261
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
        self.enterRule(localctx, 50, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
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
        self.enterRule(localctx, 52, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.logicalAndExpr()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 266
                self.match(SpacialTurtleParser.OR)
                self.state = 267
                self.logicalAndExpr()
                self.state = 272
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
        self.enterRule(localctx, 54, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.comparisonExpr()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 274
                self.match(SpacialTurtleParser.AND)
                self.state = 275
                self.comparisonExpr()
                self.state = 280
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
        self.enterRule(localctx, 56, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.additiveExpr()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17317308137472) != 0):
                self.state = 282
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17317308137472) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
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
        self.enterRule(localctx, 58, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.multiplicativeExpr()
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==44 or _la==45):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.multiplicativeExpr() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def IDIV(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.IDIV)
            else:
                return self.getToken(SpacialTurtleParser.IDIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(SpacialTurtleParser.MOD)
            else:
                return self.getToken(SpacialTurtleParser.MOD, i)

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
        self.enterRule(localctx, 60, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.unaryExpr()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1055531162664960) != 0):
                self.state = 295
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1055531162664960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.unaryExpr()
                self.state = 301
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
        self.enterRule(localctx, 62, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 52913997086720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.unaryExpr()
                pass
            elif token in [22, 23, 24, 25, 26, 33, 34, 50, 53, 54, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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

        def funcCall(self):
            return self.getTypedRuleContext(SpacialTurtleParser.FuncCallContext,0)


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
        self.enterRule(localctx, 64, self.RULE_primaryExpr)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(SpacialTurtleParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.variableRef()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(SpacialTurtleParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.match(SpacialTurtleParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 312
                self.match(SpacialTurtleParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 313
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 314
                self.expr()
                self.state = 315
                self.match(SpacialTurtleParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.varType()
                self.state = 318
                self.match(SpacialTurtleParser.LPAREN)
                self.state = 319
                self.expr()
                self.state = 320
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
        self.enterRule(localctx, 66, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(SpacialTurtleParser.ID)
            self.state = 325
            self.match(SpacialTurtleParser.LPAREN)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 172315625643835392) != 0):
                self.state = 326
                self.expr()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 327
                    self.match(SpacialTurtleParser.COMMA)
                    self.state = 328
                    self.expr()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 336
            self.match(SpacialTurtleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





