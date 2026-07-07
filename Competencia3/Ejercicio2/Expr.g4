grammar Expr;

root : expr2 EOF;

//Manera indirecta
expr : expr MENOS expr | NUM;

//Manera directa
expr2: NUM MENOS NUM;


NUM: [0-9]+;
MENOS: '-';
WS: [ \t\r\n]+ -> skip;




