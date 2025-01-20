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

// ! ---------------- PASER DEADLINE PASS 13 TEST CASE 23:59 16/1 ----------------------- */

program: NEWLINE* declared (declared | NEWLINE)* EOF;

//TODO Literal 6.6 pdf
literal:DECIMAL_LIT
       | BIN_LIT
       | OCT_LIT
       | HEX_LIT
	   | FLOAT_LIT
	   | STRING_LIT
	   | TRUE
	   | FALSE
	   | array_literal
	   | struct_literal;

//list_literal
list_literal: list_literal_noempty | ;
list_literal_noempty: literal COMMA list_literal | literal;

//basic type
all_type: INT 
        | FLOAT 
        | BOOLEAN 
        | STRING 
        | list_array_type_lit 
        | ID;
basic_type: INT 
          | FLOAT 
          | BOOLEAN 
          | STRING 
          | ID;
list_array_type_lit: array_type_lit basic_type;
array_type_lit: array_type array_type_lit | array_type;
array_type: LSPAREN DECIMAL_LIT RSPAREN;

//Array_literal
array_literal: dim_lit all_type LCPAREN list_array_element RCPAREN;
dim_lit: dim dim_lit | dim;
dim: LSPAREN DECIMAL_LIT RSPAREN;
list_array_element: array_element COMMA list_array_element | array_element;
array_element: literal | LCPAREN list_literal RCPAREN;

//Struct_literal
struct_literal: ID LCPAREN list_elements_lit? RCPAREN;
list_elements_lit: list_element COMMA list_elements_lit | list_element;
list_element: ID COLON expression;

// TODO 5.2 Expressions 6 pdf
list_expression: expression COMMA list_expression | expression;
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (EQUAL | NEQUAL | LT | LTE | GT | GTE) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (NOT | SUB) expression | expression6;
expression6: expression6 (LSPAREN expression RSPAREN | DOT expression) | expression7;
expression7: literal | LPAREN expression RPAREN | ID | ID LPAREN funcall RPAREN;

//function call
funcall: funcall_noempty | ;
funcall_noempty: expression | expression COMMA funcall_noempty;

//const declared
const_declared: CONST ID ASSIGN expression;
//variables declared
var_declared: VAR ID (all_type | all_type? ASSIGN expression);
//function declared
func_declared: FUNC ID LPAREN parameter_lit? RPAREN all_type? ignore LCPAREN (NEWLINE | list_statement)* RCPAREN ;
parameter_lit: parameter COMMA parameter_lit | parameter;
parameter: ID all_type;
//method declared
method_declared: FUNC LPAREN ID ID RPAREN ID LPAREN parameter_lit? RPAREN all_type? ignore LCPAREN (NEWLINE | list_statement)* RCPAREN;
//struct declared
struct_declared: TYPE ID STRUCT ignore LCPAREN (NEWLINE | list_statement)* RCPAREN (COCOM | NEWLINE+);
//interface_declared
interface_declared: TYPE ID INTERFACE ignore LCPAREN (NEWLINE | list_statement)* RCPAREN (COCOM | NEWLINE+);

//declared
declared:
	(var_declared COCOM)
	| (const_declared COCOM)
	| func_declared
	| method_declared
	| struct_declared
	| interface_declared;

//TODO Statement 5 and 4 pdf
list_statement: statement list_statement | statement;

//declared statement
declared_statement: declared;
//assign statement
assign_statement: list_assignment_lhs operators expression;
operators:  COLONEQUAL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
list_assignment_lhs: assignment_lhs DOT list_assignment_lhs | assignment_lhs;
assignment_lhs: (ID (list_array_index | ));
list_array_index: array_index list_array_index | array_index;
array_index: LSPAREN expression RSPAREN;
//if statement
else_statement: ELSE ignore LCPAREN (NEWLINE | list_statement)* RCPAREN;
elif_statement: | ELSE IF LPAREN expression RPAREN ignore LCPAREN (NEWLINE | list_statement)* RCPAREN elif_statement;
if_statement: IF LPAREN expression RPAREN ignore LCPAREN (NEWLINE | list_statement)* RCPAREN NEWLINE* elif_statement NEWLINE* else_statement?;
//for statement
range_loop: ID COMMA ID COLONEQUAL RANGE expression;
init_loop: (assign_statement | var_declared) COCOM expression COCOM assign_statement;
basic_loop: expression;
for_statement: FOR (basic_loop | init_loop | range_loop) ignore LCPAREN (NEWLINE | list_statement)* RCPAREN;
//break statement
break_statement: BREAK;
//continue statement
continue_statement: CONTINUE;
//call statement
call_statement: ((list_assignment_lhs DOT) | ) ID LPAREN (list_expression | ) RPAREN;
//return statement
return_statement: RETURN ignore (expression | );
//end statement
end_statement: (COCOM NEWLINE*) | (NEWLINE+);
//struct statement
struct_statement: ID all_type;
//method statement
method_parameter: ID all_type?;
method_parameter_lit: method_parameter COMMA method_parameter_lit | method_parameter;
method_statement: ID LPAREN method_parameter_lit RPAREN all_type?;
statement:
	(
		var_declared | const_declared
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
        | struct_statement
        | method_statement
	)
    end_statement;
ignore: NEWLINE*;

//! ---------------- PASER ----------------------- */

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
COLON: ':';
COMMA: ',';
COCOM: ';';
COLONEQUAL: ':=';

//TODO Separators 3.3.4 pdf
LPAREN: '(';
RPAREN: ')';
LCPAREN: '{';
RCPAREN: '}';
LSPAREN: '[';
RSPAREN: ']';

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

FLOAT_LIT: DIGITS OPT_FRAC OPT_EXP 
         | DIGITS OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: ('0' | [1-9] DIGIT*);
fragment OPT_FRAC: ('.'DIGIT*)?;
fragment OPT_EXP: ([Ee][+-]? ( DIGITS | '0'))?;

STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

//TODO skip 3.1 and 3.2 pdf
NEWLINE: '\r'? '\n';
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