# Generated from main/VoTien.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\20\4\2\t\2\3\2\3\2\7\2\7\n\2\f\2\16\2\n\13\2\5\2\f\n")
        buf.write("\2\3\2\3\2\3\2\2\2\3\2\2\2\2\20\2\13\3\2\2\2\4\f\7\3\2")
        buf.write("\2\5\7\7\4\2\2\6\5\3\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t")
        buf.write("\3\2\2\2\t\f\3\2\2\2\n\b\3\2\2\2\13\4\3\2\2\2\13\b\3\2")
        buf.write("\2\2\f\r\3\2\2\2\r\16\7\2\2\3\16\3\3\2\2\2\4\b\13")
        return buf.getvalue()


class VoTienParser ( Parser ):

    grammarFileName = "VoTien.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "ID", "ERROR_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    ERROR_STRING=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VoTienParser.EOF, 0)

        def ID(self):
            return self.getToken(VoTienParser.ID, 0)

        def ERROR_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(VoTienParser.ERROR_STRING)
            else:
                return self.getToken(VoTienParser.ERROR_STRING, i)

        def getRuleIndex(self):
            return VoTienParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = VoTienParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VoTienParser.ID]:
                self.state = 2
                self.match(VoTienParser.ID)
                pass
            elif token in [VoTienParser.EOF, VoTienParser.ERROR_STRING]:
                self.state = 6
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VoTienParser.ERROR_STRING:
                    self.state = 3
                    self.match(VoTienParser.ERROR_STRING)
                    self.state = 8
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 11
            self.match(VoTienParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





