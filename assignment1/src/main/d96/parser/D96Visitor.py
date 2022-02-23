# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declares.
    def visitClass_declares(self, ctx:D96Parser.Class_declaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_decl.
    def visitMember_decl(self, ctx:D96Parser.Member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#members.
    def visitMembers(self, ctx:D96Parser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_declare.
    def visitAtt_declare(self, ctx:D96Parser.Att_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_names.
    def visitAtt_names(self, ctx:D96Parser.Att_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_init_value.
    def visitAtt_init_value(self, ctx:D96Parser.Att_init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#values.
    def visitValues(self, ctx:D96Parser.ValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_type.
    def visitData_type(self, ctx:D96Parser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classtype.
    def visitClasstype(self, ctx:D96Parser.ClasstypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#func_declare.
    def visitFunc_declare(self, ctx:D96Parser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idnamelist.
    def visitIdnamelist(self, ctx:D96Parser.IdnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstatment.
    def visitBlockstatment(self, ctx:D96Parser.BlockstatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stamentlist.
    def visitStamentlist(self, ctx:D96Parser.StamentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staments.
    def visitStaments(self, ctx:D96Parser.StamentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stament.
    def visitStament(self, ctx:D96Parser.StamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_array_literal.
    def visitIndex_array_literal(self, ctx:D96Parser.Index_array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array.
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_stm.
    def visitVardecl_stm(self, ctx:D96Parser.Vardecl_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varlist.
    def visitVarlist(self, ctx:D96Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_names.
    def visitVariable_names(self, ctx:D96Parser.Variable_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_init_value.
    def visitVariable_init_value(self, ctx:D96Parser.Variable_init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stm.
    def visitAssign_stm(self, ctx:D96Parser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#leftassign.
    def visitLeftassign(self, ctx:D96Parser.LeftassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalarvar.
    def visitScalarvar(self, ctx:D96Parser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_exp.
    def visitIndexed_exp(self, ctx:D96Parser.Indexed_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stm.
    def visitIf_stm(self, ctx:D96Parser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stms.
    def visitElseif_stms(self, ctx:D96Parser.Elseif_stmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stm.
    def visitElseif_stm(self, ctx:D96Parser.Elseif_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stm.
    def visitElse_stm(self, ctx:D96Parser.Else_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_stm.
    def visitForin_stm(self, ctx:D96Parser.Forin_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#steploop.
    def visitSteploop(self, ctx:D96Parser.SteploopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stm.
    def visitBreak_stm(self, ctx:D96Parser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stm.
    def visitContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stm.
    def visitReturn_stm(self, ctx:D96Parser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_stm.
    def visitMethod_invocation_stm(self, ctx:D96Parser.Method_invocation_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#contructor_declare.
    def visitContructor_declare(self, ctx:D96Parser.Contructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#detructor_declare.
    def visitDetructor_declare(self, ctx:D96Parser.Detructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idname.
    def visitIdname(self, ctx:D96Parser.IdnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp0.
    def visitExp0(self, ctx:D96Parser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#func_call.
    def visitFunc_call(self, ctx:D96Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_operand.
    def visitStatic_operand(self, ctx:D96Parser.Static_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_func_call.
    def visitStatic_func_call(self, ctx:D96Parser.Static_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocate.
    def visitMethod_invocate(self, ctx:D96Parser.Method_invocateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_exp.
    def visitObject_exp(self, ctx:D96Parser.Object_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#explists.
    def visitExplists(self, ctx:D96Parser.ExplistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#explist.
    def visitExplist(self, ctx:D96Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invocate.
    def visitStatic_method_invocate(self, ctx:D96Parser.Static_method_invocateContext):
        return self.visitChildren(ctx)



del D96Parser