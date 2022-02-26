//My Id: 1915439
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_declares EOF;
class_declares: class_declare class_declares | class_declare;
/******************************************************************************************/
/*								D96 Parser												  */
/******************************************************************************************/
/****************************************************************************/
/*								2.1 Class declaration						*/
/****************************************************************************/
class_declare: CLASS ID ( Extended ID)? member_decl;
member_decl: LB memberlist RB;
memberlist: members | ;
members: member members | member;
member: att_declare | method_declare;
/****************************************************************************/
/*								2.2 Attribute declaration					*/
/****************************************************************************/
att_declare: (VAL|VAR) att_declarelist SM;
att_declarelist: att_names Extended data_type | att_init_value;
att_names: idname CM att_names | idname;
att_init_value: idname CM att_init_value CM exp | idname Extended data_type ASSIGN exp;

// values: value | ;
// value: literal CM value | literal;
data_type: primitive_type | array_type | classtype;
primitive_type: INT | FLOAT | BOOLEAN | STRING;
classtype: ID;
//empty_declare: SM;

method_declare: func_declare | contructor_declare | detructor_declare;
func_declare: (ID | DOLLARID) LP paramlist RP blockstatment;
paramlist: params | ;
params: param SM params | param;
param: idnamelist Extended data_type;
idnamelist: ID CM idnamelist | ID;
blockstatment: LB stamentlist RB; // mục 6.9
stamentlist: staments | ;
staments: stament staments | stament;
stament: vardecl_stm
		| assign_stm
		| if_stm
		| forin_stm
		| break_stm
		| continue_stm
		| return_stm
		| method_invocation_stm
		| blockstatment;


literal: (intlit | FLOAT_NUMBER | BOOLEAN_LITERAL | STRING_LITERAL | index_array_literal | multi_array | NULL);
index_array_literal: ARRAY LP explists RP; 
//primitive_literal: INTEGER | INTERGER_GT_ZERO | FLOAT_NUMBER | BOOLEAN_LITERAL | STRING_LITERAL;

// multi_array: ARRAY LP index_array_literal (CM index_array_literal)* RP;
multi_array: ARRAY LP arraylist RP;
arraylist: index_array_literal CM arraylist | index_array_literal;
array_type: ARRAY LSB (primitive_type |array_type) CM sizearray RSB;

/****************************************************************************/
/*								2.2 Statement								*/
/****************************************************************************/

vardecl_stm: (VAR | VAL) varlist SM;
varlist: variable_names Extended data_type | variable_init_value;
variable_names: ID CM variable_names | ID;
variable_init_value: ID CM variable_init_value CM exp | ID Extended data_type ASSIGN exp;

assign_stm: leftassign ASSIGN exp SM;
leftassign: scalarvar | indexed_exp;
scalarvar: ID | exp DOT ID | ID DOT ID | exp6; // check is need $
indexed_exp: exp index_operator | exp;

if_stm: IF LP exp RP blockstatment elseif_stms else_stm;
elseif_stms: elseif_stm elseif_stms | ;
elseif_stm: ELSEIF LP exp RP blockstatment;
else_stm: ELSE blockstatment | ;

forin_stm: FOREACH LP scalarvar IN exp FROMTO exp steploop RP blockstatment;
steploop: BY exp | ;

break_stm: BREAK SM;

continue_stm: CONTINUE SM;

return_stm: RETURN (exp)? SM;

method_invocation_stm: (method_invocate | static_method_invocate) SM;

contructor_declare: CONSTRUCTOR LP paramlist  RP blockstatment;
detructor_declare: DESTRUCTOR LP RP blockstatment;
idname: ID | DOLLARID;
/****************************************************************************/
/*								Expression									*/
/****************************************************************************/
// arith_operator: ADD | SUB | MUL | MOD | DIV;
// boolean_operator: NOT_EQUAL | AND | OR || EQUALDOT;
// string_operator: ADDDOT;
// relation_operator: EQUAL | NOT_EQUAL | LT | GT | LE | GE;
index_operator: LSB exp RSB | LSB exp RSB index_operator;

