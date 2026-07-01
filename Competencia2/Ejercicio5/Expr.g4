grammar Expr;

root : expr EOF;

//expr : expr MAS expr | NUM;
expr : EOF;


IF: 'if';
PRINT: 'print';

ID: [A-Za-z]+;
NUM: [0-9]+;
TEXTO: '"' ~[\r\n"]* '"';

IGUAL: '=';
MAYOR: '>';
MAS: '+';
MENOS: '-';
WS: [ \t\r\n]+ -> skip;




