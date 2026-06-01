grammar RaraLang;

// RaraLang — Iteración 3: aritmética básica con precedencia.

prog : stmt* EOF ;

stmt
    : PRINT expr        #printStmt
    | ID ASSIGN expr    #assignStmt
    ;

expr
    : expr op=(TIMES | DIVIDE) expr    #mulDiv
    | expr op=(PLUS  | MINUS)  expr    #addSub
    | '(' expr ')'                     #paren
    | INT                              #int
    | BASED_NUMBER                     #based
    | STRING                           #string
    | ID                               #var
    ;

// ─── Keywords ─────────────────────────────────────────────────────────────────

PRINT  : 'print' ;
ASSIGN : '<--' ;

// ─── Operadores aritméticos ───────────────────────────────────────────────────

PLUS   : '+' ;
MINUS  : '-' ;
TIMES  : '×' ;
DIVIDE : '÷' ;

// ─── Literales ────────────────────────────────────────────────────────────────

INT          : [0-9]+ ;
BASED_NUMBER : '[' [0-9a-fA-F]+ ':' [0-9]+ ']' ;
STRING       : '"' (~["\r\n])* '"' ;

// ─── Identificadores ──────────────────────────────────────────────────────────

ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// ─── Infraestructura ──────────────────────────────────────────────────────────

NEWLINE : [\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+  -> skip ;
