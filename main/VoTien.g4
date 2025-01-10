grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and


// TODO Identifiers
ID: (('+'|'-')?[0-9]+('.'[0-9]*)?([eE]('+'|'-')?[0-9]+)?   |   '.'[0-9]+([eE]('+'|'-')?[0-9]+)?)'l'?;

// TODO ERROR
ERROR_STRING: (.)* {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //