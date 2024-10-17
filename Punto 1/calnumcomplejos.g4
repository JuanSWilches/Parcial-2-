grammar calnumcomplejos;

// Parser rules
prog: expr+ EOF;

expr: complexNumber (op complexNumber)*;

complexNumber: '(' realPart sign imaginaryPart 'i' ')';

realPart: NUMBER;
imaginaryPart: NUMBER;
sign: '+' | '-';
op: '+' | '-' | '*' | '/';

// Lexer rules
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
