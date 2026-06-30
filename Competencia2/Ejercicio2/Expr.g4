grammar Expr;

root : expr EOF;

//expr : expr MAS expr | NUM;
expr : EOF;

IF: 'if';
ID: [A-Za-z]+;
MAYOR: '>';

NUM: [0-9]+;
MAS: '+';
MENOS: '-';
WS: [ \t\r\n]+ -> skip;




