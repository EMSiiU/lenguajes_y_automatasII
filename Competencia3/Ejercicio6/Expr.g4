grammar Expr;

root : expr2 EOF;

//Manera indirecta
expr : expr op expr op expr | NUM;
op: MAS | POR;

//Manera directa
expr2: NUM MAS NUM POR NUM;


NUM: [0-9]+;
MAS: '+';
POR: '*';
WS: [ \t\r\n]+ -> skip;

