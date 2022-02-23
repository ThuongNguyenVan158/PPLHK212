// Generated from D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link D96Parser}.
 */
public interface D96Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link D96Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(D96Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(D96Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#class_declares}.
	 * @param ctx the parse tree
	 */
	void enterClass_declares(D96Parser.Class_declaresContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#class_declares}.
	 * @param ctx the parse tree
	 */
	void exitClass_declares(D96Parser.Class_declaresContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#class_declare}.
	 * @param ctx the parse tree
	 */
	void enterClass_declare(D96Parser.Class_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#class_declare}.
	 * @param ctx the parse tree
	 */
	void exitClass_declare(D96Parser.Class_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#member_decl}.
	 * @param ctx the parse tree
	 */
	void enterMember_decl(D96Parser.Member_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#member_decl}.
	 * @param ctx the parse tree
	 */
	void exitMember_decl(D96Parser.Member_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#memberlist}.
	 * @param ctx the parse tree
	 */
	void enterMemberlist(D96Parser.MemberlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#memberlist}.
	 * @param ctx the parse tree
	 */
	void exitMemberlist(D96Parser.MemberlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#members}.
	 * @param ctx the parse tree
	 */
	void enterMembers(D96Parser.MembersContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#members}.
	 * @param ctx the parse tree
	 */
	void exitMembers(D96Parser.MembersContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#member}.
	 * @param ctx the parse tree
	 */
	void enterMember(D96Parser.MemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#member}.
	 * @param ctx the parse tree
	 */
	void exitMember(D96Parser.MemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#att_declare}.
	 * @param ctx the parse tree
	 */
	void enterAtt_declare(D96Parser.Att_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#att_declare}.
	 * @param ctx the parse tree
	 */
	void exitAtt_declare(D96Parser.Att_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#att_names}.
	 * @param ctx the parse tree
	 */
	void enterAtt_names(D96Parser.Att_namesContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#att_names}.
	 * @param ctx the parse tree
	 */
	void exitAtt_names(D96Parser.Att_namesContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#att_init_value}.
	 * @param ctx the parse tree
	 */
	void enterAtt_init_value(D96Parser.Att_init_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#att_init_value}.
	 * @param ctx the parse tree
	 */
	void exitAtt_init_value(D96Parser.Att_init_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#values}.
	 * @param ctx the parse tree
	 */
	void enterValues(D96Parser.ValuesContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#values}.
	 * @param ctx the parse tree
	 */
	void exitValues(D96Parser.ValuesContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(D96Parser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(D96Parser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#data_type}.
	 * @param ctx the parse tree
	 */
	void enterData_type(D96Parser.Data_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#data_type}.
	 * @param ctx the parse tree
	 */
	void exitData_type(D96Parser.Data_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_type(D96Parser.Primitive_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_type(D96Parser.Primitive_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#classtype}.
	 * @param ctx the parse tree
	 */
	void enterClasstype(D96Parser.ClasstypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#classtype}.
	 * @param ctx the parse tree
	 */
	void exitClasstype(D96Parser.ClasstypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#method_declare}.
	 * @param ctx the parse tree
	 */
	void enterMethod_declare(D96Parser.Method_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#method_declare}.
	 * @param ctx the parse tree
	 */
	void exitMethod_declare(D96Parser.Method_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#func_declare}.
	 * @param ctx the parse tree
	 */
	void enterFunc_declare(D96Parser.Func_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#func_declare}.
	 * @param ctx the parse tree
	 */
	void exitFunc_declare(D96Parser.Func_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(D96Parser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(D96Parser.ParamlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(D96Parser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(D96Parser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(D96Parser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(D96Parser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#idnamelist}.
	 * @param ctx the parse tree
	 */
	void enterIdnamelist(D96Parser.IdnamelistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#idnamelist}.
	 * @param ctx the parse tree
	 */
	void exitIdnamelist(D96Parser.IdnamelistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#blockstatment}.
	 * @param ctx the parse tree
	 */
	void enterBlockstatment(D96Parser.BlockstatmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#blockstatment}.
	 * @param ctx the parse tree
	 */
	void exitBlockstatment(D96Parser.BlockstatmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#stamentlist}.
	 * @param ctx the parse tree
	 */
	void enterStamentlist(D96Parser.StamentlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#stamentlist}.
	 * @param ctx the parse tree
	 */
	void exitStamentlist(D96Parser.StamentlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#staments}.
	 * @param ctx the parse tree
	 */
	void enterStaments(D96Parser.StamentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#staments}.
	 * @param ctx the parse tree
	 */
	void exitStaments(D96Parser.StamentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#stament}.
	 * @param ctx the parse tree
	 */
	void enterStament(D96Parser.StamentContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#stament}.
	 * @param ctx the parse tree
	 */
	void exitStament(D96Parser.StamentContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(D96Parser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(D96Parser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#index_array_literal}.
	 * @param ctx the parse tree
	 */
	void enterIndex_array_literal(D96Parser.Index_array_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#index_array_literal}.
	 * @param ctx the parse tree
	 */
	void exitIndex_array_literal(D96Parser.Index_array_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#primitive_literal}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_literal(D96Parser.Primitive_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#primitive_literal}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_literal(D96Parser.Primitive_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#multi_array}.
	 * @param ctx the parse tree
	 */
	void enterMulti_array(D96Parser.Multi_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#multi_array}.
	 * @param ctx the parse tree
	 */
	void exitMulti_array(D96Parser.Multi_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#array_type}.
	 * @param ctx the parse tree
	 */
	void enterArray_type(D96Parser.Array_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#array_type}.
	 * @param ctx the parse tree
	 */
	void exitArray_type(D96Parser.Array_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#vardecl_stm}.
	 * @param ctx the parse tree
	 */
	void enterVardecl_stm(D96Parser.Vardecl_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#vardecl_stm}.
	 * @param ctx the parse tree
	 */
	void exitVardecl_stm(D96Parser.Vardecl_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#varlist}.
	 * @param ctx the parse tree
	 */
	void enterVarlist(D96Parser.VarlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#varlist}.
	 * @param ctx the parse tree
	 */
	void exitVarlist(D96Parser.VarlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#variable_names}.
	 * @param ctx the parse tree
	 */
	void enterVariable_names(D96Parser.Variable_namesContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#variable_names}.
	 * @param ctx the parse tree
	 */
	void exitVariable_names(D96Parser.Variable_namesContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#variable_init_value}.
	 * @param ctx the parse tree
	 */
	void enterVariable_init_value(D96Parser.Variable_init_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#variable_init_value}.
	 * @param ctx the parse tree
	 */
	void exitVariable_init_value(D96Parser.Variable_init_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#assign_stm}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stm(D96Parser.Assign_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#assign_stm}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stm(D96Parser.Assign_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#leftassign}.
	 * @param ctx the parse tree
	 */
	void enterLeftassign(D96Parser.LeftassignContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#leftassign}.
	 * @param ctx the parse tree
	 */
	void exitLeftassign(D96Parser.LeftassignContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#scalarvar}.
	 * @param ctx the parse tree
	 */
	void enterScalarvar(D96Parser.ScalarvarContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#scalarvar}.
	 * @param ctx the parse tree
	 */
	void exitScalarvar(D96Parser.ScalarvarContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#indexed_exp}.
	 * @param ctx the parse tree
	 */
	void enterIndexed_exp(D96Parser.Indexed_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#indexed_exp}.
	 * @param ctx the parse tree
	 */
	void exitIndexed_exp(D96Parser.Indexed_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#if_stm}.
	 * @param ctx the parse tree
	 */
	void enterIf_stm(D96Parser.If_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#if_stm}.
	 * @param ctx the parse tree
	 */
	void exitIf_stm(D96Parser.If_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#elseif_stms}.
	 * @param ctx the parse tree
	 */
	void enterElseif_stms(D96Parser.Elseif_stmsContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#elseif_stms}.
	 * @param ctx the parse tree
	 */
	void exitElseif_stms(D96Parser.Elseif_stmsContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#elseif_stm}.
	 * @param ctx the parse tree
	 */
	void enterElseif_stm(D96Parser.Elseif_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#elseif_stm}.
	 * @param ctx the parse tree
	 */
	void exitElseif_stm(D96Parser.Elseif_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#else_stm}.
	 * @param ctx the parse tree
	 */
	void enterElse_stm(D96Parser.Else_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#else_stm}.
	 * @param ctx the parse tree
	 */
	void exitElse_stm(D96Parser.Else_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#forin_stm}.
	 * @param ctx the parse tree
	 */
	void enterForin_stm(D96Parser.Forin_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#forin_stm}.
	 * @param ctx the parse tree
	 */
	void exitForin_stm(D96Parser.Forin_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#steploop}.
	 * @param ctx the parse tree
	 */
	void enterSteploop(D96Parser.SteploopContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#steploop}.
	 * @param ctx the parse tree
	 */
	void exitSteploop(D96Parser.SteploopContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#break_stm}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stm(D96Parser.Break_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#break_stm}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stm(D96Parser.Break_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#continue_stm}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stm(D96Parser.Continue_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#continue_stm}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stm(D96Parser.Continue_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#return_stm}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stm(D96Parser.Return_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#return_stm}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stm(D96Parser.Return_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#method_invocation_stm}.
	 * @param ctx the parse tree
	 */
	void enterMethod_invocation_stm(D96Parser.Method_invocation_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#method_invocation_stm}.
	 * @param ctx the parse tree
	 */
	void exitMethod_invocation_stm(D96Parser.Method_invocation_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#contructor_declare}.
	 * @param ctx the parse tree
	 */
	void enterContructor_declare(D96Parser.Contructor_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#contructor_declare}.
	 * @param ctx the parse tree
	 */
	void exitContructor_declare(D96Parser.Contructor_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#detructor_declare}.
	 * @param ctx the parse tree
	 */
	void enterDetructor_declare(D96Parser.Detructor_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#detructor_declare}.
	 * @param ctx the parse tree
	 */
	void exitDetructor_declare(D96Parser.Detructor_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#idname}.
	 * @param ctx the parse tree
	 */
	void enterIdname(D96Parser.IdnameContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#idname}.
	 * @param ctx the parse tree
	 */
	void exitIdname(D96Parser.IdnameContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#index_operator}.
	 * @param ctx the parse tree
	 */
	void enterIndex_operator(D96Parser.Index_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#index_operator}.
	 * @param ctx the parse tree
	 */
	void exitIndex_operator(D96Parser.Index_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(D96Parser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(D96Parser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp0}.
	 * @param ctx the parse tree
	 */
	void enterExp0(D96Parser.Exp0Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp0}.
	 * @param ctx the parse tree
	 */
	void exitExp0(D96Parser.Exp0Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp1}.
	 * @param ctx the parse tree
	 */
	void enterExp1(D96Parser.Exp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp1}.
	 * @param ctx the parse tree
	 */
	void exitExp1(D96Parser.Exp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp2}.
	 * @param ctx the parse tree
	 */
	void enterExp2(D96Parser.Exp2Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp2}.
	 * @param ctx the parse tree
	 */
	void exitExp2(D96Parser.Exp2Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp3}.
	 * @param ctx the parse tree
	 */
	void enterExp3(D96Parser.Exp3Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp3}.
	 * @param ctx the parse tree
	 */
	void exitExp3(D96Parser.Exp3Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp4}.
	 * @param ctx the parse tree
	 */
	void enterExp4(D96Parser.Exp4Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp4}.
	 * @param ctx the parse tree
	 */
	void exitExp4(D96Parser.Exp4Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp5}.
	 * @param ctx the parse tree
	 */
	void enterExp5(D96Parser.Exp5Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp5}.
	 * @param ctx the parse tree
	 */
	void exitExp5(D96Parser.Exp5Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp6}.
	 * @param ctx the parse tree
	 */
	void enterExp6(D96Parser.Exp6Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp6}.
	 * @param ctx the parse tree
	 */
	void exitExp6(D96Parser.Exp6Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp7}.
	 * @param ctx the parse tree
	 */
	void enterExp7(D96Parser.Exp7Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp7}.
	 * @param ctx the parse tree
	 */
	void exitExp7(D96Parser.Exp7Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp8}.
	 * @param ctx the parse tree
	 */
	void enterExp8(D96Parser.Exp8Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp8}.
	 * @param ctx the parse tree
	 */
	void exitExp8(D96Parser.Exp8Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp9}.
	 * @param ctx the parse tree
	 */
	void enterExp9(D96Parser.Exp9Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp9}.
	 * @param ctx the parse tree
	 */
	void exitExp9(D96Parser.Exp9Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#exp10}.
	 * @param ctx the parse tree
	 */
	void enterExp10(D96Parser.Exp10Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#exp10}.
	 * @param ctx the parse tree
	 */
	void exitExp10(D96Parser.Exp10Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#func_call}.
	 * @param ctx the parse tree
	 */
	void enterFunc_call(D96Parser.Func_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#func_call}.
	 * @param ctx the parse tree
	 */
	void exitFunc_call(D96Parser.Func_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#static_operand}.
	 * @param ctx the parse tree
	 */
	void enterStatic_operand(D96Parser.Static_operandContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#static_operand}.
	 * @param ctx the parse tree
	 */
	void exitStatic_operand(D96Parser.Static_operandContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#static_func_call}.
	 * @param ctx the parse tree
	 */
	void enterStatic_func_call(D96Parser.Static_func_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#static_func_call}.
	 * @param ctx the parse tree
	 */
	void exitStatic_func_call(D96Parser.Static_func_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#method_invocate}.
	 * @param ctx the parse tree
	 */
	void enterMethod_invocate(D96Parser.Method_invocateContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#method_invocate}.
	 * @param ctx the parse tree
	 */
	void exitMethod_invocate(D96Parser.Method_invocateContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#object_exp}.
	 * @param ctx the parse tree
	 */
	void enterObject_exp(D96Parser.Object_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#object_exp}.
	 * @param ctx the parse tree
	 */
	void exitObject_exp(D96Parser.Object_expContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#object_exp1}.
	 * @param ctx the parse tree
	 */
	void enterObject_exp1(D96Parser.Object_exp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#object_exp1}.
	 * @param ctx the parse tree
	 */
	void exitObject_exp1(D96Parser.Object_exp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#explists}.
	 * @param ctx the parse tree
	 */
	void enterExplists(D96Parser.ExplistsContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#explists}.
	 * @param ctx the parse tree
	 */
	void exitExplists(D96Parser.ExplistsContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#explist}.
	 * @param ctx the parse tree
	 */
	void enterExplist(D96Parser.ExplistContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#explist}.
	 * @param ctx the parse tree
	 */
	void exitExplist(D96Parser.ExplistContext ctx);
	/**
	 * Enter a parse tree produced by {@link D96Parser#static_method_invocate}.
	 * @param ctx the parse tree
	 */
	void enterStatic_method_invocate(D96Parser.Static_method_invocateContext ctx);
	/**
	 * Exit a parse tree produced by {@link D96Parser#static_method_invocate}.
	 * @param ctx the parse tree
	 */
	void exitStatic_method_invocate(D96Parser.Static_method_invocateContext ctx);
}