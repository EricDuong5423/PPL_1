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
        buf.write("\u0276\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\6\2\u0080\n\2\r\2\16\2\u0081")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\u0091\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u009d\n\4\3\5\3\5\3\5\3\5\3\5\5\5\u00a4\n\5\3\6\3\6")
        buf.write("\5\6\u00a8\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00af\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\b\u00b7\n\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00c2\n\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00d2\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00dd\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00e4\n\21\3")
        buf.write("\22\3\22\3\22\5\22\u00e9\n\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00f2\n\23\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00fd\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u0105\n\26\f\26\16\26\u0108\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u0110\n\27\f\27\16\27\u0113")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u011b\n\30\f")
        buf.write("\30\16\30\u011e\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0126\n\31\f\31\16\31\u0129\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u0131\n\32\f\32\16\32\u0134\13\32\3")
        buf.write("\33\3\33\3\33\5\33\u0139\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u014a\n\34\5\34\u014c\n\34\7\34\u014e\n\34\f\34\16\34")
        buf.write("\u0151\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u015e\n\35\3\36\3\36\5\36\u0162\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u0169\n\37\3 \3 \3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\5!\u0175\n!\3!\3!\5!\u0179\n!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\5\"\u0181\n\"\3\"\3\"\5\"\u0185\n\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0191\n#\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\5%\u019a\n%\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u01a4\n&\3&\3&\5&\u01a8\n&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u01c5\n)\3*\3*\3*\3*\5*\u01cb\n*\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01e0")
        buf.write("\n.\7.\u01e2\n.\f.\16.\u01e5\13.\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u01f7\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u0201\n\61\3\61\5\61\u0204\n\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\5\62\u020b\n\62\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u021e\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3")
        buf.write("\65\3\66\3\66\3\66\3\66\5\66\u022c\n\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\39\59\u023d")
        buf.write("\n9\39\39\39\39\59\u0243\n9\39\39\39\3:\3:\3:\5:\u024b")
        buf.write("\n:\3:\3:\3;\3;\3;\3;\3<\3<\5<\u0255\n<\3=\3=\3=\3=\3")
        buf.write("=\5=\u025c\n=\3>\3>\3>\5>\u0261\n>\3>\3>\5>\u0265\n>\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u0274\n?\3?\2")
        buf.write("\t*,.\60\62\66Z@\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|\2\b\4\2\13\16\66\66\3\2\34!\3\2\27\30\3\2\31\33\4")
        buf.write("\2\30\30$$\4\2&*//\2\u0290\2\177\3\2\2\2\4\u0090\3\2\2")
        buf.write("\2\6\u009c\3\2\2\2\b\u00a3\3\2\2\2\n\u00a7\3\2\2\2\f\u00ae")
        buf.write("\3\2\2\2\16\u00b6\3\2\2\2\20\u00b8\3\2\2\2\22\u00ba\3")
        buf.write("\2\2\2\24\u00c1\3\2\2\2\26\u00c3\3\2\2\2\30\u00c7\3\2")
        buf.write("\2\2\32\u00d1\3\2\2\2\34\u00d3\3\2\2\2\36\u00dc\3\2\2")
        buf.write("\2 \u00e3\3\2\2\2\"\u00e5\3\2\2\2$\u00f1\3\2\2\2&\u00f3")
        buf.write("\3\2\2\2(\u00fc\3\2\2\2*\u00fe\3\2\2\2,\u0109\3\2\2\2")
        buf.write(".\u0114\3\2\2\2\60\u011f\3\2\2\2\62\u012a\3\2\2\2\64\u0138")
        buf.write("\3\2\2\2\66\u013a\3\2\2\28\u015d\3\2\2\2:\u0161\3\2\2")
        buf.write("\2<\u0168\3\2\2\2>\u016a\3\2\2\2@\u0170\3\2\2\2B\u017c")
        buf.write("\3\2\2\2D\u0190\3\2\2\2F\u0192\3\2\2\2H\u0199\3\2\2\2")
        buf.write("J\u019b\3\2\2\2L\u01ae\3\2\2\2N\u01b6\3\2\2\2P\u01c4\3")
        buf.write("\2\2\2R\u01ca\3\2\2\2T\u01cc\3\2\2\2V\u01ce\3\2\2\2X\u01d3")
        buf.write("\3\2\2\2Z\u01d5\3\2\2\2\\\u01e6\3\2\2\2^\u01f6\3\2\2\2")
        buf.write("`\u01f8\3\2\2\2b\u0207\3\2\2\2d\u0210\3\2\2\2f\u021d\3")
        buf.write("\2\2\2h\u0225\3\2\2\2j\u0227\3\2\2\2l\u0232\3\2\2\2n\u0235")
        buf.write("\3\2\2\2p\u023c\3\2\2\2r\u0247\3\2\2\2t\u024e\3\2\2\2")
        buf.write("v\u0252\3\2\2\2x\u025b\3\2\2\2z\u025d\3\2\2\2|\u0273\3")
        buf.write("\2\2\2~\u0080\5P)\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0084\7\2\2\3\u0084\3\3\2\2\2\u0085\u0091\7\67\2\2\u0086")
        buf.write("\u0091\78\2\2\u0087\u0091\79\2\2\u0088\u0091\7:\2\2\u0089")
        buf.write("\u0091\7;\2\2\u008a\u0091\7<\2\2\u008b\u0091\7\25\2\2")
        buf.write("\u008c\u0091\7\26\2\2\u008d\u0091\7\24\2\2\u008e\u0091")
        buf.write("\5\30\r\2\u008f\u0091\5\"\22\2\u0090\u0085\3\2\2\2\u0090")
        buf.write("\u0086\3\2\2\2\u0090\u0087\3\2\2\2\u0090\u0088\3\2\2\2")
        buf.write("\u0090\u0089\3\2\2\2\u0090\u008a\3\2\2\2\u0090\u008b\3")
        buf.write("\2\2\2\u0090\u008c\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u008f\3\2\2\2\u0091\5\3\2\2\2\u0092\u009d")
        buf.write("\7\67\2\2\u0093\u009d\78\2\2\u0094\u009d\79\2\2\u0095")
        buf.write("\u009d\7:\2\2\u0096\u009d\7;\2\2\u0097\u009d\7<\2\2\u0098")
        buf.write("\u009d\7\25\2\2\u0099\u009d\7\26\2\2\u009a\u009d\7\24")
        buf.write("\2\2\u009b\u009d\5\"\22\2\u009c\u0092\3\2\2\2\u009c\u0093")
        buf.write("\3\2\2\2\u009c\u0094\3\2\2\2\u009c\u0095\3\2\2\2\u009c")
        buf.write("\u0096\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2")
        buf.write("\u009c\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3")
        buf.write("\2\2\2\u009d\7\3\2\2\2\u009e\u009f\5\6\4\2\u009f\u00a0")
        buf.write("\7-\2\2\u00a0\u00a1\5\b\5\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a4\5\6\4\2\u00a3\u009e\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\t\3\2\2\2\u00a5\u00a8\5\f\7\2\u00a6\u00a8\3\2\2")
        buf.write("\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\13\3")
        buf.write("\2\2\2\u00a9\u00aa\5\4\3\2\u00aa\u00ab\7-\2\2\u00ab\u00ac")
        buf.write("\5\n\6\2\u00ac\u00af\3\2\2\2\u00ad\u00af\5\4\3\2\u00ae")
        buf.write("\u00a9\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\r\3\2\2\2\u00b0")
        buf.write("\u00b7\7\f\2\2\u00b1\u00b7\7\r\2\2\u00b2\u00b7\7\16\2")
        buf.write("\2\u00b3\u00b7\7\13\2\2\u00b4\u00b7\5\22\n\2\u00b5\u00b7")
        buf.write("\7\66\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b7\17\3\2\2\2\u00b8\u00b9\t\2")
        buf.write("\2\2\u00b9\21\3\2\2\2\u00ba\u00bb\5\24\13\2\u00bb\u00bc")
        buf.write("\5\20\t\2\u00bc\23\3\2\2\2\u00bd\u00be\5\26\f\2\u00be")
        buf.write("\u00bf\5\24\13\2\u00bf\u00c2\3\2\2\2\u00c0\u00c2\5\26")
        buf.write("\f\2\u00c1\u00bd\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\25")
        buf.write("\3\2\2\2\u00c3\u00c4\7\64\2\2\u00c4\u00c5\7\67\2\2\u00c5")
        buf.write("\u00c6\7\65\2\2\u00c6\27\3\2\2\2\u00c7\u00c8\5\32\16\2")
        buf.write("\u00c8\u00c9\5\16\b\2\u00c9\u00ca\7\62\2\2\u00ca\u00cb")
        buf.write("\5\36\20\2\u00cb\u00cc\7\63\2\2\u00cc\31\3\2\2\2\u00cd")
        buf.write("\u00ce\5\34\17\2\u00ce\u00cf\5\32\16\2\u00cf\u00d2\3\2")
        buf.write("\2\2\u00d0\u00d2\5\34\17\2\u00d1\u00cd\3\2\2\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d2\33\3\2\2\2\u00d3\u00d4\7\64\2\2\u00d4\u00d5")
        buf.write("\7\67\2\2\u00d5\u00d6\7\65\2\2\u00d6\35\3\2\2\2\u00d7")
        buf.write("\u00d8\5 \21\2\u00d8\u00d9\7-\2\2\u00d9\u00da\5\36\20")
        buf.write("\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5 \21\2\u00dc\u00d7")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\37\3\2\2\2\u00de\u00e4")
        buf.write("\5\b\5\2\u00df\u00e0\7\62\2\2\u00e0\u00e1\5 \21\2\u00e1")
        buf.write("\u00e2\7\63\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00de\3\2\2")
        buf.write("\2\u00e3\u00df\3\2\2\2\u00e4!\3\2\2\2\u00e5\u00e6\7\66")
        buf.write("\2\2\u00e6\u00e8\7\62\2\2\u00e7\u00e9\5$\23\2\u00e8\u00e7")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00eb\7\63\2\2\u00eb#\3\2\2\2\u00ec\u00ed\5&\24\2\u00ed")
        buf.write("\u00ee\7-\2\2\u00ee\u00ef\5$\23\2\u00ef\u00f2\3\2\2\2")
        buf.write("\u00f0\u00f2\5&\24\2\u00f1\u00ec\3\2\2\2\u00f1\u00f0\3")
        buf.write("\2\2\2\u00f2%\3\2\2\2\u00f3\u00f4\7\66\2\2\u00f4\u00f5")
        buf.write("\7,\2\2\u00f5\u00f6\5*\26\2\u00f6\'\3\2\2\2\u00f7\u00f8")
        buf.write("\5*\26\2\u00f8\u00f9\7-\2\2\u00f9\u00fa\5(\25\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00fd\5*\26\2\u00fc\u00f7\3\2\2\2")
        buf.write("\u00fc\u00fb\3\2\2\2\u00fd)\3\2\2\2\u00fe\u00ff\b\26\1")
        buf.write("\2\u00ff\u0100\5,\27\2\u0100\u0106\3\2\2\2\u0101\u0102")
        buf.write("\f\4\2\2\u0102\u0103\7#\2\2\u0103\u0105\5,\27\2\u0104")
        buf.write("\u0101\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107+\3\2\2\2\u0108\u0106\3\2\2")
        buf.write("\2\u0109\u010a\b\27\1\2\u010a\u010b\5.\30\2\u010b\u0111")
        buf.write("\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e\7\"\2\2\u010e")
        buf.write("\u0110\5.\30\2\u010f\u010c\3\2\2\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112-\3\2\2")
        buf.write("\2\u0113\u0111\3\2\2\2\u0114\u0115\b\30\1\2\u0115\u0116")
        buf.write("\5\60\31\2\u0116\u011c\3\2\2\2\u0117\u0118\f\4\2\2\u0118")
        buf.write("\u0119\t\3\2\2\u0119\u011b\5\60\31\2\u011a\u0117\3\2\2")
        buf.write("\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d/\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120")
        buf.write("\b\31\1\2\u0120\u0121\5\62\32\2\u0121\u0127\3\2\2\2\u0122")
        buf.write("\u0123\f\4\2\2\u0123\u0124\t\4\2\2\u0124\u0126\5\62\32")
        buf.write("\2\u0125\u0122\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\61\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012b\b\32\1\2\u012b\u012c\5\64\33\2\u012c")
        buf.write("\u0132\3\2\2\2\u012d\u012e\f\4\2\2\u012e\u012f\t\5\2\2")
        buf.write("\u012f\u0131\5\64\33\2\u0130\u012d\3\2\2\2\u0131\u0134")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\63\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0136\t\6\2\2\u0136")
        buf.write("\u0139\5\64\33\2\u0137\u0139\5\66\34\2\u0138\u0135\3\2")
        buf.write("\2\2\u0138\u0137\3\2\2\2\u0139\65\3\2\2\2\u013a\u013b")
        buf.write("\b\34\1\2\u013b\u013c\58\35\2\u013c\u014f\3\2\2\2\u013d")
        buf.write("\u014b\f\4\2\2\u013e\u013f\7\64\2\2\u013f\u0140\5*\26")
        buf.write("\2\u0140\u0141\7\65\2\2\u0141\u014c\3\2\2\2\u0142\u0149")
        buf.write("\7+\2\2\u0143\u014a\7\66\2\2\u0144\u0145\7\66\2\2\u0145")
        buf.write("\u0146\7\60\2\2\u0146\u0147\5:\36\2\u0147\u0148\7\61\2")
        buf.write("\2\u0148\u014a\3\2\2\2\u0149\u0143\3\2\2\2\u0149\u0144")
        buf.write("\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u013e\3\2\2\2\u014b")
        buf.write("\u0142\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u013d\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\67\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u015e")
        buf.write("\5\4\3\2\u0153\u0154\7\60\2\2\u0154\u0155\5*\26\2\u0155")
        buf.write("\u0156\7\61\2\2\u0156\u015e\3\2\2\2\u0157\u015e\7\66\2")
        buf.write("\2\u0158\u0159\7\66\2\2\u0159\u015a\7\60\2\2\u015a\u015b")
        buf.write("\5:\36\2\u015b\u015c\7\61\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u0152\3\2\2\2\u015d\u0153\3\2\2\2\u015d\u0157\3\2\2\2")
        buf.write("\u015d\u0158\3\2\2\2\u015e9\3\2\2\2\u015f\u0162\5<\37")
        buf.write("\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162;\3\2\2\2\u0163\u0169\5*\26\2\u0164\u0165")
        buf.write("\5*\26\2\u0165\u0166\7-\2\2\u0166\u0167\5<\37\2\u0167")
        buf.write("\u0169\3\2\2\2\u0168\u0163\3\2\2\2\u0168\u0164\3\2\2\2")
        buf.write("\u0169=\3\2\2\2\u016a\u016b\7\17\2\2\u016b\u016c\7\66")
        buf.write("\2\2\u016c\u016d\7%\2\2\u016d\u016e\5*\26\2\u016e\u016f")
        buf.write("\7.\2\2\u016f?\3\2\2\2\u0170\u0171\7\20\2\2\u0171\u0178")
        buf.write("\7\66\2\2\u0172\u0179\5\16\b\2\u0173\u0175\5\16\b\2\u0174")
        buf.write("\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\7%\2\2\u0177\u0179\5*\26\2\u0178\u0172\3")
        buf.write("\2\2\2\u0178\u0174\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b")
        buf.write("\7.\2\2\u017bA\3\2\2\2\u017c\u017d\7\7\2\2\u017d\u017e")
        buf.write("\7\66\2\2\u017e\u0180\7\60\2\2\u017f\u0181\5D#\2\u0180")
        buf.write("\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\7\61\2\2\u0183\u0185\5\16\b\2\u0184\u0183")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0187\7\62\2\2\u0187\u0188\5R*\2\u0188\u0189\7\63\2\2")
        buf.write("\u0189\u018a\7.\2\2\u018aC\3\2\2\2\u018b\u018c\5F$\2\u018c")
        buf.write("\u018d\7-\2\2\u018d\u018e\5D#\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u0191\5F$\2\u0190\u018b\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("E\3\2\2\2\u0192\u0193\5H%\2\u0193\u0194\5\16\b\2\u0194")
        buf.write("G\3\2\2\2\u0195\u0196\7\66\2\2\u0196\u0197\7-\2\2\u0197")
        buf.write("\u019a\5H%\2\u0198\u019a\7\66\2\2\u0199\u0195\3\2\2\2")
        buf.write("\u0199\u0198\3\2\2\2\u019aI\3\2\2\2\u019b\u019c\7\7\2")
        buf.write("\2\u019c\u019d\7\60\2\2\u019d\u019e\7\66\2\2\u019e\u019f")
        buf.write("\7\66\2\2\u019f\u01a0\7\61\2\2\u01a0\u01a1\7\66\2\2\u01a1")
        buf.write("\u01a3\7\60\2\2\u01a2\u01a4\5D#\2\u01a3\u01a2\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7\7")
        buf.write("\61\2\2\u01a6\u01a8\5\16\b\2\u01a7\u01a6\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\7\62\2")
        buf.write("\2\u01aa\u01ab\5R*\2\u01ab\u01ac\7\63\2\2\u01ac\u01ad")
        buf.write("\7.\2\2\u01adK\3\2\2\2\u01ae\u01af\7\b\2\2\u01af\u01b0")
        buf.write("\7\66\2\2\u01b0\u01b1\7\t\2\2\u01b1\u01b2\7\62\2\2\u01b2")
        buf.write("\u01b3\5R*\2\u01b3\u01b4\7\63\2\2\u01b4\u01b5\7.\2\2\u01b5")
        buf.write("M\3\2\2\2\u01b6\u01b7\7\b\2\2\u01b7\u01b8\7\66\2\2\u01b8")
        buf.write("\u01b9\7\n\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\5R*\2")
        buf.write("\u01bb\u01bc\7\63\2\2\u01bc\u01bd\7.\2\2\u01bdO\3\2\2")
        buf.write("\2\u01be\u01c5\5@!\2\u01bf\u01c5\5> \2\u01c0\u01c5\5B")
        buf.write("\"\2\u01c1\u01c5\5J&\2\u01c2\u01c5\5L\'\2\u01c3\u01c5")
        buf.write("\5N(\2\u01c4\u01be\3\2\2\2\u01c4\u01bf\3\2\2\2\u01c4\u01c0")
        buf.write("\3\2\2\2\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5Q\3\2\2\2\u01c6\u01c7\5|?\2\u01c7")
        buf.write("\u01c8\5R*\2\u01c8\u01cb\3\2\2\2\u01c9\u01cb\5|?\2\u01ca")
        buf.write("\u01c6\3\2\2\2\u01ca\u01c9\3\2\2\2\u01cbS\3\2\2\2\u01cc")
        buf.write("\u01cd\5P)\2\u01cdU\3\2\2\2\u01ce\u01cf\5Z.\2\u01cf\u01d0")
        buf.write("\5X-\2\u01d0\u01d1\5*\26\2\u01d1\u01d2\7.\2\2\u01d2W\3")
        buf.write("\2\2\2\u01d3\u01d4\t\7\2\2\u01d4Y\3\2\2\2\u01d5\u01d6")
        buf.write("\b.\1\2\u01d6\u01d7\7\66\2\2\u01d7\u01e3\3\2\2\2\u01d8")
        buf.write("\u01df\f\4\2\2\u01d9\u01da\7\64\2\2\u01da\u01db\5*\26")
        buf.write("\2\u01db\u01dc\7\65\2\2\u01dc\u01e0\3\2\2\2\u01dd\u01de")
        buf.write("\7+\2\2\u01de\u01e0\7\66\2\2\u01df\u01d9\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01d8\3\2\2\2")
        buf.write("\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3")
        buf.write("\2\2\2\u01e4[\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7")
        buf.write("\7\4\2\2\u01e7\u01e8\7\62\2\2\u01e8\u01e9\5R*\2\u01e9")
        buf.write("\u01ea\7\63\2\2\u01ea]\3\2\2\2\u01eb\u01f7\3\2\2\2\u01ec")
        buf.write("\u01ed\7\4\2\2\u01ed\u01ee\7\3\2\2\u01ee\u01ef\7\60\2")
        buf.write("\2\u01ef\u01f0\5*\26\2\u01f0\u01f1\7\61\2\2\u01f1\u01f2")
        buf.write("\7\62\2\2\u01f2\u01f3\5R*\2\u01f3\u01f4\7\63\2\2\u01f4")
        buf.write("\u01f5\5^\60\2\u01f5\u01f7\3\2\2\2\u01f6\u01eb\3\2\2\2")
        buf.write("\u01f6\u01ec\3\2\2\2\u01f7_\3\2\2\2\u01f8\u01f9\7\3\2")
        buf.write("\2\u01f9\u01fa\7\60\2\2\u01fa\u01fb\5*\26\2\u01fb\u01fc")
        buf.write("\7\61\2\2\u01fc\u01fd\7\62\2\2\u01fd\u01fe\5R*\2\u01fe")
        buf.write("\u0200\7\63\2\2\u01ff\u0201\5^\60\2\u0200\u01ff\3\2\2")
        buf.write("\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0204")
        buf.write("\5\\/\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write("\u0205\3\2\2\2\u0205\u0206\7.\2\2\u0206a\3\2\2\2\u0207")
        buf.write("\u0208\7\20\2\2\u0208\u020a\7\66\2\2\u0209\u020b\5\16")
        buf.write("\b\2\u020a\u0209\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c")
        buf.write("\3\2\2\2\u020c\u020d\7%\2\2\u020d\u020e\5*\26\2\u020e")
        buf.write("\u020f\7.\2\2\u020fc\3\2\2\2\u0210\u0211\7\66\2\2\u0211")
        buf.write("\u0212\7-\2\2\u0212\u0213\7\66\2\2\u0213\u0214\7/\2\2")
        buf.write("\u0214\u0215\7\23\2\2\u0215\u0216\5*\26\2\u0216e\3\2\2")
        buf.write("\2\u0217\u0218\7\66\2\2\u0218\u0219\5X-\2\u0219\u021a")
        buf.write("\5*\26\2\u021a\u021b\7.\2\2\u021b\u021e\3\2\2\2\u021c")
        buf.write("\u021e\5b\62\2\u021d\u0217\3\2\2\2\u021d\u021c\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0220\5*\26\2\u0220\u0221\7")
        buf.write(".\2\2\u0221\u0222\7\66\2\2\u0222\u0223\5X-\2\u0223\u0224")
        buf.write("\5*\26\2\u0224g\3\2\2\2\u0225\u0226\5*\26\2\u0226i\3\2")
        buf.write("\2\2\u0227\u022b\7\5\2\2\u0228\u022c\5h\65\2\u0229\u022c")
        buf.write("\5f\64\2\u022a\u022c\5d\63\2\u022b\u0228\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022d\u022e\7\62\2\2\u022e\u022f\5R*\2\u022f\u0230\7")
        buf.write("\63\2\2\u0230\u0231\7.\2\2\u0231k\3\2\2\2\u0232\u0233")
        buf.write("\7\22\2\2\u0233\u0234\7.\2\2\u0234m\3\2\2\2\u0235\u0236")
        buf.write("\7\21\2\2\u0236\u0237\7.\2\2\u0237o\3\2\2\2\u0238\u0239")
        buf.write("\5Z.\2\u0239\u023a\7+\2\2\u023a\u023d\3\2\2\2\u023b\u023d")
        buf.write("\3\2\2\2\u023c\u0238\3\2\2\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("\u023e\3\2\2\2\u023e\u023f\7\66\2\2\u023f\u0242\7\60\2")
        buf.write("\2\u0240\u0243\5(\25\2\u0241\u0243\3\2\2\2\u0242\u0240")
        buf.write("\3\2\2\2\u0242\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244")
        buf.write("\u0245\7\61\2\2\u0245\u0246\7.\2\2\u0246q\3\2\2\2\u0247")
        buf.write("\u024a\7\6\2\2\u0248\u024b\5*\26\2\u0249\u024b\3\2\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u024c\3")
        buf.write("\2\2\2\u024c\u024d\7.\2\2\u024ds\3\2\2\2\u024e\u024f\7")
        buf.write("\66\2\2\u024f\u0250\5\16\b\2\u0250\u0251\7.\2\2\u0251")
        buf.write("u\3\2\2\2\u0252\u0254\7\66\2\2\u0253\u0255\5\16\b\2\u0254")
        buf.write("\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255w\3\2\2\2\u0256")
        buf.write("\u0257\5v<\2\u0257\u0258\7-\2\2\u0258\u0259\5x=\2\u0259")
        buf.write("\u025c\3\2\2\2\u025a\u025c\5v<\2\u025b\u0256\3\2\2\2\u025b")
        buf.write("\u025a\3\2\2\2\u025cy\3\2\2\2\u025d\u025e\7\66\2\2\u025e")
        buf.write("\u0260\7\60\2\2\u025f\u0261\5x=\2\u0260\u025f\3\2\2\2")
        buf.write("\u0260\u0261\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0264\7")
        buf.write("\61\2\2\u0263\u0265\5\16\b\2\u0264\u0263\3\2\2\2\u0264")
        buf.write("\u0265\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0267\7.\2\2")
        buf.write("\u0267{\3\2\2\2\u0268\u0274\5@!\2\u0269\u0274\5> \2\u026a")
        buf.write("\u0274\5V,\2\u026b\u0274\5`\61\2\u026c\u0274\5j\66\2\u026d")
        buf.write("\u0274\5l\67\2\u026e\u0274\5n8\2\u026f\u0274\5p9\2\u0270")
        buf.write("\u0274\5r:\2\u0271\u0274\5t;\2\u0272\u0274\5z>\2\u0273")
        buf.write("\u0268\3\2\2\2\u0273\u0269\3\2\2\2\u0273\u026a\3\2\2\2")
        buf.write("\u0273\u026b\3\2\2\2\u0273\u026c\3\2\2\2\u0273\u026d\3")
        buf.write("\2\2\2\u0273\u026e\3\2\2\2\u0273\u026f\3\2\2\2\u0273\u0270")
        buf.write("\3\2\2\2\u0273\u0271\3\2\2\2\u0273\u0272\3\2\2\2\u0274")
        buf.write("}\3\2\2\2\66\u0081\u0090\u009c\u00a3\u00a7\u00ae\u00b6")
        buf.write("\u00c1\u00d1\u00dc\u00e3\u00e8\u00f1\u00fc\u0106\u0111")
        buf.write("\u011c\u0127\u0132\u0138\u0149\u014b\u014f\u015d\u0161")
        buf.write("\u0168\u0174\u0178\u0180\u0184\u0190\u0199\u01a3\u01a7")
        buf.write("\u01c4\u01ca\u01df\u01e3\u01f6\u0200\u0203\u020a\u021d")
        buf.write("\u022b\u023c\u0242\u024a\u0254\u025b\u0260\u0264\u0273")
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
                     "'.'", "':'", "','", "';'", "':='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                      "COMMA", "COCOM", "COLONEQUAL", "LPAREN", "RPAREN", 
                      "LCPAREN", "RCPAREN", "LSPAREN", "RSPAREN", "ID", 
                      "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "BOOL_LIT", "NIL_LIT", "NEWLINE", "WS", 
                      "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_sec_lit = 2
    RULE_list_sec_lit = 3
    RULE_list_literal = 4
    RULE_list_literal_noempty = 5
    RULE_all_type = 6
    RULE_basic_type = 7
    RULE_list_array_type_lit = 8
    RULE_array_type_lit = 9
    RULE_array_type = 10
    RULE_array_literal = 11
    RULE_dim_lit = 12
    RULE_dim = 13
    RULE_list_array_element = 14
    RULE_array_element = 15
    RULE_struct_literal = 16
    RULE_list_elements_lit = 17
    RULE_list_element = 18
    RULE_list_expression = 19
    RULE_expression = 20
    RULE_expression1 = 21
    RULE_expression2 = 22
    RULE_expression3 = 23
    RULE_expression4 = 24
    RULE_expression5 = 25
    RULE_expression6 = 26
    RULE_expression7 = 27
    RULE_funcall = 28
    RULE_funcall_noempty = 29
    RULE_const_declared = 30
    RULE_var_declared = 31
    RULE_func_declared = 32
    RULE_parameter_lit = 33
    RULE_parameter = 34
    RULE_list_ID = 35
    RULE_method_declared = 36
    RULE_struct_declared = 37
    RULE_interface_declared = 38
    RULE_declared = 39
    RULE_list_statement = 40
    RULE_declared_statement = 41
    RULE_assign_statement = 42
    RULE_operators = 43
    RULE_assignment_lhs = 44
    RULE_else_statement = 45
    RULE_elif_statement = 46
    RULE_if_statement = 47
    RULE_var_declared_for = 48
    RULE_range_loop = 49
    RULE_init_loop = 50
    RULE_basic_loop = 51
    RULE_for_statement = 52
    RULE_break_statement = 53
    RULE_continue_statement = 54
    RULE_call_statement = 55
    RULE_return_statement = 56
    RULE_struct_statement = 57
    RULE_method_parameter = 58
    RULE_method_parameter_lit = 59
    RULE_method_statement = 60
    RULE_statement = 61

    ruleNames =  [ "program", "literal", "sec_lit", "list_sec_lit", "list_literal", 
                   "list_literal_noempty", "all_type", "basic_type", "list_array_type_lit", 
                   "array_type_lit", "array_type", "array_literal", "dim_lit", 
                   "dim", "list_array_element", "array_element", "struct_literal", 
                   "list_elements_lit", "list_element", "list_expression", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "funcall", "funcall_noempty", "const_declared", "var_declared", 
                   "func_declared", "parameter_lit", "parameter", "list_ID", 
                   "method_declared", "struct_declared", "interface_declared", 
                   "declared", "list_statement", "declared_statement", "assign_statement", 
                   "operators", "assignment_lhs", "else_statement", "elif_statement", 
                   "if_statement", "var_declared_for", "range_loop", "init_loop", 
                   "basic_loop", "for_statement", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "struct_statement", 
                   "method_parameter", "method_parameter_lit", "method_statement", 
                   "statement" ]

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
    COLONEQUAL=45
    LPAREN=46
    RPAREN=47
    LCPAREN=48
    RCPAREN=49
    LSPAREN=50
    RSPAREN=51
    ID=52
    INT_LIT=53
    BIN_LIT=54
    OCT_LIT=55
    HEX_LIT=56
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

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


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
            self.state = 125 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.declared()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 129
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

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

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
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(MiniGoParser.BIN_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(MiniGoParser.HEX_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 138
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 139
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 11)
                self.state = 141
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


    class Sec_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_sec_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSec_lit" ):
                return visitor.visitSec_lit(self)
            else:
                return visitor.visitChildren(self)




    def sec_lit(self):

        localctx = MiniGoParser.Sec_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sec_lit)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(MiniGoParser.BIN_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(MiniGoParser.HEX_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 149
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 151
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 10)
                self.state = 153
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


    class List_sec_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sec_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Sec_litContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_sec_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_sec_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_sec_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_sec_lit" ):
                return visitor.visitList_sec_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_sec_lit(self):

        localctx = MiniGoParser.List_sec_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_sec_lit)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.sec_lit()
                self.state = 157
                self.match(MiniGoParser.COMMA)
                self.state = 158
                self.list_sec_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.sec_lit()
                pass


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
        self.enterRule(localctx, 8, self.RULE_list_literal)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.list_literal_noempty()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
        self.enterRule(localctx, 10, self.RULE_list_literal_noempty)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.literal()
                self.state = 168
                self.match(MiniGoParser.COMMA)
                self.state = 169
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
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

        def list_array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_type_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_all_type)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.list_array_type_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(MiniGoParser.ID)
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


    class Basic_typeContext(ParserRuleContext):
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = MiniGoParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
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


    class List_array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def basic_type(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_type_lit" ):
                return visitor.visitList_array_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_array_type_lit(self):

        localctx = MiniGoParser.List_array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_array_type_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.array_type_lit()
            self.state = 185
            self.basic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_lit" ):
                return visitor.visitArray_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_type_lit(self):

        localctx = MiniGoParser.Array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type_lit)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.array_type()
                self.state = 188
                self.array_type_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.LSPAREN)
            self.state = 194
            self.match(MiniGoParser.INT_LIT)
            self.state = 195
            self.match(MiniGoParser.RSPAREN)
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


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


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
        self.enterRule(localctx, 22, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.dim_lit()
            self.state = 198
            self.all_type()
            self.state = 199
            self.match(MiniGoParser.LCPAREN)
            self.state = 200
            self.list_array_element()
            self.state = 201
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
        self.enterRule(localctx, 24, self.RULE_dim_lit)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.dim()
                self.state = 204
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

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
        self.enterRule(localctx, 26, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.LSPAREN)
            self.state = 210
            self.match(MiniGoParser.INT_LIT)
            self.state = 211
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
        self.enterRule(localctx, 28, self.RULE_list_array_element)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.array_element()
                self.state = 214
                self.match(MiniGoParser.COMMA)
                self.state = 215
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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

        def list_sec_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_sec_litContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


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
        self.enterRule(localctx, 30, self.RULE_array_element)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.list_sec_lit()
                pass
            elif token in [MiniGoParser.LCPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(MiniGoParser.LCPAREN)
                self.state = 222
                self.array_element()
                self.state = 223
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


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def list_elements_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_elements_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MiniGoParser.ID)
            self.state = 228
            self.match(MiniGoParser.LCPAREN)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 229
                self.list_elements_lit()


            self.state = 232
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
        self.enterRule(localctx, 34, self.RULE_list_elements_lit)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.list_element()
                self.state = 235
                self.match(MiniGoParser.COMMA)
                self.state = 236
                self.list_elements_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_element" ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = MiniGoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MiniGoParser.ID)
            self.state = 242
            self.match(MiniGoParser.COLON)
            self.state = 243
            self.expression(0)
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
        self.enterRule(localctx, 38, self.RULE_list_expression)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.expression(0)
                self.state = 246
                self.match(MiniGoParser.COMMA)
                self.state = 247
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 255
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 256
                    self.match(MiniGoParser.OR)
                    self.state = 257
                    self.expression1(0) 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.match(MiniGoParser.AND)
                    self.state = 268
                    self.expression2(0) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 279
                    self.expression3(0) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.expression4(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.expression5() 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 308
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSPAREN]:
                        self.state = 316
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 317
                        self.expression(0)
                        self.state = 318
                        self.match(MiniGoParser.RSPAREN)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 320
                        self.match(MiniGoParser.DOT)
                        self.state = 327
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                        if la_ == 1:
                            self.state = 321
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 322
                            self.match(MiniGoParser.ID)
                            self.state = 323
                            self.match(MiniGoParser.LPAREN)
                            self.state = 324
                            self.funcall()
                            self.state = 325
                            self.match(MiniGoParser.RPAREN)
                            pass


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_expression7)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(MiniGoParser.LPAREN)
                self.state = 338
                self.expression(0)
                self.state = 339
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.match(MiniGoParser.ID)
                self.state = 343
                self.match(MiniGoParser.LPAREN)
                self.state = 344
                self.funcall()
                self.state = 345
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
        self.enterRule(localctx, 56, self.RULE_funcall)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
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
        self.enterRule(localctx, 58, self.RULE_funcall_noempty)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.expression(0)
                self.state = 355
                self.match(MiniGoParser.COMMA)
                self.state = 356
                self.funcall_noempty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declared" ):
                return visitor.visitConst_declared(self)
            else:
                return visitor.visitChildren(self)




    def const_declared(self):

        localctx = MiniGoParser.Const_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_const_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.CONST)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
            self.match(MiniGoParser.ASSIGN)
            self.state = 363
            self.expression(0)
            self.state = 364
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declared" ):
                return visitor.visitVar_declared(self)
            else:
                return visitor.visitChildren(self)




    def var_declared(self):

        localctx = MiniGoParser.Var_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MiniGoParser.VAR)
            self.state = 367
            self.match(MiniGoParser.ID)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 368
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 369
                    self.all_type()


                self.state = 372
                self.match(MiniGoParser.ASSIGN)
                self.state = 373
                self.expression(0)
                pass


            self.state = 376
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declared" ):
                return visitor.visitFunc_declared(self)
            else:
                return visitor.visitChildren(self)




    def func_declared(self):

        localctx = MiniGoParser.Func_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.FUNC)
            self.state = 379
            self.match(MiniGoParser.ID)
            self.state = 380
            self.match(MiniGoParser.LPAREN)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 381
                self.parameter_lit()


            self.state = 384
            self.match(MiniGoParser.RPAREN)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 385
                self.all_type()


            self.state = 388
            self.match(MiniGoParser.LCPAREN)
            self.state = 389
            self.list_statement()
            self.state = 390
            self.match(MiniGoParser.RCPAREN)
            self.state = 391
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_lit" ):
                return visitor.visitParameter_lit(self)
            else:
                return visitor.visitChildren(self)




    def parameter_lit(self):

        localctx = MiniGoParser.Parameter_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_parameter_lit)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.parameter()
                self.state = 394
                self.match(MiniGoParser.COMMA)
                self.state = 395
                self.parameter_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.list_ID()
            self.state = 401
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_ID)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(MiniGoParser.ID)
                self.state = 404
                self.match(MiniGoParser.COMMA)
                self.state = 405
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.FUNC)
            self.state = 410
            self.match(MiniGoParser.LPAREN)
            self.state = 411
            self.match(MiniGoParser.ID)
            self.state = 412
            self.match(MiniGoParser.ID)
            self.state = 413
            self.match(MiniGoParser.RPAREN)
            self.state = 414
            self.match(MiniGoParser.ID)
            self.state = 415
            self.match(MiniGoParser.LPAREN)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 416
                self.parameter_lit()


            self.state = 419
            self.match(MiniGoParser.RPAREN)
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 420
                self.all_type()


            self.state = 423
            self.match(MiniGoParser.LCPAREN)
            self.state = 424
            self.list_statement()
            self.state = 425
            self.match(MiniGoParser.RCPAREN)
            self.state = 426
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(MiniGoParser.TYPE)
            self.state = 429
            self.match(MiniGoParser.ID)
            self.state = 430
            self.match(MiniGoParser.STRUCT)
            self.state = 431
            self.match(MiniGoParser.LCPAREN)
            self.state = 432
            self.list_statement()
            self.state = 433
            self.match(MiniGoParser.RCPAREN)
            self.state = 434
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_interface_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.TYPE)
            self.state = 437
            self.match(MiniGoParser.ID)
            self.state = 438
            self.match(MiniGoParser.INTERFACE)
            self.state = 439
            self.match(MiniGoParser.LCPAREN)
            self.state = 440
            self.list_statement()
            self.state = 441
            self.match(MiniGoParser.RCPAREN)
            self.state = 442
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaredContext,0)


        def const_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaredContext,0)


        def func_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_declared)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.var_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.const_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.func_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 447
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 448
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 449
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_list_statement)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.statement()
                self.state = 453
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.declared()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def operators(self):
            return self.getTypedRuleContext(MiniGoParser.OperatorsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.assignment_lhs(0)
            self.state = 461
            self.operators()
            self.state = 462
            self.expression(0)
            self.state = 463
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = MiniGoParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.COLONEQUAL))) != 0)):
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


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assignment_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 477
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSPAREN]:
                        self.state = 471
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 472
                        self.expression(0)
                        self.state = 473
                        self.match(MiniGoParser.RSPAREN)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 475
                        self.match(MiniGoParser.DOT)
                        self.state = 476
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniGoParser.ELSE)
            self.state = 485
            self.match(MiniGoParser.LCPAREN)
            self.state = 486
            self.list_statement()
            self.state = 487
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = MiniGoParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elif_statement)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(MiniGoParser.ELSE)
                self.state = 491
                self.match(MiniGoParser.IF)
                self.state = 492
                self.match(MiniGoParser.LPAREN)
                self.state = 493
                self.expression(0)
                self.state = 494
                self.match(MiniGoParser.RPAREN)
                self.state = 495
                self.match(MiniGoParser.LCPAREN)
                self.state = 496
                self.list_statement()
                self.state = 497
                self.match(MiniGoParser.RCPAREN)
                self.state = 498
                self.elif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.IF)
            self.state = 503
            self.match(MiniGoParser.LPAREN)
            self.state = 504
            self.expression(0)
            self.state = 505
            self.match(MiniGoParser.RPAREN)
            self.state = 506
            self.match(MiniGoParser.LCPAREN)
            self.state = 507
            self.list_statement()
            self.state = 508
            self.match(MiniGoParser.RCPAREN)
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 509
                self.elif_statement()


            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 512
                self.else_statement()


            self.state = 515
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declared_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declared_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declared_for" ):
                return visitor.visitVar_declared_for(self)
            else:
                return visitor.visitChildren(self)




    def var_declared_for(self):

        localctx = MiniGoParser.Var_declared_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_var_declared_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MiniGoParser.VAR)
            self.state = 518
            self.match(MiniGoParser.ID)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 519
                self.all_type()


            self.state = 522
            self.match(MiniGoParser.ASSIGN)
            self.state = 523
            self.expression(0)
            self.state = 524
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_loop" ):
                return visitor.visitRange_loop(self)
            else:
                return visitor.visitChildren(self)




    def range_loop(self):

        localctx = MiniGoParser.Range_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.ID)
            self.state = 527
            self.match(MiniGoParser.COMMA)
            self.state = 528
            self.match(MiniGoParser.ID)
            self.state = 529
            self.match(MiniGoParser.COLONEQUAL)
            self.state = 530
            self.match(MiniGoParser.RANGE)
            self.state = 531
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COCOM(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COCOM)
            else:
                return self.getToken(MiniGoParser.COCOM, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.OperatorsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.OperatorsContext,i)


        def var_declared_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declared_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_loop" ):
                return visitor.visitInit_loop(self)
            else:
                return visitor.visitChildren(self)




    def init_loop(self):

        localctx = MiniGoParser.Init_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_init_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 533
                self.match(MiniGoParser.ID)
                self.state = 534
                self.operators()
                self.state = 535
                self.expression(0)
                self.state = 536
                self.match(MiniGoParser.COCOM)
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 538
                self.var_declared_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 541
            self.expression(0)
            self.state = 542
            self.match(MiniGoParser.COCOM)
            self.state = 543
            self.match(MiniGoParser.ID)
            self.state = 544
            self.operators()
            self.state = 545
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = MiniGoParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def basic_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_loopContext,0)


        def init_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Init_loopContext,0)


        def range_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Range_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.FOR)
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 550
                self.basic_loop()
                pass

            elif la_ == 2:
                self.state = 551
                self.init_loop()
                pass

            elif la_ == 3:
                self.state = 552
                self.range_loop()
                pass


            self.state = 555
            self.match(MiniGoParser.LCPAREN)
            self.state = 556
            self.list_statement()
            self.state = 557
            self.match(MiniGoParser.RCPAREN)
            self.state = 558
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(MiniGoParser.BREAK)
            self.state = 561
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.match(MiniGoParser.CONTINUE)
            self.state = 564
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 566
                self.assignment_lhs(0)
                self.state = 567
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 572
            self.match(MiniGoParser.ID)
            self.state = 573
            self.match(MiniGoParser.LPAREN)
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 574
                self.list_expression()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 578
            self.match(MiniGoParser.RPAREN)
            self.state = 579
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.RETURN)
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 582
                self.expression(0)
                pass
            elif token in [MiniGoParser.COCOM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 586
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_statement" ):
                return visitor.visitStruct_statement(self)
            else:
                return visitor.visitChildren(self)




    def struct_statement(self):

        localctx = MiniGoParser.Struct_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_struct_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(MiniGoParser.ID)
            self.state = 589
            self.all_type()
            self.state = 590
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_parameter" ):
                return visitor.visitMethod_parameter(self)
            else:
                return visitor.visitChildren(self)




    def method_parameter(self):

        localctx = MiniGoParser.Method_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_method_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.ID)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 593
                self.all_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_parameter_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameter_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_parameter_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_parameter_lit" ):
                return visitor.visitMethod_parameter_lit(self)
            else:
                return visitor.visitChildren(self)




    def method_parameter_lit(self):

        localctx = MiniGoParser.Method_parameter_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_method_parameter_lit)
        try:
            self.state = 601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.method_parameter()
                self.state = 597
                self.match(MiniGoParser.COMMA)
                self.state = 598
                self.method_parameter_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.method_parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def method_parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_statement" ):
                return visitor.visitMethod_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_statement(self):

        localctx = MiniGoParser.Method_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_method_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(MiniGoParser.ID)
            self.state = 604
            self.match(MiniGoParser.LPAREN)
            self.state = 606
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 605
                self.method_parameter_lit()


            self.state = 608
            self.match(MiniGoParser.RPAREN)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 609
                self.all_type()


            self.state = 612
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaredContext,0)


        def const_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaredContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def struct_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_statementContext,0)


        def method_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Method_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_statement)
        try:
            self.state = 625
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.var_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.const_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 616
                self.assign_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 617
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 618
                self.for_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 619
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 620
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 621
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 622
                self.return_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 623
                self.struct_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 624
                self.method_statement()
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
        self._predicates[20] = self.expression_sempred
        self._predicates[21] = self.expression1_sempred
        self._predicates[22] = self.expression2_sempred
        self._predicates[23] = self.expression3_sempred
        self._predicates[24] = self.expression4_sempred
        self._predicates[26] = self.expression6_sempred
        self._predicates[44] = self.assignment_lhs_sempred
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
         

    def assignment_lhs_sempred(self, localctx:Assignment_lhsContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




