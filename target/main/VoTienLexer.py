# Generated from main/VoTien.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\3\2\5\2\t\n\2\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\5\2\27\n\2")
        buf.write("\3\2\3\2\5\2\33\n\2\3\2\6\2\36\n\2\r\2\16\2\37\5\2\"\n")
        buf.write("\2\3\2\3\2\6\2&\n\2\r\2\16\2\'\3\2\3\2\5\2,\n\2\3\2\6")
        buf.write("\2/\n\2\r\2\16\2\60\5\2\63\n\2\5\2\65\n\2\3\2\5\28\n\2")
        buf.write("\3\3\7\3;\n\3\f\3\16\3>\13\3\3\3\3\3\2\2\4\3\3\5\4\3\2")
        buf.write("\5\4\2--//\3\2\62;\4\2GGgg\2N\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\3\64\3\2\2\2\5<\3\2\2\2\7\t\t\2\2\2\b\7\3\2\2\2\b\t\3")
        buf.write("\2\2\2\t\13\3\2\2\2\n\f\t\3\2\2\13\n\3\2\2\2\f\r\3\2\2")
        buf.write("\2\r\13\3\2\2\2\r\16\3\2\2\2\16\26\3\2\2\2\17\23\7\60")
        buf.write("\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3")
        buf.write("\2\2\2\23\24\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\26\17")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27!\3\2\2\2\30\32\t\4\2\2\31\33")
        buf.write("\t\2\2\2\32\31\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34")
        buf.write("\36\t\3\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2")
        buf.write("\37 \3\2\2\2 \"\3\2\2\2!\30\3\2\2\2!\"\3\2\2\2\"\65\3")
        buf.write("\2\2\2#%\7\60\2\2$&\t\3\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3")
        buf.write("\2\2\2\'(\3\2\2\2(\62\3\2\2\2)+\t\4\2\2*,\t\2\2\2+*\3")
        buf.write("\2\2\2+,\3\2\2\2,.\3\2\2\2-/\t\3\2\2.-\3\2\2\2/\60\3\2")
        buf.write("\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62)\3\2\2")
        buf.write("\2\62\63\3\2\2\2\63\65\3\2\2\2\64\b\3\2\2\2\64#\3\2\2")
        buf.write("\2\65\67\3\2\2\2\668\7n\2\2\67\66\3\2\2\2\678\3\2\2\2")
        buf.write("8\4\3\2\2\29;\13\2\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<")
        buf.write("=\3\2\2\2=?\3\2\2\2><\3\2\2\2?@\b\3\2\2@\6\3\2\2\2\21")
        buf.write("\2\b\r\23\26\32\37!\'+\60\62\64\67<\3\3\3\2")
        return buf.getvalue()


class VoTienLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    ERROR_STRING = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "ERROR_STRING" ]

    ruleNames = [ "ID", "ERROR_STRING" ]

    grammarFileName = "VoTien.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.ERROR_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


