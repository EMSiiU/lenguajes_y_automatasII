grammar Expr;

root : expr EOF;

//expr : expr MAS expr | NUM;
expr : EOF;

INT: 'int';
ASING: '=';
IDT: [a-zA-Z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
