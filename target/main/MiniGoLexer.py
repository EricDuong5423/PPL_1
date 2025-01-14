# Generated from main/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01f9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\7\64\u0157\n\64\f\64\16\64\u015a\13\64\3")
        buf.write("\65\3\65\3\65\7\65\u015f\n\65\f\65\16\65\u0162\13\65\5")
        buf.write("\65\u0164\n\65\3\66\3\66\3\66\6\66\u0169\n\66\r\66\16")
        buf.write("\66\u016a\3\66\3\66\3\67\3\67\3\67\6\67\u0172\n\67\r\67")
        buf.write("\16\67\u0173\3\67\3\67\38\38\38\68\u017b\n8\r8\168\u017c")
        buf.write("\38\38\39\39\59\u0183\n9\3:\3:\3;\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u018e\n;\3<\3<\3=\6=\u0193\n=\r=\16=\u0194\3>\3>\7>")
        buf.write("\u0199\n>\f>\16>\u019c\13>\5>\u019e\n>\3?\3?\5?\u01a2")
        buf.write("\n?\3?\5?\u01a5\n?\3@\3@\7@\u01a9\n@\f@\16@\u01ac\13@")
        buf.write("\3@\3@\3@\3A\3A\5A\u01b3\nA\3B\3B\3B\3B\5B\u01b9\nB\3")
        buf.write("C\3C\3C\3D\6D\u01bf\nD\rD\16D\u01c0\3D\3D\3E\3E\3E\3E")
        buf.write("\7E\u01c9\nE\fE\16E\u01cc\13E\3E\3E\3F\3F\3F\3F\3F\7F")
        buf.write("\u01d5\nF\fF\16F\u01d8\13F\3F\3F\3F\3F\3F\3G\3G\3G\3H")
        buf.write("\3H\7H\u01e4\nH\fH\16H\u01e7\13H\3H\3H\3H\5H\u01ec\nH")
        buf.write("\3H\3H\3I\3I\7I\u01f2\nI\fI\16I\u01f5\13I\3I\3I\3I\3\u01d6")
        buf.write("\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w\2y\2{\2}\2\177=\u0081\2\u0083\2\u0085\2\u0087>")
        buf.write("\u0089?\u008b@\u008dA\u008fB\u0091C\3\2\24\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2")
        buf.write("QQqq\3\2\629\4\2ZZzz\4\2\62;CH\4\2GGgg\4\2--//\5\2\f\f")
        buf.write("$$^^\6\2^^ppttvv\7\2$$^^ppttvv\5\2\13\f\16\17\"\"\3\2")
        buf.write("\f\f\3\3\f\f\2\u0208\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093")
        buf.write("\3\2\2\2\5\u009a\3\2\2\2\7\u009d\3\2\2\2\t\u00a2\3\2\2")
        buf.write("\2\13\u00a6\3\2\2\2\r\u00ad\3\2\2\2\17\u00b2\3\2\2\2\21")
        buf.write("\u00b7\3\2\2\2\23\u00be\3\2\2\2\25\u00c8\3\2\2\2\27\u00cf")
        buf.write("\3\2\2\2\31\u00d3\3\2\2\2\33\u00d9\3\2\2\2\35\u00e1\3")
        buf.write("\2\2\2\37\u00e7\3\2\2\2!\u00eb\3\2\2\2#\u00f4\3\2\2\2")
        buf.write("%\u00fa\3\2\2\2\'\u0100\3\2\2\2)\u0104\3\2\2\2+\u0109")
        buf.write("\3\2\2\2-\u010f\3\2\2\2/\u0111\3\2\2\2\61\u0113\3\2\2")
        buf.write("\2\63\u0115\3\2\2\2\65\u0117\3\2\2\2\67\u0119\3\2\2\2")
        buf.write("9\u011c\3\2\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0124\3")
        buf.write("\2\2\2A\u0126\3\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0131\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2")
        buf.write("O\u0139\3\2\2\2Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0142\3")
        buf.write("\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a")
        buf.write("\3\2\2\2_\u014c\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2")
        buf.write("e\u0152\3\2\2\2g\u0154\3\2\2\2i\u0163\3\2\2\2k\u0165\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0177\3\2\2\2q\u0182\3\2\2\2s\u0184")
        buf.write("\3\2\2\2u\u018d\3\2\2\2w\u018f\3\2\2\2y\u0192\3\2\2\2")
        buf.write("{\u019d\3\2\2\2}\u01a4\3\2\2\2\177\u01a6\3\2\2\2\u0081")
        buf.write("\u01b2\3\2\2\2\u0083\u01b8\3\2\2\2\u0085\u01ba\3\2\2\2")
        buf.write("\u0087\u01be\3\2\2\2\u0089\u01c4\3\2\2\2\u008b\u01cf\3")
        buf.write("\2\2\2\u008d\u01de\3\2\2\2\u008f\u01e1\3\2\2\2\u0091\u01ef")
        buf.write("\3\2\2\2\u0093\u0094\7x\2\2\u0094\u0095\7q\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7k\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7p\2\2\u0099\4\3\2\2\2\u009a\u009b\7k\2\2\u009b\u009c")
        buf.write("\7h\2\2\u009c\6\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f")
        buf.write("\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\b")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7p\2\2\u00ac\f\3\2\2\2\u00ad\u00ae")
        buf.write("\7h\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7e\2\2\u00b1\16\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7{\2\2\u00b4\u00b5\7r\2\2\u00b5\u00b6\7g\2\2\u00b6\20")
        buf.write("\3\2\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\22\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7t\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6")
        buf.write("\7e\2\2\u00c6\u00c7\7g\2\2\u00c7\24\3\2\2\2\u00c8\u00c9")
        buf.write("\7u\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\30\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7v\2\2\u00d8\32\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7p\2\2\u00e0\34")
        buf.write("\3\2\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\36")
        buf.write("\3\2\2\2\u00e7\u00e8\7x\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea \3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\"\3\2\2\2\u00f4\u00f5\7d\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9")
        buf.write("\7m\2\2\u00f9$\3\2\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff")
        buf.write("\7g\2\2\u00ff&\3\2\2\2\u0100\u0101\7p\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7n\2\2\u0103(\3\2\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7t\2\2\u0106\u0107\7w\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108*\3\2\2\2\u0109\u010a\7h\2\2\u010a\u010b")
        buf.write("\7c\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e,\3\2\2\2\u010f\u0110\7-\2\2\u0110.\3\2\2")
        buf.write("\2\u0111\u0112\7/\2\2\u0112\60\3\2\2\2\u0113\u0114\7,")
        buf.write("\2\2\u0114\62\3\2\2\2\u0115\u0116\7\61\2\2\u0116\64\3")
        buf.write("\2\2\2\u0117\u0118\7\'\2\2\u0118\66\3\2\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\u011b\7?\2\2\u011b8\3\2\2\2\u011c\u011d")
        buf.write("\7#\2\2\u011d\u011e\7?\2\2\u011e:\3\2\2\2\u011f\u0120")
        buf.write("\7>\2\2\u0120<\3\2\2\2\u0121\u0122\7>\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123>\3\2\2\2\u0124\u0125\7@\2\2\u0125@\3\2\2")
        buf.write("\2\u0126\u0127\7@\2\2\u0127\u0128\7?\2\2\u0128B\3\2\2")
        buf.write("\2\u0129\u012a\7(\2\2\u012a\u012b\7(\2\2\u012bD\3\2\2")
        buf.write("\2\u012c\u012d\7~\2\2\u012d\u012e\7~\2\2\u012eF\3\2\2")
        buf.write("\2\u012f\u0130\7#\2\2\u0130H\3\2\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132J\3\2\2\2\u0133\u0134\7-\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135L\3\2\2\2\u0136\u0137\7/\2\2\u0137\u0138\7?\2")
        buf.write("\2\u0138N\3\2\2\2\u0139\u013a\7,\2\2\u013a\u013b\7?\2")
        buf.write("\2\u013bP\3\2\2\2\u013c\u013d\7\61\2\2\u013d\u013e\7?")
        buf.write("\2\2\u013eR\3\2\2\2\u013f\u0140\7\'\2\2\u0140\u0141\7")
        buf.write("?\2\2\u0141T\3\2\2\2\u0142\u0143\7\60\2\2\u0143V\3\2\2")
        buf.write("\2\u0144\u0145\7*\2\2\u0145X\3\2\2\2\u0146\u0147\7+\2")
        buf.write("\2\u0147Z\3\2\2\2\u0148\u0149\7}\2\2\u0149\\\3\2\2\2\u014a")
        buf.write("\u014b\7\177\2\2\u014b^\3\2\2\2\u014c\u014d\7]\2\2\u014d")
        buf.write("`\3\2\2\2\u014e\u014f\7_\2\2\u014fb\3\2\2\2\u0150\u0151")
        buf.write("\7.\2\2\u0151d\3\2\2\2\u0152\u0153\7=\2\2\u0153f\3\2\2")
        buf.write("\2\u0154\u0158\t\2\2\2\u0155\u0157\t\3\2\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159h\3\2\2\2\u015a\u0158\3\2\2\2\u015b")
        buf.write("\u0164\7\62\2\2\u015c\u0160\t\4\2\2\u015d\u015f\t\5\2")
        buf.write("\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u015b\3\2\2\2\u0163\u015c\3\2\2\2")
        buf.write("\u0164j\3\2\2\2\u0165\u0166\7\62\2\2\u0166\u0168\t\6\2")
        buf.write("\2\u0167\u0169\t\7\2\2\u0168\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\b\66\2\2\u016dl\3\2\2\2\u016e")
        buf.write("\u016f\7\62\2\2\u016f\u0171\t\b\2\2\u0170\u0172\t\t\2")
        buf.write("\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\b\67\3\2\u0176n\3\2\2\2\u0177\u0178\7\62\2\2\u0178")
        buf.write("\u017a\t\n\2\2\u0179\u017b\t\13\2\2\u017a\u0179\3\2\2")
        buf.write("\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b8\4\2\u017f")
        buf.write("p\3\2\2\2\u0180\u0183\5)\25\2\u0181\u0183\5+\26\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183r\3\2\2\2\u0184")
        buf.write("\u0185\5\'\24\2\u0185t\3\2\2\2\u0186\u0187\5y=\2\u0187")
        buf.write("\u0188\5{>\2\u0188\u0189\5}?\2\u0189\u018e\3\2\2\2\u018a")
        buf.write("\u018b\5y=\2\u018b\u018c\5}?\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u0186\3\2\2\2\u018d\u018a\3\2\2\2\u018ev\3\2\2\2\u018f")
        buf.write("\u0190\t\5\2\2\u0190x\3\2\2\2\u0191\u0193\5w<\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195z\3\2\2\2\u0196\u019a\7\60\2")
        buf.write("\2\u0197\u0199\5w<\2\u0198\u0197\3\2\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u0196\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e|\3\2\2\2\u019f\u01a1\t\f\2\2\u01a0")
        buf.write("\u01a2\t\r\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a5\5y=\2\u01a4\u019f\3\2")
        buf.write("\2\2\u01a4\u01a5\3\2\2\2\u01a5~\3\2\2\2\u01a6\u01aa\7")
        buf.write("$\2\2\u01a7\u01a9\5\u0081A\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\7")
        buf.write("$\2\2\u01ae\u01af\b@\5\2\u01af\u0080\3\2\2\2\u01b0\u01b3")
        buf.write("\n\16\2\2\u01b1\u01b3\5\u0083B\2\u01b2\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u0082\3\2\2\2\u01b4\u01b5\7^\2\2")
        buf.write("\u01b5\u01b9\t\17\2\2\u01b6\u01b7\7)\2\2\u01b7\u01b9\7")
        buf.write("$\2\2\u01b8\u01b4\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u0084")
        buf.write("\3\2\2\2\u01ba\u01bb\7^\2\2\u01bb\u01bc\n\20\2\2\u01bc")
        buf.write("\u0086\3\2\2\2\u01bd\u01bf\t\21\2\2\u01be\u01bd\3\2\2")
        buf.write("\2\u01bf\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\bD\6\2\u01c3")
        buf.write("\u0088\3\2\2\2\u01c4\u01c5\7\61\2\2\u01c5\u01c6\7\61\2")
        buf.write("\2\u01c6\u01ca\3\2\2\2\u01c7\u01c9\n\22\2\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cd\u01ce\bE\6\2\u01ce\u008a\3\2\2\2\u01cf\u01d0\7")
        buf.write("\61\2\2\u01d0\u01d1\7,\2\2\u01d1\u01d6\3\2\2\2\u01d2\u01d5")
        buf.write("\5\u008bF\2\u01d3\u01d5\13\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d9\u01da\7,\2\2\u01da\u01db\7\61\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01dd\bF\6\2\u01dd\u008c\3\2\2\2\u01de")
        buf.write("\u01df\13\2\2\2\u01df\u01e0\bG\7\2\u01e0\u008e\3\2\2\2")
        buf.write("\u01e1\u01e5\7$\2\2\u01e2\u01e4\5\u0081A\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01eb\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u01e9\7\17\2\2\u01e9\u01ec\7\f\2\2\u01ea\u01ec")
        buf.write("\t\23\2\2\u01eb\u01e8\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01ee\bH\b\2\u01ee\u0090\3\2\2\2")
        buf.write("\u01ef\u01f3\7$\2\2\u01f0\u01f2\5\u0081A\2\u01f1\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f6\u01f7\5\u0085C\2\u01f7\u01f8\bI\t\2\u01f8\u0092")
        buf.write("\3\2\2\2\32\2\u0158\u0160\u0163\u016a\u0173\u017c\u0182")
        buf.write("\u018d\u0194\u019a\u019d\u01a1\u01a4\u01aa\u01b2\u01b8")
        buf.write("\u01c0\u01ca\u01d4\u01d6\u01e5\u01eb\u01f3\n\3\66\2\3")
        buf.write("\67\3\38\4\3@\5\b\2\2\3G\6\3H\7\3I\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NEQUAL = 28
    LT = 29
    LTE = 30
    GT = 31
    GTE = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    LPAREN = 43
    RPAREN = 44
    LCURPAREN = 45
    RCURPAREN = 46
    LSQUAREPAREN = 47
    RSQUAREPAREN = 48
    COM = 49
    COCOM = 50
    ID = 51
    INT_LIT = 52
    BIN_LIT = 53
    OCT_LIT = 54
    HEX_LIT = 55
    BOOL_LIT = 56
    NIL_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    WS = 60
    COMMENT_LINE = 61
    COMMENT = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'votien'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'const'", "'var'", "'continue'", "'break'", "'range'", 
            "'nil'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "AND", 
            "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "LPAREN", "RPAREN", "LCURPAREN", 
            "RCURPAREN", "LSQUAREPAREN", "RSQUAREPAREN", "COM", "COCOM", 
            "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "BOOL_LIT", 
            "NIL_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "COMMENT_LINE", 
            "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NEQUAL", 
                  "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "LPAREN", "RPAREN", "LCURPAREN", 
                  "RCURPAREN", "LSQUAREPAREN", "RSQUAREPAREN", "COM", "COCOM", 
                  "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "BOOL_LIT", 
                  "NIL_LIT", "FLOAT_LIT", "DIGIT", "DIGITS", "OPT_FRAC", 
                  "OPT_EXP", "STRING_LIT", "STRING_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "WS", "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.BIN_LIT_action 
            actions[53] = self.OCT_LIT_action 
            actions[54] = self.HEX_LIT_action 
            actions[62] = self.STRING_LIT_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def BIN_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = str(int(self.text, 2));

     

    def OCT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = str(int(self.text, 8));

     

    def HEX_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = str(int(self.text, 16));

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
                elif(self.text[-1] == '\n') :
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise IllegalEscape(self.text[1:])

     


