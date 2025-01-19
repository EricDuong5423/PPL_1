# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u00ee\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\3\2\6\28\n\2\r\2\16\29\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3E\n\3\3\4\3\4\5\4I\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5P\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7\\\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\tg\n\t\3\n\3\n\3\n\3\n\3\n\5\nn\n\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r|\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u0087\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u008f\n\20\f\20")
        buf.write("\16\20\u0092\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21")
        buf.write("\u009a\n\21\f\21\16\21\u009d\13\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00a5\n\22\f\22\16\22\u00a8\13\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\7\23\u00b0\n\23\f\23\16\23\u00b3")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00bb\n\24\f")
        buf.write("\24\16\24\u00be\13\24\3\25\3\25\3\25\5\25\u00c3\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00cf\n\26\7\26\u00d1\n\26\f\26\16\26\u00d4\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00e1\n\27\3\30\3\30\5\30\u00e5\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u00ec\n\31\3\31\2\b\36 \"$&*\32\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\7\3\2\13")
        buf.write("\16\3\2\34!\3\2\27\30\3\2\31\33\4\2\30\30$$\2\u00f1\2")
        buf.write("\67\3\2\2\2\4D\3\2\2\2\6H\3\2\2\2\bO\3\2\2\2\nQ\3\2\2")
        buf.write("\2\f[\3\2\2\2\16]\3\2\2\2\20f\3\2\2\2\22m\3\2\2\2\24o")
        buf.write("\3\2\2\2\26q\3\2\2\2\30{\3\2\2\2\32}\3\2\2\2\34\u0086")
        buf.write("\3\2\2\2\36\u0088\3\2\2\2 \u0093\3\2\2\2\"\u009e\3\2\2")
        buf.write("\2$\u00a9\3\2\2\2&\u00b4\3\2\2\2(\u00c2\3\2\2\2*\u00c4")
        buf.write("\3\2\2\2,\u00e0\3\2\2\2.\u00e4\3\2\2\2\60\u00eb\3\2\2")
        buf.write("\2\62\63\7\17\2\2\63\64\7\65\2\2\64\65\7%\2\2\658\5\36")
        buf.write("\20\2\668\7?\2\2\67\62\3\2\2\2\67\66\3\2\2\289\3\2\2\2")
        buf.write("9\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\2\2\3<\3\3\2\2\2")
        buf.write("=E\7\66\2\2>E\7;\2\2?E\7<\2\2@E\7\25\2\2AE\7\26\2\2BE")
        buf.write("\5\n\6\2CE\5\26\f\2D=\3\2\2\2D>\3\2\2\2D?\3\2\2\2D@\3")
        buf.write("\2\2\2DA\3\2\2\2DB\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FI\5\b")
        buf.write("\5\2GI\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\5\4\3")
        buf.write("\2KL\7-\2\2LM\5\6\4\2MP\3\2\2\2NP\5\4\3\2OJ\3\2\2\2ON")
        buf.write("\3\2\2\2P\t\3\2\2\2QR\5\f\7\2RS\5\24\13\2ST\7\61\2\2T")
        buf.write("U\5\20\t\2UV\7\62\2\2V\13\3\2\2\2WX\5\16\b\2XY\5\f\7\2")
        buf.write("Y\\\3\2\2\2Z\\\5\16\b\2[W\3\2\2\2[Z\3\2\2\2\\\r\3\2\2")
        buf.write("\2]^\7\63\2\2^_\7\66\2\2_`\7\64\2\2`\17\3\2\2\2ab\5\22")
        buf.write("\n\2bc\7-\2\2cd\5\20\t\2dg\3\2\2\2eg\5\22\n\2fa\3\2\2")
        buf.write("\2fe\3\2\2\2g\21\3\2\2\2hn\5\4\3\2ij\7\61\2\2jk\5\6\4")
        buf.write("\2kl\7\62\2\2ln\3\2\2\2mh\3\2\2\2mi\3\2\2\2n\23\3\2\2")
        buf.write("\2op\t\2\2\2p\25\3\2\2\2qr\7\65\2\2rs\7\61\2\2st\5\30")
        buf.write("\r\2tu\7\62\2\2u\27\3\2\2\2vw\5\32\16\2wx\7-\2\2xy\5\30")
        buf.write("\r\2y|\3\2\2\2z|\5\32\16\2{v\3\2\2\2{z\3\2\2\2|\31\3\2")
        buf.write("\2\2}~\7\65\2\2~\177\7,\2\2\177\u0080\5\4\3\2\u0080\33")
        buf.write("\3\2\2\2\u0081\u0082\5\36\20\2\u0082\u0083\7-\2\2\u0083")
        buf.write("\u0084\5\34\17\2\u0084\u0087\3\2\2\2\u0085\u0087\5\36")
        buf.write("\20\2\u0086\u0081\3\2\2\2\u0086\u0085\3\2\2\2\u0087\35")
        buf.write("\3\2\2\2\u0088\u0089\b\20\1\2\u0089\u008a\5 \21\2\u008a")
        buf.write("\u0090\3\2\2\2\u008b\u008c\f\4\2\2\u008c\u008d\7#\2\2")
        buf.write("\u008d\u008f\5 \21\2\u008e\u008b\3\2\2\2\u008f\u0092\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\37")
        buf.write("\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\b\21\1\2\u0094")
        buf.write("\u0095\5\"\22\2\u0095\u009b\3\2\2\2\u0096\u0097\f\4\2")
        buf.write("\2\u0097\u0098\7\"\2\2\u0098\u009a\5\"\22\2\u0099\u0096")
        buf.write("\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c!\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u009f\b\22\1\2\u009f\u00a0\5$\23\2\u00a0\u00a6\3\2\2")
        buf.write("\2\u00a1\u00a2\f\4\2\2\u00a2\u00a3\t\3\2\2\u00a3\u00a5")
        buf.write("\5$\23\2\u00a4\u00a1\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7#\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a9\u00aa\b\23\1\2\u00aa\u00ab\5&\24")
        buf.write("\2\u00ab\u00b1\3\2\2\2\u00ac\u00ad\f\4\2\2\u00ad\u00ae")
        buf.write("\t\4\2\2\u00ae\u00b0\5&\24\2\u00af\u00ac\3\2\2\2\u00b0")
        buf.write("\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2%\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\b\24\1")
        buf.write("\2\u00b5\u00b6\5(\25\2\u00b6\u00bc\3\2\2\2\u00b7\u00b8")
        buf.write("\f\4\2\2\u00b8\u00b9\t\5\2\2\u00b9\u00bb\5(\25\2\u00ba")
        buf.write("\u00b7\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\'\3\2\2\2\u00be\u00bc\3\2\2")
        buf.write("\2\u00bf\u00c0\t\6\2\2\u00c0\u00c3\5*\26\2\u00c1\u00c3")
        buf.write("\5*\26\2\u00c2\u00bf\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write(")\3\2\2\2\u00c4\u00c5\b\26\1\2\u00c5\u00c6\5,\27\2\u00c6")
        buf.write("\u00d2\3\2\2\2\u00c7\u00ce\f\4\2\2\u00c8\u00c9\7\63\2")
        buf.write("\2\u00c9\u00ca\5\36\20\2\u00ca\u00cb\7\64\2\2\u00cb\u00cf")
        buf.write("\3\2\2\2\u00cc\u00cd\7+\2\2\u00cd\u00cf\5\36\20\2\u00ce")
        buf.write("\u00c8\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\3\2\2\2")
        buf.write("\u00d0\u00c7\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3+\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d5\u00e1\5\4\3\2\u00d6\u00d7\7/\2\2\u00d7")
        buf.write("\u00d8\5\36\20\2\u00d8\u00d9\7\60\2\2\u00d9\u00e1\3\2")
        buf.write("\2\2\u00da\u00e1\7\65\2\2\u00db\u00dc\7\65\2\2\u00dc\u00dd")
        buf.write("\7/\2\2\u00dd\u00de\5.\30\2\u00de\u00df\7\60\2\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00d5\3\2\2\2\u00e0\u00d6\3\2\2\2")
        buf.write("\u00e0\u00da\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1-\3\2\2")
        buf.write("\2\u00e2\u00e5\5\60\31\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5/\3\2\2\2\u00e6\u00ec")
        buf.write("\5\36\20\2\u00e7\u00e8\5\36\20\2\u00e8\u00e9\7-\2\2\u00e9")
        buf.write("\u00ea\5\60\31\2\u00ea\u00ec\3\2\2\2\u00eb\u00e6\3\2\2")
        buf.write("\2\u00eb\u00e7\3\2\2\2\u00ec\61\3\2\2\2\27\679DHO[fm{")
        buf.write("\u0086\u0090\u009b\u00a6\u00b1\u00bc\u00c2\u00ce\u00d2")
        buf.write("\u00e0\u00e4\u00eb")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                      "COMMA", "COCOM", "LPAREN", "RPAREN", "LCPAREN", "RCPAREN", 
                      "LSPAREN", "RSPAREN", "ID", "DECIMAL_LIT", "BIN_LIT", 
                      "OCT_LIT", "HEX_LIT", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BOOL_LIT", "NIL_LIT", "NEWLINE", "WS", "COMMENT_LINE", 
                      "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_list_literal = 2
    RULE_list_literal_noempty = 3
    RULE_array_literal = 4
    RULE_dim_lit = 5
    RULE_dim = 6
    RULE_list_array_element = 7
    RULE_array_element = 8
    RULE_type_array = 9
    RULE_struct_literal = 10
    RULE_list_elements_lit = 11
    RULE_list_element = 12
    RULE_list_expression = 13
    RULE_expression = 14
    RULE_expression1 = 15
    RULE_expression2 = 16
    RULE_expression3 = 17
    RULE_expression4 = 18
    RULE_expression5 = 19
    RULE_expression6 = 20
    RULE_expression7 = 21
    RULE_funcall = 22
    RULE_funcall_noempty = 23

    ruleNames =  [ "program", "literal", "list_literal", "list_literal_noempty", 
                   "array_literal", "dim_lit", "dim", "list_array_element", 
                   "array_element", "type_array", "struct_literal", "list_elements_lit", 
                   "list_element", "list_expression", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "funcall", "funcall_noempty" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NEQUAL=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    DOT=41
    COLON=42
    COMMA=43
    COCOM=44
    LPAREN=45
    RPAREN=46
    LCPAREN=47
    RCPAREN=48
    LSPAREN=49
    RSPAREN=50
    ID=51
    DECIMAL_LIT=52
    BIN_LIT=53
    OCT_LIT=54
    HEX_LIT=55
    INT_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    BOOL_LIT=59
    NIL_LIT=60
    NEWLINE=61
    WS=62
    COMMENT_LINE=63
    COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

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
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CONST)
            else:
                return self.getToken(MiniGoParser.CONST, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ASSIGN)
            else:
                return self.getToken(MiniGoParser.ASSIGN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.CONST]:
                    self.state = 48
                    self.match(MiniGoParser.CONST)
                    self.state = 49
                    self.match(MiniGoParser.ID)
                    self.state = 50
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 51
                    self.expression(0)
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 52
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.CONST or _la==MiniGoParser.NEWLINE):
                    break

            self.state = 57
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(MiniGoParser.DECIMAL_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = MiniGoParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_literal)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.list_literal_noempty()
                pass
            elif token in [MiniGoParser.RCPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_noemptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_noempty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_noempty" ):
                return visitor.visitList_literal_noempty(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_noempty(self):

        localctx = MiniGoParser.List_literal_noemptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_literal_noempty)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.literal()
                self.state = 73
                self.match(MiniGoParser.COMMA)
                self.state = 74
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def type_array(self):
            return self.getTypedRuleContext(MiniGoParser.Type_arrayContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.dim_lit()
            self.state = 80
            self.type_array()
            self.state = 81
            self.match(MiniGoParser.LCPAREN)
            self.state = 82
            self.list_array_element()
            self.state = 83
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dim_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_lit" ):
                return visitor.visitDim_lit(self)
            else:
                return visitor.visitChildren(self)




    def dim_lit(self):

        localctx = MiniGoParser.Dim_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dim_lit)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.dim()
                self.state = 86
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def DECIMAL_LIT(self):
            return self.getToken(MiniGoParser.DECIMAL_LIT, 0)

        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MiniGoParser.LSPAREN)
            self.state = 92
            self.match(MiniGoParser.DECIMAL_LIT)
            self.state = 93
            self.match(MiniGoParser.RSPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_element" ):
                return visitor.visitList_array_element(self)
            else:
                return visitor.visitChildren(self)




    def list_array_element(self):

        localctx = MiniGoParser.List_array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_array_element)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.array_element()
                self.state = 96
                self.match(MiniGoParser.COMMA)
                self.state = 97
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_literal(self):
            return self.getTypedRuleContext(MiniGoParser.List_literalContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_element)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.literal()
                pass
            elif token in [MiniGoParser.LCPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(MiniGoParser.LCPAREN)
                self.state = 104
                self.list_literal()
                self.state = 105
                self.match(MiniGoParser.RCPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_array" ):
                return visitor.visitType_array(self)
            else:
                return visitor.visitChildren(self)




    def type_array(self):

        localctx = MiniGoParser.Type_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_elements_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_elements_litContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MiniGoParser.ID)
            self.state = 112
            self.match(MiniGoParser.LCPAREN)
            self.state = 113
            self.list_elements_lit()
            self.state = 114
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elements_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elements_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_elements_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements_lit" ):
                return visitor.visitList_elements_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_elements_lit(self):

        localctx = MiniGoParser.List_elements_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_elements_lit)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.list_element()
                self.state = 117
                self.match(MiniGoParser.COMMA)
                self.state = 118
                self.list_elements_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.list_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_element" ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = MiniGoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniGoParser.ID)
            self.state = 124
            self.match(MiniGoParser.COLON)
            self.state = 125
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expression)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(MiniGoParser.COMMA)
                self.state = 129
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 137
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 138
                    self.match(MiniGoParser.OR)
                    self.state = 139
                    self.expression1(0) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 148
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 149
                    self.match(MiniGoParser.AND)
                    self.state = 150
                    self.expression2(0) 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(MiniGoParser.NEQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 159
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 160
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 161
                    self.expression3(0) 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 172
                    self.expression4(0) 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.expression5() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self.expression6(0)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSPAREN]:
                        self.state = 198
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 199
                        self.expression(0)
                        self.state = 200
                        self.match(MiniGoParser.RSPAREN)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 202
                        self.match(MiniGoParser.DOT)
                        self.state = 203
                        self.expression(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression7)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MiniGoParser.LPAREN)
                self.state = 213
                self.expression(0)
                self.state = 214
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.match(MiniGoParser.ID)
                self.state = 218
                self.match(MiniGoParser.LPAREN)
                self.state = 219
                self.funcall()
                self.state = 220
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Funcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MiniGoParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcall)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.funcall_noempty()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcall_noemptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Funcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall_noempty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall_noempty" ):
                return visitor.visitFuncall_noempty(self)
            else:
                return visitor.visitChildren(self)




    def funcall_noempty(self):

        localctx = MiniGoParser.Funcall_noemptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcall_noempty)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.expression(0)
                self.state = 230
                self.match(MiniGoParser.COMMA)
                self.state = 231
                self.funcall_noempty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        self._predicates[15] = self.expression1_sempred
        self._predicates[16] = self.expression2_sempred
        self._predicates[17] = self.expression3_sempred
        self._predicates[18] = self.expression4_sempred
        self._predicates[20] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




