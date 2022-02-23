# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u029c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u0098\n\3\3\4\3\4\3\4\3\4\5\4\u009e\n\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\5\6\u00a8\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u00ae\n\7\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00ba\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00c3")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00d1\n\13\3\f\3\f\5\f\u00d5\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00dc\n\r\3\16\3\16\3\16\5\16\u00e1")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\5\21\u00ea\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00f4")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00fb\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u0105\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\5\30\u010d\n\30\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0113\n\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u011e\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u0128\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\7\35\u0134\n\35\f\35\16")
        buf.write("\35\u0137\13\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u013f")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u014e\n \3!\3!\3!\3!\5!\u0154\n!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\5$\u016b\n$\3%\3%\3%\3%\3%\3%\7%\u0173")
        buf.write("\n%\f%\16%\u0176\13%\3%\3%\6%\u017a\n%\r%\16%\u017b\5")
        buf.write("%\u017e\n%\3%\3%\5%\u0182\n%\3%\3%\7%\u0186\n%\f%\16%")
        buf.write("\u0189\13%\3%\5%\u018c\n%\3%\3%\3%\6%\u0191\n%\r%\16%")
        buf.write("\u0192\3%\3%\3%\5%\u0198\n%\3&\3&\3&\3&\5&\u019e\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u01ac\n")
        buf.write("(\3)\3)\3)\3)\3)\3)\3*\3*\3*\5*\u01b7\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3,\3,\3,\5,\u01c7\n,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\5/\u01d1\n/\3/\3/\3\60\3\60\5\60\u01d7\n\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\5\64\u01f1\n\64\3\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u01f8\n\65\3\66\3\66\3\66\3\66\3\66\5\66\u01ff\n\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0207\n\67\f\67\16")
        buf.write("\67\u020a\13\67\38\38\38\38\38\38\78\u0212\n8\f8\168\u0215")
        buf.write("\138\39\39\39\39\39\39\79\u021d\n9\f9\169\u0220\139\3")
        buf.write(":\3:\3:\5:\u0225\n:\3;\3;\3;\5;\u022a\n;\3<\3<\3<\3<\3")
        buf.write("<\7<\u0231\n<\f<\16<\u0234\13<\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\5=\u0243\n=\7=\u0245\n=\f=\16=\u0248")
        buf.write("\13=\3>\3>\3>\3>\5>\u024e\n>\3?\3?\3?\5?\u0253\n?\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0261\n@\3A\3A\3A\3")
        buf.write("A\3A\3B\3B\5B\u026a\nB\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3E\5E\u027d\nE\3E\3E\3E\7E\u0282\nE\f")
        buf.write("E\16E\u0285\13E\3E\5E\u0288\nE\3F\3F\5F\u028c\nF\3G\3")
        buf.write("G\3G\3G\3G\5G\u0293\nG\3H\3H\3H\3H\3H\3H\3H\3H\2\7lnp")
        buf.write("vxI\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\2\n\4\2\21\21\26")
        buf.write("\26\6\2\6\6\13\13\20\20\25\25\3\2?@\4\2\37\37##\7\2\36")
        buf.write("\36\"\"&&()--\4\2!!%%\4\2\34\34  \5\2$$\'\'++\2\u02ac")
        buf.write("\2\u0090\3\2\2\2\4\u0097\3\2\2\2\6\u0099\3\2\2\2\b\u00a1")
        buf.write("\3\2\2\2\n\u00a7\3\2\2\2\f\u00ad\3\2\2\2\16\u00b1\3\2")
        buf.write("\2\2\20\u00b3\3\2\2\2\22\u00c2\3\2\2\2\24\u00d0\3\2\2")
        buf.write("\2\26\u00d4\3\2\2\2\30\u00db\3\2\2\2\32\u00e0\3\2\2\2")
        buf.write("\34\u00e2\3\2\2\2\36\u00e4\3\2\2\2 \u00e9\3\2\2\2\"\u00eb")
        buf.write("\3\2\2\2$\u00f3\3\2\2\2&\u00fa\3\2\2\2(\u00fc\3\2\2\2")
        buf.write("*\u0104\3\2\2\2,\u0106\3\2\2\2.\u010c\3\2\2\2\60\u0112")
        buf.write("\3\2\2\2\62\u011d\3\2\2\2\64\u0127\3\2\2\2\66\u0129\3")
        buf.write("\2\2\28\u012e\3\2\2\2:\u013a\3\2\2\2<\u0144\3\2\2\2>\u014d")
        buf.write("\3\2\2\2@\u0153\3\2\2\2B\u0161\3\2\2\2D\u0163\3\2\2\2")
        buf.write("F\u016a\3\2\2\2H\u0197\3\2\2\2J\u019d\3\2\2\2L\u019f\3")
        buf.write("\2\2\2N\u01ab\3\2\2\2P\u01ad\3\2\2\2R\u01b6\3\2\2\2T\u01b8")
        buf.write("\3\2\2\2V\u01c6\3\2\2\2X\u01c8\3\2\2\2Z\u01cb\3\2\2\2")
        buf.write("\\\u01ce\3\2\2\2^\u01d6\3\2\2\2`\u01da\3\2\2\2b\u01e0")
        buf.write("\3\2\2\2d\u01e5\3\2\2\2f\u01f0\3\2\2\2h\u01f7\3\2\2\2")
        buf.write("j\u01fe\3\2\2\2l\u0200\3\2\2\2n\u020b\3\2\2\2p\u0216\3")
        buf.write("\2\2\2r\u0224\3\2\2\2t\u0229\3\2\2\2v\u022b\3\2\2\2x\u0235")
        buf.write("\3\2\2\2z\u024d\3\2\2\2|\u0252\3\2\2\2~\u0260\3\2\2\2")
        buf.write("\u0080\u0262\3\2\2\2\u0082\u0269\3\2\2\2\u0084\u026b\3")
        buf.write("\2\2\2\u0086\u0270\3\2\2\2\u0088\u0287\3\2\2\2\u008a\u028b")
        buf.write("\3\2\2\2\u008c\u0292\3\2\2\2\u008e\u0294\3\2\2\2\u0090")
        buf.write("\u0091\5\4\3\2\u0091\u0092\7\2\2\3\u0092\3\3\2\2\2\u0093")
        buf.write("\u0094\5\6\4\2\u0094\u0095\5\4\3\2\u0095\u0098\3\2\2\2")
        buf.write("\u0096\u0098\5\6\4\2\u0097\u0093\3\2\2\2\u0097\u0096\3")
        buf.write("\2\2\2\u0098\5\3\2\2\2\u0099\u009a\7\f\2\2\u009a\u009d")
        buf.write("\7?\2\2\u009b\u009c\7\67\2\2\u009c\u009e\7?\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\5\b\5\2\u00a0\7\3\2\2\2\u00a1\u00a2\7\60")
        buf.write("\2\2\u00a2\u00a3\5\n\6\2\u00a3\u00a4\7\61\2\2\u00a4\t")
        buf.write("\3\2\2\2\u00a5\u00a8\5\f\7\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\13\3\2\2\2\u00a9")
        buf.write("\u00aa\5\16\b\2\u00aa\u00ab\5\f\7\2\u00ab\u00ae\3\2\2")
        buf.write("\2\u00ac\u00ae\5\16\b\2\u00ad\u00a9\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\r\3\2\2\2\u00af\u00b2\5\20\t\2\u00b0\u00b2")
        buf.write("\5 \21\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\17\3\2\2\2\u00b3\u00b9\t\2\2\2\u00b4\u00b5\5\22\n\2\u00b5")
        buf.write("\u00b6\7\67\2\2\u00b6\u00b7\5\32\16\2\u00b7\u00ba\3\2")
        buf.write("\2\2\u00b8\u00ba\5\24\13\2\u00b9\u00b4\3\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7\64\2\2\u00bc")
        buf.write("\21\3\2\2\2\u00bd\u00be\5d\63\2\u00be\u00bf\7\66\2\2\u00bf")
        buf.write("\u00c0\5\22\n\2\u00c0\u00c3\3\2\2\2\u00c1\u00c3\5d\63")
        buf.write("\2\u00c2\u00bd\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\23\3")
        buf.write("\2\2\2\u00c4\u00c5\5d\63\2\u00c5\u00c6\7\66\2\2\u00c6")
        buf.write("\u00c7\5\24\13\2\u00c7\u00c8\7\66\2\2\u00c8\u00c9\5h\65")
        buf.write("\2\u00c9\u00d1\3\2\2\2\u00ca\u00cb\5d\63\2\u00cb\u00cc")
        buf.write("\7\67\2\2\u00cc\u00cd\5\32\16\2\u00cd\u00ce\7,\2\2\u00ce")
        buf.write("\u00cf\5h\65\2\u00cf\u00d1\3\2\2\2\u00d0\u00c4\3\2\2\2")
        buf.write("\u00d0\u00ca\3\2\2\2\u00d1\25\3\2\2\2\u00d2\u00d5\5\30")
        buf.write("\r\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\27\3\2\2\2\u00d6\u00d7\5\64\33\2\u00d7")
        buf.write("\u00d8\7\66\2\2\u00d8\u00d9\5\30\r\2\u00d9\u00dc\3\2\2")
        buf.write("\2\u00da\u00dc\5\64\33\2\u00db\u00d6\3\2\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\31\3\2\2\2\u00dd\u00e1\5\34\17\2\u00de")
        buf.write("\u00e1\5:\36\2\u00df\u00e1\5\36\20\2\u00e0\u00dd\3\2\2")
        buf.write("\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\33\3")
        buf.write("\2\2\2\u00e2\u00e3\t\3\2\2\u00e3\35\3\2\2\2\u00e4\u00e5")
        buf.write("\7?\2\2\u00e5\37\3\2\2\2\u00e6\u00ea\5\"\22\2\u00e7\u00ea")
        buf.write("\5`\61\2\u00e8\u00ea\5b\62\2\u00e9\u00e6\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea!\3\2\2\2\u00eb")
        buf.write("\u00ec\5d\63\2\u00ec\u00ed\7\62\2\2\u00ed\u00ee\5$\23")
        buf.write("\2\u00ee\u00ef\7\63\2\2\u00ef\u00f0\5,\27\2\u00f0#\3\2")
        buf.write("\2\2\u00f1\u00f4\5&\24\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4%\3\2\2\2\u00f5\u00f6")
        buf.write("\5(\25\2\u00f6\u00f7\7\64\2\2\u00f7\u00f8\5&\24\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00fb\5(\25\2\u00fa\u00f5\3\2\2\2")
        buf.write("\u00fa\u00f9\3\2\2\2\u00fb\'\3\2\2\2\u00fc\u00fd\5*\26")
        buf.write("\2\u00fd\u00fe\7\67\2\2\u00fe\u00ff\5\32\16\2\u00ff)\3")
        buf.write("\2\2\2\u0100\u0101\7?\2\2\u0101\u0102\7\66\2\2\u0102\u0105")
        buf.write("\5*\26\2\u0103\u0105\7?\2\2\u0104\u0100\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105+\3\2\2\2\u0106\u0107\7\60\2\2\u0107")
        buf.write("\u0108\5.\30\2\u0108\u0109\7\61\2\2\u0109-\3\2\2\2\u010a")
        buf.write("\u010d\5\60\31\2\u010b\u010d\3\2\2\2\u010c\u010a\3\2\2")
        buf.write("\2\u010c\u010b\3\2\2\2\u010d/\3\2\2\2\u010e\u010f\5\62")
        buf.write("\32\2\u010f\u0110\5\60\31\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u0113\5\62\32\2\u0112\u010e\3\2\2\2\u0112\u0111\3\2\2")
        buf.write("\2\u0113\61\3\2\2\2\u0114\u011e\5<\37\2\u0115\u011e\5")
        buf.write("D#\2\u0116\u011e\5L\'\2\u0117\u011e\5T+\2\u0118\u011e")
        buf.write("\5X-\2\u0119\u011e\5Z.\2\u011a\u011e\5\\/\2\u011b\u011e")
        buf.write("\5^\60\2\u011c\u011e\5,\27\2\u011d\u0114\3\2\2\2\u011d")
        buf.write("\u0115\3\2\2\2\u011d\u0116\3\2\2\2\u011d\u0117\3\2\2\2")
        buf.write("\u011d\u0118\3\2\2\2\u011d\u0119\3\2\2\2\u011d\u011a\3")
        buf.write("\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e\63")
        buf.write("\3\2\2\2\u011f\u0128\7:\2\2\u0120\u0128\79\2\2\u0121\u0128")
        buf.write("\7;\2\2\u0122\u0128\7<\2\2\u0123\u0128\7>\2\2\u0124\u0128")
        buf.write("\5\66\34\2\u0125\u0128\58\35\2\u0126\u0128\7\7\2\2\u0127")
        buf.write("\u011f\3\2\2\2\u0127\u0120\3\2\2\2\u0127\u0121\3\2\2\2")
        buf.write("\u0127\u0122\3\2\2\2\u0127\u0123\3\2\2\2\u0127\u0124\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2\u0128\65")
        buf.write("\3\2\2\2\u0129\u012a\7\24\2\2\u012a\u012b\7\62\2\2\u012b")
        buf.write("\u012c\5\u008aF\2\u012c\u012d\7\63\2\2\u012d\67\3\2\2")
        buf.write("\2\u012e\u012f\7\24\2\2\u012f\u0130\7\62\2\2\u0130\u0135")
        buf.write("\5\66\34\2\u0131\u0132\7\66\2\2\u0132\u0134\5\66\34\2")
        buf.write("\u0133\u0131\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3")
        buf.write("\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u0139\7\63\2\2\u01399\3\2\2\2\u013a\u013b")
        buf.write("\7\24\2\2\u013b\u013e\7.\2\2\u013c\u013f\5\34\17\2\u013d")
        buf.write("\u013f\5:\36\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\u0141\7\66\2\2\u0141\u0142")
        buf.write("\79\2\2\u0142\u0143\7/\2\2\u0143;\3\2\2\2\u0144\u0145")
        buf.write("\t\2\2\2\u0145\u0146\5> \2\u0146\u0147\7\64\2\2\u0147")
        buf.write("=\3\2\2\2\u0148\u0149\5@!\2\u0149\u014a\7\67\2\2\u014a")
        buf.write("\u014b\5\32\16\2\u014b\u014e\3\2\2\2\u014c\u014e\5B\"")
        buf.write("\2\u014d\u0148\3\2\2\2\u014d\u014c\3\2\2\2\u014e?\3\2")
        buf.write("\2\2\u014f\u0150\7?\2\2\u0150\u0151\7\66\2\2\u0151\u0154")
        buf.write("\5@!\2\u0152\u0154\7?\2\2\u0153\u014f\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154A\3\2\2\2\u0155\u0156\7?\2\2\u0156\u0157")
        buf.write("\7\66\2\2\u0157\u0158\5B\"\2\u0158\u0159\7\66\2\2\u0159")
        buf.write("\u015a\5h\65\2\u015a\u0162\3\2\2\2\u015b\u015c\7?\2\2")
        buf.write("\u015c\u015d\7\67\2\2\u015d\u015e\5\32\16\2\u015e\u015f")
        buf.write("\7,\2\2\u015f\u0160\5h\65\2\u0160\u0162\3\2\2\2\u0161")
        buf.write("\u0155\3\2\2\2\u0161\u015b\3\2\2\2\u0162C\3\2\2\2\u0163")
        buf.write("\u0164\5F$\2\u0164\u0165\7,\2\2\u0165\u0166\5h\65\2\u0166")
        buf.write("\u0167\7\64\2\2\u0167E\3\2\2\2\u0168\u016b\5H%\2\u0169")
        buf.write("\u016b\5J&\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("G\3\2\2\2\u016c\u0198\7?\2\2\u016d\u0198\5h\65\2\u016e")
        buf.write("\u016f\7?\2\2\u016f\u0170\7*\2\2\u0170\u017d\7@\2\2\u0171")
        buf.write("\u0173\5f\64\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u017e\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7\65\2\2\u0178")
        buf.write("\u017a\7?\2\2\u0179\u0177\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3")
        buf.write("\2\2\2\u017d\u0174\3\2\2\2\u017d\u0179\3\2\2\2\u017e\u0198")
        buf.write("\3\2\2\2\u017f\u0180\7\33\2\2\u0180\u0182\7\65\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0187\7?\2\2\u0184\u0186\5f\64\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0198\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018c\7\33\2\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2")
        buf.write("\2\u018c\u018d\3\2\2\2\u018d\u0190\7?\2\2\u018e\u018f")
        buf.write("\7\65\2\2\u018f\u0191\7?\2\2\u0190\u018e\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193\u0198\3\2\2\2\u0194\u0195\7?\2\2\u0195\u0196\7")
        buf.write("*\2\2\u0196\u0198\7@\2\2\u0197\u016c\3\2\2\2\u0197\u016d")
        buf.write("\3\2\2\2\u0197\u016e\3\2\2\2\u0197\u0181\3\2\2\2\u0197")
        buf.write("\u018b\3\2\2\2\u0197\u0194\3\2\2\2\u0198I\3\2\2\2\u0199")
        buf.write("\u019a\5h\65\2\u019a\u019b\5f\64\2\u019b\u019e\3\2\2\2")
        buf.write("\u019c\u019e\5h\65\2\u019d\u0199\3\2\2\2\u019d\u019c\3")
        buf.write("\2\2\2\u019eK\3\2\2\2\u019f\u01a0\7\16\2\2\u01a0\u01a1")
        buf.write("\7\62\2\2\u01a1\u01a2\5h\65\2\u01a2\u01a3\7\63\2\2\u01a3")
        buf.write("\u01a4\5,\27\2\u01a4\u01a5\5N(\2\u01a5\u01a6\5R*\2\u01a6")
        buf.write("M\3\2\2\2\u01a7\u01a8\5P)\2\u01a8\u01a9\5N(\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a7\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01acO\3\2\2\2\u01ad\u01ae\7\23\2\2\u01ae")
        buf.write("\u01af\7\62\2\2\u01af\u01b0\5h\65\2\u01b0\u01b1\7\63\2")
        buf.write("\2\u01b1\u01b2\5,\27\2\u01b2Q\3\2\2\2\u01b3\u01b4\7\30")
        buf.write("\2\2\u01b4\u01b7\5,\27\2\u01b5\u01b7\3\2\2\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7S\3\2\2\2\u01b8\u01b9")
        buf.write("\7\5\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\5H%\2\u01bb")
        buf.write("\u01bc\7\31\2\2\u01bc\u01bd\5h\65\2\u01bd\u01be\78\2\2")
        buf.write("\u01be\u01bf\5h\65\2\u01bf\u01c0\5V,\2\u01c0\u01c1\7\63")
        buf.write("\2\2\u01c1\u01c2\5,\27\2\u01c2U\3\2\2\2\u01c3\u01c4\7")
        buf.write("\27\2\2\u01c4\u01c7\5h\65\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7W\3\2\2\2\u01c8")
        buf.write("\u01c9\7\4\2\2\u01c9\u01ca\7\64\2\2\u01caY\3\2\2\2\u01cb")
        buf.write("\u01cc\7\t\2\2\u01cc\u01cd\7\64\2\2\u01cd[\3\2\2\2\u01ce")
        buf.write("\u01d0\7\32\2\2\u01cf\u01d1\5h\65\2\u01d0\u01cf\3\2\2")
        buf.write("\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3")
        buf.write("\7\64\2\2\u01d3]\3\2\2\2\u01d4\u01d7\5\u0086D\2\u01d5")
        buf.write("\u01d7\5\u008eH\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2")
        buf.write("\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7\64\2\2\u01d9_\3")
        buf.write("\2\2\2\u01da\u01db\7\b\2\2\u01db\u01dc\7\62\2\2\u01dc")
        buf.write("\u01dd\5$\23\2\u01dd\u01de\7\63\2\2\u01de\u01df\5,\27")
        buf.write("\2\u01dfa\3\2\2\2\u01e0\u01e1\7\r\2\2\u01e1\u01e2\7\62")
        buf.write("\2\2\u01e2\u01e3\7\63\2\2\u01e3\u01e4\5,\27\2\u01e4c\3")
        buf.write("\2\2\2\u01e5\u01e6\t\4\2\2\u01e6e\3\2\2\2\u01e7\u01e8")
        buf.write("\7.\2\2\u01e8\u01e9\5h\65\2\u01e9\u01ea\7/\2\2\u01ea\u01f1")
        buf.write("\3\2\2\2\u01eb\u01ec\7.\2\2\u01ec\u01ed\5h\65\2\u01ed")
        buf.write("\u01ee\7/\2\2\u01ee\u01ef\5f\64\2\u01ef\u01f1\3\2\2\2")
        buf.write("\u01f0\u01e7\3\2\2\2\u01f0\u01eb\3\2\2\2\u01f1g\3\2\2")
        buf.write("\2\u01f2\u01f3\5j\66\2\u01f3\u01f4\t\5\2\2\u01f4\u01f5")
        buf.write("\5j\66\2\u01f5\u01f8\3\2\2\2\u01f6\u01f8\5j\66\2\u01f7")
        buf.write("\u01f2\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8i\3\2\2\2\u01f9")
        buf.write("\u01fa\5l\67\2\u01fa\u01fb\t\6\2\2\u01fb\u01fc\5l\67\2")
        buf.write("\u01fc\u01ff\3\2\2\2\u01fd\u01ff\5l\67\2\u01fe\u01f9\3")
        buf.write("\2\2\2\u01fe\u01fd\3\2\2\2\u01ffk\3\2\2\2\u0200\u0201")
        buf.write("\b\67\1\2\u0201\u0202\5n8\2\u0202\u0208\3\2\2\2\u0203")
        buf.write("\u0204\f\4\2\2\u0204\u0205\t\7\2\2\u0205\u0207\5n8\2\u0206")
        buf.write("\u0203\3\2\2\2\u0207\u020a\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209m\3\2\2\2\u020a\u0208\3\2\2")
        buf.write("\2\u020b\u020c\b8\1\2\u020c\u020d\5p9\2\u020d\u0213\3")
        buf.write("\2\2\2\u020e\u020f\f\4\2\2\u020f\u0210\t\b\2\2\u0210\u0212")
        buf.write("\5p9\2\u0211\u020e\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211")
        buf.write("\3\2\2\2\u0213\u0214\3\2\2\2\u0214o\3\2\2\2\u0215\u0213")
        buf.write("\3\2\2\2\u0216\u0217\b9\1\2\u0217\u0218\5r:\2\u0218\u021e")
        buf.write("\3\2\2\2\u0219\u021a\f\4\2\2\u021a\u021b\t\t\2\2\u021b")
        buf.write("\u021d\5r:\2\u021c\u0219\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021fq\3\2\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0221\u0222\7\35\2\2\u0222\u0225\5r:\2")
        buf.write("\u0223\u0225\5t;\2\u0224\u0221\3\2\2\2\u0224\u0223\3\2")
        buf.write("\2\2\u0225s\3\2\2\2\u0226\u0227\7 \2\2\u0227\u022a\5t")
        buf.write(";\2\u0228\u022a\5v<\2\u0229\u0226\3\2\2\2\u0229\u0228")
        buf.write("\3\2\2\2\u022au\3\2\2\2\u022b\u022c\b<\1\2\u022c\u022d")
        buf.write("\5x=\2\u022d\u0232\3\2\2\2\u022e\u022f\f\4\2\2\u022f\u0231")
        buf.write("\5f\64\2\u0230\u022e\3\2\2\2\u0231\u0234\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233w\3\2\2\2\u0234")
        buf.write("\u0232\3\2\2\2\u0235\u0236\b=\1\2\u0236\u0237\5z>\2\u0237")
        buf.write("\u0246\3\2\2\2\u0238\u0239\f\4\2\2\u0239\u0242\7\65\2")
        buf.write("\2\u023a\u0243\7?\2\2\u023b\u0243\5\u0080A\2\u023c\u023d")
        buf.write("\7\60\2\2\u023d\u023e\5h\65\2\u023e\u023f\7\61\2\2\u023f")
        buf.write("\u0243\3\2\2\2\u0240\u0241\7?\2\2\u0241\u0243\5f\64\2")
        buf.write("\u0242\u023a\3\2\2\2\u0242\u023b\3\2\2\2\u0242\u023c\3")
        buf.write("\2\2\2\u0242\u0240\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u0238")
        buf.write("\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246")
        buf.write("\u0247\3\2\2\2\u0247y\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write("\u024a\7?\2\2\u024a\u024b\7*\2\2\u024b\u024e\5\u0082B")
        buf.write("\2\u024c\u024e\5|?\2\u024d\u0249\3\2\2\2\u024d\u024c\3")
        buf.write("\2\2\2\u024e{\3\2\2\2\u024f\u0250\7\22\2\2\u0250\u0253")
        buf.write("\5\u0080A\2\u0251\u0253\5~@\2\u0252\u024f\3\2\2\2\u0252")
        buf.write("\u0251\3\2\2\2\u0253}\3\2\2\2\u0254\u0261\5\64\33\2\u0255")
        buf.write("\u0261\7\n\2\2\u0256\u0261\7\17\2\2\u0257\u0261\7?\2\2")
        buf.write("\u0258\u0261\7\33\2\2\u0259\u025a\7?\2\2\u025a\u025b\7")
        buf.write("*\2\2\u025b\u0261\7@\2\2\u025c\u025d\7\62\2\2\u025d\u025e")
        buf.write("\5h\65\2\u025e\u025f\7\63\2\2\u025f\u0261\3\2\2\2\u0260")
        buf.write("\u0254\3\2\2\2\u0260\u0255\3\2\2\2\u0260\u0256\3\2\2\2")
        buf.write("\u0260\u0257\3\2\2\2\u0260\u0258\3\2\2\2\u0260\u0259\3")
        buf.write("\2\2\2\u0260\u025c\3\2\2\2\u0261\177\3\2\2\2\u0262\u0263")
        buf.write("\7?\2\2\u0263\u0264\7\62\2\2\u0264\u0265\5\u008aF\2\u0265")
        buf.write("\u0266\7\63\2\2\u0266\u0081\3\2\2\2\u0267\u026a\7@\2\2")
        buf.write("\u0268\u026a\5\u0084C\2\u0269\u0267\3\2\2\2\u0269\u0268")
        buf.write("\3\2\2\2\u026a\u0083\3\2\2\2\u026b\u026c\7@\2\2\u026c")
        buf.write("\u026d\7\62\2\2\u026d\u026e\5\u008aF\2\u026e\u026f\7\63")
        buf.write("\2\2\u026f\u0085\3\2\2\2\u0270\u0271\5\u0088E\2\u0271")
        buf.write("\u0272\7\65\2\2\u0272\u0273\7?\2\2\u0273\u0274\7\62\2")
        buf.write("\2\u0274\u0275\5\u008aF\2\u0275\u0276\7\63\2\2\u0276\u0087")
        buf.write("\3\2\2\2\u0277\u0288\7?\2\2\u0278\u0279\7\22\2\2\u0279")
        buf.write("\u0288\5\u0080A\2\u027a\u0288\7\33\2\2\u027b\u027d\7\33")
        buf.write("\2\2\u027c\u027b\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027e")
        buf.write("\3\2\2\2\u027e\u0283\7?\2\2\u027f\u0280\7\65\2\2\u0280")
        buf.write("\u0282\7?\2\2\u0281\u027f\3\2\2\2\u0282\u0285\3\2\2\2")
        buf.write("\u0283\u0281\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0288\3")
        buf.write("\2\2\2\u0285\u0283\3\2\2\2\u0286\u0288\5h\65\2\u0287\u0277")
        buf.write("\3\2\2\2\u0287\u0278\3\2\2\2\u0287\u027a\3\2\2\2\u0287")
        buf.write("\u027c\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u0089\3\2\2\2")
        buf.write("\u0289\u028c\5\u008cG\2\u028a\u028c\3\2\2\2\u028b\u0289")
        buf.write("\3\2\2\2\u028b\u028a\3\2\2\2\u028c\u008b\3\2\2\2\u028d")
        buf.write("\u028e\5h\65\2\u028e\u028f\7\66\2\2\u028f\u0290\5\u008c")
        buf.write("G\2\u0290\u0293\3\2\2\2\u0291\u0293\5h\65\2\u0292\u028d")
        buf.write("\3\2\2\2\u0292\u0291\3\2\2\2\u0293\u008d\3\2\2\2\u0294")
        buf.write("\u0295\7?\2\2\u0295\u0296\7*\2\2\u0296\u0297\7@\2\2\u0297")
        buf.write("\u0298\7\62\2\2\u0298\u0299\5\u008aF\2\u0299\u029a\7\63")
        buf.write("\2\2\u029a\u008f\3\2\2\2=\u0097\u009d\u00a7\u00ad\u00b1")
        buf.write("\u00b9\u00c2\u00d0\u00d4\u00db\u00e0\u00e9\u00f3\u00fa")
        buf.write("\u0104\u010c\u0112\u011d\u0127\u0135\u013e\u014d\u0153")
        buf.write("\u0161\u016a\u0174\u017b\u017d\u0181\u0187\u018b\u0192")
        buf.write("\u0197\u019d\u01ab\u01b6\u01c6\u01d0\u01d6\u01f0\u01f7")
        buf.write("\u01fe\u0208\u0213\u021e\u0224\u0229\u0232\u0242\u0246")
        buf.write("\u024d\u0252\u0260\u0269\u027c\u0283\u0287\u028b\u0292")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Foreach'", "'Int'", 
                     "'Null'", "'Constructor'", "'Continue'", "'True'", 
                     "'Float'", "'Class'", "'Destructor'", "'If'", "'False'", 
                     "'Boolean'", "'Val'", "'New'", "'Elseif'", "'Array'", 
                     "'String'", "'Var'", "'By'", "'Else'", "'In'", "'Return'", 
                     "'Self'", "'+'", "'!'", "'!='", "'==.'", "'-'", "'&&'", 
                     "'<'", "'+.'", "'*'", "'||'", "'<='", "'/'", "'=='", 
                     "'>'", "'::'", "'%'", "'='", "'>='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "'.'", "','", "':'", 
                     "'..'" ]

    symbolicNames = [ "<INVALID>", "BLOCK_CMT", "BREAK", "FOREACH", "INT", 
                      "NULL", "CONSTRUCTOR", "CONTINUE", "TRUE", "FLOAT", 
                      "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "VAL", 
                      "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", "ELSE", 
                      "IN", "RETURN", "SELF", "ADD", "NOT", "NOT_EQUAL", 
                      "EQUALDOT", "SUB", "AND", "LT", "ADDDOT", "MUL", "OR", 
                      "LE", "DIV", "EQUAL", "GT", "SC", "MOD", "ASSIGN", 
                      "GE", "LSB", "RSB", "LB", "RB", "LP", "RP", "SM", 
                      "DOT", "CM", "Extended", "FROMTO", "INTERGER_GT_ZERO", 
                      "INTEGER", "FLOAT_NUMBER", "BOOLEAN_LITERAL", "UNCLOSE_STRING", 
                      "STRING_LITERAL", "ID", "DOLLARID", "WS", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declares = 1
    RULE_class_declare = 2
    RULE_member_decl = 3
    RULE_memberlist = 4
    RULE_members = 5
    RULE_member = 6
    RULE_att_declare = 7
    RULE_att_names = 8
    RULE_att_init_value = 9
    RULE_values = 10
    RULE_value = 11
    RULE_data_type = 12
    RULE_primitive_type = 13
    RULE_classtype = 14
    RULE_method_declare = 15
    RULE_func_declare = 16
    RULE_paramlist = 17
    RULE_params = 18
    RULE_param = 19
    RULE_idnamelist = 20
    RULE_blockstatment = 21
    RULE_stamentlist = 22
    RULE_staments = 23
    RULE_stament = 24
    RULE_literal = 25
    RULE_index_array_literal = 26
    RULE_multi_array = 27
    RULE_array_type = 28
    RULE_vardecl_stm = 29
    RULE_varlist = 30
    RULE_variable_names = 31
    RULE_variable_init_value = 32
    RULE_assign_stm = 33
    RULE_leftassign = 34
    RULE_scalarvar = 35
    RULE_indexed_exp = 36
    RULE_if_stm = 37
    RULE_elseif_stms = 38
    RULE_elseif_stm = 39
    RULE_else_stm = 40
    RULE_forin_stm = 41
    RULE_steploop = 42
    RULE_break_stm = 43
    RULE_continue_stm = 44
    RULE_return_stm = 45
    RULE_method_invocation_stm = 46
    RULE_contructor_declare = 47
    RULE_detructor_declare = 48
    RULE_idname = 49
    RULE_index_operator = 50
    RULE_exp = 51
    RULE_exp0 = 52
    RULE_exp1 = 53
    RULE_exp2 = 54
    RULE_exp3 = 55
    RULE_exp4 = 56
    RULE_exp5 = 57
    RULE_exp6 = 58
    RULE_exp7 = 59
    RULE_exp8 = 60
    RULE_exp9 = 61
    RULE_exp10 = 62
    RULE_func_call = 63
    RULE_static_operand = 64
    RULE_static_func_call = 65
    RULE_method_invocate = 66
    RULE_object_exp = 67
    RULE_explists = 68
    RULE_explist = 69
    RULE_static_method_invocate = 70

    ruleNames =  [ "program", "class_declares", "class_declare", "member_decl", 
                   "memberlist", "members", "member", "att_declare", "att_names", 
                   "att_init_value", "values", "value", "data_type", "primitive_type", 
                   "classtype", "method_declare", "func_declare", "paramlist", 
                   "params", "param", "idnamelist", "blockstatment", "stamentlist", 
                   "staments", "stament", "literal", "index_array_literal", 
                   "multi_array", "array_type", "vardecl_stm", "varlist", 
                   "variable_names", "variable_init_value", "assign_stm", 
                   "leftassign", "scalarvar", "indexed_exp", "if_stm", "elseif_stms", 
                   "elseif_stm", "else_stm", "forin_stm", "steploop", "break_stm", 
                   "continue_stm", "return_stm", "method_invocation_stm", 
                   "contructor_declare", "detructor_declare", "idname", 
                   "index_operator", "exp", "exp0", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "func_call", "static_operand", "static_func_call", "method_invocate", 
                   "object_exp", "explists", "explist", "static_method_invocate" ]

    EOF = Token.EOF
    BLOCK_CMT=1
    BREAK=2
    FOREACH=3
    INT=4
    NULL=5
    CONSTRUCTOR=6
    CONTINUE=7
    TRUE=8
    FLOAT=9
    CLASS=10
    DESTRUCTOR=11
    IF=12
    FALSE=13
    BOOLEAN=14
    VAL=15
    NEW=16
    ELSEIF=17
    ARRAY=18
    STRING=19
    VAR=20
    BY=21
    ELSE=22
    IN=23
    RETURN=24
    SELF=25
    ADD=26
    NOT=27
    NOT_EQUAL=28
    EQUALDOT=29
    SUB=30
    AND=31
    LT=32
    ADDDOT=33
    MUL=34
    OR=35
    LE=36
    DIV=37
    EQUAL=38
    GT=39
    SC=40
    MOD=41
    ASSIGN=42
    GE=43
    LSB=44
    RSB=45
    LB=46
    RB=47
    LP=48
    RP=49
    SM=50
    DOT=51
    CM=52
    Extended=53
    FROMTO=54
    INTERGER_GT_ZERO=55
    INTEGER=56
    FLOAT_NUMBER=57
    BOOLEAN_LITERAL=58
    UNCLOSE_STRING=59
    STRING_LITERAL=60
    ID=61
    DOLLARID=62
    WS=63
    ILLEGAL_ESCAPE=64
    ERROR_CHAR=65

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

        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.class_declares()
            self.state = 143
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declaresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declares" ):
                return visitor.visitClass_declares(self)
            else:
                return visitor.visitChildren(self)




    def class_declares(self):

        localctx = D96Parser.Class_declaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declares)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.class_declare()
                self.state = 146
                self.class_declares()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.class_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def member_decl(self):
            return self.getTypedRuleContext(D96Parser.Member_declContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D96Parser.CLASS)
            self.state = 152
            self.match(D96Parser.ID)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Extended:
                self.state = 153
                self.match(D96Parser.Extended)
                self.state = 154
                self.match(D96Parser.ID)


            self.state = 157
            self.member_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_decl" ):
                return visitor.visitMember_decl(self)
            else:
                return visitor.visitChildren(self)




    def member_decl(self):

        localctx = D96Parser.Member_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(D96Parser.LB)
            self.state = 160
            self.memberlist()
            self.state = 161
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = D96Parser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.VAL, D96Parser.VAR, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.members()
                pass
            elif token in [D96Parser.RB]:
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


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def members(self):
            return self.getTypedRuleContext(D96Parser.MembersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = D96Parser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_members)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.member()
                self.state = 168
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_declare(self):
            return self.getTypedRuleContext(D96Parser.Att_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.att_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.method_declare()
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


    class Att_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def att_names(self):
            return self.getTypedRuleContext(D96Parser.Att_namesContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def att_init_value(self):
            return self.getTypedRuleContext(D96Parser.Att_init_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_att_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_declare" ):
                return visitor.visitAtt_declare(self)
            else:
                return visitor.visitChildren(self)




    def att_declare(self):

        localctx = D96Parser.Att_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_att_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 178
                self.att_names()
                self.state = 179
                self.match(D96Parser.Extended)
                self.state = 180
                self.data_type()
                pass

            elif la_ == 2:
                self.state = 182
                self.att_init_value()
                pass


            self.state = 185
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def att_names(self):
            return self.getTypedRuleContext(D96Parser.Att_namesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_att_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_names" ):
                return visitor.visitAtt_names(self)
            else:
                return visitor.visitChildren(self)




    def att_names(self):

        localctx = D96Parser.Att_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_att_names)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.idname()
                self.state = 188
                self.match(D96Parser.CM)
                self.state = 189
                self.att_names()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.idname()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_init_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def att_init_value(self):
            return self.getTypedRuleContext(D96Parser.Att_init_valueContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_init_value" ):
                return visitor.visitAtt_init_value(self)
            else:
                return visitor.visitChildren(self)




    def att_init_value(self):

        localctx = D96Parser.Att_init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_att_init_value)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.idname()
                self.state = 195
                self.match(D96Parser.CM)
                self.state = 196
                self.att_init_value()
                self.state = 197
                self.match(D96Parser.CM)
                self.state = 198
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.idname()
                self.state = 201
                self.match(D96Parser.Extended)
                self.state = 202
                self.data_type()
                self.state = 203
                self.match(D96Parser.ASSIGN)
                self.state = 204
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = D96Parser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_values)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NULL, D96Parser.ARRAY, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.value()
                pass
            elif token in [D96Parser.EOF]:
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.literal()
                self.state = 213
                self.match(D96Parser.CM)
                self.state = 214
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def classtype(self):
            return self.getTypedRuleContext(D96Parser.ClasstypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data_type)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.classtype()
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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


    class ClasstypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstype" ):
                return visitor.visitClasstype(self)
            else:
                return visitor.visitChildren(self)




    def classtype(self):

        localctx = D96Parser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_declare(self):
            return self.getTypedRuleContext(D96Parser.Func_declareContext,0)


        def contructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Contructor_declareContext,0)


        def detructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Detructor_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_method_declare)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.func_declare()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.contructor_declare()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.detructor_declare()
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


    class Func_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = D96Parser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.idname()
            self.state = 234
            self.match(D96Parser.LP)
            self.state = 235
            self.paramlist()
            self.state = 236
            self.match(D96Parser.RP)
            self.state = 237
            self.blockstatment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramlist)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.params()
                pass
            elif token in [D96Parser.RP]:
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


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_params)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.param()
                self.state = 244
                self.match(D96Parser.SM)
                self.state = 245
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idnamelist(self):
            return self.getTypedRuleContext(D96Parser.IdnamelistContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.idnamelist()
            self.state = 251
            self.match(D96Parser.Extended)
            self.state = 252
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdnamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def idnamelist(self):
            return self.getTypedRuleContext(D96Parser.IdnamelistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idnamelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdnamelist" ):
                return visitor.visitIdnamelist(self)
            else:
                return visitor.visitChildren(self)




    def idnamelist(self):

        localctx = D96Parser.IdnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idnamelist)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(D96Parser.ID)
                self.state = 255
                self.match(D96Parser.CM)
                self.state = 256
                self.idnamelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def stamentlist(self):
            return self.getTypedRuleContext(D96Parser.StamentlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_blockstatment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstatment" ):
                return visitor.visitBlockstatment(self)
            else:
                return visitor.visitChildren(self)




    def blockstatment(self):

        localctx = D96Parser.BlockstatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(D96Parser.LB)
            self.state = 261
            self.stamentlist()
            self.state = 262
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StamentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staments(self):
            return self.getTypedRuleContext(D96Parser.StamentsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stamentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStamentlist" ):
                return visitor.visitStamentlist(self)
            else:
                return visitor.visitChildren(self)




    def stamentlist(self):

        localctx = D96Parser.StamentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stamentlist)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BREAK, D96Parser.FOREACH, D96Parser.NULL, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.IF, D96Parser.FALSE, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.RETURN, D96Parser.SELF, D96Parser.NOT, D96Parser.SUB, D96Parser.LB, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.staments()
                pass
            elif token in [D96Parser.RB]:
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


    class StamentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stament(self):
            return self.getTypedRuleContext(D96Parser.StamentContext,0)


        def staments(self):
            return self.getTypedRuleContext(D96Parser.StamentsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_staments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaments" ):
                return visitor.visitStaments(self)
            else:
                return visitor.visitChildren(self)




    def staments(self):

        localctx = D96Parser.StamentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_staments)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.stament()
                self.state = 269
                self.staments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.stament()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StamentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl_stm(self):
            return self.getTypedRuleContext(D96Parser.Vardecl_stmContext,0)


        def assign_stm(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(D96Parser.If_stmContext,0)


        def forin_stm(self):
            return self.getTypedRuleContext(D96Parser.Forin_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(D96Parser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(D96Parser.Return_stmContext,0)


        def method_invocation_stm(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_stmContext,0)


        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stament

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStament" ):
                return visitor.visitStament(self)
            else:
                return visitor.visitChildren(self)




    def stament(self):

        localctx = D96Parser.StamentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stament)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.vardecl_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.assign_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.if_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.forin_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 278
                self.break_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.continue_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 280
                self.return_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 281
                self.method_invocation_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 282
                self.blockstatment()
                pass


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

        def INTEGER(self):
            return self.getToken(D96Parser.INTEGER, 0)

        def INTERGER_GT_ZERO(self):
            return self.getToken(D96Parser.INTERGER_GT_ZERO, 0)

        def FLOAT_NUMBER(self):
            return self.getToken(D96Parser.FLOAT_NUMBER, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def index_array_literal(self):
            return self.getTypedRuleContext(D96Parser.Index_array_literalContext,0)


        def multi_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_arrayContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 285
                self.match(D96Parser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 286
                self.match(D96Parser.INTERGER_GT_ZERO)
                pass

            elif la_ == 3:
                self.state = 287
                self.match(D96Parser.FLOAT_NUMBER)
                pass

            elif la_ == 4:
                self.state = 288
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.state = 289
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 6:
                self.state = 290
                self.index_array_literal()
                pass

            elif la_ == 7:
                self.state = 291
                self.multi_array()
                pass

            elif la_ == 8:
                self.state = 292
                self.match(D96Parser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def explists(self):
            return self.getTypedRuleContext(D96Parser.ExplistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_array_literal" ):
                return visitor.visitIndex_array_literal(self)
            else:
                return visitor.visitChildren(self)




    def index_array_literal(self):

        localctx = D96Parser.Index_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(D96Parser.ARRAY)
            self.state = 296
            self.match(D96Parser.LP)
            self.state = 297
            self.explists()
            self.state = 298
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def index_array_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Index_array_literalContext)
            else:
                return self.getTypedRuleContext(D96Parser.Index_array_literalContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_array" ):
                return visitor.visitMulti_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_array(self):

        localctx = D96Parser.Multi_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_multi_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(D96Parser.ARRAY)
            self.state = 301
            self.match(D96Parser.LP)
            self.state = 302
            self.index_array_literal()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 303
                self.match(D96Parser.CM)
                self.state = 304
                self.index_array_literal()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self.match(D96Parser.RP)
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

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INTERGER_GT_ZERO(self):
            return self.getToken(D96Parser.INTERGER_GT_ZERO, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.ARRAY)
            self.state = 313
            self.match(D96Parser.LSB)
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 314
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 315
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 318
            self.match(D96Parser.CM)
            self.state = 319
            self.match(D96Parser.INTERGER_GT_ZERO)
            self.state = 320
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vardecl_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_stm" ):
                return visitor.visitVardecl_stm(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_stm(self):

        localctx = D96Parser.Vardecl_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_vardecl_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 323
            self.varlist()
            self.state = 324
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_names(self):
            return self.getTypedRuleContext(D96Parser.Variable_namesContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def variable_init_value(self):
            return self.getTypedRuleContext(D96Parser.Variable_init_valueContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = D96Parser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_varlist)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.variable_names()
                self.state = 327
                self.match(D96Parser.Extended)
                self.state = 328
                self.data_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.variable_init_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def variable_names(self):
            return self.getTypedRuleContext(D96Parser.Variable_namesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_names" ):
                return visitor.visitVariable_names(self)
            else:
                return visitor.visitChildren(self)




    def variable_names(self):

        localctx = D96Parser.Variable_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_variable_names)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(D96Parser.ID)
                self.state = 334
                self.match(D96Parser.CM)
                self.state = 335
                self.variable_names()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_init_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def variable_init_value(self):
            return self.getTypedRuleContext(D96Parser.Variable_init_valueContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def Extended(self):
            return self.getToken(D96Parser.Extended, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_init_value" ):
                return visitor.visitVariable_init_value(self)
            else:
                return visitor.visitChildren(self)




    def variable_init_value(self):

        localctx = D96Parser.Variable_init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_variable_init_value)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(D96Parser.ID)
                self.state = 340
                self.match(D96Parser.CM)
                self.state = 341
                self.variable_init_value()
                self.state = 342
                self.match(D96Parser.CM)
                self.state = 343
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(D96Parser.ID)
                self.state = 346
                self.match(D96Parser.Extended)
                self.state = 347
                self.data_type()
                self.state = 348
                self.match(D96Parser.ASSIGN)
                self.state = 349
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leftassign(self):
            return self.getTypedRuleContext(D96Parser.LeftassignContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = D96Parser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.leftassign()
            self.state = 354
            self.match(D96Parser.ASSIGN)
            self.state = 355
            self.exp()
            self.state = 356
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarvar(self):
            return self.getTypedRuleContext(D96Parser.ScalarvarContext,0)


        def indexed_exp(self):
            return self.getTypedRuleContext(D96Parser.Indexed_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_leftassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftassign" ):
                return visitor.visitLeftassign(self)
            else:
                return visitor.visitChildren(self)




    def leftassign(self):

        localctx = D96Parser.LeftassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_leftassign)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.scalarvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.indexed_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SC(self):
            return self.getToken(D96Parser.SC, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def index_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Index_operatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.Index_operatorContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalarvar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarvar" ):
                return visitor.visitScalarvar(self)
            else:
                return visitor.visitChildren(self)




    def scalarvar(self):

        localctx = D96Parser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_scalarvar)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.match(D96Parser.ID)
                self.state = 365
                self.match(D96Parser.SC)
                self.state = 366
                self.match(D96Parser.DOLLARID)
                self.state = 379
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.IN, D96Parser.ASSIGN, D96Parser.LSB]:
                    self.state = 370
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.LSB:
                        self.state = 367
                        self.index_operator()
                        self.state = 372
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                elif token in [D96Parser.DOT]:
                    self.state = 375 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 373
                        self.match(D96Parser.DOT)
                        self.state = 374
                        self.match(D96Parser.ID)
                        self.state = 377 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==D96Parser.DOT):
                            break

                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.SELF:
                    self.state = 381
                    self.match(D96Parser.SELF)
                    self.state = 382
                    self.match(D96Parser.DOT)


                self.state = 385
                self.match(D96Parser.ID)
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.LSB:
                    self.state = 386
                    self.index_operator()
                    self.state = 391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.SELF:
                    self.state = 392
                    self.match(D96Parser.SELF)


                self.state = 395
                self.match(D96Parser.ID)
                self.state = 398 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 396
                    self.match(D96Parser.DOT)
                    self.state = 397
                    self.match(D96Parser.ID)
                    self.state = 400 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.DOT):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 402
                self.match(D96Parser.ID)
                self.state = 403
                self.match(D96Parser.SC)
                self.state = 404
                self.match(D96Parser.DOLLARID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_exp" ):
                return visitor.visitIndexed_exp(self)
            else:
                return visitor.visitChildren(self)




    def indexed_exp(self):

        localctx = D96Parser.Indexed_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_indexed_exp)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.exp()
                self.state = 408
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def elseif_stms(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmsContext,0)


        def else_stm(self):
            return self.getTypedRuleContext(D96Parser.Else_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = D96Parser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(D96Parser.IF)
            self.state = 414
            self.match(D96Parser.LP)
            self.state = 415
            self.exp()
            self.state = 416
            self.match(D96Parser.RP)
            self.state = 417
            self.blockstatment()
            self.state = 418
            self.elseif_stms()
            self.state = 419
            self.else_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stm(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmContext,0)


        def elseif_stms(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stms" ):
                return visitor.visitElseif_stms(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stms(self):

        localctx = D96Parser.Elseif_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elseif_stms)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.elseif_stm()
                self.state = 422
                self.elseif_stms()
                pass
            elif token in [D96Parser.BREAK, D96Parser.FOREACH, D96Parser.NULL, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.IF, D96Parser.FALSE, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.ELSE, D96Parser.RETURN, D96Parser.SELF, D96Parser.NOT, D96Parser.SUB, D96Parser.LB, D96Parser.RB, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
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


    class Elseif_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stm" ):
                return visitor.visitElseif_stm(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stm(self):

        localctx = D96Parser.Elseif_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elseif_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(D96Parser.ELSEIF)
            self.state = 428
            self.match(D96Parser.LP)
            self.state = 429
            self.exp()
            self.state = 430
            self.match(D96Parser.RP)
            self.state = 431
            self.blockstatment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stm" ):
                return visitor.visitElse_stm(self)
            else:
                return visitor.visitChildren(self)




    def else_stm(self):

        localctx = D96Parser.Else_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_else_stm)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(D96Parser.ELSE)
                self.state = 434
                self.blockstatment()
                pass
            elif token in [D96Parser.BREAK, D96Parser.FOREACH, D96Parser.NULL, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.IF, D96Parser.FALSE, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.RETURN, D96Parser.SELF, D96Parser.NOT, D96Parser.SUB, D96Parser.LB, D96Parser.RB, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
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


    class Forin_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def scalarvar(self):
            return self.getTypedRuleContext(D96Parser.ScalarvarContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def FROMTO(self):
            return self.getToken(D96Parser.FROMTO, 0)

        def steploop(self):
            return self.getTypedRuleContext(D96Parser.SteploopContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_forin_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin_stm" ):
                return visitor.visitForin_stm(self)
            else:
                return visitor.visitChildren(self)




    def forin_stm(self):

        localctx = D96Parser.Forin_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forin_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.FOREACH)
            self.state = 439
            self.match(D96Parser.LP)
            self.state = 440
            self.scalarvar()
            self.state = 441
            self.match(D96Parser.IN)
            self.state = 442
            self.exp()
            self.state = 443
            self.match(D96Parser.FROMTO)
            self.state = 444
            self.exp()
            self.state = 445
            self.steploop()
            self.state = 446
            self.match(D96Parser.RP)
            self.state = 447
            self.blockstatment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SteploopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_steploop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSteploop" ):
                return visitor.visitSteploop(self)
            else:
                return visitor.visitChildren(self)




    def steploop(self):

        localctx = D96Parser.SteploopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_steploop)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(D96Parser.BY)
                self.state = 450
                self.exp()
                pass
            elif token in [D96Parser.RP]:
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


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = D96Parser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(D96Parser.BREAK)
            self.state = 455
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = D96Parser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(D96Parser.CONTINUE)
            self.state = 458
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = D96Parser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(D96Parser.RETURN)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NULL) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.LP) | (1 << D96Parser.INTERGER_GT_ZERO) | (1 << D96Parser.INTEGER) | (1 << D96Parser.FLOAT_NUMBER) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ID))) != 0):
                self.state = 461
                self.exp()


            self.state = 464
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Method_invocateContext,0)


        def static_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stm" ):
                return visitor.visitMethod_invocation_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stm(self):

        localctx = D96Parser.Method_invocation_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_method_invocation_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 466
                self.method_invocate()
                pass

            elif la_ == 2:
                self.state = 467
                self.static_method_invocate()
                pass


            self.state = 470
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Contructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_contructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContructor_declare" ):
                return visitor.visitContructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def contructor_declare(self):

        localctx = D96Parser.Contructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_contructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 473
            self.match(D96Parser.LP)
            self.state = 474
            self.paramlist()
            self.state = 475
            self.match(D96Parser.RP)
            self.state = 476
            self.blockstatment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockstatment(self):
            return self.getTypedRuleContext(D96Parser.BlockstatmentContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_detructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetructor_declare" ):
                return visitor.visitDetructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def detructor_declare(self):

        localctx = D96Parser.Detructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_detructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(D96Parser.DESTRUCTOR)
            self.state = 479
            self.match(D96Parser.LP)
            self.state = 480
            self.match(D96Parser.RP)
            self.state = 481
            self.blockstatment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdname" ):
                return visitor.visitIdname(self)
            else:
                return visitor.visitChildren(self)




    def idname(self):

        localctx = D96Parser.IdnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_idname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLARID):
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


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_index_operator)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(D96Parser.LSB)
                self.state = 486
                self.exp()
                self.state = 487
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(D96Parser.LSB)
                self.state = 490
                self.exp()
                self.state = 491
                self.match(D96Parser.RSB)
                self.state = 492
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp0Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp0Context,i)


        def ADDDOT(self):
            return self.getToken(D96Parser.ADDDOT, 0)

        def EQUALDOT(self):
            return self.getToken(D96Parser.EQUALDOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.exp0()
                self.state = 497
                _la = self._input.LA(1)
                if not(_la==D96Parser.EQUALDOT or _la==D96Parser.ADDDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 498
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_exp0)
        self._la = 0 # Token type
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.exp1(0)
                self.state = 504
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LE) | (1 << D96Parser.EQUAL) | (1 << D96Parser.GT) | (1 << D96Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 505
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 513
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 514
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 515
                    self.exp2(0) 
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 524
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 525
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 526
                    self.exp3(0) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 535
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 536
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 537
                    self.exp4() 
                self.state = 542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = D96Parser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_exp4)
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(D96Parser.NOT)
                self.state = 544
                self.exp4()
                pass
            elif token in [D96Parser.NULL, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.exp5()
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


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_exp5)
        try:
            self.state = 551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(D96Parser.SUB)
                self.state = 549
                self.exp5()
                pass
            elif token in [D96Parser.NULL, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.exp6(0)
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


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.exp7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 556
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 557
                    self.index_operator() 
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(D96Parser.Func_callContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 580
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 566
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 567
                    self.match(D96Parser.DOT)
                    self.state = 576
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                    if la_ == 1:
                        self.state = 568
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 569
                        self.func_call()
                        pass

                    elif la_ == 3:
                        self.state = 570
                        self.match(D96Parser.LB)
                        self.state = 571
                        self.exp()
                        self.state = 572
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 4:
                        self.state = 574
                        self.match(D96Parser.ID)
                        self.state = 575
                        self.index_operator()
                        pass

             
                self.state = 582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SC(self):
            return self.getToken(D96Parser.SC, 0)

        def static_operand(self):
            return self.getTypedRuleContext(D96Parser.Static_operandContext,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = D96Parser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_exp8)
        try:
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(D96Parser.ID)
                self.state = 584
                self.match(D96Parser.SC)
                self.state = 585
                self.static_operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def func_call(self):
            return self.getTypedRuleContext(D96Parser.Func_callContext,0)


        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_exp9)
        try:
            self.state = 592
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.match(D96Parser.NEW)
                self.state = 590
                self.func_call()
                pass
            elif token in [D96Parser.NULL, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.exp10()
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


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def SC(self):
            return self.getToken(D96Parser.SC, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_exp10)
        try:
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
                self.match(D96Parser.TRUE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 596
                self.match(D96Parser.FALSE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 597
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 598
                self.match(D96Parser.SELF)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 599
                self.match(D96Parser.ID)
                self.state = 600
                self.match(D96Parser.SC)
                self.state = 601
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 602
                self.match(D96Parser.LP)
                self.state = 603
                self.exp()
                self.state = 604
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def explists(self):
            return self.getTypedRuleContext(D96Parser.ExplistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = D96Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(D96Parser.ID)
            self.state = 609
            self.match(D96Parser.LP)
            self.state = 610
            self.explists()
            self.state = 611
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_operandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def static_func_call(self):
            return self.getTypedRuleContext(D96Parser.Static_func_callContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_operand" ):
                return visitor.visitStatic_operand(self)
            else:
                return visitor.visitChildren(self)




    def static_operand(self):

        localctx = D96Parser.Static_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_static_operand)
        try:
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.static_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def explists(self):
            return self.getTypedRuleContext(D96Parser.ExplistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_func_call" ):
                return visitor.visitStatic_func_call(self)
            else:
                return visitor.visitChildren(self)




    def static_func_call(self):

        localctx = D96Parser.Static_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_static_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(D96Parser.DOLLARID)
            self.state = 618
            self.match(D96Parser.LP)
            self.state = 619
            self.explists()
            self.state = 620
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_exp(self):
            return self.getTypedRuleContext(D96Parser.Object_expContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def explists(self):
            return self.getTypedRuleContext(D96Parser.ExplistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocate" ):
                return visitor.visitMethod_invocate(self)
            else:
                return visitor.visitChildren(self)




    def method_invocate(self):

        localctx = D96Parser.Method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_method_invocate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.object_exp()
            self.state = 623
            self.match(D96Parser.DOT)
            self.state = 624
            self.match(D96Parser.ID)
            self.state = 625
            self.match(D96Parser.LP)
            self.state = 626
            self.explists()
            self.state = 627
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def func_call(self):
            return self.getTypedRuleContext(D96Parser.Func_callContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_exp" ):
                return visitor.visitObject_exp(self)
            else:
                return visitor.visitChildren(self)




    def object_exp(self):

        localctx = D96Parser.Object_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_object_exp)
        self._la = 0 # Token type
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 630
                self.match(D96Parser.NEW)
                self.state = 631
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 632
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 634
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.SELF:
                    self.state = 633
                    self.match(D96Parser.SELF)


                self.state = 636
                self.match(D96Parser.ID)
                self.state = 641
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 637
                        self.match(D96Parser.DOT)
                        self.state = 638
                        self.match(D96Parser.ID) 
                    self.state = 643
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 644
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_explists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplists" ):
                return visitor.visitExplists(self)
            else:
                return visitor.visitChildren(self)




    def explists(self):

        localctx = D96Parser.ExplistsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_explists)
        try:
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NULL, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NOT, D96Parser.SUB, D96Parser.LP, D96Parser.INTERGER_GT_ZERO, D96Parser.INTEGER, D96Parser.FLOAT_NUMBER, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.explist()
                pass
            elif token in [D96Parser.RP]:
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


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = D96Parser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_explist)
        try:
            self.state = 656
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.exp()
                self.state = 652
                self.match(D96Parser.CM)
                self.state = 653
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 655
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SC(self):
            return self.getToken(D96Parser.SC, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def explists(self):
            return self.getTypedRuleContext(D96Parser.ExplistsContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocate" ):
                return visitor.visitStatic_method_invocate(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocate(self):

        localctx = D96Parser.Static_method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_static_method_invocate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(D96Parser.ID)
            self.state = 659
            self.match(D96Parser.SC)
            self.state = 660
            self.match(D96Parser.DOLLARID)
            self.state = 661
            self.match(D96Parser.LP)
            self.state = 662
            self.explists()
            self.state = 663
            self.match(D96Parser.RP)
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
        self._predicates[53] = self.exp1_sempred
        self._predicates[54] = self.exp2_sempred
        self._predicates[55] = self.exp3_sempred
        self._predicates[58] = self.exp6_sempred
        self._predicates[59] = self.exp7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




