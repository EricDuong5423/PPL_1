# Generated from /home/don/Code/Course/PPL/Template_BTL_PPL/main/VoTien.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,12,78,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,5,7,48,8,7,10,7,12,7,51,9,7,1,8,4,8,54,8,8,11,8,12,8,55,
        1,9,1,9,1,9,1,9,5,9,62,8,9,10,9,12,9,65,9,9,1,9,1,9,1,10,4,10,70,
        8,10,11,10,12,10,71,1,10,1,10,1,11,1,11,1,11,0,0,12,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,5,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,1,0,10,10,3,0,8,
        10,12,13,32,32,81,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,29,1,0,0,
        0,5,31,1,0,0,0,7,33,1,0,0,0,9,39,1,0,0,0,11,41,1,0,0,0,13,43,1,0,
        0,0,15,45,1,0,0,0,17,53,1,0,0,0,19,57,1,0,0,0,21,69,1,0,0,0,23,75,
        1,0,0,0,25,26,5,105,0,0,26,27,5,110,0,0,27,28,5,116,0,0,28,2,1,0,
        0,0,29,30,5,43,0,0,30,4,1,0,0,0,31,32,5,61,0,0,32,6,1,0,0,0,33,34,
        5,112,0,0,34,35,5,114,0,0,35,36,5,105,0,0,36,37,5,110,0,0,37,38,
        5,116,0,0,38,8,1,0,0,0,39,40,5,40,0,0,40,10,1,0,0,0,41,42,5,41,0,
        0,42,12,1,0,0,0,43,44,5,59,0,0,44,14,1,0,0,0,45,49,7,0,0,0,46,48,
        7,1,0,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,
        50,16,1,0,0,0,51,49,1,0,0,0,52,54,7,2,0,0,53,52,1,0,0,0,54,55,1,
        0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,18,1,0,0,0,57,58,5,35,0,0,58,
        59,5,35,0,0,59,63,1,0,0,0,60,62,8,3,0,0,61,60,1,0,0,0,62,65,1,0,
        0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,
        6,9,0,0,67,20,1,0,0,0,68,70,7,4,0,0,69,68,1,0,0,0,70,71,1,0,0,0,
        71,69,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,6,10,0,0,74,22,1,
        0,0,0,75,76,9,0,0,0,76,77,6,11,1,0,77,24,1,0,0,0,5,0,49,55,63,71,
        2,6,0,0,1,11,0
    ]

class VoTienLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    ADD = 2
    ASSIGNI = 3
    PRINT = 4
    LP = 5
    RP = 6
    COMCOMMA = 7
    ID = 8
    INT_LIT = 9
    COMMENTS = 10
    WS = 11
    ERROR_CHAR = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'+'", "'='", "'print'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ADD", "ASSIGNI", "PRINT", "LP", "RP", "COMCOMMA", "ID", 
            "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INT", "ADD", "ASSIGNI", "PRINT", "LP", "RP", "COMCOMMA", 
                  "ID", "INT_LIT", "COMMENTS", "WS", "ERROR_CHAR" ]

    grammarFileName = "VoTien.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


