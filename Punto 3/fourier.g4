// Fourier.g4
grammar Fourier;

// Reglas de producción
program: (statement)*;

statement: functionStatement | pulseStatement;

functionStatement: 'F' '(' expression ')' '=' 'F' '(' expression ')' ;

pulseStatement: 'P' '(' pulseType ')' '=' 'P' '(' pulseType ')' ;

pulseType: 'rectangular' | 'triangular' | 'dirac' | 'signum' | 'cos' | 'sin';

expression: ID | INT | FLOAT;

ID: [a-zA-Z]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
WS: [ \t\n\r]+ -> skip;
