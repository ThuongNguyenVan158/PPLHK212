from tkinter.messagebox import NO
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    #program: class_declares EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.class_declares()))
    #class_declares: class_declare class_declares | class_declare;
    def visitClass_declares(self, ctx: D96Parser.Class_declaresContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.class_declare())] + self.visit(ctx.class_declares())
        return [self.visit(ctx.class_declare())]
    #class_declare: CLASS ID ( Extended ID)? member_decl;
    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        memlist = self.visit(ctx.member_decl())
        if ctx.getChildCount() == 3:
            return ClassDecl(Id(ctx.ID().getText()), memlist)
        return ClassDecl(Id(ctx.ID(0).getText()), memlist, Id(ctx.ID(1).getText()))
    #member_decl: LB memberlist RB;
    def visitMember_decl(self, ctx: D96Parser.Member_declContext):
        return self.visit(ctx.memberlist())
    #memberlist: members | ;
    def visitMemberlist(self, ctx: D96Parser.MemberlistContext):
        if ctx.members():
            return self.visit(ctx.members())
        return []
    #members: member members | member;
    def visitMembers(self, ctx: D96Parser.MembersContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.member())] + self.visit(ctx.members())
        return [self.visit(ctx.member())]
    #member: att_declare | method_declare;
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.att_declare():
            return self.visit(ctx.att_declare())
        return self.visit(ctx.method_declare())
    #att_declare: (VAL|VAR) att_declarelist SM;
    def visitAtt_declare(self, ctx: D96Parser.Att_declareContext):
        attlist = self.visit(ctx.att_declarelist())
        if ctx.VAR():
            attdecl = []
            if len(attlist[0]) == 3:
                for i in range(len(attlist)):
                    if attlist[i][1] == "nonstatic":
                        attdecl += [AttributeDecl(Instance(), VarDecl(attlist[i][0], attlist[i][2]))]
                    else: attdecl += [AttributeDecl(Static(), VarDecl(attlist[i][0], attlist[i][2]))]
            else: 
                for i in range(len(attlist)):
                    if attlist[i][1] == "nonstatic":
                        attdecl += [AttributeDecl(Instance(), VarDecl(attlist[i][0], attlist[i][2], attlist[i][3]))]
                    else: attdecl += [AttributeDecl(Static(), VarDecl(attlist[i][0], attlist[i][2], attlist[i][3]))]
            return attdecl
        elif ctx.VAL():
            constattdecl = []
            if len(attlist[0]) == 3:
                for i in range(len(attlist)):
                    if attlist[i][1] == "nonstatic":
                        constattdecl += [AttributeDecl(Instance(), ConstDecl(attlist[i][0], attlist[i][2]))]
                    else: constattdecl += [AttributeDecl(Static(), ConstDecl(attlist[i][0], attlist[i][2]))]
            else: 
                for i in range(len(attlist)):
                    if attlist[i][1] == "nonstatic":
                        constattdecl += [AttributeDecl(Instance(), ConstDecl(attlist[i][0], attlist[i][2], attlist[i][3]))]
                    else: constattdecl += [AttributeDecl(Static(), ConstDecl(attlist[i][0], attlist[i][2], attlist[i][3]))]
            return constattdecl
    #att_declarelist: att_names Extended data_type | att_init_value;
    def visitAtt_declarelist(self, ctx: D96Parser.Att_declarelistContext):
        if ctx.getChildCount() == 3:
            attlist = self.visit(ctx.att_names())
            data_typ = self.visit(ctx.data_type())
            return [[idname[0], idname[1], data_typ] for idname in attlist]
        else:
            initlist = self.visit(ctx.att_init_value())
            tailarr = initlist[-1]
            typ = tailarr[2]
            idlist = []
            typlist =[]
            explist = []
            vardecllist = []
            for i in range(len(initlist)):
                idlist = idlist + [initlist[i][0]]
                typlist = typlist + [initlist[i][1]]
                explist = explist + [initlist[len(initlist) - i -1][2]]
            for i in range(len(initlist)):
                vardecllist = vardecllist + [[idlist[i], typlist[i], typ, explist[i]]]
            return vardecllist
    #att_names: idname CM att_names | idname;
    def visitAtt_names(self, ctx: D96Parser.Att_namesContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.idname())] + self.visit(ctx.att_names())
        return [self.visit(ctx.idname())]
    #att_init_value: idname CM att_init_value CM exp | idname Extended data_type ASSIGN exp;
    def visitAtt_init_value(self, ctx: D96Parser.Att_init_valueContext):
        if ctx.att_init_value():
            id = self.visit(ctx.idname())
            expr = self.visit(ctx.exp())
            return [[id[0], id[1], 'Int', expr]] + self.visit(ctx.variable_init_value())
        else:
            id = self.visit(ctx.idname())
            expr = self.visit(ctx.exp())
            typ = self.visit(ctx.data_type())
            return [[id[0], id[1], typ, expr]]
    #data_type: primitive_type | array_type | classtype;
    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else: return self.visit(ctx.classtype())
    #primitive_type: INT | FLOAT | BOOLEAN | STRING;
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        return StringType()
    #classtype: ID;
    def visitClasstype(self, ctx: D96Parser.ClasstypeContext):
        return ClassType(Id(ctx.ID().getText()))
    #method_declare: func_declare | contructor_declare | detructor_declare;
    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        if ctx.func_declare():
            return self.visit(ctx.func_declare())
        elif ctx.contructor_declare():
            return self.visit(ctx.contructor_declare())
        else: return self.visit(ctx.detructor_declare())
    #func_declare: (ID | DOLLARID) LP paramlist RP blockstatment;
    def visitFunc_declare(self, ctx: D96Parser.Func_declareContext):
        if ctx.DOLLARID():
            ismethodStatic = True
        else: ismethodStatic = False
        parameterlist = self.visit(ctx.paramlist())
        block = self.visit(ctx.blockstatment())
        if ismethodStatic:
            return MethodDecl(Static(), Id(ctx.DOLLARID().getText()), parameterlist, block)
        return MethodDecl(Instance(), Id(ctx.ID().getText()), parameterlist, block)
    #paramlist: params | ;
    def visitParamlist(self, ctx: D96Parser.ParamlistContext):
        if ctx.params():
            return self.visit(ctx.params())
        return []
    #params: param SM params | param;
    def visitParams(self, ctx: D96Parser.ParamsContext):
        if ctx.getChildCount() == 3:
            return [VarDecl(id,typ) for (id,typ) in self.visit(ctx.param())] + self.visit(ctx.params())
        return [VarDecl(id,typ) for (id,typ) in self.visit(ctx.param())]
    #param: idnamelist Extended data_type;
    def visitParam(self, ctx: D96Parser.ParamContext):
        id_list = self.visit(ctx.idnamelist())
        data_typ = self.visit(ctx.data_type())
        return [(id,data_typ) for id in id_list]
    #idnamelist: ID CM idnamelist | ID;
    def visitIdnamelist(self, ctx: D96Parser.IdnamelistContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idnamelist())
        return [Id(ctx.ID().getText())]
    #blockstatment: LB stamentlist RB; // mục 6.9
    def visitBlockstatment(self, ctx: D96Parser.BlockstatmentContext):
        return Block(self.visit(ctx.stamentlist()))
    #stamentlist: staments | ;
    def visitStamentlist(self, ctx: D96Parser.StamentlistContext):
        if ctx.staments():
            return self.visit(ctx.staments())
        return []
    #staments: stament staments | stament;
    def visitStaments(self, ctx: D96Parser.StamentsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.stament())] + self.visit(ctx.staments())
        return [self.visit(ctx.stament())]
    #stament: vardecl_stm
		# | assign_stm
		# | if_stm
		# | forin_stm
		# | break_stm
		# | continue_stm
		# | return_stm
		# | method_invocation_stm
		# | blockstatment;
    def visitStament(self, ctx: D96Parser.StamentContext):
        if ctx.vardecl_stm():
            return self.visit(ctx.vardecl_stm())
        elif ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        elif ctx.if_stm():
            return self.visit(ctx.forin_stm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        elif ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        elif ctx.return_stm():
            return self.visit(ctx.return_stm())
        elif ctx.method_invocation_stm():
            return self.visit(ctx.method_invocation_stm())
        else: return self.visit(ctx.blockstatment())
    #literal: (INTEGER| INTERGER_GT_ZERO | FLOAT_NUMBER | BOOLEAN_LITERAL | STRING_LITERAL | index_array_literal | multi_array | NULL);
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTEGER():
            return IntLiteral(int(ctx.INTEGER().getText()))
        elif ctx.INTERGER_GT_ZERO:
            return IntLiteral(int(ctx.INTERGER_GT_ZERO().getText()))
        elif ctx.FLOAT_NUMBER():
            return FloatLiteral(float(ctx.FLOAT_NUMBER().getText()))
        elif ctx.BOOLEAN_LITERAL():
            if ctx.BOOLEAN_LITERAL().getText() == "True":
                return BooleanLiteral(True)
            else: return BooleanLiteral(False)
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.index_array_literal():
            return self.visit(ctx.index_array_literal())
        elif ctx.multi_array():
            return self.visit(ctx.multi_array())
        elif ctx.NULL():
            return NullLiteral()
    #index_array_literal: ARRAY LP explists RP; 
    def visitIndex_array_literal(self, ctx: D96Parser.Index_array_literalContext):
        return ArrayLiteral(self.visit(ctx.explists()))
    #multi_array: ARRAY LP arraylist RP;
    def visitMulti_array(self, ctx: D96Parser.Multi_arrayContext):
        return ArrayLiteral(self.visit(ctx.arraylist()))
    #arraylist: index_array_literal CM arraylist | index_array_literal;
    def visitArraylist(self, ctx: D96Parser.ArraylistContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.index_array_literal(0))] + self.visit(ctx.arraylist())
        else: return [self.visit(ctx.index_array_literal(0))]
    #array_type: ARRAY LSB (primitive_type |array_type) CM INTERGER_GT_ZERO RSB;
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        if ctx.primitive_type():
            typ = self.visit(ctx.primitive_type())
        else: typ = self.visit(ctx.array_type())
        sizearr = int(ctx.INTERGER_GT_ZERO().getText())
        return ArrayType(sizearr, typ)

