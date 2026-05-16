grammar SpacialTurtle;

@parser::header {
from typing import Dict, Any, List
}

program : statement* EOF ;

statement
    : command
    | declaration
    | assignStmt
    | faceBlock
    | ifStmt
    | whileStmt
    | forStmt
    | funcDef
    | returnStmt
    | printStmt
    | exprStmt
    | breakStmt     
    | continueStmt
    ;

faceStatement
    : command
    | declaration
    | assignStmt
    | ifStmt
    | whileStmt
    | forStmt
    | returnStmt
    | printStmt
    | exprStmt
    | breakStmt     
    | continueStmt
    ;

command
    : moveCmd
    | turnCmd
    | penCmd
    | exportCmd
    ;

moveCmd : MOVE expr ;

turnCmd
    : TURNX expr
    | TURNY expr
    | TURNZ expr
    | GTURNX expr
    | GTURNY expr
    | GTURNZ expr
    ;

penCmd : PEN (UP | DOWN) ;

faceBlock : FACE '{' faceStatement* '}' ;

exportCmd : EXPORT ;

declaration : varType ID ('=' expr)? ;

varType : INT_K | FLOAT_K | BOOL_K | STRING_K ;

assignStmt : variableRef '=' expr ;

exprStmt : expr ;

block : '{' statement* '}' | statement ;

ifStmt : IF '(' expr ')' block (ELSE block)? ;
whileStmt : WHILE '(' expr ')' block ;

forStmt : FOR '(' (declaration | assignStmt)? ';' expr? ';' assignStmt? ')' block ;

funcDef : FUNC ID '(' typedParamList? ')' (':' varType)? '{' statement* '}' ;
returnStmt : RETURN expr? ;
typedParamList : paramWithType (',' paramWithType)* ;
paramWithType : ID ':' varType ;
breakStmt : BREAK ';'? ;     
continueStmt : CONTINUE ';'? ;
variableRef
    : PARENT '::' variableRef
    | ID
    ;

printStmt : PRINT '(' (expr (',' expr)*)? ')' ;

expr : logicalOrExpr ;

logicalOrExpr : logicalAndExpr ( OR logicalAndExpr )* ;

logicalAndExpr : comparisonExpr ( AND comparisonExpr )* ;

comparisonExpr
    : additiveExpr ( (EQ | NEQ | LT | GT | LE | GE) additiveExpr )?
    ;

additiveExpr
    : multiplicativeExpr ( (PLUS | MINUS) multiplicativeExpr )*
    ;

multiplicativeExpr
    : unaryExpr ( (MUL | DIV | IDIV | MOD) unaryExpr )*
    ;

unaryExpr
    : (PLUS | MINUS | NOT) unaryExpr
    | primaryExpr
    ;

primaryExpr
    : NUMBER
    | funcCall
    | variableRef
    | TRUE
    | FALSE
    | STRING
    | LPAREN expr RPAREN
    | varType '(' expr ')'
    ;

funcCall : ID '(' (expr (',' expr)*)? ')' ;

MOVE   : 'move';
TURNX  : 'turnX';
TURNY  : 'turnY';
TURNZ  : 'turnZ';
GTURNX : 'gturnX';
GTURNY : 'gturnY';
GTURNZ : 'gturnZ';
PEN    : 'pen';
UP     : 'up';
DOWN   : 'down';
FACE   : 'face';
EXPORT : 'export';
PRINT  : 'print';
BREAK  : 'break';
CONTINUE : 'continue';

PARENT  : 'parent';
INT_K   : 'int';
FLOAT_K : 'float';
BOOL_K  : 'bool';
STRING_K : 'string';

IF    : 'if';
ELSE  : 'else';
WHILE : 'while';
FOR   : 'for';
FUNC  : 'func';
RETURN: 'return';
TRUE  : 'true';
FALSE : 'false';
AND   : 'and';
OR    : 'or';
NOT   : 'not';
EQ    : '==';
NEQ   : '!=';
LT    : '<';
GT    : '>';
LE    : '<=';
GE    : '>=';
PLUS  : '+';
MINUS : '-';
MUL   : '*';
DIV   : '/';
IDIV  : '//';
MOD   : '%';
LPAREN: '(';
RPAREN: ')';
COMMA : ',';


ID : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : '-'? [0-9]+ ('.' [0-9]+)?;
COMMENT : '#' ~[\r\n]* -> skip;
WS : [ \t\r\n]+ -> skip;
STRING : '"' ~["\r\n]* '"' ;