exp: exp0 (ADDDOT | EQUALDOT) exp0 | exp0;
exp0: exp1 (EQUAL | NOT_EQUAL | GT | LT | GE | LE) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (ADD | SUB) exp3 | exp3;
exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: SUB exp5 | exp6;
exp6: exp6 index_operator | exp7;
exp7: exp7 DOT (ID| func_call) | exp8;
exp8: ID SC static_operand | exp9;
exp9: NEW func_call| exp10;
exp10: literal| TRUE | FALSE | ID | SELF | ID SC DOLLARID | LP exp RP; // check is have self
/****************************************************************************/
/*									Member access							*/
/****************************************************************************/
func_call: ID LP explists RP;
static_operand: DOLLARID | static_func_call;
static_func_call:DOLLARID LP explists RP; 

// att_access: objclass DOT ID;
// objclass: exp | SELF | ID;

// static_att_access: ID SC DOLLARID; // name need only static att

method_invocate: object_exp DOT func_call;
object_exp: ID | exp;


static_method_invocate: ID SC static_func_call;

explists: explist | ;
explist: exp CM explist | exp;
sizearray: (DECIMAL_INTEGER_GT_ZERO| OCT_INTEGER_GT_ZERO| HEX_INTEGER_GT_ZERO| BIN_INTEGER_GT_ZERO) ;
intlit: (DECIMAL_INTEGER| OCT_INTEGER| HEX_INTEGER| BIN_INTEGER | DECIMAL_INTEGER_GT_ZERO| OCT_INTEGER_GT_ZERO| HEX_INTEGER_GT_ZERO| BIN_INTEGER_GT_ZERO);




/******************************************************************************************/
/*								D96 Lexer												  */
/******************************************************************************************/

/****************************************************************************/
/*								2.1 Class declaration						*/
/****************************************************************************/

/****************************************************************************/
/*								3.1 Characters set							*/
/****************************************************************************/

/****************************************************************************/
/*								3.2 Comment									*/
/****************************************************************************/
BLOCK_CMT: '##' (BLOCK_CMT | .)*? '##' -> skip;

/****************************************************************************/
/*								3.4 keyword									*/
/****************************************************************************/
BREAK: 'Break';
FOREACH: 'Foreach';
INT: 'Int';
NULL: 'Null';
CONSTRUCTOR: 'Constructor';
CONTINUE: 'Continue';
TRUE: 'True';
FLOAT: 'Float';
CLASS: 'Class';
DESTRUCTOR: 'Destructor';
IF: 'If';
FALSE: 'False';
BOOLEAN: 'Boolean';
VAL: 'Val';
NEW: 'New';
ELSEIF: 'Elseif';
ARRAY: 'Array';
STRING: 'String';
VAR: 'Var';
BY: 'By';
ELSE: 'Else';
IN: 'In';
RETURN: 'Return';
SELF: 'Self';

/****************************************************************************/
/*								3.5 Operators								*/
/****************************************************************************/
ADD: '+';
NOT: '!';
NOT_EQUAL: '!=';
EQUALDOT: '==.';
SUB: '-';
AND: '&&';
LT: '<';
ADDDOT: '+.';
MUL: '*';
OR: '||';
LE: '<=';
// DOT_OP: DOT; // check istrue?
DIV: '/';
EQUAL: '==';
GT: '>';
SC: '::';
MOD: '%';
ASSIGN: '=';
GE: '>=';
// NEW_OP: NEW;	//check istrue?

/****************************************************************************/
/*								3.6 Seperators								*/
/****************************************************************************/
LSB: '[';
RSB: ']';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SM: ';';
DOT: '.';
CM: ',';
Extended: ':';
FROMTO: '..';

/****************************************************************************/
/*								3.7 Literals								*/
/****************************************************************************/

