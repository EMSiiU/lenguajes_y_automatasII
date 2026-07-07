grammar Expr;
root : expr EOF;
expr : IF ID MAYOR NUM;

IF: 'if';

ID: [A-Za-z]+;
NUM: [0-9]+;

IGUAL: '=';
MAYOR: '>';
MAS: '+';
MENOS: '-';
WS: [ \t\r\n]+ -> skip;


