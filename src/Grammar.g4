grammar Grammar;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   ID                          # id
    |   INT                         # int
    |   DEC                         # dec
    |   STRING                      # String
    |   '[' (expr)* (op=(','|', '| ' ,') expr)* ']'            # List
    |   expr '[' expr ']'            # Index
    |   '(' expr ')'                # parens
    |   expr op=('*'|'/'|'%') expr  # MulDiv
    |   expr op=('**'|'//') expr    # ExpFlo
    |   expr op=('+'|'-') expr      # AddSub
    |   expr op='in' expr           # OpIn
    |   expr op=('>'|'>='|'<'|'<='|'=='|'!='|'<>') expr     # Comparators
    |   NOT expr                    # Not
    |   expr op=('and'|'or') expr   # AndOr
    |   op=('true'|'false')         # Bool
    ;
//expr (',' expr)*
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
DEC :   [0-9]* ('.' [0-9]+);             // match real numbers
STRING: '"' [a-zA-Z0-9 ,./;:'"]* '"';
COM1:   ',';
COM2:   ', ';
COM3:   ' , ';
COM4:   ' ,';
NOT :   'not ';
QUOTE:  '"';
MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
ADD :   '+' ;
SUB :   '-' ;
EXP :   '**';
FLO :   '//';
GRT :   '>';
GRE :   '>=';
LET :   '<';
LEE :   '<=';
EQL :   '==';
NEQ :   '!=';
NEQQ:   '<>';
AND :   'and';
OR  :   'or';
TRUE:   'true';
FALSE:  'false';
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace