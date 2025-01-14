grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

program: 'votien'+ EOF;

// ! ---------------- LEXER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//TODO Operators 3.3.3 pdf
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
DOT: '.';

//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LCURPAREN: '{';
RCURPAREN: '}';
LSQUAREPAREN: '[';
RSQUAREPAREN: ']';
COM: ',';
COCOM: ';';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//TODO Literals 3.3.5 pdf
INT_LIT: '0'| [1-9][0-9]*;
BIN_LIT: '0'[bB][0-1]+{
    self.text = str(int(self.text, 2));
};
OCT_LIT: '0'[oO][0-7]+{
    self.text = str(int(self.text, 8));
};

HEX_LIT: '0'[xX][0-9A-F]+{
    self.text = str(int(self.text, 16));
};


FLOAT_LIT: DIGITS OPT_FRAC OPT_EXP | DIGITS OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: DIGIT+;
fragment OPT_FRAC: ('.'DIGIT*)?;
fragment OPT_EXP: ([Ee][+-]? DIGITS)?;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\f\r\n]+ -> skip; // skip spaces, tabs 
COMMENT: '//' ~[\n]* -> skip;
COMMENTS: (('/*' COMMENTS*? '*/') | ('/*' .*? '*/')) -> skip;

STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\];

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'U' {
    raise UncloseString(self.text[1:-2])
};
ILLEGAL_ESCAPE:
	'I' {
    raise IllegalEscape(self.text[1:])
};

//! ---------------- LEXER ----------------------- */