//INTERGER_GT_ZERO: (DECIMAL_INTEGER_GT_ZERO| OCT_INTEGER_GT_ZERO| HEX_INTEGER_GT_ZERO| BIN_INTEGER_GT_ZERO) { self.text = self.text.replace("_", "") };
DECIMAL_INTEGER_GT_ZERO: NON_ZERO_DIGIT DIGIT* ('_'? DIGIT+)* { self.text = self.text.replace("_", "") };

DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* ('_'? DIGIT+)* { self.text = self.text.replace("_", "") }  
						| '0';

OCT_INTEGER_GT_ZERO: '0' NON_OCT_DIGIT OCT_DIGIT* ('_'? OCT_DIGIT+)* { self.text = self.text.replace("_", "") };

OCT_INTEGER: '0' NON_OCT_DIGIT OCT_DIGIT* ('_'? OCT_DIGIT+)* { self.text = self.text.replace("_", "") }
					| '00';

HEX_INTEGER_GT_ZERO: '0' [xX] NON_HEX_DIGIT HEX_DIGIT* ('_'? HEX_DIGIT+)* { self.text = self.text.replace("_", "") };

HEX_INTEGER: '0' [xX] NON_HEX_DIGIT HEX_DIGIT* ('_'? HEX_DIGIT+)* { self.text = self.text.replace("_", "") }
					|'0' [xX] '0';

BIN_INTEGER_GT_ZERO: '0' [bB] NON_BIN_DIGIT BIN_DIGIT* ('_'? BIN_DIGIT+)* { self.text = self.text.replace("_", "") };

BIN_INTEGER: '0' [bB] NON_BIN_DIGIT BIN_DIGIT* ('_'? BIN_DIGIT+)* { self.text = self.text.replace("_", "") }
					| '0' [bB] '0';

FLOAT_NUMBER: (POINT_FLOAT| EXPONENT_FLOAT) { self.text = self.text.replace("_", "") };

BOOLEAN_LITERAL: TRUE | FALSE; // check is needed Boolean literal

//STRING_LITERAL: '"' ( S_CHAR | S_ESCAPE ) '"' { self.text = self.text[:] };
UNCLOSE_STRING:
	'"' STR_CHAR* {
                raise UncloseString(self.text[1:])
            };
STRING_LITERAL:'"' STR_CHAR* '"' {self.text = self.text[1:-1]};




/****************************************************************************/
/*								4.3 Class types								*/
/****************************************************************************/


/****************************************************************************/
/*								3.7 Literals								*/
/****************************************************************************/

/****************************************************************************/
/*								3.7 Literals								*/
/****************************************************************************/

/****************************************************************************/
/*								3.7 New special character					*/
/****************************************************************************/

/****************************************************************************/
/*								Fragment									*/
/****************************************************************************/
// fragment for interger
fragment NON_ZERO_DIGIT: [1-9];

fragment DIGIT: [0-9];

fragment OCT_DIGIT: [0-7];
fragment NON_OCT_DIGIT: [1-7];

fragment HEX_DIGIT: [0-9A-F];
fragment NON_HEX_DIGIT: [1-9A-F];

fragment BIN_DIGIT: [01];
fragment NON_BIN_DIGIT: '1';

// fragment for float
fragment POINT_FLOAT: INT_PART FRACTION | FRACTION EXPONENT;

/// exponentfloat ::=  (intpart | pointfloat) exponent 
fragment EXPONENT_FLOAT: INT_PART FRACTION?  EXPONENT;

/// intpart       ::=  digit+
fragment INT_PART: DECIMAL_INTEGER ;

/// fraction      ::=  "." digit+
fragment FRACTION: '.' DIGIT*;

/// exponent      ::=  ("e" | "E") ["+" | "-"] digit+
fragment EXPONENT: [eE] [+-]? DIGIT+;

fragment STR_CHAR: '\'"' | ~[\b\t\f\r\n"\\] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr'\\];

/****************************************************************************/
/*								3.3 Identify								*/
/****************************************************************************/
ID: [_a-zA-Z][_a-zA-Z0-9]* ;
DOLLARID: '$' [_a-zA-Z0-9]+;

fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~'"' | '\\';
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
                raise IllegalEscape(self.text[1:])
            };
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};


