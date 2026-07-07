grammar Expr;

root : expr EOF;

expr : INT IDT IGUAL valor;
valor: NUM | IDT;

INT: 'int';
IGUAL: '=';
IDT: [a-zA-Z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;

