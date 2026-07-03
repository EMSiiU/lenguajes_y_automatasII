grammar Expr;

root : expr EOF;

//expr : expr MAS expr | NUM;
expr : EOF;

IF: 'if';
MAYOR_QUE: '>';
PARENTESIS_ABRE: '(';
PARENTESIS_CIERRA: ')';
IDT: [a-zA-Z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
