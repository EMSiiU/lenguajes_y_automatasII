grammar Expr;

root : expr EOF;
expr : PRINT PAR1 CADENA PAR2 PUNTO_COMA;

PRINT: 'print';
PAR1: '(';
PAR2: ')';
PUNTO_COMA: ';';
CADENA: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;

