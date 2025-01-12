grammar VoTien;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

//! -------------------------- Lexical structure ----------------------- // TODO KeyWord and


// TODO Identifiers
ID: (([a-z]{1,})|([A-Z]{1,})|([0-9]{1,})|(~[a-zA-Z0-9]{1,}))+{8,};
// TODO ERROR
ERROR_STRING: (.)* {raise ErrorToken(self.text)};

//!  -------------------------- end Lexical structure ------------------- //

// //! --------------------------  parser structure ----------------------- //

// declared
program: (ID | ERROR_STRING*) EOF;


// //! -------------------------- end  parser structure ----------------------- //