grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and


// TODO Identifiers
ID: '<div' ( ' ' | '\t' )* ( ('class' | 'id' | 'style') '=' '"' ~["]+ '"' )* '>' ( (~[<]+ | '<div' ( ' ' | '\t' )* ( ('class' | 'id' | 'style') '=' '"' ~["]+ '"' )* '>' .*? '</div>'? )* '</div>'? )+;

// TODO ERROR
ERROR_STRING: (.)* {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //