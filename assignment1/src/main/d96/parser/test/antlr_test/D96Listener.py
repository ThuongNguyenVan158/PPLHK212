# Generated from D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#class_declares.
    def enterClass_declares(self, ctx:D96Parser.Class_declaresContext):
        pass

    # Exit a parse tree produced by D96Parser#class_declares.
    def exitClass_declares(self, ctx:D96Parser.Class_declaresContext):
        pass


    # Enter a parse tree produced by D96Parser#class_declare.
    def enterClass_declare(self, ctx:D96Parser.Class_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#class_declare.
    def exitClass_declare(self, ctx:D96Parser.Class_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#member_decl.
    def enterMember_decl(self, ctx:D96Parser.Member_declContext):
        pass

    # Exit a parse tree produced by D96Parser#member_decl.
    def exitMember_decl(self, ctx:D96Parser.Member_declContext):
        pass


    # Enter a parse tree produced by D96Parser#memberlist.
    def enterMemberlist(self, ctx:D96Parser.MemberlistContext):
        pass

    # Exit a parse tree produced by D96Parser#memberlist.
    def exitMemberlist(self, ctx:D96Parser.MemberlistContext):
        pass


    # Enter a parse tree produced by D96Parser#members.
    def enterMembers(self, ctx:D96Parser.MembersContext):
        pass

    # Exit a parse tree produced by D96Parser#members.
    def exitMembers(self, ctx:D96Parser.MembersContext):
        pass


    # Enter a parse tree produced by D96Parser#member.
    def enterMember(self, ctx:D96Parser.MemberContext):
        pass

    # Exit a parse tree produced by D96Parser#member.
    def exitMember(self, ctx:D96Parser.MemberContext):
        pass


    # Enter a parse tree produced by D96Parser#att_declare.
    def enterAtt_declare(self, ctx:D96Parser.Att_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#att_declare.
    def exitAtt_declare(self, ctx:D96Parser.Att_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#att_names.
    def enterAtt_names(self, ctx:D96Parser.Att_namesContext):
        pass

    # Exit a parse tree produced by D96Parser#att_names.
    def exitAtt_names(self, ctx:D96Parser.Att_namesContext):
        pass


    # Enter a parse tree produced by D96Parser#identname.
    def enterIdentname(self, ctx:D96Parser.IdentnameContext):
        pass

    # Exit a parse tree produced by D96Parser#identname.
    def exitIdentname(self, ctx:D96Parser.IdentnameContext):
        pass


    # Enter a parse tree produced by D96Parser#att_init_value.
    def enterAtt_init_value(self, ctx:D96Parser.Att_init_valueContext):
        pass

    # Exit a parse tree produced by D96Parser#att_init_value.
    def exitAtt_init_value(self, ctx:D96Parser.Att_init_valueContext):
        pass


    # Enter a parse tree produced by D96Parser#values.
    def enterValues(self, ctx:D96Parser.ValuesContext):
        pass

    # Exit a parse tree produced by D96Parser#values.
    def exitValues(self, ctx:D96Parser.ValuesContext):
        pass


    # Enter a parse tree produced by D96Parser#value.
    def enterValue(self, ctx:D96Parser.ValueContext):
        pass

    # Exit a parse tree produced by D96Parser#value.
    def exitValue(self, ctx:D96Parser.ValueContext):
        pass


    # Enter a parse tree produced by D96Parser#data_type.
    def enterData_type(self, ctx:D96Parser.Data_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#data_type.
    def exitData_type(self, ctx:D96Parser.Data_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#primitive_type.
    def enterPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#primitive_type.
    def exitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#classtype.
    def enterClasstype(self, ctx:D96Parser.ClasstypeContext):
        pass

    # Exit a parse tree produced by D96Parser#classtype.
    def exitClasstype(self, ctx:D96Parser.ClasstypeContext):
        pass


    # Enter a parse tree produced by D96Parser#method_declare.
    def enterMethod_declare(self, ctx:D96Parser.Method_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#method_declare.
    def exitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#func_declare.
    def enterFunc_declare(self, ctx:D96Parser.Func_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#func_declare.
    def exitFunc_declare(self, ctx:D96Parser.Func_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#paramlist.
    def enterParamlist(self, ctx:D96Parser.ParamlistContext):
        pass

    # Exit a parse tree produced by D96Parser#paramlist.
    def exitParamlist(self, ctx:D96Parser.ParamlistContext):
        pass


    # Enter a parse tree produced by D96Parser#params.
    def enterParams(self, ctx:D96Parser.ParamsContext):
        pass

    # Exit a parse tree produced by D96Parser#params.
    def exitParams(self, ctx:D96Parser.ParamsContext):
        pass


    # Enter a parse tree produced by D96Parser#param.
    def enterParam(self, ctx:D96Parser.ParamContext):
        pass

    # Exit a parse tree produced by D96Parser#param.
    def exitParam(self, ctx:D96Parser.ParamContext):
        pass


    # Enter a parse tree produced by D96Parser#blockstatment.
    def enterBlockstatment(self, ctx:D96Parser.BlockstatmentContext):
        pass

    # Exit a parse tree produced by D96Parser#blockstatment.
    def exitBlockstatment(self, ctx:D96Parser.BlockstatmentContext):
        pass


    # Enter a parse tree produced by D96Parser#stamentlist.
    def enterStamentlist(self, ctx:D96Parser.StamentlistContext):
        pass

    # Exit a parse tree produced by D96Parser#stamentlist.
    def exitStamentlist(self, ctx:D96Parser.StamentlistContext):
        pass


    # Enter a parse tree produced by D96Parser#staments.
    def enterStaments(self, ctx:D96Parser.StamentsContext):
        pass

    # Exit a parse tree produced by D96Parser#staments.
    def exitStaments(self, ctx:D96Parser.StamentsContext):
        pass


    # Enter a parse tree produced by D96Parser#stament.
    def enterStament(self, ctx:D96Parser.StamentContext):
        pass

    # Exit a parse tree produced by D96Parser#stament.
    def exitStament(self, ctx:D96Parser.StamentContext):
        pass


    # Enter a parse tree produced by D96Parser#literal.
    def enterLiteral(self, ctx:D96Parser.LiteralContext):
        pass

    # Exit a parse tree produced by D96Parser#literal.
    def exitLiteral(self, ctx:D96Parser.LiteralContext):
        pass


    # Enter a parse tree produced by D96Parser#index_array_literal.
    def enterIndex_array_literal(self, ctx:D96Parser.Index_array_literalContext):
        pass

    # Exit a parse tree produced by D96Parser#index_array_literal.
    def exitIndex_array_literal(self, ctx:D96Parser.Index_array_literalContext):
        pass


    # Enter a parse tree produced by D96Parser#primitive_literal.
    def enterPrimitive_literal(self, ctx:D96Parser.Primitive_literalContext):
        pass

    # Exit a parse tree produced by D96Parser#primitive_literal.
    def exitPrimitive_literal(self, ctx:D96Parser.Primitive_literalContext):
        pass


    # Enter a parse tree produced by D96Parser#multi_array.
    def enterMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        pass

    # Exit a parse tree produced by D96Parser#multi_array.
    def exitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        pass


    # Enter a parse tree produced by D96Parser#array_type.
    def enterArray_type(self, ctx:D96Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by D96Parser#array_type.
    def exitArray_type(self, ctx:D96Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by D96Parser#vardecl_stm.
    def enterVardecl_stm(self, ctx:D96Parser.Vardecl_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#vardecl_stm.
    def exitVardecl_stm(self, ctx:D96Parser.Vardecl_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#varlist.
    def enterVarlist(self, ctx:D96Parser.VarlistContext):
        pass

    # Exit a parse tree produced by D96Parser#varlist.
    def exitVarlist(self, ctx:D96Parser.VarlistContext):
        pass


    # Enter a parse tree produced by D96Parser#variable_names.
    def enterVariable_names(self, ctx:D96Parser.Variable_namesContext):
        pass

    # Exit a parse tree produced by D96Parser#variable_names.
    def exitVariable_names(self, ctx:D96Parser.Variable_namesContext):
        pass


    # Enter a parse tree produced by D96Parser#variable_init_value.
    def enterVariable_init_value(self, ctx:D96Parser.Variable_init_valueContext):
        pass

    # Exit a parse tree produced by D96Parser#variable_init_value.
    def exitVariable_init_value(self, ctx:D96Parser.Variable_init_valueContext):
        pass


    # Enter a parse tree produced by D96Parser#assign_stm.
    def enterAssign_stm(self, ctx:D96Parser.Assign_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#assign_stm.
    def exitAssign_stm(self, ctx:D96Parser.Assign_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#leftassign.
    def enterLeftassign(self, ctx:D96Parser.LeftassignContext):
        pass

    # Exit a parse tree produced by D96Parser#leftassign.
    def exitLeftassign(self, ctx:D96Parser.LeftassignContext):
        pass


    # Enter a parse tree produced by D96Parser#scalarvar.
    def enterScalarvar(self, ctx:D96Parser.ScalarvarContext):
        pass

    # Exit a parse tree produced by D96Parser#scalarvar.
    def exitScalarvar(self, ctx:D96Parser.ScalarvarContext):
        pass


    # Enter a parse tree produced by D96Parser#indexed_exp.
    def enterIndexed_exp(self, ctx:D96Parser.Indexed_expContext):
        pass

    # Exit a parse tree produced by D96Parser#indexed_exp.
    def exitIndexed_exp(self, ctx:D96Parser.Indexed_expContext):
        pass


    # Enter a parse tree produced by D96Parser#if_stm.
    def enterIf_stm(self, ctx:D96Parser.If_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#if_stm.
    def exitIf_stm(self, ctx:D96Parser.If_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#elseif_stms.
    def enterElseif_stms(self, ctx:D96Parser.Elseif_stmsContext):
        pass

    # Exit a parse tree produced by D96Parser#elseif_stms.
    def exitElseif_stms(self, ctx:D96Parser.Elseif_stmsContext):
        pass


    # Enter a parse tree produced by D96Parser#elseif_stm.
    def enterElseif_stm(self, ctx:D96Parser.Elseif_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#elseif_stm.
    def exitElseif_stm(self, ctx:D96Parser.Elseif_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#else_stm.
    def enterElse_stm(self, ctx:D96Parser.Else_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#else_stm.
    def exitElse_stm(self, ctx:D96Parser.Else_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#forin_stm.
    def enterForin_stm(self, ctx:D96Parser.Forin_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#forin_stm.
    def exitForin_stm(self, ctx:D96Parser.Forin_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#steploop.
    def enterSteploop(self, ctx:D96Parser.SteploopContext):
        pass

    # Exit a parse tree produced by D96Parser#steploop.
    def exitSteploop(self, ctx:D96Parser.SteploopContext):
        pass


    # Enter a parse tree produced by D96Parser#break_stm.
    def enterBreak_stm(self, ctx:D96Parser.Break_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#break_stm.
    def exitBreak_stm(self, ctx:D96Parser.Break_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#continue_stm.
    def enterContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#continue_stm.
    def exitContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#return_stm.
    def enterReturn_stm(self, ctx:D96Parser.Return_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#return_stm.
    def exitReturn_stm(self, ctx:D96Parser.Return_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#method_invocation_stm.
    def enterMethod_invocation_stm(self, ctx:D96Parser.Method_invocation_stmContext):
        pass

    # Exit a parse tree produced by D96Parser#method_invocation_stm.
    def exitMethod_invocation_stm(self, ctx:D96Parser.Method_invocation_stmContext):
        pass


    # Enter a parse tree produced by D96Parser#contructor_declare.
    def enterContructor_declare(self, ctx:D96Parser.Contructor_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#contructor_declare.
    def exitContructor_declare(self, ctx:D96Parser.Contructor_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#detructor_declare.
    def enterDetructor_declare(self, ctx:D96Parser.Detructor_declareContext):
        pass

    # Exit a parse tree produced by D96Parser#detructor_declare.
    def exitDetructor_declare(self, ctx:D96Parser.Detructor_declareContext):
        pass


    # Enter a parse tree produced by D96Parser#arith_operator.
    def enterArith_operator(self, ctx:D96Parser.Arith_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#arith_operator.
    def exitArith_operator(self, ctx:D96Parser.Arith_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#boolean_operator.
    def enterBoolean_operator(self, ctx:D96Parser.Boolean_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#boolean_operator.
    def exitBoolean_operator(self, ctx:D96Parser.Boolean_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#string_operator.
    def enterString_operator(self, ctx:D96Parser.String_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#string_operator.
    def exitString_operator(self, ctx:D96Parser.String_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#relation_operator.
    def enterRelation_operator(self, ctx:D96Parser.Relation_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#relation_operator.
    def exitRelation_operator(self, ctx:D96Parser.Relation_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#index_operator.
    def enterIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        pass

    # Exit a parse tree produced by D96Parser#index_operator.
    def exitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        pass


    # Enter a parse tree produced by D96Parser#exp.
    def enterExp(self, ctx:D96Parser.ExpContext):
        pass

    # Exit a parse tree produced by D96Parser#exp.
    def exitExp(self, ctx:D96Parser.ExpContext):
        pass


    # Enter a parse tree produced by D96Parser#exp0.
    def enterExp0(self, ctx:D96Parser.Exp0Context):
        pass

    # Exit a parse tree produced by D96Parser#exp0.
    def exitExp0(self, ctx:D96Parser.Exp0Context):
        pass


    # Enter a parse tree produced by D96Parser#exp1.
    def enterExp1(self, ctx:D96Parser.Exp1Context):
        pass

    # Exit a parse tree produced by D96Parser#exp1.
    def exitExp1(self, ctx:D96Parser.Exp1Context):
        pass


    # Enter a parse tree produced by D96Parser#exp2.
    def enterExp2(self, ctx:D96Parser.Exp2Context):
        pass

    # Exit a parse tree produced by D96Parser#exp2.
    def exitExp2(self, ctx:D96Parser.Exp2Context):
        pass


    # Enter a parse tree produced by D96Parser#exp3.
    def enterExp3(self, ctx:D96Parser.Exp3Context):
        pass

    # Exit a parse tree produced by D96Parser#exp3.
    def exitExp3(self, ctx:D96Parser.Exp3Context):
        pass


    # Enter a parse tree produced by D96Parser#exp4.
    def enterExp4(self, ctx:D96Parser.Exp4Context):
        pass

    # Exit a parse tree produced by D96Parser#exp4.
    def exitExp4(self, ctx:D96Parser.Exp4Context):
        pass


    # Enter a parse tree produced by D96Parser#exp5.
    def enterExp5(self, ctx:D96Parser.Exp5Context):
        pass

    # Exit a parse tree produced by D96Parser#exp5.
    def exitExp5(self, ctx:D96Parser.Exp5Context):
        pass


    # Enter a parse tree produced by D96Parser#exp6.
    def enterExp6(self, ctx:D96Parser.Exp6Context):
        pass

    # Exit a parse tree produced by D96Parser#exp6.
    def exitExp6(self, ctx:D96Parser.Exp6Context):
        pass


    # Enter a parse tree produced by D96Parser#exp7.
    def enterExp7(self, ctx:D96Parser.Exp7Context):
        pass

    # Exit a parse tree produced by D96Parser#exp7.
    def exitExp7(self, ctx:D96Parser.Exp7Context):
        pass


    # Enter a parse tree produced by D96Parser#exp8.
    def enterExp8(self, ctx:D96Parser.Exp8Context):
        pass

    # Exit a parse tree produced by D96Parser#exp8.
    def exitExp8(self, ctx:D96Parser.Exp8Context):
        pass


    # Enter a parse tree produced by D96Parser#exp9.
    def enterExp9(self, ctx:D96Parser.Exp9Context):
        pass

    # Exit a parse tree produced by D96Parser#exp9.
    def exitExp9(self, ctx:D96Parser.Exp9Context):
        pass


    # Enter a parse tree produced by D96Parser#exp10.
    def enterExp10(self, ctx:D96Parser.Exp10Context):
        pass

    # Exit a parse tree produced by D96Parser#exp10.
    def exitExp10(self, ctx:D96Parser.Exp10Context):
        pass


    # Enter a parse tree produced by D96Parser#func_call.
    def enterFunc_call(self, ctx:D96Parser.Func_callContext):
        pass

    # Exit a parse tree produced by D96Parser#func_call.
    def exitFunc_call(self, ctx:D96Parser.Func_callContext):
        pass


    # Enter a parse tree produced by D96Parser#static_operand.
    def enterStatic_operand(self, ctx:D96Parser.Static_operandContext):
        pass

    # Exit a parse tree produced by D96Parser#static_operand.
    def exitStatic_operand(self, ctx:D96Parser.Static_operandContext):
        pass


    # Enter a parse tree produced by D96Parser#static_func_call.
    def enterStatic_func_call(self, ctx:D96Parser.Static_func_callContext):
        pass

    # Exit a parse tree produced by D96Parser#static_func_call.
    def exitStatic_func_call(self, ctx:D96Parser.Static_func_callContext):
        pass


    # Enter a parse tree produced by D96Parser#method_invocate.
    def enterMethod_invocate(self, ctx:D96Parser.Method_invocateContext):
        pass

    # Exit a parse tree produced by D96Parser#method_invocate.
    def exitMethod_invocate(self, ctx:D96Parser.Method_invocateContext):
        pass


    # Enter a parse tree produced by D96Parser#explists.
    def enterExplists(self, ctx:D96Parser.ExplistsContext):
        pass

    # Exit a parse tree produced by D96Parser#explists.
    def exitExplists(self, ctx:D96Parser.ExplistsContext):
        pass


    # Enter a parse tree produced by D96Parser#explist.
    def enterExplist(self, ctx:D96Parser.ExplistContext):
        pass

    # Exit a parse tree produced by D96Parser#explist.
    def exitExplist(self, ctx:D96Parser.ExplistContext):
        pass


    # Enter a parse tree produced by D96Parser#static_method_invocate.
    def enterStatic_method_invocate(self, ctx:D96Parser.Static_method_invocateContext):
        pass

    # Exit a parse tree produced by D96Parser#static_method_invocate.
    def exitStatic_method_invocate(self, ctx:D96Parser.Static_method_invocateContext):
        pass



del D96Parser