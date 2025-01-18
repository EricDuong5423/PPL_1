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
        buf.write("\u00dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3\2\6\2")
        buf.write("\62\n\2\r\2\16\2\63\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3?\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5K\n\5\3\6\3\6\3\6\3\6\3\7\5\7R\n\7\3\7\3\7\3\7\5\7W")
        buf.write("\n\7\3\7\5\7Z\n\7\3\7\5\7]\n\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\5\nk\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\fv\n\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\7\r~\n\r\f\r\16\r\u0081\13\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u0089\n\16\f\16\16\16\u008c\13\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u0094\n\17\f\17\16\17\u0097")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u009f\n\20\f")
        buf.write("\20\16\20\u00a2\13\20\3\21\3\21\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00aa\n\21\f\21\16\21\u00ad\13\21\3\22\3\22\3\22\5")
        buf.write("\22\u00b2\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00be\n\23\7\23\u00c0\n\23\f\23\16\23")
        buf.write("\u00c3\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u00d0\n\24\3\25\3\25\5\25\u00d4\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00db\n\26\3\26\2\b\30")
        buf.write("\32\34\36 $\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*\2\7\3\2\13\16\3\2\34!\3\2\27\30\3\2\31\33\4\2")
        buf.write("\30\30$$\2\u00e3\2\61\3\2\2\2\4>\3\2\2\2\6@\3\2\2\2\b")
        buf.write("J\3\2\2\2\nL\3\2\2\2\f\\\3\2\2\2\16^\3\2\2\2\20`\3\2\2")
        buf.write("\2\22j\3\2\2\2\24l\3\2\2\2\26u\3\2\2\2\30w\3\2\2\2\32")
        buf.write("\u0082\3\2\2\2\34\u008d\3\2\2\2\36\u0098\3\2\2\2 \u00a3")
        buf.write("\3\2\2\2\"\u00b1\3\2\2\2$\u00b3\3\2\2\2&\u00cf\3\2\2\2")
        buf.write("(\u00d3\3\2\2\2*\u00da\3\2\2\2,-\7\17\2\2-.\7\65\2\2.")
        buf.write("/\7%\2\2/\62\5\30\r\2\60\62\7?\2\2\61,\3\2\2\2\61\60\3")
        buf.write("\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\66\7\2\2\3\66\3\3\2\2\2\67?\7\66\2\28?\7;")
        buf.write("\2\29?\7<\2\2:?\7\25\2\2;?\7\26\2\2<?\5\6\4\2=?\5\20\t")
        buf.write("\2>\67\3\2\2\2>8\3\2\2\2>9\3\2\2\2>:\3\2\2\2>;\3\2\2\2")
        buf.write("><\3\2\2\2>=\3\2\2\2?\5\3\2\2\2@A\5\b\5\2AB\5\16\b\2B")
        buf.write("C\7\61\2\2CD\5\f\7\2DE\7\62\2\2E\7\3\2\2\2FG\5\n\6\2G")
        buf.write("H\5\b\5\2HK\3\2\2\2IK\5\n\6\2JF\3\2\2\2JI\3\2\2\2K\t\3")
        buf.write("\2\2\2LM\7\63\2\2MN\7\66\2\2NO\7\64\2\2O\13\3\2\2\2PR")
        buf.write("\7\61\2\2QP\3\2\2\2QR\3\2\2\2RS\3\2\2\2SV\5\4\3\2TU\7")
        buf.write("-\2\2UW\5\f\7\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XZ\7\62\2")
        buf.write("\2YX\3\2\2\2YZ\3\2\2\2Z]\3\2\2\2[]\5\4\3\2\\Q\3\2\2\2")
        buf.write("\\[\3\2\2\2]\r\3\2\2\2^_\t\2\2\2_\17\3\2\2\2`a\7\65\2")
        buf.write("\2ab\7\61\2\2bc\5\22\n\2cd\7\62\2\2d\21\3\2\2\2ef\5\24")
        buf.write("\13\2fg\7-\2\2gh\5\22\n\2hk\3\2\2\2ik\5\24\13\2je\3\2")
        buf.write("\2\2ji\3\2\2\2k\23\3\2\2\2lm\7\65\2\2mn\7,\2\2no\5\4\3")
        buf.write("\2o\25\3\2\2\2pq\5\30\r\2qr\7-\2\2rs\5\26\f\2sv\3\2\2")
        buf.write("\2tv\5\30\r\2up\3\2\2\2ut\3\2\2\2v\27\3\2\2\2wx\b\r\1")
        buf.write("\2xy\5\32\16\2y\177\3\2\2\2z{\f\4\2\2{|\7#\2\2|~\5\32")
        buf.write("\16\2}z\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\31\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083")
        buf.write("\b\16\1\2\u0083\u0084\5\34\17\2\u0084\u008a\3\2\2\2\u0085")
        buf.write("\u0086\f\4\2\2\u0086\u0087\7\"\2\2\u0087\u0089\5\34\17")
        buf.write("\2\u0088\u0085\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\33\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008d\u008e\b\17\1\2\u008e\u008f\5\36\20\2\u008f")
        buf.write("\u0095\3\2\2\2\u0090\u0091\f\4\2\2\u0091\u0092\t\3\2\2")
        buf.write("\u0092\u0094\5\36\20\2\u0093\u0090\3\2\2\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\35\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\b\20\1\2\u0099")
        buf.write("\u009a\5 \21\2\u009a\u00a0\3\2\2\2\u009b\u009c\f\4\2\2")
        buf.write("\u009c\u009d\t\4\2\2\u009d\u009f\5 \21\2\u009e\u009b\3")
        buf.write("\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\37\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4")
        buf.write("\b\21\1\2\u00a4\u00a5\5\"\22\2\u00a5\u00ab\3\2\2\2\u00a6")
        buf.write("\u00a7\f\4\2\2\u00a7\u00a8\t\5\2\2\u00a8\u00aa\5\"\22")
        buf.write("\2\u00a9\u00a6\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac!\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\u00af\t\6\2\2\u00af\u00b2\5$\23\2\u00b0")
        buf.write("\u00b2\5$\23\2\u00b1\u00ae\3\2\2\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2#\3\2\2\2\u00b3\u00b4\b\23\1\2\u00b4\u00b5\5&\24")
        buf.write("\2\u00b5\u00c1\3\2\2\2\u00b6\u00bd\f\4\2\2\u00b7\u00b8")
        buf.write("\7\63\2\2\u00b8\u00b9\5\30\r\2\u00b9\u00ba\7\64\2\2\u00ba")
        buf.write("\u00be\3\2\2\2\u00bb\u00bc\7+\2\2\u00bc\u00be\5\30\r\2")
        buf.write("\u00bd\u00b7\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c0\3")
        buf.write("\2\2\2\u00bf\u00b6\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2%\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c4\u00d0\5\4\3\2\u00c5\u00c6\7/\2\2\u00c6")
        buf.write("\u00c7\5\30\r\2\u00c7\u00c8\7\60\2\2\u00c8\u00d0\3\2\2")
        buf.write("\2\u00c9\u00d0\7\65\2\2\u00ca\u00cb\7\65\2\2\u00cb\u00cc")
        buf.write("\7/\2\2\u00cc\u00cd\5(\25\2\u00cd\u00ce\7\60\2\2\u00ce")
        buf.write("\u00d0\3\2\2\2\u00cf\u00c4\3\2\2\2\u00cf\u00c5\3\2\2\2")
        buf.write("\u00cf\u00c9\3\2\2\2\u00cf\u00ca\3\2\2\2\u00d0\'\3\2\2")
        buf.write("\2\u00d1\u00d4\5*\26\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4)\3\2\2\2\u00d5\u00db")
        buf.write("\5\30\r\2\u00d6\u00d7\5\30\r\2\u00d7\u00d8\7-\2\2\u00d8")
        buf.write("\u00d9\5*\26\2\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2\2")
        buf.write("\u00da\u00d6\3\2\2\2\u00db+\3\2\2\2\27\61\63>JQVY\\ju")
        buf.write("\177\u008a\u0095\u00a0\u00ab\u00b1\u00bd\u00c1\u00cf\u00d3")
        buf.write("\u00da")
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
    RULE_array_literal = 2
    RULE_dim_lit = 3
    RULE_dim = 4
    RULE_list_expression_lit = 5
    RULE_type_array = 6
    RULE_struct_literal = 7
    RULE_list_elements_lit = 8
    RULE_list_element = 9
    RULE_list_expression = 10
    RULE_expression = 11
    RULE_expression1 = 12
    RULE_expression2 = 13
    RULE_expression3 = 14
    RULE_expression4 = 15
    RULE_expression5 = 16
    RULE_expression6 = 17
    RULE_expression7 = 18
    RULE_funcall = 19
    RULE_funcall_noempty = 20

    ruleNames =  [ "program", "literal", "array_literal", "dim_lit", "dim", 
                   "list_expression_lit", "type_array", "struct_literal", 
                   "list_elements_lit", "list_element", "list_expression", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "funcall", "funcall_noempty" ]

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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.CONST]:
                    self.state = 42
                    self.match(MiniGoParser.CONST)
                    self.state = 43
                    self.match(MiniGoParser.ID)
                    self.state = 44
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 45
                    self.expression(0)
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 46
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.CONST or _la==MiniGoParser.NEWLINE):
                    break

            self.state = 51
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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DECIMAL_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(MiniGoParser.DECIMAL_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
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

        def list_expression_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_litContext,0)


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
        self.enterRule(localctx, 4, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.dim_lit()
            self.state = 63
            self.type_array()
            self.state = 64
            self.match(MiniGoParser.LCPAREN)
            self.state = 65
            self.list_expression_lit()
            self.state = 66
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
        self.enterRule(localctx, 6, self.RULE_dim_lit)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.dim()
                self.state = 69
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
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
        self.enterRule(localctx, 8, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MiniGoParser.LSPAREN)
            self.state = 75
            self.match(MiniGoParser.DECIMAL_LIT)
            self.state = 76
            self.match(MiniGoParser.RSPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expression_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_expression_litContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression_lit" ):
                return visitor.visitList_expression_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_expression_lit(self):

        localctx = MiniGoParser.List_expression_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_expression_lit)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LCPAREN:
                    self.state = 78
                    self.match(MiniGoParser.LCPAREN)


                self.state = 81
                self.literal()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 82
                    self.match(MiniGoParser.COMMA)
                    self.state = 83
                    self.list_expression_lit()


                self.state = 87
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 86
                    self.match(MiniGoParser.RCPAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.literal()
                pass


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
        self.enterRule(localctx, 12, self.RULE_type_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
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
        self.enterRule(localctx, 14, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MiniGoParser.ID)
            self.state = 95
            self.match(MiniGoParser.LCPAREN)
            self.state = 96
            self.list_elements_lit()
            self.state = 97
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
        self.enterRule(localctx, 16, self.RULE_list_elements_lit)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.list_element()
                self.state = 100
                self.match(MiniGoParser.COMMA)
                self.state = 101
                self.list_elements_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
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
        self.enterRule(localctx, 18, self.RULE_list_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MiniGoParser.ID)
            self.state = 107
            self.match(MiniGoParser.COLON)
            self.state = 108
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
        self.enterRule(localctx, 20, self.RULE_list_expression)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.expression(0)
                self.state = 111
                self.match(MiniGoParser.COMMA)
                self.state = 112
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 120
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 121
                    self.match(MiniGoParser.OR)
                    self.state = 122
                    self.expression1(0) 
                self.state = 127
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 131
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 132
                    self.match(MiniGoParser.AND)
                    self.state = 133
                    self.expression2(0) 
                self.state = 138
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 142
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 143
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 144
                    self.expression3(0) 
                self.state = 149
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 153
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 154
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 155
                    self.expression4(0) 
                self.state = 160
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 164
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 165
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 166
                    self.expression5() 
                self.state = 171
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
        self.enterRule(localctx, 32, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.expression6(0)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 180
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 187
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSPAREN]:
                        self.state = 181
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 182
                        self.expression(0)
                        self.state = 183
                        self.match(MiniGoParser.RSPAREN)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 185
                        self.match(MiniGoParser.DOT)
                        self.state = 186
                        self.expression(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 193
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
        self.enterRule(localctx, 36, self.RULE_expression7)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(MiniGoParser.LPAREN)
                self.state = 196
                self.expression(0)
                self.state = 197
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.match(MiniGoParser.ID)
                self.state = 201
                self.match(MiniGoParser.LPAREN)
                self.state = 202
                self.funcall()
                self.state = 203
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
        self.enterRule(localctx, 38, self.RULE_funcall)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.DECIMAL_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
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
        self.enterRule(localctx, 40, self.RULE_funcall_noempty)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.expression(0)
                self.state = 213
                self.match(MiniGoParser.COMMA)
                self.state = 214
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
        self._predicates[11] = self.expression_sempred
        self._predicates[12] = self.expression1_sempred
        self._predicates[13] = self.expression2_sempred
        self._predicates[14] = self.expression3_sempred
        self._predicates[15] = self.expression4_sempred
        self._predicates[17] = self.expression6_sempred
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
         




