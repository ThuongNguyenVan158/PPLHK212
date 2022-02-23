// Generated from D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BLOCK_CMT=1, BREAK=2, FOREACH=3, INT=4, NULL=5, CONSTRUCTOR=6, CONTINUE=7, 
		TRUE=8, FLOAT=9, CLASS=10, DESTRUCTOR=11, IF=12, FALSE=13, BOOLEAN=14, 
		VAL=15, NEW=16, ELSEIF=17, ARRAY=18, STRING=19, VAR=20, BY=21, ELSE=22, 
		IN=23, RETURN=24, SELF=25, ADD=26, NOT=27, NOT_EQUAL=28, EQUALDOT=29, 
		SUB=30, AND=31, LT=32, ADDDOT=33, MUL=34, OR=35, LE=36, DIV=37, EQUAL=38, 
		GT=39, SC=40, MOD=41, ASSIGN=42, GE=43, LSB=44, RSB=45, LB=46, RB=47, 
		LP=48, RP=49, SM=50, DOT=51, CM=52, Extended=53, FROMTO=54, INTERGER_GT_ZERO=55, 
		INTEGER=56, FLOAT_NUMBER=57, BOOLEAN_LITERAL=58, STRING_LITERAL=59, ID=60, 
		DOLLARID=61, WS=62, UNCLOSE_STRING=63, ILLEGAL_ESCAPE=64, ERROR_CHAR=65;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BLOCK_CMT", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", "CONTINUE", 
			"TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", "VAL", 
			"NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", "ELSE", "IN", "RETURN", 
			"SELF", "ADD", "NOT", "NOT_EQUAL", "EQUALDOT", "SUB", "AND", "LT", "ADDDOT", 
			"MUL", "OR", "LE", "DIV", "EQUAL", "GT", "SC", "MOD", "ASSIGN", "GE", 
			"LSB", "RSB", "LB", "RB", "LP", "RP", "SM", "DOT", "CM", "Extended", 
			"FROMTO", "INTERGER_GT_ZERO", "INTEGER", "DECIMAL_INTEGER", "DECIMAL_INTEGER_GT_ZERO", 
			"OCT_INTEGER", "OCT_INTEGER_GT_ZERO", "HEX_INTEGER", "HEX_INTEGER_GT_ZERO", 
			"BIN_INTEGER", "BIN_INTEGER_GT_ZERO", "FLOAT_NUMBER", "BOOLEAN_LITERAL", 
			"STRING_LITERAL", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", "NON_OCT_DIGIT", 
			"HEX_DIGIT", "NON_HEX_DIGIT", "BIN_DIGIT", "NON_BIN_DIGIT", "POINT_FLOAT", 
			"EXPONENT_FLOAT", "INT_PART", "FRACTION", "EXPONENT", "STR_CHAR", "ESC_SEQ", 
			"ID", "DOLLARID", "ESC_ILLEGAL", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'Break'", "'Foreach'", "'Int'", "'Null'", "'Constructor'", 
			"'Continue'", "'True'", "'Float'", "'Class'", "'Destructor'", "'If'", 
			"'False'", "'Boolean'", "'Val'", "'New'", "'Elseif'", "'Array'", "'String'", 
			"'Var'", "'By'", "'Else'", "'In'", "'Return'", "'Self'", "'+'", "'!'", 
			"'!='", "'==.'", "'-'", "'&&'", "'<'", "'+.'", "'*'", "'||'", "'<='", 
			"'/'", "'=='", "'>'", "'::'", "'%'", "'='", "'>='", "'['", "']'", "'{'", 
			"'}'", "'('", "')'", "';'", "'.'", "','", "':'", "'..'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BLOCK_CMT", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
			"CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", "IF", "FALSE", "BOOLEAN", 
			"VAL", "NEW", "ELSEIF", "ARRAY", "STRING", "VAR", "BY", "ELSE", "IN", 
			"RETURN", "SELF", "ADD", "NOT", "NOT_EQUAL", "EQUALDOT", "SUB", "AND", 
			"LT", "ADDDOT", "MUL", "OR", "LE", "DIV", "EQUAL", "GT", "SC", "MOD", 
			"ASSIGN", "GE", "LSB", "RSB", "LB", "RB", "LP", "RP", "SM", "DOT", "CM", 
			"Extended", "FROMTO", "INTERGER_GT_ZERO", "INTEGER", "FLOAT_NUMBER", 
			"BOOLEAN_LITERAL", "STRING_LITERAL", "ID", "DOLLARID", "WS", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public D96Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C\u02d7\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\2\3\2\3\2\7\2\u00bb\n\2"+
		"\f\2\16\2\u00be\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33"+
		"\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3"+
		"!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3"+
		")\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62"+
		"\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\38\38\5"+
		"8\u019e\n8\39\39\39\39\59\u01a4\n9\3:\3:\7:\u01a8\n:\f:\16:\u01ab\13:"+
		"\3:\5:\u01ae\n:\3:\6:\u01b1\n:\r:\16:\u01b2\7:\u01b5\n:\f:\16:\u01b8\13"+
		":\3:\5:\u01bb\n:\3;\3;\7;\u01bf\n;\f;\16;\u01c2\13;\3;\5;\u01c5\n;\3;"+
		"\6;\u01c8\n;\r;\16;\u01c9\7;\u01cc\n;\f;\16;\u01cf\13;\3<\3<\3<\7<\u01d4"+
		"\n<\f<\16<\u01d7\13<\3<\5<\u01da\n<\3<\6<\u01dd\n<\r<\16<\u01de\7<\u01e1"+
		"\n<\f<\16<\u01e4\13<\3<\3<\5<\u01e8\n<\3=\3=\3=\7=\u01ed\n=\f=\16=\u01f0"+
		"\13=\3=\5=\u01f3\n=\3=\6=\u01f6\n=\r=\16=\u01f7\7=\u01fa\n=\f=\16=\u01fd"+
		"\13=\3>\3>\3>\3>\7>\u0203\n>\f>\16>\u0206\13>\3>\5>\u0209\n>\3>\6>\u020c"+
		"\n>\r>\16>\u020d\7>\u0210\n>\f>\16>\u0213\13>\3>\3>\3>\5>\u0218\n>\3?"+
		"\3?\3?\3?\7?\u021e\n?\f?\16?\u0221\13?\3?\5?\u0224\n?\3?\6?\u0227\n?\r"+
		"?\16?\u0228\7?\u022b\n?\f?\16?\u022e\13?\3@\3@\3@\3@\7@\u0234\n@\f@\16"+
		"@\u0237\13@\3@\5@\u023a\n@\3@\6@\u023d\n@\r@\16@\u023e\7@\u0241\n@\f@"+
		"\16@\u0244\13@\3@\3@\3@\5@\u0249\n@\3A\3A\3A\3A\7A\u024f\nA\fA\16A\u0252"+
		"\13A\3A\5A\u0255\nA\3A\6A\u0258\nA\rA\16A\u0259\7A\u025c\nA\fA\16A\u025f"+
		"\13A\3B\3B\5B\u0263\nB\3C\3C\5C\u0267\nC\3D\3D\7D\u026b\nD\fD\16D\u026e"+
		"\13D\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3M\3"+
		"M\3M\3M\5M\u0288\nM\3N\3N\5N\u028c\nN\3N\3N\3O\3O\3P\3P\7P\u0294\nP\f"+
		"P\16P\u0297\13P\3Q\3Q\5Q\u029b\nQ\3Q\6Q\u029e\nQ\rQ\16Q\u029f\3R\3R\3"+
		"R\3R\5R\u02a6\nR\3S\3S\3S\3T\3T\7T\u02ad\nT\fT\16T\u02b0\13T\3U\3U\6U"+
		"\u02b4\nU\rU\16U\u02b5\3V\3V\3V\3V\3V\5V\u02bd\nV\3W\6W\u02c0\nW\rW\16"+
		"W\u02c1\3W\3W\3X\3X\7X\u02c8\nX\fX\16X\u02cb\13X\3Y\3Y\7Y\u02cf\nY\fY"+
		"\16Y\u02d2\13Y\3Y\3Y\3Z\3Z\3\u00bc\2[\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.["+
		"/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y\2{\2}\2\177\2\u0081"+
		"\2\u0083;\u0085<\u0087=\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093"+
		"\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5"+
		"\2\u00a7>\u00a9?\u00ab\2\u00ad@\u00afA\u00b1B\u00b3C\3\2\23\4\2ZZzz\4"+
		"\2DDdd\3\2\63;\3\2\62;\3\2\629\3\2\639\4\2\62;CH\4\2\63;CH\3\2\62\63\4"+
		"\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;"+
		"C\\aac|\3\2$$\5\2\13\f\16\17\"\"\2\u02fb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3"+
		"\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2"+
		"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)"+
		"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2"+
		"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2"+
		"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3"+
		"\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2"+
		"\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2"+
		"g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2\u0083"+
		"\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2"+
		"\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\3\u00b5"+
		"\3\2\2\2\5\u00c4\3\2\2\2\7\u00ca\3\2\2\2\t\u00d2\3\2\2\2\13\u00d6\3\2"+
		"\2\2\r\u00db\3\2\2\2\17\u00e7\3\2\2\2\21\u00f0\3\2\2\2\23\u00f5\3\2\2"+
		"\2\25\u00fb\3\2\2\2\27\u0101\3\2\2\2\31\u010c\3\2\2\2\33\u010f\3\2\2\2"+
		"\35\u0115\3\2\2\2\37\u011d\3\2\2\2!\u0121\3\2\2\2#\u0125\3\2\2\2%\u012c"+
		"\3\2\2\2\'\u0132\3\2\2\2)\u0139\3\2\2\2+\u013d\3\2\2\2-\u0140\3\2\2\2"+
		"/\u0145\3\2\2\2\61\u0148\3\2\2\2\63\u014f\3\2\2\2\65\u0154\3\2\2\2\67"+
		"\u0156\3\2\2\29\u0158\3\2\2\2;\u015b\3\2\2\2=\u015f\3\2\2\2?\u0161\3\2"+
		"\2\2A\u0164\3\2\2\2C\u0166\3\2\2\2E\u0169\3\2\2\2G\u016b\3\2\2\2I\u016e"+
		"\3\2\2\2K\u0171\3\2\2\2M\u0173\3\2\2\2O\u0176\3\2\2\2Q\u0178\3\2\2\2S"+
		"\u017b\3\2\2\2U\u017d\3\2\2\2W\u017f\3\2\2\2Y\u0182\3\2\2\2[\u0184\3\2"+
		"\2\2]\u0186\3\2\2\2_\u0188\3\2\2\2a\u018a\3\2\2\2c\u018c\3\2\2\2e\u018e"+
		"\3\2\2\2g\u0190\3\2\2\2i\u0192\3\2\2\2k\u0194\3\2\2\2m\u0196\3\2\2\2o"+
		"\u019d\3\2\2\2q\u01a3\3\2\2\2s\u01ba\3\2\2\2u\u01bc\3\2\2\2w\u01e7\3\2"+
		"\2\2y\u01e9\3\2\2\2{\u0217\3\2\2\2}\u0219\3\2\2\2\177\u0248\3\2\2\2\u0081"+
		"\u024a\3\2\2\2\u0083\u0262\3\2\2\2\u0085\u0266\3\2\2\2\u0087\u0268\3\2"+
		"\2\2\u0089\u0271\3\2\2\2\u008b\u0273\3\2\2\2\u008d\u0275\3\2\2\2\u008f"+
		"\u0277\3\2\2\2\u0091\u0279\3\2\2\2\u0093\u027b\3\2\2\2\u0095\u027d\3\2"+
		"\2\2\u0097\u027f\3\2\2\2\u0099\u0287\3\2\2\2\u009b\u0289\3\2\2\2\u009d"+
		"\u028f\3\2\2\2\u009f\u0291\3\2\2\2\u00a1\u0298\3\2\2\2\u00a3\u02a5\3\2"+
		"\2\2\u00a5\u02a7\3\2\2\2\u00a7\u02aa\3\2\2\2\u00a9\u02b1\3\2\2\2\u00ab"+
		"\u02bc\3\2\2\2\u00ad\u02bf\3\2\2\2\u00af\u02c5\3\2\2\2\u00b1\u02cc\3\2"+
		"\2\2\u00b3\u02d5\3\2\2\2\u00b5\u00b6\7%\2\2\u00b6\u00b7\7%\2\2\u00b7\u00bc"+
		"\3\2\2\2\u00b8\u00bb\5\3\2\2\u00b9\u00bb\13\2\2\2\u00ba\u00b8\3\2\2\2"+
		"\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bc\u00ba"+
		"\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7%\2\2\u00c0"+
		"\u00c1\7%\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\2\2\2\u00c3\4\3\2\2\2"+
		"\u00c4\u00c5\7D\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8"+
		"\7c\2\2\u00c8\u00c9\7m\2\2\u00c9\6\3\2\2\2\u00ca\u00cb\7H\2\2\u00cb\u00cc"+
		"\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7c\2\2\u00cf"+
		"\u00d0\7e\2\2\u00d0\u00d1\7j\2\2\u00d1\b\3\2\2\2\u00d2\u00d3\7K\2\2\u00d3"+
		"\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\n\3\2\2\2\u00d6\u00d7\7P\2\2\u00d7"+
		"\u00d8\7w\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7n\2\2\u00da\f\3\2\2\2\u00db"+
		"\u00dc\7E\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7u\2\2"+
		"\u00df\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3"+
		"\7e\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7t\2\2\u00e6"+
		"\16\3\2\2\2\u00e7\u00e8\7E\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea"+
		"\u00eb\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2"+
		"\u00ee\u00ef\7g\2\2\u00ef\20\3\2\2\2\u00f0\u00f1\7V\2\2\u00f1\u00f2\7"+
		"t\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4\7g\2\2\u00f4\22\3\2\2\2\u00f5\u00f6"+
		"\7H\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7c\2\2\u00f9"+
		"\u00fa\7v\2\2\u00fa\24\3\2\2\2\u00fb\u00fc\7E\2\2\u00fc\u00fd\7n\2\2\u00fd"+
		"\u00fe\7c\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7u\2\2\u0100\26\3\2\2\2\u0101"+
		"\u0102\7F\2\2\u0102\u0103\7g\2\2\u0103\u0104\7u\2\2\u0104\u0105\7v\2\2"+
		"\u0105\u0106\7t\2\2\u0106\u0107\7w\2\2\u0107\u0108\7e\2\2\u0108\u0109"+
		"\7v\2\2\u0109\u010a\7q\2\2\u010a\u010b\7t\2\2\u010b\30\3\2\2\2\u010c\u010d"+
		"\7K\2\2\u010d\u010e\7h\2\2\u010e\32\3\2\2\2\u010f\u0110\7H\2\2\u0110\u0111"+
		"\7c\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114"+
		"\34\3\2\2\2\u0115\u0116\7D\2\2\u0116\u0117\7q\2\2\u0117\u0118\7q\2\2\u0118"+
		"\u0119\7n\2\2\u0119\u011a\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c\7p\2\2"+
		"\u011c\36\3\2\2\2\u011d\u011e\7X\2\2\u011e\u011f\7c\2\2\u011f\u0120\7"+
		"n\2\2\u0120 \3\2\2\2\u0121\u0122\7P\2\2\u0122\u0123\7g\2\2\u0123\u0124"+
		"\7y\2\2\u0124\"\3\2\2\2\u0125\u0126\7G\2\2\u0126\u0127\7n\2\2\u0127\u0128"+
		"\7u\2\2\u0128\u0129\7g\2\2\u0129\u012a\7k\2\2\u012a\u012b\7h\2\2\u012b"+
		"$\3\2\2\2\u012c\u012d\7C\2\2\u012d\u012e\7t\2\2\u012e\u012f\7t\2\2\u012f"+
		"\u0130\7c\2\2\u0130\u0131\7{\2\2\u0131&\3\2\2\2\u0132\u0133\7U\2\2\u0133"+
		"\u0134\7v\2\2\u0134\u0135\7t\2\2\u0135\u0136\7k\2\2\u0136\u0137\7p\2\2"+
		"\u0137\u0138\7i\2\2\u0138(\3\2\2\2\u0139\u013a\7X\2\2\u013a\u013b\7c\2"+
		"\2\u013b\u013c\7t\2\2\u013c*\3\2\2\2\u013d\u013e\7D\2\2\u013e\u013f\7"+
		"{\2\2\u013f,\3\2\2\2\u0140\u0141\7G\2\2\u0141\u0142\7n\2\2\u0142\u0143"+
		"\7u\2\2\u0143\u0144\7g\2\2\u0144.\3\2\2\2\u0145\u0146\7K\2\2\u0146\u0147"+
		"\7p\2\2\u0147\60\3\2\2\2\u0148\u0149\7T\2\2\u0149\u014a\7g\2\2\u014a\u014b"+
		"\7v\2\2\u014b\u014c\7w\2\2\u014c\u014d\7t\2\2\u014d\u014e\7p\2\2\u014e"+
		"\62\3\2\2\2\u014f\u0150\7U\2\2\u0150\u0151\7g\2\2\u0151\u0152\7n\2\2\u0152"+
		"\u0153\7h\2\2\u0153\64\3\2\2\2\u0154\u0155\7-\2\2\u0155\66\3\2\2\2\u0156"+
		"\u0157\7#\2\2\u01578\3\2\2\2\u0158\u0159\7#\2\2\u0159\u015a\7?\2\2\u015a"+
		":\3\2\2\2\u015b\u015c\7?\2\2\u015c\u015d\7?\2\2\u015d\u015e\7\60\2\2\u015e"+
		"<\3\2\2\2\u015f\u0160\7/\2\2\u0160>\3\2\2\2\u0161\u0162\7(\2\2\u0162\u0163"+
		"\7(\2\2\u0163@\3\2\2\2\u0164\u0165\7>\2\2\u0165B\3\2\2\2\u0166\u0167\7"+
		"-\2\2\u0167\u0168\7\60\2\2\u0168D\3\2\2\2\u0169\u016a\7,\2\2\u016aF\3"+
		"\2\2\2\u016b\u016c\7~\2\2\u016c\u016d\7~\2\2\u016dH\3\2\2\2\u016e\u016f"+
		"\7>\2\2\u016f\u0170\7?\2\2\u0170J\3\2\2\2\u0171\u0172\7\61\2\2\u0172L"+
		"\3\2\2\2\u0173\u0174\7?\2\2\u0174\u0175\7?\2\2\u0175N\3\2\2\2\u0176\u0177"+
		"\7@\2\2\u0177P\3\2\2\2\u0178\u0179\7<\2\2\u0179\u017a\7<\2\2\u017aR\3"+
		"\2\2\2\u017b\u017c\7\'\2\2\u017cT\3\2\2\2\u017d\u017e\7?\2\2\u017eV\3"+
		"\2\2\2\u017f\u0180\7@\2\2\u0180\u0181\7?\2\2\u0181X\3\2\2\2\u0182\u0183"+
		"\7]\2\2\u0183Z\3\2\2\2\u0184\u0185\7_\2\2\u0185\\\3\2\2\2\u0186\u0187"+
		"\7}\2\2\u0187^\3\2\2\2\u0188\u0189\7\177\2\2\u0189`\3\2\2\2\u018a\u018b"+
		"\7*\2\2\u018bb\3\2\2\2\u018c\u018d\7+\2\2\u018dd\3\2\2\2\u018e\u018f\7"+
		"=\2\2\u018ff\3\2\2\2\u0190\u0191\7\60\2\2\u0191h\3\2\2\2\u0192\u0193\7"+
		".\2\2\u0193j\3\2\2\2\u0194\u0195\7<\2\2\u0195l\3\2\2\2\u0196\u0197\7\60"+
		"\2\2\u0197\u0198\7\60\2\2\u0198n\3\2\2\2\u0199\u019e\5u;\2\u019a\u019e"+
		"\5y=\2\u019b\u019e\5}?\2\u019c\u019e\5\u0081A\2\u019d\u0199\3\2\2\2\u019d"+
		"\u019a\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019ep\3\2\2\2"+
		"\u019f\u01a4\5s:\2\u01a0\u01a4\5w<\2\u01a1\u01a4\5{>\2\u01a2\u01a4\5\177"+
		"@\2\u01a3\u019f\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3"+
		"\u01a2\3\2\2\2\u01a4r\3\2\2\2\u01a5\u01a9\5\u0089E\2\u01a6\u01a8\5\u008b"+
		"F\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9"+
		"\u01aa\3\2\2\2\u01aa\u01b6\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\7a"+
		"\2\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af"+
		"\u01b1\5\u008bF\2\u01b0\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0"+
		"\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01ad\3\2\2\2\u01b5"+
		"\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01bb\3\2"+
		"\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bb\7\62\2\2\u01ba\u01a5\3\2\2\2\u01ba"+
		"\u01b9\3\2\2\2\u01bbt\3\2\2\2\u01bc\u01c0\5\u0089E\2\u01bd\u01bf\5\u008b"+
		"F\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0"+
		"\u01c1\3\2\2\2\u01c1\u01cd\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\7a"+
		"\2\2\u01c4\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6"+
		"\u01c8\5\u008bF\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7"+
		"\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01c4\3\2\2\2\u01cc"+
		"\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01cev\3\2\2\2"+
		"\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7\62\2\2\u01d1\u01d5\5\u008fH\2\u01d2"+
		"\u01d4\5\u008dG\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3"+
		"\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01e2\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8"+
		"\u01da\7a\2\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2"+
		"\2\2\u01db\u01dd\5\u008dG\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de"+
		"\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01d9\3\2"+
		"\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3"+
		"\u01e8\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7\62\2\2\u01e6\u01e8\7"+
		"\62\2\2\u01e7\u01d0\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8x\3\2\2\2\u01e9\u01ea"+
		"\7\62\2\2\u01ea\u01ee\5\u008fH\2\u01eb\u01ed\5\u008dG\2\u01ec\u01eb\3"+
		"\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef"+
		"\u01fb\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f3\7a\2\2\u01f2\u01f1\3\2"+
		"\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f6\5\u008dG\2\u01f5"+
		"\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2"+
		"\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f2\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb"+
		"\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fcz\3\2\2\2\u01fd\u01fb\3\2\2\2"+
		"\u01fe\u01ff\7\62\2\2\u01ff\u0200\t\2\2\2\u0200\u0204\5\u0093J\2\u0201"+
		"\u0203\5\u0091I\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202"+
		"\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0211\3\2\2\2\u0206\u0204\3\2\2\2\u0207"+
		"\u0209\7a\2\2\u0208\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2"+
		"\2\2\u020a\u020c\5\u0091I\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d"+
		"\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u0208\3\2"+
		"\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212"+
		"\u0218\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0215\7\62\2\2\u0215\u0216\t"+
		"\2\2\2\u0216\u0218\7\62\2\2\u0217\u01fe\3\2\2\2\u0217\u0214\3\2\2\2\u0218"+
		"|\3\2\2\2\u0219\u021a\7\62\2\2\u021a\u021b\t\2\2\2\u021b\u021f\5\u0093"+
		"J\2\u021c\u021e\5\u0091I\2\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f"+
		"\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u022c\3\2\2\2\u0221\u021f\3\2"+
		"\2\2\u0222\u0224\7a\2\2\u0223\u0222\3\2\2\2\u0223\u0224\3\2\2\2\u0224"+
		"\u0226\3\2\2\2\u0225\u0227\5\u0091I\2\u0226\u0225\3\2\2\2\u0227\u0228"+
		"\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2\u022a"+
		"\u0223\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2"+
		"\2\2\u022d~\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\7\62\2\2\u0230\u0231"+
		"\t\3\2\2\u0231\u0235\5\u0097L\2\u0232\u0234\5\u0095K\2\u0233\u0232\3\2"+
		"\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236"+
		"\u0242\3\2\2\2\u0237\u0235\3\2\2\2\u0238\u023a\7a\2\2\u0239\u0238\3\2"+
		"\2\2\u0239\u023a\3\2\2\2\u023a\u023c\3\2\2\2\u023b\u023d\5\u0095K\2\u023c"+
		"\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2"+
		"\2\2\u023f\u0241\3\2\2\2\u0240\u0239\3\2\2\2\u0241\u0244\3\2\2\2\u0242"+
		"\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0249\3\2\2\2\u0244\u0242\3\2"+
		"\2\2\u0245\u0246\7\62\2\2\u0246\u0247\t\3\2\2\u0247\u0249\7\62\2\2\u0248"+
		"\u022f\3\2\2\2\u0248\u0245\3\2\2\2\u0249\u0080\3\2\2\2\u024a\u024b\7\62"+
		"\2\2\u024b\u024c\t\3\2\2\u024c\u0250\5\u0097L\2\u024d\u024f\5\u0095K\2"+
		"\u024e\u024d\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251"+
		"\3\2\2\2\u0251\u025d\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0255\7a\2\2\u0254"+
		"\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0257\3\2\2\2\u0256\u0258\5\u0095"+
		"K\2\u0257\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0257\3\2\2\2\u0259"+
		"\u025a\3\2\2\2\u025a\u025c\3\2\2\2\u025b\u0254\3\2\2\2\u025c\u025f\3\2"+
		"\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0082\3\2\2\2\u025f"+
		"\u025d\3\2\2\2\u0260\u0263\5\u0099M\2\u0261\u0263\5\u009bN\2\u0262\u0260"+
		"\3\2\2\2\u0262\u0261\3\2\2\2\u0263\u0084\3\2\2\2\u0264\u0267\5\21\t\2"+
		"\u0265\u0267\5\33\16\2\u0266\u0264\3\2\2\2\u0266\u0265\3\2\2\2\u0267\u0086"+
		"\3\2\2\2\u0268\u026c\7$\2\2\u0269\u026b\5\u00a3R\2\u026a\u0269\3\2\2\2"+
		"\u026b\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026f"+
		"\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0270\7$\2\2\u0270\u0088\3\2\2\2\u0271"+
		"\u0272\t\4\2\2\u0272\u008a\3\2\2\2\u0273\u0274\t\5\2\2\u0274\u008c\3\2"+
		"\2\2\u0275\u0276\t\6\2\2\u0276\u008e\3\2\2\2\u0277\u0278\t\7\2\2\u0278"+
		"\u0090\3\2\2\2\u0279\u027a\t\b\2\2\u027a\u0092\3\2\2\2\u027b\u027c\t\t"+
		"\2\2\u027c\u0094\3\2\2\2\u027d\u027e\t\n\2\2\u027e\u0096\3\2\2\2\u027f"+
		"\u0280\7\63\2\2\u0280\u0098\3\2\2\2\u0281\u0282\5\u009dO\2\u0282\u0283"+
		"\5\u009fP\2\u0283\u0288\3\2\2\2\u0284\u0285\5\u009fP\2\u0285\u0286\5\u00a1"+
		"Q\2\u0286\u0288\3\2\2\2\u0287\u0281\3\2\2\2\u0287\u0284\3\2\2\2\u0288"+
		"\u009a\3\2\2\2\u0289\u028b\5\u009dO\2\u028a\u028c\5\u009fP\2\u028b\u028a"+
		"\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028e\5\u00a1Q"+
		"\2\u028e\u009c\3\2\2\2\u028f\u0290\5s:\2\u0290\u009e\3\2\2\2\u0291\u0295"+
		"\7\60\2\2\u0292\u0294\5\u008bF\2\u0293\u0292\3\2\2\2\u0294\u0297\3\2\2"+
		"\2\u0295\u0293\3\2\2\2\u0295\u0296\3\2\2\2\u0296\u00a0\3\2\2\2\u0297\u0295"+
		"\3\2\2\2\u0298\u029a\t\13\2\2\u0299\u029b\t\f\2\2\u029a\u0299\3\2\2\2"+
		"\u029a\u029b\3\2\2\2\u029b\u029d\3\2\2\2\u029c\u029e\5\u008bF\2\u029d"+
		"\u029c\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2"+
		"\2\2\u02a0\u00a2\3\2\2\2\u02a1\u02a2\7)\2\2\u02a2\u02a6\7$\2\2\u02a3\u02a6"+
		"\n\r\2\2\u02a4\u02a6\5\u00a5S\2\u02a5\u02a1\3\2\2\2\u02a5\u02a3\3\2\2"+
		"\2\u02a5\u02a4\3\2\2\2\u02a6\u00a4\3\2\2\2\u02a7\u02a8\7^\2\2\u02a8\u02a9"+
		"\t\16\2\2\u02a9\u00a6\3\2\2\2\u02aa\u02ae\t\17\2\2\u02ab\u02ad\t\20\2"+
		"\2\u02ac\u02ab\3\2\2\2\u02ad\u02b0\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02af"+
		"\3\2\2\2\u02af\u00a8\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b1\u02b3\7&\2\2\u02b2"+
		"\u02b4\t\20\2\2\u02b3\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b5\u02b3\3"+
		"\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u00aa\3\2\2\2\u02b7\u02b8\7^\2\2\u02b8"+
		"\u02bd\n\16\2\2\u02b9\u02ba\7)\2\2\u02ba\u02bd\n\21\2\2\u02bb\u02bd\7"+
		"^\2\2\u02bc\u02b7\3\2\2\2\u02bc\u02b9\3\2\2\2\u02bc\u02bb\3\2\2\2\u02bd"+
		"\u00ac\3\2\2\2\u02be\u02c0\t\22\2\2\u02bf\u02be\3\2\2\2\u02c0\u02c1\3"+
		"\2\2\2\u02c1\u02bf\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3"+
		"\u02c4\bW\2\2\u02c4\u00ae\3\2\2\2\u02c5\u02c9\7$\2\2\u02c6\u02c8\5\u00a3"+
		"R\2\u02c7\u02c6\3\2\2\2\u02c8\u02cb\3\2\2\2\u02c9\u02c7\3\2\2\2\u02c9"+
		"\u02ca\3\2\2\2\u02ca\u00b0\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cc\u02d0\7$"+
		"\2\2\u02cd\u02cf\5\u00a3R\2\u02ce\u02cd\3\2\2\2\u02cf\u02d2\3\2\2\2\u02d0"+
		"\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d3\3\2\2\2\u02d2\u02d0\3\2"+
		"\2\2\u02d3\u02d4\5\u00abV\2\u02d4\u00b2\3\2\2\2\u02d5\u02d6\13\2\2\2\u02d6"+
		"\u00b4\3\2\2\2:\2\u00ba\u00bc\u019d\u01a3\u01a9\u01ad\u01b2\u01b6\u01ba"+
		"\u01c0\u01c4\u01c9\u01cd\u01d5\u01d9\u01de\u01e2\u01e7\u01ee\u01f2\u01f7"+
		"\u01fb\u0204\u0208\u020d\u0211\u0217\u021f\u0223\u0228\u022c\u0235\u0239"+
		"\u023e\u0242\u0248\u0250\u0254\u0259\u025d\u0262\u0266\u026c\u0287\u028b"+
		"\u0295\u029a\u029f\u02a5\u02ae\u02b5\u02bc\u02c1\u02c9\u02d0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}