# /****************************************************************************/
# /*								2.2 Statement								*/
# /****************************************************************************/   
    #vardecl_stm: (VAR | VAL) varlist SM;
    def visitVardecl_stm(self, ctx: D96Parser.Vardecl_stmContext):
        varli = self.visit(ctx.varlist())
        if ctx.VAR():
            vardecl = []
            if len(varli[0]) == 2:
                for i in len(varli):
                    vardecl += [VarDecl(varli[i][0], varli[i][1])]
            else: 
                for i in len(varli):
                    vardecl += [VarDecl(varli[i][0], varli[i][1], varli[i][2])]
            return vardecl
        elif ctx.VAL():
            constdecl = []
            if len(varli[0]) == 2:
                for i in len(varli):
                    constdecl += [ConstDecl(varli[i][0], varli[i][1])]
            else: 
                for i in len(varli):
                    constdecl += [ConstDecl(varli[i][0], varli[i][1], varli[i][2])]
            return constdecl
    #varlist: variable_names Extended data_type | variable_init_value;
    def visitVarlist(self, ctx: D96Parser.VarlistContext):
        if ctx.getChildCount() == 3:
            name_list = self.visit(ctx.variable_names())
            data_typ = self.visit(ctx.data_type())
            return [[idname, data_typ] for idname in name_list]
        else:
            initlist = self.visit(ctx.variable_init_value())
            tailarr = initlist[-1]
            typ = tailarr[1]
            idlist = []
            explist = []
            vardecllist = []
            for i in range(len(initlist)):
                idlist = idlist + initlist[i][0]
                explist = explist + initlist[len(initlist) - i -1][2]
            for i in range(len(initlist)):
                vardecllist = vardecllist + [[idlist[i],typ, explist[i]]]
            return vardecllist
    #variable_names: ID CM variable_names | ID;
    def visitVariable_names(self, ctx: D96Parser.Variable_namesContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.variable_names())
        return [Id(ctx.ID().getText())]
    #variable_init_value: ID CM variable_init_value CM exp | ID Extended data_type ASSIGN exp;
    def visitVariable_init_value(self, ctx: D96Parser.Variable_init_valueContext):
        if ctx.variable_init_value():
            expr = self.visit(ctx.exp())
            return [(Id(ctx.ID().getText()), 'Int', expr)] + self.visit(ctx.variable_init_value())
        else:
            expr = self.visit(ctx.exp())
            typ = self.visit(ctx.data_type())
            return [(Id(ctx.ID().getText()), typ, expr)]
    #assign_stm: leftassign ASSIGN exp SM;
    def visitAssign_stm(self, ctx: D96Parser.Assign_stmContext):
        return Assign(self.visit(ctx.leftassign()), self.visit(ctx.exp()))
    #leftassign: scalarvar | indexed_exp;
    def visitLeftassign(self, ctx: D96Parser.LeftassignContext):
        if ctx.scalarvar():
            return self.visit(ctx.scalarvar())
        return self.visit(ctx.indexed_exp())
    #scalarvar: ID | exp DOT ID | ID DOT ID | exp6; // check is need $
    def visitScalarvar(self, ctx: D96Parser.ScalarvarContext):
        if ctx.getChildCount() == 3:
            if ctx.exp():
                return FieldAccess(self.visit(ctx.exp(), Id(ctx.ID().getText())))
            else: return FieldAccess(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()))
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.exp6())
    #indexed_exp: exp index_operator | exp;
    def visitIndexed_exp(self, ctx: D96Parser.Indexed_expContext):
        if ctx.getChildCount() == 2:
            listexp = self.visit(ctx.index_operator())
            return ArrayCell(self.visit(ctx.exp()), listexp)
        return self.visit(ctx.exp())
    #if_stm: IF LP exp RP blockstatment elseif_stms else_stm;
    def visitIf_stm(self, ctx: D96Parser.If_stmContext):
        expr = self.visit(ctx.exp())
        block = self.visit(ctx.blockstatment())
        elseiflist = self.visit(ctx.elseif_stms)
        elsestm = self.visit(ctx.else_stm())
        if not elseiflist:
            if not elsestm:
                return If(expr, block)
            else: return If(expr, block, elsestm[0])
        
        temp = []
        if not elsestm:
            temp = [If(elseiflist[len(elseiflist)-1][0], elseiflist[len(elseiflist)-1][1])]
        else: temp = [If(elseiflist[len(elseiflist)-1][0], elseiflist[len(elseiflist)-1][1], elsestm[0])]
        for i in range(len(elseiflist) -1):
            elseblock = [If(elseiflist[len(elseiflist)-i-1][0], elseiflist[len(elseiflist)-i-1][1], temp[0])]
            temp = elseblock
        return elseblock[0]
    #elseif_stms: elseif_stm elseif_stms | ;
    def visitElseif_stms(self, ctx: D96Parser.Elseif_stmsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.elseif_stm())] + self.visit(ctx.elseif_stms())
        return []
    #elseif_stm: ELSEIF LP exp RP blockstatment;
    def visitElseif_stm(self, ctx: D96Parser.Elseif_stmContext):
        return [self.visit(ctx.exp()), self.visit(ctx.blockstatment())]
    #else_stm: ELSE blockstatment | ;
    def visitElse_stm(self, ctx: D96Parser.Else_stmContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.blockstatment())]
        else: return []
    #forin_stm: FOREACH LP scalarvar IN exp FROMTO exp steploop RP blockstatment;
    def visitForin_stm(self, ctx: D96Parser.Forin_stmContext):
        step = self.visit(ctx.steploop())
        loopstm = self.visit(ctx.blockstatment())
        id = self.visit(ctx.scalarvar())
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        if not step:
            return For(id, exp1, exp2, loopstm)
        return For(id, exp1, exp2, loopstm, step[0])
    #steploop: BY exp | ;
    def visitSteploop(self, ctx: D96Parser.SteploopContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.exp())]
        else: return []
    #break_stm: BREAK SM;
    def visitBreak_stm(self, ctx: D96Parser.Break_stmContext):
        return Break()
    #continue_stm: CONTINUE SM;
    def visitContinue_stm(self, ctx: D96Parser.Continue_stmContext):
        return Continue()
    #return_stm: RETURN (exp)? SM;
    def visitReturn_stm(self, ctx: D96Parser.Return_stmContext):
        if ctx.getChildCount() == 3:
            return Return(self.visit(ctx.exp()))
        else: return Return()
    #method_invocation_stm: (method_invocate | static_method_invocate) SM;
    def visitMethod_invocation_stm(self, ctx: D96Parser.Method_invocation_stmContext):
        if ctx.method_invocate():
            return self.visit(ctx.method_invocate())
        else: return self.visit(ctx.static_method_invocate())
    #contructor_declare: CONSTRUCTOR LP paramlist  RP blockstatment;
    def visitContructor_declare(self, ctx: D96Parser.Contructor_declareContext):
        para = self.visit(ctx.paramlist())
        block = self.visit(ctx.blockstatment())
        return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), para, block)
    #detructor_declare: DESTRUCTOR LP RP blockstatment;
    def visitDetructor_declare(self, ctx: D96Parser.Detructor_declareContext):
        block = self.visit(ctx.blockstatment())
        return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], block)
    #idname: ID | DOLLARID;
    def visitIdname(self, ctx: D96Parser.IdnameContext):
        if ctx.ID():
            return [Id(ctx.ID().getText()), "nonstatic"]
        else: return [Id(ctx.DOLLARID().getText()), "static"]
    
