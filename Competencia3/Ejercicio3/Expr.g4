grammar Expr;

root : expr2 EOF;

//Manera indirecta
expr : ID IGUAL expr |ID|NUM;

//Manera directa
expr2: ID IGUAL NUM;

ID: [A-Za-z]+;
NUM: [0-9]+;

IGUAL: '=';
MAS: '+';
MENOS: '-';
WS: [ \t\r\n]+ -> skip;


