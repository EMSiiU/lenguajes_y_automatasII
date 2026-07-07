grammar Expr;
root : expr2 EOF;

//Manera indirecta
expr : expr MAS expr | NUM;

//Manera directa
expr2: NUM MAS NUM;

NUM: [0-9]+;
MAS: '+';
WS: [ \t\r\n]+ -> skip;