# /****************************************************************************/
# /*						Expression					                      */
# /****************************************************************************/   
    #index_operator: LSB exp RSB | LSB exp RSB index_operator;
    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.index_operator())
    #exp: exp0 (ADDDOT | EQUALDOT) exp0 | exp0;
    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    #exp0: exp1 (EQUAL | NOT_EQUAL | GT | LT | GE | LE) exp1 | exp1;
    def visitExp0(self, ctx: D96Parser.Exp0Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    #exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    #exp2: exp2 (ADD | SUB) exp3 | exp3;
    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    #exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))
    #exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))
    #exp5: SUB exp5 | exp6;
    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))
    #exp6: exp6 index_operator | exp7;
    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.getChildCount() == 2:
            listexp = self.visit(ctx.index_operator())
            return ArrayCell(self.visit(ctx.exp6()), listexp)
        return self.visit(ctx.exp7())
    #exp7: exp7 DOT (ID| func_call) | exp8;
    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.getChildCount() == 3:
            exp = self.visit(ctx.exp7())
            if ctx.ID():
                return FieldAccess(exp, Id(ctx.ID().getText()))
            else:
                func = self.visit(ctx.func_call())
                return CallExpr(exp, func[0], func[1])
        else: return self.visit(ctx.exp8())
    #exp8: ID SC static_operand | exp9;
    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.getChildCount() == 3:
            sttoperand = self.visit(ctx.static_operand())
            if len(sttoperand) == 1:
                return FieldAccess(Id(ctx.ID().getText()), sttoperand[0])
            else: return CallExpr(Id(ctx.ID().getText()), sttoperand[0], sttoperand[1])
        return self.visit(ctx.exp9())
    #exp9: NEW func_call| exp10;
    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.getChildCount() == 2:
            func = self.visit(ctx.func_call())
            return NewExpr(func[0], func[1])
        return self.visit(ctx.exp10())
    #exp10: literal| TRUE | FALSE | ID | SELF | ID SC DOLLARID | LP exp RP; chưa biểu diễn được ID SC DOLLARID
    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.getChildCount() ==3:
            if ctx.exp():
                return self.visit(ctx.exp())
            else: return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLARID().getText()))

