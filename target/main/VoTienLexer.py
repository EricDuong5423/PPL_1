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
        buf.write("\35\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\6\2\20\n\2\r\2\16\2\21\3\2\3\2\3\3\7\3\27\n\3\f\3\16")
        buf.write("\3\32\13\3\3\3\3\3\2\2\4\3\3\5\4\3\2\6\3\2c|\3\2C\\\3")
        buf.write("\2\62;\5\2\62;C\\c|\2!\2\3\3\2\2\2\2\5\3\2\2\2\3\17\3")
        buf.write("\2\2\2\5\30\3\2\2\2\7\b\t\2\2\2\b\20\b\2\2\2\t\n\t\3\2")
        buf.write("\2\n\20\b\2\3\2\13\f\t\4\2\2\f\20\b\2\4\2\r\16\n\5\2\2")
        buf.write("\16\20\b\2\5\2\17\7\3\2\2\2\17\t\3\2\2\2\17\13\3\2\2\2")
        buf.write("\17\r\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\24\b\2\6\2\24\4\3\2\2\2\25\27\13\2")
        buf.write("\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\b\3\7\2\34\6")
        buf.write("\3\2\2\2\6\2\17\21\30\b\3\2\2\3\2\3\3\2\4\3\2\5\3\2\6")
        buf.write("\3\3\7")
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
            actions[0] = self.ID_action 
            actions[1] = self.ERROR_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            1,
     

        if actionIndex == 1:
            1,
     

        if actionIndex == 2:
            1,
     

        if actionIndex == 3:
            1,
     

        if actionIndex == 4:
            8,
     

    def ERROR_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


