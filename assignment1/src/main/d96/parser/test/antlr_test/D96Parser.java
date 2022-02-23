// Generated from D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Parser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_class_declares = 1, RULE_class_declare = 2, RULE_member_decl = 3, 
		RULE_memberlist = 4, RULE_members = 5, RULE_member = 6, RULE_att_declare = 7, 
		RULE_att_names = 8, RULE_att_init_value = 9, RULE_values = 10, RULE_value = 11, 
		RULE_data_type = 12, RULE_primitive_type = 13, RULE_classtype = 14, RULE_method_declare = 15, 
		RULE_func_declare = 16, RULE_paramlist = 17, RULE_params = 18, RULE_param = 19, 
		RULE_idnamelist = 20, RULE_blockstatment = 21, RULE_stamentlist = 22, 
		RULE_staments = 23, RULE_stament = 24, RULE_literal = 25, RULE_index_array_literal = 26, 
		RULE_primitive_literal = 27, RULE_multi_array = 28, RULE_array_type = 29, 
		RULE_vardecl_stm = 30, RULE_varlist = 31, RULE_variable_names = 32, RULE_variable_init_value = 33, 
		RULE_assign_stm = 34, RULE_leftassign = 35, RULE_scalarvar = 36, RULE_indexed_exp = 37, 
		RULE_if_stm = 38, RULE_elseif_stms = 39, RULE_elseif_stm = 40, RULE_else_stm = 41, 
		RULE_forin_stm = 42, RULE_steploop = 43, RULE_break_stm = 44, RULE_continue_stm = 45, 
		RULE_return_stm = 46, RULE_method_invocation_stm = 47, RULE_contructor_declare = 48, 
		RULE_detructor_declare = 49, RULE_idname = 50, RULE_index_operator = 51, 
		RULE_exp = 52, RULE_exp0 = 53, RULE_exp1 = 54, RULE_exp2 = 55, RULE_exp3 = 56, 
		RULE_exp4 = 57, RULE_exp5 = 58, RULE_exp6 = 59, RULE_exp7 = 60, RULE_exp8 = 61, 
		RULE_exp9 = 62, RULE_exp10 = 63, RULE_func_call = 64, RULE_static_operand = 65, 
		RULE_static_func_call = 66, RULE_method_invocate = 67, RULE_object_exp = 68, 
		RULE_object_exp1 = 69, RULE_explists = 70, RULE_explist = 71, RULE_static_method_invocate = 72;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_declares", "class_declare", "member_decl", "memberlist", 
			"members", "member", "att_declare", "att_names", "att_init_value", "values", 
			"value", "data_type", "primitive_type", "classtype", "method_declare", 
			"func_declare", "paramlist", "params", "param", "idnamelist", "blockstatment", 
			"stamentlist", "staments", "stament", "literal", "index_array_literal", 
			"primitive_literal", "multi_array", "array_type", "vardecl_stm", "varlist", 
			"variable_names", "variable_init_value", "assign_stm", "leftassign", 
			"scalarvar", "indexed_exp", "if_stm", "elseif_stms", "elseif_stm", "else_stm", 
			"forin_stm", "steploop", "break_stm", "continue_stm", "return_stm", "method_invocation_stm", 
			"contructor_declare", "detructor_declare", "idname", "index_operator", 
			"exp", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", 
			"exp8", "exp9", "exp10", "func_call", "static_operand", "static_func_call", 
			"method_invocate", "object_exp", "object_exp1", "explists", "explist", 
			"static_method_invocate"
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

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public D96Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public Class_declaresContext class_declares() {
			return getRuleContext(Class_declaresContext.class,0);
		}
		public TerminalNode EOF() { return getToken(D96Parser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			class_declares();
			setState(147);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declaresContext extends ParserRuleContext {
		public Class_declareContext class_declare() {
			return getRuleContext(Class_declareContext.class,0);
		}
		public Class_declaresContext class_declares() {
			return getRuleContext(Class_declaresContext.class,0);
		}
		public Class_declaresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_declares; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterClass_declares(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitClass_declares(this);
		}
	}

	public final Class_declaresContext class_declares() throws RecognitionException {
		Class_declaresContext _localctx = new Class_declaresContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_declares);
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(149);
				class_declare();
				setState(150);
				class_declares();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				class_declare();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declareContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(D96Parser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public Member_declContext member_decl() {
			return getRuleContext(Member_declContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Class_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterClass_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitClass_declare(this);
		}
	}

	public final Class_declareContext class_declare() throws RecognitionException {
		Class_declareContext _localctx = new Class_declareContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_class_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(CLASS);
			setState(156);
			match(ID);
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Extended) {
				{
				setState(157);
				match(Extended);
				setState(158);
				match(ID);
				}
			}

			setState(161);
			member_decl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Member_declContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public MemberlistContext memberlist() {
			return getRuleContext(MemberlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Member_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_member_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMember_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMember_decl(this);
		}
	}

	public final Member_declContext member_decl() throws RecognitionException {
		Member_declContext _localctx = new Member_declContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_member_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(LB);
			setState(164);
			memberlist();
			setState(165);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemberlistContext extends ParserRuleContext {
		public MembersContext members() {
			return getRuleContext(MembersContext.class,0);
		}
		public MemberlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memberlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMemberlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMemberlist(this);
		}
	}

	public final MemberlistContext memberlist() throws RecognitionException {
		MemberlistContext _localctx = new MemberlistContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_memberlist);
		try {
			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONSTRUCTOR:
			case DESTRUCTOR:
			case VAL:
			case VAR:
			case ID:
			case DOLLARID:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				members();
				}
				break;
			case RB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MembersContext extends ParserRuleContext {
		public MemberContext member() {
			return getRuleContext(MemberContext.class,0);
		}
		public MembersContext members() {
			return getRuleContext(MembersContext.class,0);
		}
		public MembersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_members; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMembers(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMembers(this);
		}
	}

	public final MembersContext members() throws RecognitionException {
		MembersContext _localctx = new MembersContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_members);
		try {
			setState(175);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				member();
				setState(172);
				members();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(174);
				member();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemberContext extends ParserRuleContext {
		public Att_declareContext att_declare() {
			return getRuleContext(Att_declareContext.class,0);
		}
		public Method_declareContext method_declare() {
			return getRuleContext(Method_declareContext.class,0);
		}
		public MemberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_member; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMember(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMember(this);
		}
	}

	public final MemberContext member() throws RecognitionException {
		MemberContext _localctx = new MemberContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_member);
		try {
			setState(179);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAL:
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				att_declare();
				}
				break;
			case CONSTRUCTOR:
			case DESTRUCTOR:
			case ID:
			case DOLLARID:
				enterOuterAlt(_localctx, 2);
				{
				setState(178);
				method_declare();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Att_declareContext extends ParserRuleContext {
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public TerminalNode VAL() { return getToken(D96Parser.VAL, 0); }
		public TerminalNode VAR() { return getToken(D96Parser.VAR, 0); }
		public Att_namesContext att_names() {
			return getRuleContext(Att_namesContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public Att_init_valueContext att_init_value() {
			return getRuleContext(Att_init_valueContext.class,0);
		}
		public Att_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_att_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterAtt_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitAtt_declare(this);
		}
	}

	public final Att_declareContext att_declare() throws RecognitionException {
		Att_declareContext _localctx = new Att_declareContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_att_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			_la = _input.LA(1);
			if ( !(_la==VAL || _la==VAR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(182);
				att_names();
				setState(183);
				match(Extended);
				setState(184);
				data_type();
				}
				break;
			case 2:
				{
				setState(186);
				att_init_value();
				}
				break;
			}
			setState(189);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Att_namesContext extends ParserRuleContext {
		public IdnameContext idname() {
			return getRuleContext(IdnameContext.class,0);
		}
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public Att_namesContext att_names() {
			return getRuleContext(Att_namesContext.class,0);
		}
		public Att_namesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_att_names; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterAtt_names(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitAtt_names(this);
		}
	}

	public final Att_namesContext att_names() throws RecognitionException {
		Att_namesContext _localctx = new Att_namesContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_att_names);
		try {
			setState(196);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(191);
				idname();
				setState(192);
				match(CM);
				setState(193);
				att_names();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(195);
				idname();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Att_init_valueContext extends ParserRuleContext {
		public IdnameContext idname() {
			return getRuleContext(IdnameContext.class,0);
		}
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Att_init_valueContext att_init_value() {
			return getRuleContext(Att_init_valueContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public Att_init_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_att_init_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterAtt_init_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitAtt_init_value(this);
		}
	}

	public final Att_init_valueContext att_init_value() throws RecognitionException {
		Att_init_valueContext _localctx = new Att_init_valueContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_att_init_value);
		try {
			setState(210);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(198);
				idname();
				setState(199);
				match(CM);
				setState(200);
				att_init_value();
				setState(201);
				match(CM);
				setState(202);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(204);
				idname();
				setState(205);
				match(Extended);
				setState(206);
				data_type();
				setState(207);
				match(ASSIGN);
				setState(208);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValuesContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ValuesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_values; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterValues(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitValues(this);
		}
	}

	public final ValuesContext values() throws RecognitionException {
		ValuesContext _localctx = new ValuesContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_values);
		try {
			setState(214);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NULL:
			case ARRAY:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(212);
				value();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_value);
		try {
			setState(221);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(216);
				literal();
				setState(217);
				match(CM);
				setState(218);
				value();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(220);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Data_typeContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public ClasstypeContext classtype() {
			return getRuleContext(ClasstypeContext.class,0);
		}
		public Data_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterData_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitData_type(this);
		}
	}

	public final Data_typeContext data_type() throws RecognitionException {
		Data_typeContext _localctx = new Data_typeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_data_type);
		try {
			setState(226);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(223);
				primitive_type();
				}
				break;
			case ARRAY:
				enterOuterAlt(_localctx, 2);
				{
				setState(224);
				array_type();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(225);
				classtype();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(D96Parser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(D96Parser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(D96Parser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(D96Parser.STRING, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterPrimitive_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitPrimitive_type(this);
		}
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClasstypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public ClasstypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterClasstype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitClasstype(this);
		}
	}

	public final ClasstypeContext classtype() throws RecognitionException {
		ClasstypeContext _localctx = new ClasstypeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_classtype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declareContext extends ParserRuleContext {
		public Func_declareContext func_declare() {
			return getRuleContext(Func_declareContext.class,0);
		}
		public Contructor_declareContext contructor_declare() {
			return getRuleContext(Contructor_declareContext.class,0);
		}
		public Detructor_declareContext detructor_declare() {
			return getRuleContext(Detructor_declareContext.class,0);
		}
		public Method_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMethod_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMethod_declare(this);
		}
	}

	public final Method_declareContext method_declare() throws RecognitionException {
		Method_declareContext _localctx = new Method_declareContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_method_declare);
		try {
			setState(235);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case DOLLARID:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				func_declare();
				}
				break;
			case CONSTRUCTOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(233);
				contructor_declare();
				}
				break;
			case DESTRUCTOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(234);
				detructor_declare();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_declareContext extends ParserRuleContext {
		public IdnameContext idname() {
			return getRuleContext(IdnameContext.class,0);
		}
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Func_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterFunc_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitFunc_declare(this);
		}
	}

	public final Func_declareContext func_declare() throws RecognitionException {
		Func_declareContext _localctx = new Func_declareContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_func_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			idname();
			setState(238);
			match(LP);
			setState(239);
			paramlist();
			setState(240);
			match(RP);
			setState(241);
			blockstatment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamlistContext extends ParserRuleContext {
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterParamlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitParamlist(this);
		}
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_paramlist);
		try {
			setState(245);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case DOLLARID:
				enterOuterAlt(_localctx, 1);
				{
				setState(243);
				params();
				}
				break;
			case RP:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterParams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitParams(this);
		}
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_params);
		try {
			setState(252);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(247);
				param();
				setState(248);
				match(SM);
				setState(249);
				params();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(251);
				param();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public IdnamelistContext idnamelist() {
			return getRuleContext(IdnamelistContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			idnamelist();
			setState(255);
			match(Extended);
			setState(256);
			data_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdnamelistContext extends ParserRuleContext {
		public IdnameContext idname() {
			return getRuleContext(IdnameContext.class,0);
		}
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public IdnamelistContext idnamelist() {
			return getRuleContext(IdnamelistContext.class,0);
		}
		public IdnamelistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idnamelist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIdnamelist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIdnamelist(this);
		}
	}

	public final IdnamelistContext idnamelist() throws RecognitionException {
		IdnamelistContext _localctx = new IdnamelistContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_idnamelist);
		try {
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(258);
				idname();
				setState(259);
				match(CM);
				setState(260);
				idnamelist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
				idname();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockstatmentContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public StamentlistContext stamentlist() {
			return getRuleContext(StamentlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public BlockstatmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockstatment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterBlockstatment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitBlockstatment(this);
		}
	}

	public final BlockstatmentContext blockstatment() throws RecognitionException {
		BlockstatmentContext _localctx = new BlockstatmentContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_blockstatment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(LB);
			setState(266);
			stamentlist();
			setState(267);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StamentlistContext extends ParserRuleContext {
		public StamentsContext staments() {
			return getRuleContext(StamentsContext.class,0);
		}
		public StamentlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stamentlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStamentlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStamentlist(this);
		}
	}

	public final StamentlistContext stamentlist() throws RecognitionException {
		StamentlistContext _localctx = new StamentlistContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_stamentlist);
		try {
			setState(271);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BREAK:
			case FOREACH:
			case NULL:
			case CONTINUE:
			case TRUE:
			case IF:
			case FALSE:
			case VAL:
			case NEW:
			case ARRAY:
			case VAR:
			case RETURN:
			case SELF:
			case NOT:
			case SUB:
			case LB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				staments();
				}
				break;
			case RB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StamentsContext extends ParserRuleContext {
		public StamentContext stament() {
			return getRuleContext(StamentContext.class,0);
		}
		public StamentsContext staments() {
			return getRuleContext(StamentsContext.class,0);
		}
		public StamentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_staments; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStaments(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStaments(this);
		}
	}

	public final StamentsContext staments() throws RecognitionException {
		StamentsContext _localctx = new StamentsContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_staments);
		try {
			setState(277);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(273);
				stament();
				setState(274);
				staments();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(276);
				stament();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StamentContext extends ParserRuleContext {
		public Vardecl_stmContext vardecl_stm() {
			return getRuleContext(Vardecl_stmContext.class,0);
		}
		public Assign_stmContext assign_stm() {
			return getRuleContext(Assign_stmContext.class,0);
		}
		public If_stmContext if_stm() {
			return getRuleContext(If_stmContext.class,0);
		}
		public Forin_stmContext forin_stm() {
			return getRuleContext(Forin_stmContext.class,0);
		}
		public Break_stmContext break_stm() {
			return getRuleContext(Break_stmContext.class,0);
		}
		public Continue_stmContext continue_stm() {
			return getRuleContext(Continue_stmContext.class,0);
		}
		public Return_stmContext return_stm() {
			return getRuleContext(Return_stmContext.class,0);
		}
		public Method_invocation_stmContext method_invocation_stm() {
			return getRuleContext(Method_invocation_stmContext.class,0);
		}
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public StamentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stament; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStament(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStament(this);
		}
	}

	public final StamentContext stament() throws RecognitionException {
		StamentContext _localctx = new StamentContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_stament);
		try {
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(279);
				vardecl_stm();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(280);
				assign_stm();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(281);
				if_stm();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(282);
				forin_stm();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(283);
				break_stm();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(284);
				continue_stm();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(285);
				return_stm();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(286);
				method_invocation_stm();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(287);
				blockstatment();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(D96Parser.INTEGER, 0); }
		public TerminalNode INTERGER_GT_ZERO() { return getToken(D96Parser.INTERGER_GT_ZERO, 0); }
		public TerminalNode FLOAT_NUMBER() { return getToken(D96Parser.FLOAT_NUMBER, 0); }
		public TerminalNode BOOLEAN_LITERAL() { return getToken(D96Parser.BOOLEAN_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(D96Parser.STRING_LITERAL, 0); }
		public Index_array_literalContext index_array_literal() {
			return getRuleContext(Index_array_literalContext.class,0);
		}
		public Multi_arrayContext multi_array() {
			return getRuleContext(Multi_arrayContext.class,0);
		}
		public TerminalNode NULL() { return getToken(D96Parser.NULL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(290);
				match(INTEGER);
				}
				break;
			case 2:
				{
				setState(291);
				match(INTERGER_GT_ZERO);
				}
				break;
			case 3:
				{
				setState(292);
				match(FLOAT_NUMBER);
				}
				break;
			case 4:
				{
				setState(293);
				match(BOOLEAN_LITERAL);
				}
				break;
			case 5:
				{
				setState(294);
				match(STRING_LITERAL);
				}
				break;
			case 6:
				{
				setState(295);
				index_array_literal();
				}
				break;
			case 7:
				{
				setState(296);
				multi_array();
				}
				break;
			case 8:
				{
				setState(297);
				match(NULL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_array_literalContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public List<Primitive_literalContext> primitive_literal() {
			return getRuleContexts(Primitive_literalContext.class);
		}
		public Primitive_literalContext primitive_literal(int i) {
			return getRuleContext(Primitive_literalContext.class,i);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Index_array_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_array_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIndex_array_literal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIndex_array_literal(this);
		}
	}

	public final Index_array_literalContext index_array_literal() throws RecognitionException {
		Index_array_literalContext _localctx = new Index_array_literalContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_index_array_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(ARRAY);
			setState(301);
			match(LP);
			setState(302);
			primitive_literal();
			setState(307);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(303);
				match(CM);
				setState(304);
				primitive_literal();
				}
				}
				setState(309);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(310);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_literalContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(D96Parser.INTEGER, 0); }
		public TerminalNode INTERGER_GT_ZERO() { return getToken(D96Parser.INTERGER_GT_ZERO, 0); }
		public TerminalNode FLOAT_NUMBER() { return getToken(D96Parser.FLOAT_NUMBER, 0); }
		public TerminalNode BOOLEAN_LITERAL() { return getToken(D96Parser.BOOLEAN_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(D96Parser.STRING_LITERAL, 0); }
		public Primitive_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterPrimitive_literal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitPrimitive_literal(this);
		}
	}

	public final Primitive_literalContext primitive_literal() throws RecognitionException {
		Primitive_literalContext _localctx = new Primitive_literalContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_primitive_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTERGER_GT_ZERO) | (1L << INTEGER) | (1L << FLOAT_NUMBER) | (1L << BOOLEAN_LITERAL) | (1L << STRING_LITERAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Multi_arrayContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public List<Index_array_literalContext> index_array_literal() {
			return getRuleContexts(Index_array_literalContext.class);
		}
		public Index_array_literalContext index_array_literal(int i) {
			return getRuleContext(Index_array_literalContext.class,i);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Multi_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multi_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMulti_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMulti_array(this);
		}
	}

	public final Multi_arrayContext multi_array() throws RecognitionException {
		Multi_arrayContext _localctx = new Multi_arrayContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_multi_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(ARRAY);
			setState(315);
			match(LP);
			setState(316);
			index_array_literal();
			setState(321);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(317);
				match(CM);
				setState(318);
				index_array_literal();
				}
				}
				setState(323);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(324);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LSB() { return getToken(D96Parser.LSB, 0); }
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public TerminalNode INTERGER_GT_ZERO() { return getToken(D96Parser.INTERGER_GT_ZERO, 0); }
		public TerminalNode RSB() { return getToken(D96Parser.RSB, 0); }
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterArray_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitArray_type(this);
		}
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(ARRAY);
			setState(327);
			match(LSB);
			setState(330);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				{
				setState(328);
				primitive_type();
				}
				break;
			case ARRAY:
				{
				setState(329);
				array_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(332);
			match(CM);
			setState(333);
			match(INTERGER_GT_ZERO);
			setState(334);
			match(RSB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vardecl_stmContext extends ParserRuleContext {
		public VarlistContext varlist() {
			return getRuleContext(VarlistContext.class,0);
		}
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public TerminalNode VAR() { return getToken(D96Parser.VAR, 0); }
		public TerminalNode VAL() { return getToken(D96Parser.VAL, 0); }
		public Vardecl_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterVardecl_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitVardecl_stm(this);
		}
	}

	public final Vardecl_stmContext vardecl_stm() throws RecognitionException {
		Vardecl_stmContext _localctx = new Vardecl_stmContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_vardecl_stm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			_la = _input.LA(1);
			if ( !(_la==VAL || _la==VAR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(337);
			varlist();
			setState(338);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarlistContext extends ParserRuleContext {
		public Variable_namesContext variable_names() {
			return getRuleContext(Variable_namesContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public Variable_init_valueContext variable_init_value() {
			return getRuleContext(Variable_init_valueContext.class,0);
		}
		public VarlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterVarlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitVarlist(this);
		}
	}

	public final VarlistContext varlist() throws RecognitionException {
		VarlistContext _localctx = new VarlistContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_varlist);
		try {
			setState(345);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(340);
				variable_names();
				setState(341);
				match(Extended);
				setState(342);
				data_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(344);
				variable_init_value();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_namesContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public Variable_namesContext variable_names() {
			return getRuleContext(Variable_namesContext.class,0);
		}
		public Variable_namesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_names; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterVariable_names(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitVariable_names(this);
		}
	}

	public final Variable_namesContext variable_names() throws RecognitionException {
		Variable_namesContext _localctx = new Variable_namesContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_variable_names);
		try {
			setState(351);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(ID);
				setState(348);
				match(CM);
				setState(349);
				variable_names();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(350);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_init_valueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Variable_init_valueContext variable_init_value() {
			return getRuleContext(Variable_init_valueContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode Extended() { return getToken(D96Parser.Extended, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public Variable_init_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_init_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterVariable_init_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitVariable_init_value(this);
		}
	}

	public final Variable_init_valueContext variable_init_value() throws RecognitionException {
		Variable_init_valueContext _localctx = new Variable_init_valueContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_variable_init_value);
		try {
			setState(365);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(353);
				match(ID);
				setState(354);
				match(CM);
				setState(355);
				variable_init_value();
				setState(356);
				match(CM);
				setState(357);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(359);
				match(ID);
				setState(360);
				match(Extended);
				setState(361);
				data_type();
				setState(362);
				match(ASSIGN);
				setState(363);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmContext extends ParserRuleContext {
		public LeftassignContext leftassign() {
			return getRuleContext(LeftassignContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public Assign_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterAssign_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitAssign_stm(this);
		}
	}

	public final Assign_stmContext assign_stm() throws RecognitionException {
		Assign_stmContext _localctx = new Assign_stmContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_assign_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			leftassign();
			setState(368);
			match(ASSIGN);
			setState(369);
			exp();
			setState(370);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LeftassignContext extends ParserRuleContext {
		public ScalarvarContext scalarvar() {
			return getRuleContext(ScalarvarContext.class,0);
		}
		public Indexed_expContext indexed_exp() {
			return getRuleContext(Indexed_expContext.class,0);
		}
		public LeftassignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leftassign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterLeftassign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitLeftassign(this);
		}
	}

	public final LeftassignContext leftassign() throws RecognitionException {
		LeftassignContext _localctx = new LeftassignContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_leftassign);
		try {
			setState(374);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(372);
				scalarvar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(373);
				indexed_exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ScalarvarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public ScalarvarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalarvar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterScalarvar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitScalarvar(this);
		}
	}

	public final ScalarvarContext scalarvar() throws RecognitionException {
		ScalarvarContext _localctx = new ScalarvarContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_scalarvar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Indexed_expContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public List<Index_operatorContext> index_operator() {
			return getRuleContexts(Index_operatorContext.class);
		}
		public Index_operatorContext index_operator(int i) {
			return getRuleContext(Index_operatorContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public TerminalNode SELF() { return getToken(D96Parser.SELF, 0); }
		public List<TerminalNode> DOT() { return getTokens(D96Parser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(D96Parser.DOT, i);
		}
		public Indexed_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_indexed_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIndexed_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIndexed_exp(this);
		}
	}

	public final Indexed_expContext indexed_exp() throws RecognitionException {
		Indexed_expContext _localctx = new Indexed_expContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_indexed_exp);
		int _la;
		try {
			setState(402);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(378);
				exp();
				setState(379);
				index_operator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SELF) {
					{
					setState(381);
					match(SELF);
					setState(382);
					match(DOT);
					}
				}

				setState(385);
				match(ID);
				setState(389);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LSB) {
					{
					{
					setState(386);
					index_operator();
					}
					}
					setState(391);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(393);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SELF) {
					{
					setState(392);
					match(SELF);
					}
				}

				setState(395);
				match(ID);
				setState(398); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(396);
					match(DOT);
					setState(397);
					match(ID);
					}
					}
					setState(400); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==DOT );
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(D96Parser.IF, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Elseif_stmsContext elseif_stms() {
			return getRuleContext(Elseif_stmsContext.class,0);
		}
		public Else_stmContext else_stm() {
			return getRuleContext(Else_stmContext.class,0);
		}
		public If_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIf_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIf_stm(this);
		}
	}

	public final If_stmContext if_stm() throws RecognitionException {
		If_stmContext _localctx = new If_stmContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_if_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(404);
			match(IF);
			setState(405);
			match(LP);
			setState(406);
			exp();
			setState(407);
			match(RP);
			setState(408);
			blockstatment();
			setState(409);
			elseif_stms();
			setState(410);
			else_stm();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Elseif_stmsContext extends ParserRuleContext {
		public Elseif_stmContext elseif_stm() {
			return getRuleContext(Elseif_stmContext.class,0);
		}
		public Elseif_stmsContext elseif_stms() {
			return getRuleContext(Elseif_stmsContext.class,0);
		}
		public Elseif_stmsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseif_stms; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterElseif_stms(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitElseif_stms(this);
		}
	}

	public final Elseif_stmsContext elseif_stms() throws RecognitionException {
		Elseif_stmsContext _localctx = new Elseif_stmsContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_elseif_stms);
		try {
			setState(416);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ELSEIF:
				enterOuterAlt(_localctx, 1);
				{
				setState(412);
				elseif_stm();
				setState(413);
				elseif_stms();
				}
				break;
			case BREAK:
			case FOREACH:
			case NULL:
			case CONTINUE:
			case TRUE:
			case IF:
			case FALSE:
			case VAL:
			case NEW:
			case ARRAY:
			case VAR:
			case ELSE:
			case RETURN:
			case SELF:
			case NOT:
			case SUB:
			case LB:
			case RB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Elseif_stmContext extends ParserRuleContext {
		public TerminalNode ELSEIF() { return getToken(D96Parser.ELSEIF, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Elseif_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseif_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterElseif_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitElseif_stm(this);
		}
	}

	public final Elseif_stmContext elseif_stm() throws RecognitionException {
		Elseif_stmContext _localctx = new Elseif_stmContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_elseif_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(418);
			match(ELSEIF);
			setState(419);
			match(LP);
			setState(420);
			exp();
			setState(421);
			match(RP);
			setState(422);
			blockstatment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_stmContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(D96Parser.ELSE, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Else_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterElse_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitElse_stm(this);
		}
	}

	public final Else_stmContext else_stm() throws RecognitionException {
		Else_stmContext _localctx = new Else_stmContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_else_stm);
		try {
			setState(427);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ELSE:
				enterOuterAlt(_localctx, 1);
				{
				setState(424);
				match(ELSE);
				setState(425);
				blockstatment();
				}
				break;
			case BREAK:
			case FOREACH:
			case NULL:
			case CONTINUE:
			case TRUE:
			case IF:
			case FALSE:
			case VAL:
			case NEW:
			case ARRAY:
			case VAR:
			case RETURN:
			case SELF:
			case NOT:
			case SUB:
			case LB:
			case RB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Forin_stmContext extends ParserRuleContext {
		public TerminalNode FOREACH() { return getToken(D96Parser.FOREACH, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ScalarvarContext scalarvar() {
			return getRuleContext(ScalarvarContext.class,0);
		}
		public TerminalNode IN() { return getToken(D96Parser.IN, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode FROMTO() { return getToken(D96Parser.FROMTO, 0); }
		public SteploopContext steploop() {
			return getRuleContext(SteploopContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Forin_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forin_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterForin_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitForin_stm(this);
		}
	}

	public final Forin_stmContext forin_stm() throws RecognitionException {
		Forin_stmContext _localctx = new Forin_stmContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_forin_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			match(FOREACH);
			setState(430);
			match(LP);
			setState(431);
			scalarvar();
			setState(432);
			match(IN);
			setState(433);
			exp();
			setState(434);
			match(FROMTO);
			setState(435);
			exp();
			setState(436);
			steploop();
			setState(437);
			match(RP);
			setState(438);
			blockstatment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SteploopContext extends ParserRuleContext {
		public TerminalNode BY() { return getToken(D96Parser.BY, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public SteploopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_steploop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterSteploop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitSteploop(this);
		}
	}

	public final SteploopContext steploop() throws RecognitionException {
		SteploopContext _localctx = new SteploopContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_steploop);
		try {
			setState(443);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BY:
				enterOuterAlt(_localctx, 1);
				{
				setState(440);
				match(BY);
				setState(441);
				exp();
				}
				break;
			case RP:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stmContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(D96Parser.BREAK, 0); }
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public Break_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterBreak_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitBreak_stm(this);
		}
	}

	public final Break_stmContext break_stm() throws RecognitionException {
		Break_stmContext _localctx = new Break_stmContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_break_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(445);
			match(BREAK);
			setState(446);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_stmContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(D96Parser.CONTINUE, 0); }
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public Continue_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterContinue_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitContinue_stm(this);
		}
	}

	public final Continue_stmContext continue_stm() throws RecognitionException {
		Continue_stmContext _localctx = new Continue_stmContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_continue_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(448);
			match(CONTINUE);
			setState(449);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stmContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(D96Parser.RETURN, 0); }
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode DOLLARID() { return getToken(D96Parser.DOLLARID, 0); }
		public Return_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterReturn_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitReturn_stm(this);
		}
	}

	public final Return_stmContext return_stm() throws RecognitionException {
		Return_stmContext _localctx = new Return_stmContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_return_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
			match(RETURN);
			setState(454);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NULL:
			case TRUE:
			case FALSE:
			case NEW:
			case ARRAY:
			case SELF:
			case NOT:
			case SUB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				{
				setState(452);
				exp();
				}
				break;
			case DOLLARID:
				{
				setState(453);
				match(DOLLARID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(456);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_invocation_stmContext extends ParserRuleContext {
		public TerminalNode SM() { return getToken(D96Parser.SM, 0); }
		public Method_invocateContext method_invocate() {
			return getRuleContext(Method_invocateContext.class,0);
		}
		public Static_method_invocateContext static_method_invocate() {
			return getRuleContext(Static_method_invocateContext.class,0);
		}
		public Method_invocation_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_invocation_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMethod_invocation_stm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMethod_invocation_stm(this);
		}
	}

	public final Method_invocation_stmContext method_invocation_stm() throws RecognitionException {
		Method_invocation_stmContext _localctx = new Method_invocation_stmContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_method_invocation_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(460);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(458);
				method_invocate();
				}
				break;
			case 2:
				{
				setState(459);
				static_method_invocate();
				}
				break;
			}
			setState(462);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Contructor_declareContext extends ParserRuleContext {
		public TerminalNode CONSTRUCTOR() { return getToken(D96Parser.CONSTRUCTOR, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Contructor_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contructor_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterContructor_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitContructor_declare(this);
		}
	}

	public final Contructor_declareContext contructor_declare() throws RecognitionException {
		Contructor_declareContext _localctx = new Contructor_declareContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_contructor_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(464);
			match(CONSTRUCTOR);
			setState(465);
			match(LP);
			setState(466);
			paramlist();
			setState(467);
			match(RP);
			setState(468);
			blockstatment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Detructor_declareContext extends ParserRuleContext {
		public TerminalNode DESTRUCTOR() { return getToken(D96Parser.DESTRUCTOR, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public BlockstatmentContext blockstatment() {
			return getRuleContext(BlockstatmentContext.class,0);
		}
		public Detructor_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_detructor_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterDetructor_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitDetructor_declare(this);
		}
	}

	public final Detructor_declareContext detructor_declare() throws RecognitionException {
		Detructor_declareContext _localctx = new Detructor_declareContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_detructor_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(470);
			match(DESTRUCTOR);
			setState(471);
			match(LP);
			setState(472);
			match(RP);
			setState(473);
			blockstatment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdnameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode DOLLARID() { return getToken(D96Parser.DOLLARID, 0); }
		public IdnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idname; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIdname(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIdname(this);
		}
	}

	public final IdnameContext idname() throws RecognitionException {
		IdnameContext _localctx = new IdnameContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_idname);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(475);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==DOLLARID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_operatorContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(D96Parser.LSB, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RSB() { return getToken(D96Parser.RSB, 0); }
		public Index_operatorContext index_operator() {
			return getRuleContext(Index_operatorContext.class,0);
		}
		public Index_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterIndex_operator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitIndex_operator(this);
		}
	}

	public final Index_operatorContext index_operator() throws RecognitionException {
		Index_operatorContext _localctx = new Index_operatorContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_index_operator);
		try {
			setState(486);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(477);
				match(LSB);
				setState(478);
				exp();
				setState(479);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(481);
				match(LSB);
				setState(482);
				exp();
				setState(483);
				match(RSB);
				setState(484);
				index_operator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public List<Exp0Context> exp0() {
			return getRuleContexts(Exp0Context.class);
		}
		public Exp0Context exp0(int i) {
			return getRuleContext(Exp0Context.class,i);
		}
		public TerminalNode ADDDOT() { return getToken(D96Parser.ADDDOT, 0); }
		public TerminalNode EQUALDOT() { return getToken(D96Parser.EQUALDOT, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_exp);
		int _la;
		try {
			setState(493);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(488);
				exp0();
				setState(489);
				_la = _input.LA(1);
				if ( !(_la==EQUALDOT || _la==ADDDOT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(490);
				exp0();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(492);
				exp0();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp0Context extends ParserRuleContext {
		public List<Exp1Context> exp1() {
			return getRuleContexts(Exp1Context.class);
		}
		public Exp1Context exp1(int i) {
			return getRuleContext(Exp1Context.class,i);
		}
		public TerminalNode EQUAL() { return getToken(D96Parser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(D96Parser.NOT_EQUAL, 0); }
		public TerminalNode GT() { return getToken(D96Parser.GT, 0); }
		public TerminalNode LT() { return getToken(D96Parser.LT, 0); }
		public TerminalNode GE() { return getToken(D96Parser.GE, 0); }
		public TerminalNode LE() { return getToken(D96Parser.LE, 0); }
		public Exp0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp0; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp0(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp0(this);
		}
	}

	public final Exp0Context exp0() throws RecognitionException {
		Exp0Context _localctx = new Exp0Context(_ctx, getState());
		enterRule(_localctx, 106, RULE_exp0);
		int _la;
		try {
			setState(500);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(495);
				exp1(0);
				setState(496);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NOT_EQUAL) | (1L << LT) | (1L << LE) | (1L << EQUAL) | (1L << GT) | (1L << GE))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(497);
				exp1(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(499);
				exp1(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp1Context extends ParserRuleContext {
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
		}
		public TerminalNode AND() { return getToken(D96Parser.AND, 0); }
		public TerminalNode OR() { return getToken(D96Parser.OR, 0); }
		public Exp1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp1(this);
		}
	}

	public final Exp1Context exp1() throws RecognitionException {
		return exp1(0);
	}

	private Exp1Context exp1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp1Context _localctx = new Exp1Context(_ctx, _parentState);
		Exp1Context _prevctx = _localctx;
		int _startState = 108;
		enterRecursionRule(_localctx, 108, RULE_exp1, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(503);
			exp2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(510);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp1);
					setState(505);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(506);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(507);
					exp2(0);
					}
					} 
				}
				setState(512);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp2Context extends ParserRuleContext {
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public TerminalNode ADD() { return getToken(D96Parser.ADD, 0); }
		public TerminalNode SUB() { return getToken(D96Parser.SUB, 0); }
		public Exp2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp2(this);
		}
	}

	public final Exp2Context exp2() throws RecognitionException {
		return exp2(0);
	}

	private Exp2Context exp2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp2Context _localctx = new Exp2Context(_ctx, _parentState);
		Exp2Context _prevctx = _localctx;
		int _startState = 110;
		enterRecursionRule(_localctx, 110, RULE_exp2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(514);
			exp3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(521);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp2);
					setState(516);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(517);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(518);
					exp3(0);
					}
					} 
				}
				setState(523);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp3Context extends ParserRuleContext {
		public Exp4Context exp4() {
			return getRuleContext(Exp4Context.class,0);
		}
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public TerminalNode MUL() { return getToken(D96Parser.MUL, 0); }
		public TerminalNode DIV() { return getToken(D96Parser.DIV, 0); }
		public TerminalNode MOD() { return getToken(D96Parser.MOD, 0); }
		public Exp3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp3(this);
		}
	}

	public final Exp3Context exp3() throws RecognitionException {
		return exp3(0);
	}

	private Exp3Context exp3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp3Context _localctx = new Exp3Context(_ctx, _parentState);
		Exp3Context _prevctx = _localctx;
		int _startState = 112;
		enterRecursionRule(_localctx, 112, RULE_exp3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(525);
			exp4();
			}
			_ctx.stop = _input.LT(-1);
			setState(532);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp3);
					setState(527);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(528);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(529);
					exp4();
					}
					} 
				}
				setState(534);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp4Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(D96Parser.NOT, 0); }
		public Exp4Context exp4() {
			return getRuleContext(Exp4Context.class,0);
		}
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public Exp4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp4(this);
		}
	}

	public final Exp4Context exp4() throws RecognitionException {
		Exp4Context _localctx = new Exp4Context(_ctx, getState());
		enterRule(_localctx, 114, RULE_exp4);
		try {
			setState(538);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(535);
				match(NOT);
				setState(536);
				exp4();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case NEW:
			case ARRAY:
			case SELF:
			case SUB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(537);
				exp5();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp5Context extends ParserRuleContext {
		public TerminalNode SUB() { return getToken(D96Parser.SUB, 0); }
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public Exp6Context exp6() {
			return getRuleContext(Exp6Context.class,0);
		}
		public Exp5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp5; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp5(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp5(this);
		}
	}

	public final Exp5Context exp5() throws RecognitionException {
		Exp5Context _localctx = new Exp5Context(_ctx, getState());
		enterRule(_localctx, 116, RULE_exp5);
		try {
			setState(543);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(540);
				match(SUB);
				setState(541);
				exp5();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case NEW:
			case ARRAY:
			case SELF:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(542);
				exp6(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp6Context extends ParserRuleContext {
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
		public Exp6Context exp6() {
			return getRuleContext(Exp6Context.class,0);
		}
		public Index_operatorContext index_operator() {
			return getRuleContext(Index_operatorContext.class,0);
		}
		public Exp6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp6; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp6(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp6(this);
		}
	}

	public final Exp6Context exp6() throws RecognitionException {
		return exp6(0);
	}

	private Exp6Context exp6(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp6Context _localctx = new Exp6Context(_ctx, _parentState);
		Exp6Context _prevctx = _localctx;
		int _startState = 118;
		enterRecursionRule(_localctx, 118, RULE_exp6, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(546);
			exp7(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(552);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp6Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp6);
					setState(548);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(549);
					index_operator();
					}
					} 
				}
				setState(554);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp7Context extends ParserRuleContext {
		public Exp8Context exp8() {
			return getRuleContext(Exp8Context.class,0);
		}
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
		public TerminalNode DOT() { return getToken(D96Parser.DOT, 0); }
		public Exp7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp7; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp7(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp7(this);
		}
	}

	public final Exp7Context exp7() throws RecognitionException {
		return exp7(0);
	}

	private Exp7Context exp7(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp7Context _localctx = new Exp7Context(_ctx, _parentState);
		Exp7Context _prevctx = _localctx;
		int _startState = 120;
		enterRecursionRule(_localctx, 120, RULE_exp7, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(556);
			exp8();
			}
			_ctx.stop = _input.LT(-1);
			setState(563);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,45,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp7Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp7);
					setState(558);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(559);
					match(DOT);
					setState(560);
					exp8();
					}
					} 
				}
				setState(565);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,45,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp8Context extends ParserRuleContext {
		public Exp9Context exp9() {
			return getRuleContext(Exp9Context.class,0);
		}
		public TerminalNode SC() { return getToken(D96Parser.SC, 0); }
		public Static_operandContext static_operand() {
			return getRuleContext(Static_operandContext.class,0);
		}
		public Exp8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp8; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp8(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp8(this);
		}
	}

	public final Exp8Context exp8() throws RecognitionException {
		Exp8Context _localctx = new Exp8Context(_ctx, getState());
		enterRule(_localctx, 122, RULE_exp8);
		try {
			setState(571);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(566);
				exp9();
				setState(567);
				match(SC);
				setState(568);
				static_operand();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(570);
				exp9();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp9Context extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(D96Parser.NEW, 0); }
		public Exp9Context exp9() {
			return getRuleContext(Exp9Context.class,0);
		}
		public Exp10Context exp10() {
			return getRuleContext(Exp10Context.class,0);
		}
		public Exp9Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp9; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp9(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp9(this);
		}
	}

	public final Exp9Context exp9() throws RecognitionException {
		Exp9Context _localctx = new Exp9Context(_ctx, getState());
		enterRule(_localctx, 124, RULE_exp9);
		try {
			setState(576);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEW:
				enterOuterAlt(_localctx, 1);
				{
				setState(573);
				match(NEW);
				setState(574);
				exp9();
				}
				break;
			case NULL:
			case TRUE:
			case FALSE:
			case ARRAY:
			case SELF:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(575);
				exp10();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp10Context extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode TRUE() { return getToken(D96Parser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(D96Parser.FALSE, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode SELF() { return getToken(D96Parser.SELF, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Exp10Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp10; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExp10(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExp10(this);
		}
	}

	public final Exp10Context exp10() throws RecognitionException {
		Exp10Context _localctx = new Exp10Context(_ctx, getState());
		enterRule(_localctx, 126, RULE_exp10);
		try {
			setState(588);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(578);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(579);
				match(TRUE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(580);
				match(FALSE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(581);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(582);
				match(SELF);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(583);
				func_call();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(584);
				match(LP);
				setState(585);
				exp();
				setState(586);
				match(RP);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExplistsContext explists() {
			return getRuleContext(ExplistsContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterFunc_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitFunc_call(this);
		}
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(590);
			match(ID);
			setState(591);
			match(LP);
			setState(592);
			explists();
			setState(593);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Static_operandContext extends ParserRuleContext {
		public TerminalNode DOLLARID() { return getToken(D96Parser.DOLLARID, 0); }
		public Static_func_callContext static_func_call() {
			return getRuleContext(Static_func_callContext.class,0);
		}
		public Static_operandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_operand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStatic_operand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStatic_operand(this);
		}
	}

	public final Static_operandContext static_operand() throws RecognitionException {
		Static_operandContext _localctx = new Static_operandContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_static_operand);
		try {
			setState(597);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(595);
				match(DOLLARID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(596);
				static_func_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Static_func_callContext extends ParserRuleContext {
		public TerminalNode DOLLARID() { return getToken(D96Parser.DOLLARID, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExplistsContext explists() {
			return getRuleContext(ExplistsContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Static_func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_func_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStatic_func_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStatic_func_call(this);
		}
	}

	public final Static_func_callContext static_func_call() throws RecognitionException {
		Static_func_callContext _localctx = new Static_func_callContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_static_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(599);
			match(DOLLARID);
			setState(600);
			match(LP);
			setState(601);
			explists();
			setState(602);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_invocateContext extends ParserRuleContext {
		public Object_expContext object_exp() {
			return getRuleContext(Object_expContext.class,0);
		}
		public TerminalNode DOT() { return getToken(D96Parser.DOT, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExplistsContext explists() {
			return getRuleContext(ExplistsContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Method_invocateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_invocate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterMethod_invocate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitMethod_invocate(this);
		}
	}

	public final Method_invocateContext method_invocate() throws RecognitionException {
		Method_invocateContext _localctx = new Method_invocateContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_method_invocate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(604);
			object_exp();
			setState(605);
			match(DOT);
			setState(606);
			match(ID);
			setState(607);
			match(LP);
			setState(608);
			explists();
			setState(609);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Object_expContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public TerminalNode NEW() { return getToken(D96Parser.NEW, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode SELF() { return getToken(D96Parser.SELF, 0); }
		public Object_expContext object_exp() {
			return getRuleContext(Object_expContext.class,0);
		}
		public List<TerminalNode> DOT() { return getTokens(D96Parser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(D96Parser.DOT, i);
		}
		public Object_exp1Context object_exp1() {
			return getRuleContext(Object_exp1Context.class,0);
		}
		public Object_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_object_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterObject_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitObject_exp(this);
		}
	}

	public final Object_expContext object_exp() throws RecognitionException {
		Object_expContext _localctx = new Object_expContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_object_exp);
		int _la;
		try {
			int _alt;
			setState(632);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,53,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(611);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(612);
				match(NEW);
				setState(613);
				func_call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(614);
				match(SELF);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(616);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SELF) {
					{
					setState(615);
					match(SELF);
					}
				}

				setState(618);
				match(ID);
				setState(623);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(619);
						match(DOT);
						setState(620);
						match(ID);
						}
						} 
					}
					setState(625);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,51,_ctx);
				}
				setState(628);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==DOT) {
					{
					setState(626);
					match(DOT);
					setState(627);
					func_call();
					}
				}

				setState(630);
				object_exp();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(631);
				object_exp1();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Object_exp1Context extends ParserRuleContext {
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public Object_expContext object_exp() {
			return getRuleContext(Object_expContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Object_exp1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_object_exp1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterObject_exp1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitObject_exp1(this);
		}
	}

	public final Object_exp1Context object_exp1() throws RecognitionException {
		Object_exp1Context _localctx = new Object_exp1Context(_ctx, getState());
		enterRule(_localctx, 138, RULE_object_exp1);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(634);
			match(LP);
			setState(635);
			object_exp();
			setState(636);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExplistsContext extends ParserRuleContext {
		public ExplistContext explist() {
			return getRuleContext(ExplistContext.class,0);
		}
		public ExplistsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explists; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExplists(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExplists(this);
		}
	}

	public final ExplistsContext explists() throws RecognitionException {
		ExplistsContext _localctx = new ExplistsContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_explists);
		try {
			setState(640);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NULL:
			case TRUE:
			case FALSE:
			case NEW:
			case ARRAY:
			case SELF:
			case NOT:
			case SUB:
			case LP:
			case INTERGER_GT_ZERO:
			case INTEGER:
			case FLOAT_NUMBER:
			case BOOLEAN_LITERAL:
			case STRING_LITERAL:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(638);
				explist();
				}
				break;
			case RP:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExplistContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public ExplistContext explist() {
			return getRuleContext(ExplistContext.class,0);
		}
		public ExplistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterExplist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitExplist(this);
		}
	}

	public final ExplistContext explist() throws RecognitionException {
		ExplistContext _localctx = new ExplistContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_explist);
		try {
			setState(647);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(642);
				exp();
				setState(643);
				match(CM);
				setState(644);
				explist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(646);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Static_method_invocateContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode SC() { return getToken(D96Parser.SC, 0); }
		public TerminalNode DOLLARID() { return getToken(D96Parser.DOLLARID, 0); }
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public ExplistsContext explists() {
			return getRuleContext(ExplistsContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public Static_method_invocateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_method_invocate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterStatic_method_invocate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitStatic_method_invocate(this);
		}
	}

	public final Static_method_invocateContext static_method_invocate() throws RecognitionException {
		Static_method_invocateContext _localctx = new Static_method_invocateContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_static_method_invocate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(649);
			match(ID);
			setState(650);
			match(SC);
			setState(651);
			match(DOLLARID);
			setState(652);
			match(LP);
			setState(653);
			explists();
			setState(654);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 54:
			return exp1_sempred((Exp1Context)_localctx, predIndex);
		case 55:
			return exp2_sempred((Exp2Context)_localctx, predIndex);
		case 56:
			return exp3_sempred((Exp3Context)_localctx, predIndex);
		case 59:
			return exp6_sempred((Exp6Context)_localctx, predIndex);
		case 60:
			return exp7_sempred((Exp7Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp1_sempred(Exp1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp2_sempred(Exp2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp3_sempred(Exp3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp6_sempred(Exp6Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp7_sempred(Exp7Context _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C\u0293\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u009c\n\3\3\4\3\4\3\4\3\4\5"+
		"\4\u00a2\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6\u00ac\n\6\3\7\3\7\3\7"+
		"\3\7\5\7\u00b2\n\7\3\b\3\b\5\b\u00b6\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00be"+
		"\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00c7\n\n\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d5\n\13\3\f\3\f\5\f\u00d9"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00e0\n\r\3\16\3\16\3\16\5\16\u00e5\n\16"+
		"\3\17\3\17\3\20\3\20\3\21\3\21\3\21\5\21\u00ee\n\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\23\3\23\5\23\u00f8\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00ff"+
		"\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u010a\n\26\3\27"+
		"\3\27\3\27\3\27\3\30\3\30\5\30\u0112\n\30\3\31\3\31\3\31\3\31\5\31\u0118"+
		"\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0123\n\32\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u012d\n\33\3\34\3\34\3\34\3\34"+
		"\3\34\7\34\u0134\n\34\f\34\16\34\u0137\13\34\3\34\3\34\3\35\3\35\3\36"+
		"\3\36\3\36\3\36\3\36\7\36\u0142\n\36\f\36\16\36\u0145\13\36\3\36\3\36"+
		"\3\37\3\37\3\37\3\37\5\37\u014d\n\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3"+
		"!\3!\3!\3!\3!\5!\u015c\n!\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3#\3#\3#\3#\3"+
		"#\3#\3#\3#\3#\3#\3#\3#\5#\u0170\n#\3$\3$\3$\3$\3$\3%\3%\5%\u0179\n%\3"+
		"&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0182\n\'\3\'\3\'\7\'\u0186\n\'\f\'\16\'"+
		"\u0189\13\'\3\'\5\'\u018c\n\'\3\'\3\'\3\'\6\'\u0191\n\'\r\'\16\'\u0192"+
		"\5\'\u0195\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\5)\u01a3\n)\3*\3*\3"+
		"*\3*\3*\3*\3+\3+\3+\5+\u01ae\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3"+
		"-\3-\5-\u01be\n-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\5\60\u01c9\n\60\3\60"+
		"\3\60\3\61\3\61\5\61\u01cf\n\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62"+
		"\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65"+
		"\3\65\3\65\5\65\u01e9\n\65\3\66\3\66\3\66\3\66\3\66\5\66\u01f0\n\66\3"+
		"\67\3\67\3\67\3\67\3\67\5\67\u01f7\n\67\38\38\38\38\38\38\78\u01ff\n8"+
		"\f8\168\u0202\138\39\39\39\39\39\39\79\u020a\n9\f9\169\u020d\139\3:\3"+
		":\3:\3:\3:\3:\7:\u0215\n:\f:\16:\u0218\13:\3;\3;\3;\5;\u021d\n;\3<\3<"+
		"\3<\5<\u0222\n<\3=\3=\3=\3=\3=\7=\u0229\n=\f=\16=\u022c\13=\3>\3>\3>\3"+
		">\3>\3>\7>\u0234\n>\f>\16>\u0237\13>\3?\3?\3?\3?\3?\5?\u023e\n?\3@\3@"+
		"\3@\5@\u0243\n@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u024f\nA\3B\3B\3B\3B"+
		"\3B\3C\3C\5C\u0258\nC\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F"+
		"\3F\5F\u026b\nF\3F\3F\3F\7F\u0270\nF\fF\16F\u0273\13F\3F\3F\5F\u0277\n"+
		"F\3F\3F\5F\u027b\nF\3G\3G\3G\3G\3H\3H\5H\u0283\nH\3I\3I\3I\3I\3I\5I\u028a"+
		"\nI\3J\3J\3J\3J\3J\3J\3J\3J\2\7nprxzK\2\4\6\b\n\f\16\20\22\24\26\30\32"+
		"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080"+
		"\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\13\4\2\21\21"+
		"\26\26\6\2\6\6\13\13\20\20\25\25\3\29=\3\2>?\4\2\37\37##\7\2\36\36\"\""+
		"&&()--\4\2!!%%\4\2\34\34  \5\2$$\'\'++\2\u0299\2\u0094\3\2\2\2\4\u009b"+
		"\3\2\2\2\6\u009d\3\2\2\2\b\u00a5\3\2\2\2\n\u00ab\3\2\2\2\f\u00b1\3\2\2"+
		"\2\16\u00b5\3\2\2\2\20\u00b7\3\2\2\2\22\u00c6\3\2\2\2\24\u00d4\3\2\2\2"+
		"\26\u00d8\3\2\2\2\30\u00df\3\2\2\2\32\u00e4\3\2\2\2\34\u00e6\3\2\2\2\36"+
		"\u00e8\3\2\2\2 \u00ed\3\2\2\2\"\u00ef\3\2\2\2$\u00f7\3\2\2\2&\u00fe\3"+
		"\2\2\2(\u0100\3\2\2\2*\u0109\3\2\2\2,\u010b\3\2\2\2.\u0111\3\2\2\2\60"+
		"\u0117\3\2\2\2\62\u0122\3\2\2\2\64\u012c\3\2\2\2\66\u012e\3\2\2\28\u013a"+
		"\3\2\2\2:\u013c\3\2\2\2<\u0148\3\2\2\2>\u0152\3\2\2\2@\u015b\3\2\2\2B"+
		"\u0161\3\2\2\2D\u016f\3\2\2\2F\u0171\3\2\2\2H\u0178\3\2\2\2J\u017a\3\2"+
		"\2\2L\u0194\3\2\2\2N\u0196\3\2\2\2P\u01a2\3\2\2\2R\u01a4\3\2\2\2T\u01ad"+
		"\3\2\2\2V\u01af\3\2\2\2X\u01bd\3\2\2\2Z\u01bf\3\2\2\2\\\u01c2\3\2\2\2"+
		"^\u01c5\3\2\2\2`\u01ce\3\2\2\2b\u01d2\3\2\2\2d\u01d8\3\2\2\2f\u01dd\3"+
		"\2\2\2h\u01e8\3\2\2\2j\u01ef\3\2\2\2l\u01f6\3\2\2\2n\u01f8\3\2\2\2p\u0203"+
		"\3\2\2\2r\u020e\3\2\2\2t\u021c\3\2\2\2v\u0221\3\2\2\2x\u0223\3\2\2\2z"+
		"\u022d\3\2\2\2|\u023d\3\2\2\2~\u0242\3\2\2\2\u0080\u024e\3\2\2\2\u0082"+
		"\u0250\3\2\2\2\u0084\u0257\3\2\2\2\u0086\u0259\3\2\2\2\u0088\u025e\3\2"+
		"\2\2\u008a\u027a\3\2\2\2\u008c\u027c\3\2\2\2\u008e\u0282\3\2\2\2\u0090"+
		"\u0289\3\2\2\2\u0092\u028b\3\2\2\2\u0094\u0095\5\4\3\2\u0095\u0096\7\2"+
		"\2\3\u0096\3\3\2\2\2\u0097\u0098\5\6\4\2\u0098\u0099\5\4\3\2\u0099\u009c"+
		"\3\2\2\2\u009a\u009c\5\6\4\2\u009b\u0097\3\2\2\2\u009b\u009a\3\2\2\2\u009c"+
		"\5\3\2\2\2\u009d\u009e\7\f\2\2\u009e\u00a1\7>\2\2\u009f\u00a0\7\67\2\2"+
		"\u00a0\u00a2\7>\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3"+
		"\3\2\2\2\u00a3\u00a4\5\b\5\2\u00a4\7\3\2\2\2\u00a5\u00a6\7\60\2\2\u00a6"+
		"\u00a7\5\n\6\2\u00a7\u00a8\7\61\2\2\u00a8\t\3\2\2\2\u00a9\u00ac\5\f\7"+
		"\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\13"+
		"\3\2\2\2\u00ad\u00ae\5\16\b\2\u00ae\u00af\5\f\7\2\u00af\u00b2\3\2\2\2"+
		"\u00b0\u00b2\5\16\b\2\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\r"+
		"\3\2\2\2\u00b3\u00b6\5\20\t\2\u00b4\u00b6\5 \21\2\u00b5\u00b3\3\2\2\2"+
		"\u00b5\u00b4\3\2\2\2\u00b6\17\3\2\2\2\u00b7\u00bd\t\2\2\2\u00b8\u00b9"+
		"\5\22\n\2\u00b9\u00ba\7\67\2\2\u00ba\u00bb\5\32\16\2\u00bb\u00be\3\2\2"+
		"\2\u00bc\u00be\5\24\13\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be"+
		"\u00bf\3\2\2\2\u00bf\u00c0\7\64\2\2\u00c0\21\3\2\2\2\u00c1\u00c2\5f\64"+
		"\2\u00c2\u00c3\7\66\2\2\u00c3\u00c4\5\22\n\2\u00c4\u00c7\3\2\2\2\u00c5"+
		"\u00c7\5f\64\2\u00c6\u00c1\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\23\3\2\2"+
		"\2\u00c8\u00c9\5f\64\2\u00c9\u00ca\7\66\2\2\u00ca\u00cb\5\24\13\2\u00cb"+
		"\u00cc\7\66\2\2\u00cc\u00cd\5j\66\2\u00cd\u00d5\3\2\2\2\u00ce\u00cf\5"+
		"f\64\2\u00cf\u00d0\7\67\2\2\u00d0\u00d1\5\32\16\2\u00d1\u00d2\7,\2\2\u00d2"+
		"\u00d3\5j\66\2\u00d3\u00d5\3\2\2\2\u00d4\u00c8\3\2\2\2\u00d4\u00ce\3\2"+
		"\2\2\u00d5\25\3\2\2\2\u00d6\u00d9\5\30\r\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6"+
		"\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\27\3\2\2\2\u00da\u00db\5\64\33\2\u00db"+
		"\u00dc\7\66\2\2\u00dc\u00dd\5\30\r\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5"+
		"\64\33\2\u00df\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\31\3\2\2\2\u00e1"+
		"\u00e5\5\34\17\2\u00e2\u00e5\5<\37\2\u00e3\u00e5\5\36\20\2\u00e4\u00e1"+
		"\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\33\3\2\2\2\u00e6"+
		"\u00e7\t\3\2\2\u00e7\35\3\2\2\2\u00e8\u00e9\7>\2\2\u00e9\37\3\2\2\2\u00ea"+
		"\u00ee\5\"\22\2\u00eb\u00ee\5b\62\2\u00ec\u00ee\5d\63\2\u00ed\u00ea\3"+
		"\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee!\3\2\2\2\u00ef\u00f0"+
		"\5f\64\2\u00f0\u00f1\7\62\2\2\u00f1\u00f2\5$\23\2\u00f2\u00f3\7\63\2\2"+
		"\u00f3\u00f4\5,\27\2\u00f4#\3\2\2\2\u00f5\u00f8\5&\24\2\u00f6\u00f8\3"+
		"\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8%\3\2\2\2\u00f9\u00fa"+
		"\5(\25\2\u00fa\u00fb\7\64\2\2\u00fb\u00fc\5&\24\2\u00fc\u00ff\3\2\2\2"+
		"\u00fd\u00ff\5(\25\2\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\'\3"+
		"\2\2\2\u0100\u0101\5*\26\2\u0101\u0102\7\67\2\2\u0102\u0103\5\32\16\2"+
		"\u0103)\3\2\2\2\u0104\u0105\5f\64\2\u0105\u0106\7\66\2\2\u0106\u0107\5"+
		"*\26\2\u0107\u010a\3\2\2\2\u0108\u010a\5f\64\2\u0109\u0104\3\2\2\2\u0109"+
		"\u0108\3\2\2\2\u010a+\3\2\2\2\u010b\u010c\7\60\2\2\u010c\u010d\5.\30\2"+
		"\u010d\u010e\7\61\2\2\u010e-\3\2\2\2\u010f\u0112\5\60\31\2\u0110\u0112"+
		"\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112/\3\2\2\2\u0113"+
		"\u0114\5\62\32\2\u0114\u0115\5\60\31\2\u0115\u0118\3\2\2\2\u0116\u0118"+
		"\5\62\32\2\u0117\u0113\3\2\2\2\u0117\u0116\3\2\2\2\u0118\61\3\2\2\2\u0119"+
		"\u0123\5> \2\u011a\u0123\5F$\2\u011b\u0123\5N(\2\u011c\u0123\5V,\2\u011d"+
		"\u0123\5Z.\2\u011e\u0123\5\\/\2\u011f\u0123\5^\60\2\u0120\u0123\5`\61"+
		"\2\u0121\u0123\5,\27\2\u0122\u0119\3\2\2\2\u0122\u011a\3\2\2\2\u0122\u011b"+
		"\3\2\2\2\u0122\u011c\3\2\2\2\u0122\u011d\3\2\2\2\u0122\u011e\3\2\2\2\u0122"+
		"\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123\63\3\2\2"+
		"\2\u0124\u012d\7:\2\2\u0125\u012d\79\2\2\u0126\u012d\7;\2\2\u0127\u012d"+
		"\7<\2\2\u0128\u012d\7=\2\2\u0129\u012d\5\66\34\2\u012a\u012d\5:\36\2\u012b"+
		"\u012d\7\7\2\2\u012c\u0124\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0126\3\2"+
		"\2\2\u012c\u0127\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u0129\3\2\2\2\u012c"+
		"\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d\65\3\2\2\2\u012e\u012f\7\24\2"+
		"\2\u012f\u0130\7\62\2\2\u0130\u0135\58\35\2\u0131\u0132\7\66\2\2\u0132"+
		"\u0134\58\35\2\u0133\u0131\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2"+
		"\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138"+
		"\u0139\7\63\2\2\u0139\67\3\2\2\2\u013a\u013b\t\4\2\2\u013b9\3\2\2\2\u013c"+
		"\u013d\7\24\2\2\u013d\u013e\7\62\2\2\u013e\u0143\5\66\34\2\u013f\u0140"+
		"\7\66\2\2\u0140\u0142\5\66\34\2\u0141\u013f\3\2\2\2\u0142\u0145\3\2\2"+
		"\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143"+
		"\3\2\2\2\u0146\u0147\7\63\2\2\u0147;\3\2\2\2\u0148\u0149\7\24\2\2\u0149"+
		"\u014c\7.\2\2\u014a\u014d\5\34\17\2\u014b\u014d\5<\37\2\u014c\u014a\3"+
		"\2\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\7\66\2\2\u014f"+
		"\u0150\79\2\2\u0150\u0151\7/\2\2\u0151=\3\2\2\2\u0152\u0153\t\2\2\2\u0153"+
		"\u0154\5@!\2\u0154\u0155\7\64\2\2\u0155?\3\2\2\2\u0156\u0157\5B\"\2\u0157"+
		"\u0158\7\67\2\2\u0158\u0159\5\32\16\2\u0159\u015c\3\2\2\2\u015a\u015c"+
		"\5D#\2\u015b\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015cA\3\2\2\2\u015d\u015e"+
		"\7>\2\2\u015e\u015f\7\66\2\2\u015f\u0162\5B\"\2\u0160\u0162\7>\2\2\u0161"+
		"\u015d\3\2\2\2\u0161\u0160\3\2\2\2\u0162C\3\2\2\2\u0163\u0164\7>\2\2\u0164"+
		"\u0165\7\66\2\2\u0165\u0166\5D#\2\u0166\u0167\7\66\2\2\u0167\u0168\5j"+
		"\66\2\u0168\u0170\3\2\2\2\u0169\u016a\7>\2\2\u016a\u016b\7\67\2\2\u016b"+
		"\u016c\5\32\16\2\u016c\u016d\7,\2\2\u016d\u016e\5j\66\2\u016e\u0170\3"+
		"\2\2\2\u016f\u0163\3\2\2\2\u016f\u0169\3\2\2\2\u0170E\3\2\2\2\u0171\u0172"+
		"\5H%\2\u0172\u0173\7,\2\2\u0173\u0174\5j\66\2\u0174\u0175\7\64\2\2\u0175"+
		"G\3\2\2\2\u0176\u0179\5J&\2\u0177\u0179\5L\'\2\u0178\u0176\3\2\2\2\u0178"+
		"\u0177\3\2\2\2\u0179I\3\2\2\2\u017a\u017b\7>\2\2\u017bK\3\2\2\2\u017c"+
		"\u017d\5j\66\2\u017d\u017e\5h\65\2\u017e\u0195\3\2\2\2\u017f\u0180\7\33"+
		"\2\2\u0180\u0182\7\65\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182"+
		"\u0183\3\2\2\2\u0183\u0187\7>\2\2\u0184\u0186\5h\65\2\u0185\u0184\3\2"+
		"\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188"+
		"\u0195\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018c\7\33\2\2\u018b\u018a\3"+
		"\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u0190\7>\2\2\u018e"+
		"\u018f\7\65\2\2\u018f\u0191\7>\2\2\u0190\u018e\3\2\2\2\u0191\u0192\3\2"+
		"\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194"+
		"\u017c\3\2\2\2\u0194\u0181\3\2\2\2\u0194\u018b\3\2\2\2\u0195M\3\2\2\2"+
		"\u0196\u0197\7\16\2\2\u0197\u0198\7\62\2\2\u0198\u0199\5j\66\2\u0199\u019a"+
		"\7\63\2\2\u019a\u019b\5,\27\2\u019b\u019c\5P)\2\u019c\u019d\5T+\2\u019d"+
		"O\3\2\2\2\u019e\u019f\5R*\2\u019f\u01a0\5P)\2\u01a0\u01a3\3\2\2\2\u01a1"+
		"\u01a3\3\2\2\2\u01a2\u019e\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3Q\3\2\2\2"+
		"\u01a4\u01a5\7\23\2\2\u01a5\u01a6\7\62\2\2\u01a6\u01a7\5j\66\2\u01a7\u01a8"+
		"\7\63\2\2\u01a8\u01a9\5,\27\2\u01a9S\3\2\2\2\u01aa\u01ab\7\30\2\2\u01ab"+
		"\u01ae\5,\27\2\u01ac\u01ae\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ad\u01ac\3\2"+
		"\2\2\u01aeU\3\2\2\2\u01af\u01b0\7\5\2\2\u01b0\u01b1\7\62\2\2\u01b1\u01b2"+
		"\5J&\2\u01b2\u01b3\7\31\2\2\u01b3\u01b4\5j\66\2\u01b4\u01b5\78\2\2\u01b5"+
		"\u01b6\5j\66\2\u01b6\u01b7\5X-\2\u01b7\u01b8\7\63\2\2\u01b8\u01b9\5,\27"+
		"\2\u01b9W\3\2\2\2\u01ba\u01bb\7\27\2\2\u01bb\u01be\5j\66\2\u01bc\u01be"+
		"\3\2\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2\u01beY\3\2\2\2\u01bf"+
		"\u01c0\7\4\2\2\u01c0\u01c1\7\64\2\2\u01c1[\3\2\2\2\u01c2\u01c3\7\t\2\2"+
		"\u01c3\u01c4\7\64\2\2\u01c4]\3\2\2\2\u01c5\u01c8\7\32\2\2\u01c6\u01c9"+
		"\5j\66\2\u01c7\u01c9\7?\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9"+
		"\u01ca\3\2\2\2\u01ca\u01cb\7\64\2\2\u01cb_\3\2\2\2\u01cc\u01cf\5\u0088"+
		"E\2\u01cd\u01cf\5\u0092J\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf"+
		"\u01d0\3\2\2\2\u01d0\u01d1\7\64\2\2\u01d1a\3\2\2\2\u01d2\u01d3\7\b\2\2"+
		"\u01d3\u01d4\7\62\2\2\u01d4\u01d5\5$\23\2\u01d5\u01d6\7\63\2\2\u01d6\u01d7"+
		"\5,\27\2\u01d7c\3\2\2\2\u01d8\u01d9\7\r\2\2\u01d9\u01da\7\62\2\2\u01da"+
		"\u01db\7\63\2\2\u01db\u01dc\5,\27\2\u01dce\3\2\2\2\u01dd\u01de\t\5\2\2"+
		"\u01deg\3\2\2\2\u01df\u01e0\7.\2\2\u01e0\u01e1\5j\66\2\u01e1\u01e2\7/"+
		"\2\2\u01e2\u01e9\3\2\2\2\u01e3\u01e4\7.\2\2\u01e4\u01e5\5j\66\2\u01e5"+
		"\u01e6\7/\2\2\u01e6\u01e7\5h\65\2\u01e7\u01e9\3\2\2\2\u01e8\u01df\3\2"+
		"\2\2\u01e8\u01e3\3\2\2\2\u01e9i\3\2\2\2\u01ea\u01eb\5l\67\2\u01eb\u01ec"+
		"\t\6\2\2\u01ec\u01ed\5l\67\2\u01ed\u01f0\3\2\2\2\u01ee\u01f0\5l\67\2\u01ef"+
		"\u01ea\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0k\3\2\2\2\u01f1\u01f2\5n8\2\u01f2"+
		"\u01f3\t\7\2\2\u01f3\u01f4\5n8\2\u01f4\u01f7\3\2\2\2\u01f5\u01f7\5n8\2"+
		"\u01f6\u01f1\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7m\3\2\2\2\u01f8\u01f9\b"+
		"8\1\2\u01f9\u01fa\5p9\2\u01fa\u0200\3\2\2\2\u01fb\u01fc\f\4\2\2\u01fc"+
		"\u01fd\t\b\2\2\u01fd\u01ff\5p9\2\u01fe\u01fb\3\2\2\2\u01ff\u0202\3\2\2"+
		"\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201o\3\2\2\2\u0202\u0200"+
		"\3\2\2\2\u0203\u0204\b9\1\2\u0204\u0205\5r:\2\u0205\u020b\3\2\2\2\u0206"+
		"\u0207\f\4\2\2\u0207\u0208\t\t\2\2\u0208\u020a\5r:\2\u0209\u0206\3\2\2"+
		"\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020cq"+
		"\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u020f\b:\1\2\u020f\u0210\5t;\2\u0210"+
		"\u0216\3\2\2\2\u0211\u0212\f\4\2\2\u0212\u0213\t\n\2\2\u0213\u0215\5t"+
		";\2\u0214\u0211\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216"+
		"\u0217\3\2\2\2\u0217s\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u021a\7\35\2\2"+
		"\u021a\u021d\5t;\2\u021b\u021d\5v<\2\u021c\u0219\3\2\2\2\u021c\u021b\3"+
		"\2\2\2\u021du\3\2\2\2\u021e\u021f\7 \2\2\u021f\u0222\5v<\2\u0220\u0222"+
		"\5x=\2\u0221\u021e\3\2\2\2\u0221\u0220\3\2\2\2\u0222w\3\2\2\2\u0223\u0224"+
		"\b=\1\2\u0224\u0225\5z>\2\u0225\u022a\3\2\2\2\u0226\u0227\f\4\2\2\u0227"+
		"\u0229\5h\65\2\u0228\u0226\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2"+
		"\2\2\u022a\u022b\3\2\2\2\u022by\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u022e"+
		"\b>\1\2\u022e\u022f\5|?\2\u022f\u0235\3\2\2\2\u0230\u0231\f\4\2\2\u0231"+
		"\u0232\7\65\2\2\u0232\u0234\5|?\2\u0233\u0230\3\2\2\2\u0234\u0237\3\2"+
		"\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236{\3\2\2\2\u0237\u0235"+
		"\3\2\2\2\u0238\u0239\5~@\2\u0239\u023a\7*\2\2\u023a\u023b\5\u0084C\2\u023b"+
		"\u023e\3\2\2\2\u023c\u023e\5~@\2\u023d\u0238\3\2\2\2\u023d\u023c\3\2\2"+
		"\2\u023e}\3\2\2\2\u023f\u0240\7\22\2\2\u0240\u0243\5~@\2\u0241\u0243\5"+
		"\u0080A\2\u0242\u023f\3\2\2\2\u0242\u0241\3\2\2\2\u0243\177\3\2\2\2\u0244"+
		"\u024f\5\64\33\2\u0245\u024f\7\n\2\2\u0246\u024f\7\17\2\2\u0247\u024f"+
		"\7>\2\2\u0248\u024f\7\33\2\2\u0249\u024f\5\u0082B\2\u024a\u024b\7\62\2"+
		"\2\u024b\u024c\5j\66\2\u024c\u024d\7\63\2\2\u024d\u024f\3\2\2\2\u024e"+
		"\u0244\3\2\2\2\u024e\u0245\3\2\2\2\u024e\u0246\3\2\2\2\u024e\u0247\3\2"+
		"\2\2\u024e\u0248\3\2\2\2\u024e\u0249\3\2\2\2\u024e\u024a\3\2\2\2\u024f"+
		"\u0081\3\2\2\2\u0250\u0251\7>\2\2\u0251\u0252\7\62\2\2\u0252\u0253\5\u008e"+
		"H\2\u0253\u0254\7\63\2\2\u0254\u0083\3\2\2\2\u0255\u0258\7?\2\2\u0256"+
		"\u0258\5\u0086D\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u0085"+
		"\3\2\2\2\u0259\u025a\7?\2\2\u025a\u025b\7\62\2\2\u025b\u025c\5\u008eH"+
		"\2\u025c\u025d\7\63\2\2\u025d\u0087\3\2\2\2\u025e\u025f\5\u008aF\2\u025f"+
		"\u0260\7\65\2\2\u0260\u0261\7>\2\2\u0261\u0262\7\62\2\2\u0262\u0263\5"+
		"\u008eH\2\u0263\u0264\7\63\2\2\u0264\u0089\3\2\2\2\u0265\u027b\7>\2\2"+
		"\u0266\u0267\7\22\2\2\u0267\u027b\5\u0082B\2\u0268\u027b\7\33\2\2\u0269"+
		"\u026b\7\33\2\2\u026a\u0269\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u026c\3"+
		"\2\2\2\u026c\u0271\7>\2\2\u026d\u026e\7\65\2\2\u026e\u0270\7>\2\2\u026f"+
		"\u026d\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f\3\2\2\2\u0271\u0272\3\2"+
		"\2\2\u0272\u0276\3\2\2\2\u0273\u0271\3\2\2\2\u0274\u0275\7\65\2\2\u0275"+
		"\u0277\5\u0082B\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278"+
		"\3\2\2\2\u0278\u027b\5\u008aF\2\u0279\u027b\5\u008cG\2\u027a\u0265\3\2"+
		"\2\2\u027a\u0266\3\2\2\2\u027a\u0268\3\2\2\2\u027a\u026a\3\2\2\2\u027a"+
		"\u0279\3\2\2\2\u027b\u008b\3\2\2\2\u027c\u027d\7\62\2\2\u027d\u027e\5"+
		"\u008aF\2\u027e\u027f\7\63\2\2\u027f\u008d\3\2\2\2\u0280\u0283\5\u0090"+
		"I\2\u0281\u0283\3\2\2\2\u0282\u0280\3\2\2\2\u0282\u0281\3\2\2\2\u0283"+
		"\u008f\3\2\2\2\u0284\u0285\5j\66\2\u0285\u0286\7\66\2\2\u0286\u0287\5"+
		"\u0090I\2\u0287\u028a\3\2\2\2\u0288\u028a\5j\66\2\u0289\u0284\3\2\2\2"+
		"\u0289\u0288\3\2\2\2\u028a\u0091\3\2\2\2\u028b\u028c\7>\2\2\u028c\u028d"+
		"\7*\2\2\u028d\u028e\7?\2\2\u028e\u028f\7\62\2\2\u028f\u0290\5\u008eH\2"+
		"\u0290\u0291\7\63\2\2\u0291\u0093\3\2\2\2:\u009b\u00a1\u00ab\u00b1\u00b5"+
		"\u00bd\u00c6\u00d4\u00d8\u00df\u00e4\u00ed\u00f7\u00fe\u0109\u0111\u0117"+
		"\u0122\u012c\u0135\u0143\u014c\u015b\u0161\u016f\u0178\u0181\u0187\u018b"+
		"\u0192\u0194\u01a2\u01ad\u01bd\u01c8\u01ce\u01e8\u01ef\u01f6\u0200\u020b"+
		"\u0216\u021c\u0221\u022a\u0235\u023d\u0242\u024e\u0257\u026a\u0271\u0276"+
		"\u027a\u0282\u0289";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}