# /****************************************************************************/
# /*					Member access						                  */
# /****************************************************************************/
    #func_call: ID LP explists RP;
    def visitFunc_call(self, ctx: D96Parser.Func_callContext):
        expli = self.visit(ctx.explists())
        return [Id(ctx.ID().getText()), expli]
    #static_operand: DOLLARID | static_func_call;
    def visitStatic_operand(self, ctx: D96Parser.Static_operandContext):
        if ctx.DOLLARID():
            return [Id(ctx.DOLLARID().getText())]
        else: return self.visit(ctx.static_func_call())
    #static_func_call:DOLLARID LP explists RP; 
    def visitStatic_func_call(self, ctx: D96Parser.Static_func_callContext):
        expli = self.visit(ctx.explists())
        return [Id(ctx.DOLLARID().getText()), expli]
    #method_invocate: object_exp DOT func_call;
    def visitMethod_invocate(self, ctx: D96Parser.Method_invocateContext):
        arglist =  self.visit(ctx.func_call())
        return CallStmt(self.visit(ctx.object_exp()), arglist[0], arglist[1])
    #object_exp: ID | exp;
    def visitObject_exp(self, ctx: D96Parser.Object_expContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else: return self.visit(ctx.exp())
    #static_method_invocate: ID SC static_func_call;
    def visitStatic_method_invocate(self, ctx: D96Parser.Static_method_invocateContext):
        arglist =  self.visit(ctx.static_func_call())
        return CallStmt(Id(ctx.ID().getText()), arglist[0], arglist[1])
    #explists: explist | ;
    def visitExplists(self, ctx: D96Parser.ExplistsContext):
        if ctx.explist():
            return self.visit(ctx.explist())
        else:  return []
    #explist: exp CM explist | exp;
    def visitExplist(self, ctx: D96Parser.ExplistContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())] + self.visit(ctx.explist())
        else: return [self.visit(ctx.exp())]
