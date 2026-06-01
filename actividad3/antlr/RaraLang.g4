grammar RaraLang;

// RaraLang — Iteración 6: while y bloques de sentencias

prog : stmt* EOF ;

stmt
    : PRINT expr                        #printStmt
    | ID ASSIGN expr                    #assignStmt
    | IF expr THEN stmt (ELSE stmt)?    #ifStmt
    | WHILE expr DO stmt                #whileStmt
    | '{' stmt* '}'                     #blockStmt
    ;

expr
    : expr op=(TIMES | DIVIDE | MOD | DPLS) expr    #mulDiv
    | expr op=(PLUS  | MINUS  | AVG)        expr    #addSub
    | expr op=(EQ | NEQ | LT | GT)          expr    #compare
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
IF     : 'if' ;
THEN   : 'then' ;
ELSE   : 'else' ;
WHILE  : 'while' ;
DO     : 'do' ;

// ─── Comparadores ─────────────────────────────────────────────────────────────

EQ  : '==' ;
NEQ : '!=' ;
LT  : '<' ;
GT  : '>' ;

// ─── Operadores aritméticos ───────────────────────────────────────────────────

PLUS   : '+' ;
MINUS  : '-' ;
TIMES  : '×' ;
DIVIDE : '÷' ;

// ─── Operadores Unicode ───────────────────────────────────────────────────────

MOD  : '⊞' ;
DPLS : '⊠' ;
AVG  : '≈' ;
UNEG : '±' ;

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
