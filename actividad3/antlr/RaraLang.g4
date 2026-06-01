grammar RaraLang;

// RaraLang — Iteración 4: operadores Unicode ⊞ ⊠ ≈ ±

prog : stmt* EOF ;

stmt
    : PRINT expr        #printStmt
    | ID ASSIGN expr    #assignStmt
    ;

expr
    : expr op=(TIMES | DIVIDE | MOD | DPLS) expr    #mulDiv
    | expr op=(PLUS  | MINUS  | AVG)        expr    #addSub
    | UNEG expr                                      #neg
    | '(' expr ')'                                   #paren
    | INT                                            #int
    | BASED_NUMBER                                   #based
    | STRING                                         #string
    | ID                                             #var
    ;

// ─── Keywords ─────────────────────────────────────────────────────────────────

PRINT  : 'print' ;
ASSIGN : '<--' ;

// ─── Operadores aritméticos ───────────────────────────────────────────────────

PLUS   : '+' ;
MINUS  : '-' ;
TIMES  : '×' ;
DIVIDE : '÷' ;

// ─── Operadores Unicode ───────────────────────────────────────────────────────

MOD  : '⊞' ;   // módulo (residuo)
DPLS : '⊠' ;   // doble más: 2a + b
AVG  : '≈' ;   // promedio entero: floor((a+b)/2)
UNEG : '±' ;   // negación unaria: -x

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
