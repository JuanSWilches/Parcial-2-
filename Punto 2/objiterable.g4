grammar objiterable;

program: statementList EOF;

statementList: statement*;

statement: mappingStatement | filteringStatement | complexMapping | complexFiltering;

mappingStatement: 'MAP' '(' functionCall ',' iterableValue ')';

filteringStatement: 'FILTER' '(' functionCall ',' iterableValue ')';

complexMapping: 'MAP' '(' functionCall ',' iterableValue ',' optionalParameter ')';

complexFiltering: 'FILTER' '(' functionCall ',' iterableValue ',' optionalParameter ')';

functionCall: functionIdentifier;

iterableValue: listExpression | tupleExpression | functionIdentifier;

listExpression: '[' itemList? ']';

tupleExpression: '(' itemList? ')';

itemList: item (',' item)*;

item: NUMBER_LITERAL | functionIdentifier;

functionIdentifier: FUNCTION_NAME;

optionalParameter: NUMBER_LITERAL | STRING_LITERAL;

FUNCTION_NAME: [a-zA-Z_][a-zA-Z_0-9]*;

NUMBER_LITERAL: [0-9]+;

STRING_LITERAL: '"' ~["]* '"';

WHITESPACE: [ \t\r\n]+ -> skip;

