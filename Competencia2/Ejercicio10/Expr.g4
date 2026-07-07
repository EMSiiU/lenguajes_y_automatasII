grammar Expr;

root : expr EOF;

//expr : expr MAS expr | NUM;
expr : EOF;

PRINT: 'print';
PARENTESIS_ABRE: '(';
PARENTESIS_CIERRA: ')';
PUNTO_COMA: ';';
CADENA: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;
