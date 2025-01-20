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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0210\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u015b\n\65\f\65\16\65\u015e\13\65\3\66")
        buf.write("\3\66\3\66\7\66\u0163\n\66\f\66\16\66\u0166\13\66\5\66")
        buf.write("\u0168\n\66\3\67\3\67\3\67\6\67\u016d\n\67\r\67\16\67")
        buf.write("\u016e\3\67\3\67\38\38\38\68\u0176\n8\r8\168\u0177\38")
        buf.write("\38\39\39\39\69\u017f\n9\r9\169\u0180\39\39\3:\3:\3:\3")
        buf.write(":\5:\u0189\n:\3;\3;\3;\3;\3;\3;\3;\5;\u0192\n;\3<\3<\3")
        buf.write("=\3=\3=\7=\u0199\n=\f=\16=\u019c\13=\5=\u019e\n=\3>\3")
        buf.write(">\7>\u01a2\n>\f>\16>\u01a5\13>\5>\u01a7\n>\3?\3?\5?\u01ab")
        buf.write("\n?\3?\3?\5?\u01af\n?\5?\u01b1\n?\3@\3@\7@\u01b5\n@\f")
        buf.write("@\16@\u01b8\13@\3@\3@\3@\3A\3A\5A\u01bf\nA\3B\3B\3B\3")
        buf.write("B\5B\u01c5\nB\3C\3C\3C\3D\3D\5D\u01cc\nD\3E\3E\3F\5F\u01d1")
        buf.write("\nF\3F\3F\3G\6G\u01d6\nG\rG\16G\u01d7\3G\3G\3H\3H\3H\3")
        buf.write("H\7H\u01e0\nH\fH\16H\u01e3\13H\3H\3H\3I\3I\3I\3I\3I\7")
        buf.write("I\u01ec\nI\fI\16I\u01ef\13I\3I\3I\3I\3I\3I\3J\3J\3J\3")
        buf.write("K\3K\7K\u01fb\nK\fK\16K\u01fe\13K\3K\3K\3K\5K\u0203\n")
        buf.write("K\3K\3K\3L\3L\7L\u0209\nL\fL\16L\u020c\13L\3L\3L\3L\3")
        buf.write("\u01ed\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081\2\u0083\2\u0085\2")
        buf.write("\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093D\u0095")
        buf.write("E\u0097F\3\2\23\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2")
        buf.write("\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62")
        buf.write(";CHch\4\2GGgg\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\5\2\13")
        buf.write("\13\16\17\"\"\3\2\f\f\3\3\f\f\2\u0225\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2\177\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u009c\3\2\2\2\7\u00a1\3\2\2")
        buf.write("\2\t\u00a5\3\2\2\2\13\u00ac\3\2\2\2\r\u00b1\3\2\2\2\17")
        buf.write("\u00b6\3\2\2\2\21\u00bd\3\2\2\2\23\u00c7\3\2\2\2\25\u00ce")
        buf.write("\3\2\2\2\27\u00d2\3\2\2\2\31\u00d8\3\2\2\2\33\u00e0\3")
        buf.write("\2\2\2\35\u00e6\3\2\2\2\37\u00ea\3\2\2\2!\u00f3\3\2\2")
        buf.write("\2#\u00f9\3\2\2\2%\u00ff\3\2\2\2\'\u0103\3\2\2\2)\u0108")
        buf.write("\3\2\2\2+\u010e\3\2\2\2-\u0110\3\2\2\2/\u0112\3\2\2\2")
        buf.write("\61\u0114\3\2\2\2\63\u0116\3\2\2\2\65\u0118\3\2\2\2\67")
        buf.write("\u011b\3\2\2\29\u011e\3\2\2\2;\u0120\3\2\2\2=\u0123\3")
        buf.write("\2\2\2?\u0125\3\2\2\2A\u0128\3\2\2\2C\u012b\3\2\2\2E\u012e")
        buf.write("\3\2\2\2G\u0130\3\2\2\2I\u0132\3\2\2\2K\u0135\3\2\2\2")
        buf.write("M\u0138\3\2\2\2O\u013b\3\2\2\2Q\u013e\3\2\2\2S\u0141\3")
        buf.write("\2\2\2U\u0143\3\2\2\2W\u0145\3\2\2\2Y\u0147\3\2\2\2[\u0149")
        buf.write("\3\2\2\2]\u014c\3\2\2\2_\u014e\3\2\2\2a\u0150\3\2\2\2")
        buf.write("c\u0152\3\2\2\2e\u0154\3\2\2\2g\u0156\3\2\2\2i\u0158\3")
        buf.write("\2\2\2k\u0167\3\2\2\2m\u0169\3\2\2\2o\u0172\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u0188\3\2\2\2u\u0191\3\2\2\2w\u0193\3\2\2\2")
        buf.write("y\u019d\3\2\2\2{\u01a6\3\2\2\2}\u01b0\3\2\2\2\177\u01b2")
        buf.write("\3\2\2\2\u0081\u01be\3\2\2\2\u0083\u01c4\3\2\2\2\u0085")
        buf.write("\u01c6\3\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01cd\3\2\2\2")
        buf.write("\u008b\u01d0\3\2\2\2\u008d\u01d5\3\2\2\2\u008f\u01db\3")
        buf.write("\2\2\2\u0091\u01e6\3\2\2\2\u0093\u01f5\3\2\2\2\u0095\u01f8")
        buf.write("\3\2\2\2\u0097\u0206\3\2\2\2\u0099\u009a\7k\2\2\u009a")
        buf.write("\u009b\7h\2\2\u009b\4\3\2\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7n\2\2\u009e\u009f\7u\2\2\u009f\u00a0\7g\2\2\u00a0")
        buf.write("\6\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3\7q\2\2\u00a3")
        buf.write("\u00a4\7t\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7t\2\2\u00a6")
        buf.write("\u00a7\7g\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7w\2\2\u00a9")
        buf.write("\u00aa\7t\2\2\u00aa\u00ab\7p\2\2\u00ab\n\3\2\2\2\u00ac")
        buf.write("\u00ad\7h\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write("\u00b0\7e\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\u00b3\7{\2\2\u00b3\u00b4\7r\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\16\3\2\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7e\2\2\u00bb")
        buf.write("\u00bc\7v\2\2\u00bc\20\3\2\2\2\u00bd\u00be\7k\2\2\u00be")
        buf.write("\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4\7c\2\2\u00c4")
        buf.write("\u00c5\7e\2\2\u00c5\u00c6\7g\2\2\u00c6\22\3\2\2\2\u00c7")
        buf.write("\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca")
        buf.write("\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7i\2\2\u00cd")
        buf.write("\24\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0")
        buf.write("\u00d1\7v\2\2\u00d1\26\3\2\2\2\u00d2\u00d3\7h\2\2\u00d3")
        buf.write("\u00d4\7n\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7c\2\2\u00d6")
        buf.write("\u00d7\7v\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7d\2\2\u00d9")
        buf.write("\u00da\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7n\2\2\u00dc")
        buf.write("\u00dd\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write("\32\3\2\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7q\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7v\2\2\u00e5")
        buf.write("\34\3\2\2\2\u00e6\u00e7\7x\2\2\u00e7\u00e8\7c\2\2\u00e8")
        buf.write("\u00e9\7t\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7e\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7v\2\2\u00ee")
        buf.write("\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7w\2\2\u00f1")
        buf.write("\u00f2\7g\2\2\u00f2 \3\2\2\2\u00f3\u00f4\7d\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7c\2\2\u00f7")
        buf.write("\u00f8\7m\2\2\u00f8\"\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa")
        buf.write("\u00fb\7c\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7i\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe$\3\2\2\2\u00ff\u0100\7p\2\2\u0100")
        buf.write("\u0101\7k\2\2\u0101\u0102\7n\2\2\u0102&\3\2\2\2\u0103")
        buf.write("\u0104\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106\7w\2\2\u0106")
        buf.write("\u0107\7g\2\2\u0107(\3\2\2\2\u0108\u0109\7h\2\2\u0109")
        buf.write("\u010a\7c\2\2\u010a\u010b\7n\2\2\u010b\u010c\7u\2\2\u010c")
        buf.write("\u010d\7g\2\2\u010d*\3\2\2\2\u010e\u010f\7-\2\2\u010f")
        buf.write(",\3\2\2\2\u0110\u0111\7/\2\2\u0111.\3\2\2\2\u0112\u0113")
        buf.write("\7,\2\2\u0113\60\3\2\2\2\u0114\u0115\7\61\2\2\u0115\62")
        buf.write("\3\2\2\2\u0116\u0117\7\'\2\2\u0117\64\3\2\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119\u011a\7?\2\2\u011a\66\3\2\2\2\u011b\u011c")
        buf.write("\7#\2\2\u011c\u011d\7?\2\2\u011d8\3\2\2\2\u011e\u011f")
        buf.write("\7>\2\2\u011f:\3\2\2\2\u0120\u0121\7>\2\2\u0121\u0122")
        buf.write("\7?\2\2\u0122<\3\2\2\2\u0123\u0124\7@\2\2\u0124>\3\2\2")
        buf.write("\2\u0125\u0126\7@\2\2\u0126\u0127\7?\2\2\u0127@\3\2\2")
        buf.write("\2\u0128\u0129\7(\2\2\u0129\u012a\7(\2\2\u012aB\3\2\2")
        buf.write("\2\u012b\u012c\7~\2\2\u012c\u012d\7~\2\2\u012dD\3\2\2")
        buf.write("\2\u012e\u012f\7#\2\2\u012fF\3\2\2\2\u0130\u0131\7?\2")
        buf.write("\2\u0131H\3\2\2\2\u0132\u0133\7-\2\2\u0133\u0134\7?\2")
        buf.write("\2\u0134J\3\2\2\2\u0135\u0136\7/\2\2\u0136\u0137\7?\2")
        buf.write("\2\u0137L\3\2\2\2\u0138\u0139\7,\2\2\u0139\u013a\7?\2")
        buf.write("\2\u013aN\3\2\2\2\u013b\u013c\7\61\2\2\u013c\u013d\7?")
        buf.write("\2\2\u013dP\3\2\2\2\u013e\u013f\7\'\2\2\u013f\u0140\7")
        buf.write("?\2\2\u0140R\3\2\2\2\u0141\u0142\7\60\2\2\u0142T\3\2\2")
        buf.write("\2\u0143\u0144\7<\2\2\u0144V\3\2\2\2\u0145\u0146\7.\2")
        buf.write("\2\u0146X\3\2\2\2\u0147\u0148\7=\2\2\u0148Z\3\2\2\2\u0149")
        buf.write("\u014a\7<\2\2\u014a\u014b\7?\2\2\u014b\\\3\2\2\2\u014c")
        buf.write("\u014d\7*\2\2\u014d^\3\2\2\2\u014e\u014f\7+\2\2\u014f")
        buf.write("`\3\2\2\2\u0150\u0151\7}\2\2\u0151b\3\2\2\2\u0152\u0153")
        buf.write("\7\177\2\2\u0153d\3\2\2\2\u0154\u0155\7]\2\2\u0155f\3")
        buf.write("\2\2\2\u0156\u0157\7_\2\2\u0157h\3\2\2\2\u0158\u015c\t")
        buf.write("\2\2\2\u0159\u015b\t\3\2\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("j\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0168\7\62\2\2\u0160")
        buf.write("\u0164\t\4\2\2\u0161\u0163\t\5\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u015f")
        buf.write("\3\2\2\2\u0167\u0160\3\2\2\2\u0168l\3\2\2\2\u0169\u016a")
        buf.write("\7\62\2\2\u016a\u016c\t\6\2\2\u016b\u016d\t\7\2\2\u016c")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b")
        buf.write("\67\2\2\u0171n\3\2\2\2\u0172\u0173\7\62\2\2\u0173\u0175")
        buf.write("\t\b\2\2\u0174\u0176\t\t\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017a\b8\3\2\u017ap\3\2\2\2")
        buf.write("\u017b\u017c\7\62\2\2\u017c\u017e\t\n\2\2\u017d\u017f")
        buf.write("\t\13\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0183\b9\4\2\u0183r\3\2\2\2\u0184\u0189\5k\66\2")
        buf.write("\u0185\u0189\5m\67\2\u0186\u0189\5o8\2\u0187\u0189\5q")
        buf.write("9\2\u0188\u0184\3\2\2\2\u0188\u0185\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0187\3\2\2\2\u0189t\3\2\2\2\u018a\u018b")
        buf.write("\5y=\2\u018b\u018c\5{>\2\u018c\u018d\5}?\2\u018d\u0192")
        buf.write("\3\2\2\2\u018e\u018f\5y=\2\u018f\u0190\5}?\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u018a\3\2\2\2\u0191\u018e\3\2\2\2\u0192")
        buf.write("v\3\2\2\2\u0193\u0194\t\5\2\2\u0194x\3\2\2\2\u0195\u019e")
        buf.write("\7\62\2\2\u0196\u019a\t\4\2\2\u0197\u0199\5w<\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019d\u0195\3\2\2\2\u019d\u0196\3\2\2\2\u019ez")
        buf.write("\3\2\2\2\u019f\u01a3\7\60\2\2\u01a0\u01a2\5w<\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u019f\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7|")
        buf.write("\3\2\2\2\u01a8\u01aa\t\f\2\2\u01a9\u01ab\t\r\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ae\3\2\2\2")
        buf.write("\u01ac\u01af\5y=\2\u01ad\u01af\7\62\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01a8")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1~\3\2\2\2\u01b2\u01b6")
        buf.write("\7$\2\2\u01b3\u01b5\5\u0081A\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7")
        buf.write("$\2\2\u01ba\u01bb\b@\5\2\u01bb\u0080\3\2\2\2\u01bc\u01bf")
        buf.write("\n\16\2\2\u01bd\u01bf\5\u0083B\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u0082\3\2\2\2\u01c0\u01c1\7^\2\2")
        buf.write("\u01c1\u01c5\t\17\2\2\u01c2\u01c3\7)\2\2\u01c3\u01c5\7")
        buf.write("$\2\2\u01c4\u01c0\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u0084")
        buf.write("\3\2\2\2\u01c6\u01c7\7^\2\2\u01c7\u01c8\n\17\2\2\u01c8")
        buf.write("\u0086\3\2\2\2\u01c9\u01cc\5\'\24\2\u01ca\u01cc\5)\25")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u0088")
        buf.write("\3\2\2\2\u01cd\u01ce\5%\23\2\u01ce\u008a\3\2\2\2\u01cf")
        buf.write("\u01d1\7\17\2\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2")
        buf.write("\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\7\f\2\2\u01d3\u008c")
        buf.write("\3\2\2\2\u01d4\u01d6\t\20\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2")
        buf.write("\u01d8\u01d9\3\2\2\2\u01d9\u01da\bG\6\2\u01da\u008e\3")
        buf.write("\2\2\2\u01db\u01dc\7\61\2\2\u01dc\u01dd\7\61\2\2\u01dd")
        buf.write("\u01e1\3\2\2\2\u01de\u01e0\n\21\2\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e5\bH\6\2\u01e5\u0090\3\2\2\2\u01e6\u01e7\7\61\2\2")
        buf.write("\u01e7\u01e8\7,\2\2\u01e8\u01ed\3\2\2\2\u01e9\u01ec\5")
        buf.write("\u0091I\2\u01ea\u01ec\13\2\2\2\u01eb\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3")
        buf.write("\2\2\2\u01f0\u01f1\7,\2\2\u01f1\u01f2\7\61\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f4\bI\6\2\u01f4\u0092\3\2\2\2\u01f5")
        buf.write("\u01f6\13\2\2\2\u01f6\u01f7\bJ\7\2\u01f7\u0094\3\2\2\2")
        buf.write("\u01f8\u01fc\7$\2\2\u01f9\u01fb\5\u0081A\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u0202\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01ff\u0200\7\17\2\2\u0200\u0203\7\f\2\2\u0201\u0203")
        buf.write("\t\22\2\2\u0202\u01ff\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0205\bK\b\2\u0205\u0096\3\2\2\2")
        buf.write("\u0206\u020a\7$\2\2\u0207\u0209\5\u0081A\2\u0208\u0207")
        buf.write("\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020d\u020e\5\u0085C\2\u020e\u020f\bL\t\2\u020f\u0098")
        buf.write("\3\2\2\2\36\2\u015c\u0164\u0167\u016e\u0177\u0180\u0188")
        buf.write("\u0191\u019a\u019d\u01a3\u01a6\u01aa\u01ae\u01b0\u01b6")
        buf.write("\u01be\u01c4\u01cb\u01d0\u01d7\u01e1\u01eb\u01ed\u01fc")
        buf.write("\u0202\u020a\n\3\67\2\38\3\39\4\3@\5\b\2\2\3J\6\3K\7\3")
        buf.write("L\b")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NEQUAL = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    ADD_ASSIGN = 36
    SUB_ASSIGN = 37
    MUL_ASSIGN = 38
    DIV_ASSIGN = 39
    MOD_ASSIGN = 40
    DOT = 41
    COLON = 42
    COMMA = 43
    COCOM = 44
    COLONEQUAL = 45
    LPAREN = 46
    RPAREN = 47
    LCPAREN = 48
    RCPAREN = 49
    LSPAREN = 50
    RSPAREN = 51
    ID = 52
    DECIMAL_LIT = 53
    BIN_LIT = 54
    OCT_LIT = 55
    HEX_LIT = 56
    INT_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    BOOL_LIT = 60
    NIL_LIT = 61
    NEWLINE = 62
    WS = 63
    COMMENT_LINE = 64
    COMMENT = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "','", "';'", "':='", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "AND", 
            "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "COMMA", "COCOM", 
            "COLONEQUAL", "LPAREN", "RPAREN", "LCPAREN", "RCPAREN", "LSPAREN", 
            "RSPAREN", "ID", "DECIMAL_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", 
            "NEWLINE", "WS", "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NEQUAL", 
                  "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "COLON", "COMMA", "COCOM", "COLONEQUAL", 
                  "LPAREN", "RPAREN", "LCPAREN", "RCPAREN", "LSPAREN", "RSPAREN", 
                  "ID", "DECIMAL_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
                  "INT_LIT", "FLOAT_LIT", "DIGIT", "DIGITS", "OPT_FRAC", 
                  "OPT_EXP", "STRING_LIT", "STRING_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "BOOL_LIT", "NIL_LIT", "NEWLINE", "WS", "COMMENT_LINE", 
                  "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[53] = self.BIN_LIT_action 
            actions[54] = self.OCT_LIT_action 
            actions[55] = self.HEX_LIT_action 
            actions[62] = self.STRING_LIT_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
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

     


