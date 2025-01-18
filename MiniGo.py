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
DECIMAL_LIT: '0'| [1-9][0-9]*;
BIN_LIT: '0'[bB][0-1]+{
    self.text = str(int(self.text, 2));
};
OCT_LIT: '0'[oO][0-7]+{
    self.text = str(int(self.text, 8));
};
HEX_LIT: '0'[xX][0-9A-Fa-f]+{
    self.text = str(int(self.text, 16));
};
INT_LIT: DECIMAL_LIT | BIN_LIT | OCT_LIT | HEX_LIT;

FLOAT_LIT: POR_OR_NEGA START_DIGIT DIGITS OPT_FRAC OPT_EXP 
         | POR_OR_NEGA START_DIGIT DIGITS OPT_EXP;
fragment START_DIGIT: [1-9];
fragment DIGIT: [0-9];
fragment DIGITS: DIGIT*;
fragment OPT_FRAC: ('.'DIGIT*)?;
fragment OPT_EXP: ([Ee]POR_OR_NEGA (START_DIGIT DIGITS | '0'))?;
fragment POR_OR_NEGA: [+-]?;

STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

//TODO skip 3.1 and 3.2 pdf
LINE_BREAK: '\r'? '\n';
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs 
COMMENT_LINE: '//' ~[\n]* -> skip;
COMMENT: ('/*' (COMMENT | .)*? '*/') -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:'"' STRING_CHAR* ('\r\n' | '\n' | EOF){
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif(self.text[-1] == '\n') :
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:'"' STRING_CHAR* ESC_ILLEGAL{
    raise IllegalEscape(self.text[1:])
};

//! ---------------- LEXER ----------------------- */