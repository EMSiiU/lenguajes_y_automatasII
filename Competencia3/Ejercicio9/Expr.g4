grammar Expr;

root : expr EOF;
expr : IF PAR1 valor MAYOR valor PAR2;
valor: NUM | IDT;

IF: 'if';
MAYOR: '>';
PAR1: '(';
PAR2: ')';
IDT: [a-zA-Z]+[a-zA-Z0-9]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;

