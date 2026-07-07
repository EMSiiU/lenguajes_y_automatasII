grammar Expr;

root : expr EOF;
expr :IDT MAYOR_IGUAL valor;
valor: NUM | IDT;


MAYOR_IGUAL: '>=';
IDT: [a-zA-Z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;

