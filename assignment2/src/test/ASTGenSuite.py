import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """Class Shape:Vu {

}
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[])])"
        self.assertTrue(TestAST.test(input, expect, 1))

    def test_2(self):
        input = """Class Shape:Vu {
                        getArea() {

                        }
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[MethodDecl(Id(getArea),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 2))

    def test_3(self):
        input = """Class Shape:Vu {
                        $getNumOfShape() {

                        }
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[MethodDecl(Id($getNumOfShape),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 3))

    def test_4(self):
        input = """Class Shape:Vu {
                        Constructor(){
                        }
                        Destructor(){
                        }
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 4))

    def test_5(self):
        input = """Class Shape:Vu {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType))])])"
        self.assertTrue(TestAST.test(input, expect, 5))

    def test_6(self):
        input = """Class Shape:Vu {
                        Val $numOfShape,numOfShape: Int=1,2;
                        Var x: Float;
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 6))

    def test_7(self):
        input = """Class Shape:Vu {
                        Val $numOfShape,numOfShape: Int=1,2;
                        Var x: Float;
                        $getNumOfShape() {

                        }
                    }
"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 7))

    def test_8(self):
        input = """Class Shape:Vu {
                        Val $numOfShape,numOfShape: Int=1,2;
                        Var x: Float;
                        $getNumOfShape() {

                        }
                    }
                    Class Rectangle: Shape {
                        getArea() {

                        }
                    }

"""
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 8))

    def test_9(self):
        input = """Class Shape:Vu {
                            Val $numOfShape,numOfShape: Int=1,2;
                            Var x: Float;
                            $getNumOfShape() {
                                Out.printInt(Shape::$numOfShape);
                            }
                       }
   """
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 9))

    def test_10(self):
        input = """Class Shape:Vu {
                             Val $numOfShape,numOfShape: Int=1,2;
                             Var x: Float;
                             $getNumOfShape() {
                                 Return Self.length * Self.width;
                             }
                        }
    """
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 10))

    def test_11(self):
        input = """Class Shape:Vu {
                             Val $numOfShape,numOfShape: Int=1,2;
                             Var x: Float;
                             $getNumOfShape() {
                                 Return hey::$numOfShape;
                             }
                        }
    """
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(hey),Id($numOfShape)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 11))

    def test_12(self):
        input = """Class Shape:Vu {
                             Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                             Var $x, $y : Int = 0, 0;
                             $getNumOfShape() {
                                 Return hey::$numOfShape;
                             }
                        }
    """
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(hey),Id($numOfShape)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 12))

    def test_13(self):
        input = """Class Shape:Vu {
                             Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                             Var $x, $y : Int = 0, 0;
                             Constructor(x,y,z:Int;k:Float){
                             }
                             Destructor(){
                             }
                        }
    """
        expect = "Program([ClassDecl(Id(Shape),Id(Vu),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5)))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),IntType),param(Id(k),FloatType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 13))

    def test_14(self):
        """More complex program"""
        input = """Class Program:sv{
                        main(){
                                d.dinh(1,2,3);
                                {
                                    If(a){}
                                    Elseif(b){}
                                    Elseif(c){}
                                }
                            }
                        }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id(main),Static,[],Block([Call(Id(d),Id(dinh),[IntLit(1),IntLit(2),IntLit(3)]),Block([If(Id(a),Block([]),If(Id(b),Block([]),If(Id(c),Block([]))))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 14))

    def test_15(self):
        """More complex program"""
        input = """Class Program:sv{
                        main(){
                                d.dinh(1,2,3);
                                {
                                    If(a){}
                                    Elseif(b){}
                                    Elseif(c){}
                                }
                                ## This is a
                                    multi-line
                                    comment.
                                ##
                            }
                        }"""
        expect="Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id(main),Static,[],Block([Call(Id(d),Id(dinh),[IntLit(1),IntLit(2),IntLit(3)]),Block([If(Id(a),Block([]),If(Id(b),Block([]),If(Id(c),Block([]))))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 15))

    # --------------LITERAL------------------------
    def test_16(self):
        """More complex program"""
        input = """Class Program:sv{
                        Var x,y,z,k,m,l:Int=06_2,0xA8_F,0XA8F,0b10_01,0B1001,1_234;
                    }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(50))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2703))),AttributeDecl(Instance,VarDecl(Id(z),IntType,IntLit(2703))),AttributeDecl(Instance,VarDecl(Id(k),IntType,IntLit(9))),AttributeDecl(Instance,VarDecl(Id(m),IntType,IntLit(9))),AttributeDecl(Instance,VarDecl(Id(l),IntType,IntLit(1234)))])])"
        self.assertTrue(TestAST.test(input, expect, 16))

    def test_17(self):
        """More complex program"""
        input = """Class Program:sv{
                        Var q,w,e,r,t,y,u,i,o,p:Float=12.34e-10,12.34E-10, 12.34, 32e+10,.23e-2,1_234.567,12.000000000,12.100000,12.1E-001,12.1E-0000;
                    }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),FloatType,FloatLit(1.234e-09))),AttributeDecl(Instance,VarDecl(Id(w),FloatType,FloatLit(1.234e-09))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(12.34))),AttributeDecl(Instance,VarDecl(Id(r),FloatType,FloatLit(320000000000.0))),AttributeDecl(Instance,VarDecl(Id(t),FloatType,FloatLit(0.0023))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1234.567))),AttributeDecl(Instance,VarDecl(Id(u),FloatType,FloatLit(12.0))),AttributeDecl(Instance,VarDecl(Id(i),FloatType,FloatLit(12.1))),AttributeDecl(Instance,VarDecl(Id(o),FloatType,FloatLit(1.21))),AttributeDecl(Instance,VarDecl(Id(p),FloatType,FloatLit(12.1)))])])"
        self.assertTrue(TestAST.test(input, expect, 17))

    def test_18(self):
        """More complex program"""
        input = """Class Program:sv{
                        Var q,$s:Boolean=True,False;
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($s),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input, expect, 18))

    def test_19(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var q,$s,c:String="hey","This is a \\\b\f\r\n\t\' string containing tab \t","He asked me: '"Where is John?'"";
                     }"""
        expect = r"""Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),StringType,StringLit(hey))),AttributeDecl(Static,VarDecl(Id($s),StringType,StringLit(This is a \\\b\f\r\n\t\' string containing tab \t))),AttributeDecl(Instance,VarDecl(Id(c),StringType,StringLit(He asked me: '"Where is John?'")))])])"""
        self.assertTrue(TestAST.test(input, expect, 19))

    def test_20(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var q,$s,c:Array[Int, 5]=Array(1, 5, 7, 12),Array("Kangxi", "Yongzheng", "Qianlong"),Array(12.34e-10,12.34E-10, 12.34, 32e+10);
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),ArrayType(5,IntType),[IntLit(1),IntLit(5),IntLit(7),IntLit(12)])),AttributeDecl(Static,VarDecl(Id($s),ArrayType(5,IntType),[StringLit(Kangxi),StringLit(Yongzheng),StringLit(Qianlong)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(5,IntType),[FloatLit(1.234e-09),FloatLit(1.234e-09),FloatLit(12.34),FloatLit(320000000000.0)]))])])"
        self.assertTrue(TestAST.test(input, expect, 20))

    def test_21(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var q,y,z:Array[Array[String,3],3]=Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    Array("Saab", "5", "2"),
                                                                    Array("Land Rover", "17", "15")
                                                            ),
                                                        Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    2,1
                                                            ),
                                                        Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    Array(1, 5, 7, 12),
                                                                    Array(12.34e-10,12.34E-10, 12.34, 32e+10)
                                                            )

                                                            ;

                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],IntLit(2),IntLit(1)])),AttributeDecl(Instance,VarDecl(Id(z),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[IntLit(1),IntLit(5),IntLit(7),IntLit(12)],[FloatLit(1.234e-09),FloatLit(1.234e-09),FloatLit(12.34),FloatLit(320000000000.0)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 21))

    def test_22(self):
        """More complex program"""
        input = r"""
                    Class Program:sv{
                       Val x,y,$z:Vu=New Vu(),New Yeu(x,x+y,New Hey()),New Tho();
                     }
                     """
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(Vu)),NewExpr(Id(Vu),[]))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(Vu)),NewExpr(Id(Yeu),[Id(x),BinaryOp(+,Id(x),Id(y)),NewExpr(Id(Hey),[])]))),AttributeDecl(Static,ConstDecl(Id($z),ClassType(Id(Vu)),NewExpr(Id(Tho),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 22))

    # ------------Expression Testing----------------

    def test_23(self):
        """More complex program"""
        # Arithmetic operators
        input = r"""Class Program:sv{
                        Var x:Int=(3-2+1*8%4/3)/10;
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),IntType,BinaryOp(/,BinaryOp(+,BinaryOp(-,IntLit(3),IntLit(2)),BinaryOp(/,BinaryOp(%,BinaryOp(*,IntLit(1),IntLit(8)),IntLit(4)),IntLit(3))),IntLit(10))))])])"
        self.assertTrue(TestAST.test(input, expect, 23))

    def test_24(self):
        """More complex program"""
        # Boolean operators
        input = r"""Class Program:sv{
                        $testBoolean(){
                            If(((!a&&k)||(c&&b))&&("sds"==."sds")){
                            }
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($testBoolean),Static,[],Block([If(BinaryOp(&&,BinaryOp(||,BinaryOp(&&,UnaryOp(!,Id(a)),Id(k)),BinaryOp(&&,Id(c),Id(b))),BinaryOp(==.,StringLit(sds),StringLit(sds))),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 24))

    def test_25(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var x:String="asds"+."sda";
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),StringType,BinaryOp(+.,StringLit(asds),StringLit(sda))))])])"
        self.assertTrue(TestAST.test(input, expect, 25))

    def test_26(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        $testBoolean(){
                            If(
                                (
                                    (x==(1-3/6))
                                    &&
                                    (m!=("8"+."32"))
                                )

                                &&
                                (
                                    (
                                        (k>2)&&(k<2*n+1)
                                    )
                                    &&
                                    (
                                        (x<=3)
                                        >=
                                        (x-2)
                                    )
                                )
                            )
                            {}
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($testBoolean),Static,[],Block([If(BinaryOp(&&,BinaryOp(&&,BinaryOp(==,Id(x),BinaryOp(-,IntLit(1),BinaryOp(/,IntLit(3),IntLit(6)))),BinaryOp(!=,Id(m),BinaryOp(+.,StringLit(8),StringLit(32)))),BinaryOp(&&,BinaryOp(&&,BinaryOp(>,Id(k),IntLit(2)),BinaryOp(<,Id(k),BinaryOp(+,BinaryOp(*,IntLit(2),Id(n)),IntLit(1)))),BinaryOp(>=,BinaryOp(<=,Id(x),IntLit(3)),BinaryOp(-,Id(x),IntLit(2))))),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 26))

    def test_27(self):
        """More complex program"""
        # Index operators
        input = r"""Class Program:sv{
                        Var x:Array[Int,3]=Array(vu[1][2][3],yeu[3/4+5],tho[New Tho(2)]);
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(3,IntType),[ArrayCell(Id(vu),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(yeu),[BinaryOp(+,BinaryOp(/,IntLit(3),IntLit(4)),IntLit(5))]),ArrayCell(Id(tho),[NewExpr(Id(Tho),[IntLit(2)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 27))

    def test_28(self):
        """More complex program"""
        # Member access
        input = r"""Class Program:sv{
                            Var x: Int=Array((1+2).h.k[1],Vu::$Tho, New Yeu(Vu,Tho).Vu(Yeu.Tho,Tho[3000]),Vu::$Yeu(Tho,New Very(Much+3000)));
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),IntType,[ArrayCell(FieldAccess(FieldAccess(BinaryOp(+,IntLit(1),IntLit(2)),Id(h)),Id(k)),[IntLit(1)])," \
                 "FieldAccess(Id(Vu),Id($Tho))," \
                 "CallExpr(NewExpr(Id(Yeu),[Id(Vu),Id(Tho)]),Id(Vu),[FieldAccess(Id(Yeu),Id(Tho)),ArrayCell(Id(Tho),[IntLit(3000)])])," \
                 "CallExpr(Id(Vu),Id($Yeu),[Id(Tho),NewExpr(Id(Very),[BinaryOp(+,Id(Much),IntLit(3000))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 28))

    def test_29(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var x: Int=Array(Self.h.k[1],Vu::$Tho, New Yeu(Vu,Tho).Vu(Self.Tho,Tho[3000]),Vu::$Yeu(Tho,New Very(Much+3000)));
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),IntType,[ArrayCell(FieldAccess(FieldAccess(Self(),Id(h)),Id(k)),[IntLit(1)]),FieldAccess(Id(Vu),Id($Tho)),CallExpr(NewExpr(Id(Yeu),[Id(Vu),Id(Tho)]),Id(Vu),[FieldAccess(Self(),Id(Tho)),ArrayCell(Id(Tho),[IntLit(3000)])]),CallExpr(Id(Vu),Id($Yeu),[Id(Tho),NewExpr(Id(Very),[BinaryOp(+,Id(Much),IntLit(3000))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 29))

    def test_30(self):
        """More complex program"""
        input = r"""
                    Class Program1:sv{
                      main(a,b,c:Int; d,e,f:Float){}
                     }
                     """
        expect="Program([ClassDecl(Id(Program1),Id(sv),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),FloatType),param(Id(e),FloatType),param(Id(f),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 30))


    # -----------------STATEMENT--------------------
    def test_31(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        $checkStmt(){
                            Var x:Int=3;
                            Val y,z:Float =4_1.3e-3, 4.23;
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([VarDecl(Id(x),IntType,IntLit(3)),ConstDecl(Id(y),FloatType,FloatLit(0.0413)),ConstDecl(Id(z),FloatType,FloatLit(4.23))]))])])"
        self.assertTrue(TestAST.test(input, expect, 31))

    def test_32(self):
        """More complex program"""
        input = r"""Class Program:sv{
                          $checkStmt(){
                           x=3;
                           x[1][2][3]=3;
                           x.y.z[1]=m::$z();
                           x::$s=x.l.y();
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([AssignStmt(Id(x),IntLit(3)),AssignStmt(ArrayCell(Id(x),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(3)),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(x),Id(y)),Id(z)),[IntLit(1)]),CallExpr(Id(m),Id($z),[])),AssignStmt(FieldAccess(Id(x),Id($s)),CallExpr(FieldAccess(Id(x),Id(l)),Id(y),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 32))

    def test_33(self):
        """More complex program"""
        input = r"""Class Program:sv{
                          $checkStmt(){
                            ##Find max in 3 elements##

                            Var x,y,z:Int;
                            realtime.scanf(x,y,z);
                            Var max:Int=x;

                            If ((x>y) && (x>z)){
                                max=x;
                            }
                            Elseif ((y>z) && (y>x)){
                                max=y;
                            }
                            Else{
                                max=z;
                            }
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),Call(Id(realtime),Id(scanf),[Id(x),Id(y),Id(z)]),VarDecl(Id(max),IntType,Id(x)),If(BinaryOp(&&,BinaryOp(>,Id(x),Id(y)),BinaryOp(>,Id(x),Id(z))),Block([AssignStmt(Id(max),Id(x))]),If(BinaryOp(&&,BinaryOp(>,Id(y),Id(z)),BinaryOp(>,Id(y),Id(x))),Block([AssignStmt(Id(max),Id(y))]),Block([AssignStmt(Id(max),Id(z))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 33))

    def test_34(self):
        """More complex program"""
        input = r"""Class Program:sv{
                          $checkStmt(){
                            Var x:Array[Int,3]=process.repeat(0,3);
                            Foreach (i In 0 .. x.length) {
                                process.scanf(x[i]);
                            }
                            Var max:Int=x[0];
                            Foreach (i In 0 .. x.length) {
                                If(max<x[i]){
                                    max= x[i];
                                }
                            }
                            process.print(max);
                            }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([VarDecl(Id(x),ArrayType(3,IntType),CallExpr(Id(process),Id(repeat),[IntLit(0),IntLit(3)])),For(Id(i),IntLit(0),FieldAccess(Id(x),Id(length)),IntLit(1),Block([Call(Id(process),Id(scanf),[ArrayCell(Id(x),[Id(i)])])])]),VarDecl(Id(max),IntType,ArrayCell(Id(x),[IntLit(0)])),For(Id(i),IntLit(0),FieldAccess(Id(x),Id(length)),IntLit(1),Block([If(BinaryOp(<,Id(max),ArrayCell(Id(x),[Id(i)])),Block([AssignStmt(Id(max),ArrayCell(Id(x),[Id(i)]))]))])]),Call(Id(process),Id(print),[Id(max)])]))])])"
        self.assertTrue(TestAST.test(input, expect,34))
    def test_35(self):
        """More complex program"""
        input = r"""Class Program:sv{
                          $checkStmt(){
                           Shape::$getNumOfShape(x,3+1,5/6);
                           process.print(x,3+1,5/6);
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([Call(Id(Shape),Id($getNumOfShape),[Id(x),BinaryOp(+,IntLit(3),IntLit(1)),BinaryOp(/,IntLit(5),IntLit(6))]),Call(Id(process),Id(print),[Id(x),BinaryOp(+,IntLit(3),IntLit(1)),BinaryOp(/,IntLit(5),IntLit(6))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 35))


    def test_36(self):
        """More complex program"""
        input = r"""Class Program:sv{
                          $checkStmt(){
                           Break;
                           Continue;
                           Return I.love.you(Vu,Tho);
                           {
                                Break;
                                Continue;
                               Return I.love.you(Vu,Tho);
                           }
                        }
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id($checkStmt),Static,[],Block([Break,Continue,Return(CallExpr(FieldAccess(Id(I),Id(love)),Id(you),[Id(Vu),Id(Tho)])),Block([Break,Continue,Return(CallExpr(FieldAccess(Id(I),Id(love)),Id(you),[Id(Vu),Id(Tho)]))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 36))

    def test_37(self):
        """More complex program"""
        input = """Class Program:sv{
                        main(a,b:Int){
                                d.dinh(1,2,3);
                                {
                                    If(a){}
                                    Elseif(b){}
                                    Elseif(c){}
                                }
                            }
                        }
                        Class Program{
                        main(){

                        }
                        }
                        """
        expect="Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Call(Id(d),Id(dinh),[IntLit(1),IntLit(2),IntLit(3)]),Block([If(Id(a),Block([]),If(Id(b),Block([]),If(Id(c),Block([]))))])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 37))

    def test_38(self):
        """Simple program: int main() {} """
        input = """
            Class A{ }
            Class B{ }
            Class C{ }
            Class D{ }
            """
        expect = "Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[]),ClassDecl(Id(D),[])])"
        self.assertTrue(TestAST.test(input, expect, 38))

    def test_39(self):
        """Simple program: int main() {} """
        input = """
            Class A : B{ }
            Class B : A{ }
            Class C {
                Val a: Int;
                Var b: Float;
            }

            """
        expect = "Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(B),Id(A),[]),ClassDecl(Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 39))

    def test_40(self):
        """Simple program: int main() {} """
        input = """
            Class Test {
                Val a, b, c: Int;
                Var b, d: Float;
            }

            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 40))

    def test_41(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val a, $b, c: Int;
                Var $b, d: Float;
                Val $c: Int = 10;
            }
            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input, expect, 41))

    def test_42(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val a, $b, c: Int;
                Var $b, d: Array[Int,5];
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,VarDecl(Id($b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input, expect, 42))

    def test_43(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x, num_of_shape: Int = 1, 2, 3;
                Var $b: Array[Int,3] = Array(1,2,3);
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(num_of_shape),IntType,IntLit(3))),AttributeDecl(Static,VarDecl(Id($b),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)]))])])"
        self.assertTrue(TestAST.test(input, expect, 43))

    def test_44(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x, num_of_shape: Int = 1, 2, 3;
                Var $b, c: Array[Int,3] = Array(1,2,3), Array("tao", "la", "khang");
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(num_of_shape),IntType,IntLit(3))),AttributeDecl(Static,VarDecl(Id($b),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(3,IntType),[StringLit(tao),StringLit(la),StringLit(khang)]))])])"
        self.assertTrue(TestAST.test(input, expect,44))

    def test_45(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x: Int = 1, 2;
                Var $b: String = "khang";
                getMethod(){

                }
                $getMem(a, b: Int){

                }
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($b),StringType,StringLit(khang))),MethodDecl(Id(getMethod),Instance,[],Block([])),MethodDecl(Id($getMem),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 45))

    def test_46(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                getMethod(a,b: Float; c: Int){
                    Val a, b: Float;
                }
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[MethodDecl(Id(getMethod),Instance,[param(Id(a),FloatType),param(Id(b),FloatType),param(Id(c),IntType)],Block([ConstDecl(Id(a),FloatType,None),ConstDecl(Id(b),FloatType,None)]))])])"
        self.assertTrue(TestAST.test(input, expect, 46))

    def test_47(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x: Int = 1, 2;
                Var $b: String = "khang";

                $getShape(a,b: Float){
                    Val a,b: Float;
                    a = 12;
                    b = 15.35;
                }

                getMethod() {

                }
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($b),StringType,StringLit(khang))),MethodDecl(Id($getShape),Static,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),FloatType,None),ConstDecl(Id(b),FloatType,None),AssignStmt(Id(a),IntLit(12)),AssignStmt(Id(b),FloatLit(15.35))])),MethodDecl(Id(getMethod),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 47))

    def test_48(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x: Int = 1, 2;
                Var $b: String = "khang";

                $getShape(a,b: Float){
                    Val a,b: Float = 1.96, 2.54;
                    Return 5;
                }

                Constructor(a,b: Int) {
                    Return 7;
                }

            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($b),StringType,StringLit(khang))),MethodDecl(Id($getShape),Static,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),FloatType,FloatLit(1.96)),ConstDecl(Id(b),FloatType,FloatLit(2.54)),Return(IntLit(5))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(IntLit(7))]))])])"
        self.assertTrue(TestAST.test(input, expect, 48))

    def test_49(self):
        """Simple program: int main() {} """
        input = """
            Class Test : khang{
                Val khang, $x: Int = 1, 2;
                Var $b: String = "khang";

                $getShape(a,b: Float){
                    Val a,b: Float = 1.96, 2.54;
                    Return 5;
                }

                Destructor() {
                    Return khang;
                }

                Constructor() {
                    Return hahaha;
                }
            }

            """
        expect = "Program([ClassDecl(Id(Test),Id(khang),[AttributeDecl(Instance,ConstDecl(Id(khang),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($b),StringType,StringLit(khang))),MethodDecl(Id($getShape),Static,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([ConstDecl(Id(a),FloatType,FloatLit(1.96)),ConstDecl(Id(b),FloatType,FloatLit(2.54)),Return(IntLit(5))])),MethodDecl(Id(Destructor),Instance,[],Block([Return(Id(khang))])),MethodDecl(Id(Constructor),Instance,[],Block([Return(Id(hahaha))]))])])"
        self.assertTrue(TestAST.test(input, expect, 49))

    def test_50(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
               main() {
                Val a: Int;
                Var b: Float;
               }

               main(a,b: Int){
                Return "khang";
               }
            }

            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),VarDecl(Id(b),FloatType)])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(StringLit(khang))]))])])"
        self.assertTrue(TestAST.test(input, expect, 50))

    def test_51(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                main() {
                    Val a: Int;
                    Var b: Float;
               }
            }

            Class test {
                main() { }
                main(a,b: Int){
                    Val a: String;
                }
            }

            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),VarDecl(Id(b),FloatType)]))]),ClassDecl(Id(test),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([ConstDecl(Id(a),StringType,None)]))])])"
        self.assertTrue(TestAST.test(input, expect, 51))

    def test_52(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                    Val a: Int = 5;
                    getMethod(x: Float){
                        a = 3;
                        a[1] = b[1][2][3][4];
                        Self.a = a;
                    }

            }

            """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(5))),MethodDecl(Id(getMethod),Instance,[param(Id(x),FloatType)],Block([AssignStmt(Id(a),IntLit(3)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(b),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(FieldAccess(Self(),Id(a)),Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 52))

    def test_53(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                Test() {
                    Val a: Int = 5;
                    a[1][2][3] = b[1][2][3][4];
                    a.method = b.ba;
                    Self.a = a + c;
               }
            }

            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Test),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(5)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(b),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(FieldAccess(Id(a),Id(method)),FieldAccess(Id(b),Id(ba))),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(+,Id(a),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 53))

    def test_54(self):
        """Simple program: int main() {} """
        input = """
            Class Test {
                    Val a: Int = 5;
                    getMethod(x: Float){
                        a::$method = b.ba;
                        a.b.c.d = e.b.e.f;
                    }
                    Var $b, $c: Array[Int, 5];
            }

            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(5))),MethodDecl(Id(getMethod),Instance,[param(Id(x),FloatType)],Block([AssignStmt(FieldAccess(Id(a),Id($method)),FieldAccess(Id(b),Id(ba))),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(FieldAccess(FieldAccess(Id(e),Id(b)),Id(e)),Id(f)))])),AttributeDecl(Static,VarDecl(Id($b),ArrayType(5,IntType))),AttributeDecl(Static,VarDecl(Id($c),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input, expect, 54))

    def test_55(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                Test() {
                    Val a: Int = 5;
                    a = -2;
                    b = 1 + 2*5 - 6;
                    b = b == 5;
               }
            }

            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Test),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(5)),AssignStmt(Id(a),UnaryOp(-,IntLit(2))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(5))),IntLit(6))),AssignStmt(Id(b),BinaryOp(==,Id(b),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 55))

    def test_56(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                Test() {
                    Val a, b: Int = 5+6*7+2, a == b;
                    Var x, y: Boolean = (5+6)*7-10/5, 7+10*(12-5/2);
               }
            }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Test),Instance,[],Block([ConstDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,IntLit(5),BinaryOp(*,IntLit(6),IntLit(7))),IntLit(2))),ConstDecl(Id(b),IntType,BinaryOp(==,Id(a),Id(b))),VarDecl(Id(x),BoolType,BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(5),IntLit(6)),IntLit(7)),BinaryOp(/,IntLit(10),IntLit(5)))),VarDecl(Id(y),BoolType,BinaryOp(+,IntLit(7),BinaryOp(*,IntLit(10),BinaryOp(-,IntLit(12),BinaryOp(/,IntLit(5),IntLit(2))))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 56))

    def test_57(self):
        """Simple program: int main() {} """
        input = """
            Class Program {
                    Val a, b: Int = 5+6%7+2/2, a != b;
                    getMethod(x: Float){
                        a[12+75] = a[1==2][a>=b][c||d];
                        self.x = 10%2;
                    }
            }
            """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,IntLit(5),BinaryOp(%,IntLit(6),IntLit(7))),BinaryOp(/,IntLit(2),IntLit(2))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(!=,Id(a),Id(b)))),MethodDecl(Id(getMethod),Instance,[param(Id(x),FloatType)],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(12),IntLit(75))]),ArrayCell(Id(a),[BinaryOp(==,IntLit(1),IntLit(2)),BinaryOp(>=,Id(a),Id(b)),BinaryOp(||,Id(c),Id(d))])),AssignStmt(FieldAccess(Id(self),Id(x)),BinaryOp(%,IntLit(10),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 57))

    def test_58(self):
        """Simple program: int main() {} """
        input = """
           Class Program {
                reCalcu() {
                    Var arr : Array[Float, 2];
                    arr = Array(1, 4.44);
                    Out.printFloat(arr[1]);
                    Val arr_2 : Array[Array[Int, 3], 4];
                    arr_2 = Array(
                        Array(4, 4),
                        Array(12, 4.4),
                        Array(3.2323, 0),
                        Array(23, 56)
                    );
                    Return value ;
                }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(reCalcu),Instance,[],Block([VarDecl(Id(arr),ArrayType(2,FloatType)),AssignStmt(Id(arr),[IntLit(1),FloatLit(4.44)]),Call(Id(Out),Id(printFloat),[ArrayCell(Id(arr),[IntLit(1)])]),ConstDecl(Id(arr_2),ArrayType(4,ArrayType(3,IntType)),None),AssignStmt(Id(arr_2),[[IntLit(4),IntLit(4)],[IntLit(12),FloatLit(4.4)],[FloatLit(3.2323),IntLit(0)],[IntLit(23),IntLit(56)]]),Return(Id(value))]))])])"
        self.assertTrue(TestAST.test(input, expect, 58))

    def test_59(self):
        """Simple program: int main() {} """
        input = """
            Class A{
                $khang(){
                    Var a: Boolean = True;
                    Val a, b: Array[Array[Array[Boolean,5],2],3] = Array() , Array(Array(Array(1,2),Array(3,4)), Array(Array("khang","hana")));
                }
            }
            """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($khang),Static,[],Block([VarDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(a),ArrayType(3,ArrayType(2,ArrayType(5,BoolType))),[]),ConstDecl(Id(b),ArrayType(3,ArrayType(2,ArrayType(5,BoolType))),[[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]],[[StringLit(khang),StringLit(hana)]]])]))])])"
        self.assertTrue(TestAST.test(input, expect, 59))

    def test_60(self):
        """More complex program"""
        input = """Class Program:sv{
                            Var x,y,z,k,m,l:Int=06_2,0xA8_F,0XA8F,0b10_01,0B1001,1_234;
                        }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(50))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2703))),AttributeDecl(Instance,VarDecl(Id(z),IntType,IntLit(2703))),AttributeDecl(Instance,VarDecl(Id(k),IntType,IntLit(9))),AttributeDecl(Instance,VarDecl(Id(m),IntType,IntLit(9))),AttributeDecl(Instance,VarDecl(Id(l),IntType,IntLit(1234)))])])"
        self.assertTrue(TestAST.test(input, expect, 60))

    def test_61(self):
        """More complex program"""
        input = """Class Program:sv{
                            Var q,w,e,r,t,y,u,i,o,p:Float=12.34e-10,12.34E-10, 12.34, 32e+10,.23e-2,1_234.567,12.000000000,12.100000,12.1E-001,12.1E-0000;
                        }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),FloatType,FloatLit(1.234e-09))),AttributeDecl(Instance,VarDecl(Id(w),FloatType,FloatLit(1.234e-09))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(12.34))),AttributeDecl(Instance,VarDecl(Id(r),FloatType,FloatLit(320000000000.0))),AttributeDecl(Instance,VarDecl(Id(t),FloatType,FloatLit(0.0023))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1234.567))),AttributeDecl(Instance,VarDecl(Id(u),FloatType,FloatLit(12.0))),AttributeDecl(Instance,VarDecl(Id(i),FloatType,FloatLit(12.1))),AttributeDecl(Instance,VarDecl(Id(o),FloatType,FloatLit(1.21))),AttributeDecl(Instance,VarDecl(Id(p),FloatType,FloatLit(12.1)))])])"
        self.assertTrue(TestAST.test(input, expect, 61))

    def test_62(self):
        """More complex program"""
        input = """Class Program:sv{
                            Var q,$s:Boolean=True,False;
                         }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($s),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input, expect, 62))

    def test_63(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var q,$s,c:Array[Int, 5]=Array(1, 5, 7, 12),Array("Kangxi", "Yongzheng", "Qianlong"),Array(12.34e-10,12.34E-10, 12.34, 32e+10);
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),ArrayType(5,IntType),[IntLit(1),IntLit(5),IntLit(7),IntLit(12)])),AttributeDecl(Static,VarDecl(Id($s),ArrayType(5,IntType),[StringLit(Kangxi),StringLit(Yongzheng),StringLit(Qianlong)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(5,IntType),[FloatLit(1.234e-09),FloatLit(1.234e-09),FloatLit(12.34),FloatLit(320000000000.0)]))])])"
        self.assertTrue(TestAST.test(input, expect, 63))

    def test_64(self):
        """More complex program"""
        input = r"""Class Program:sv{
                        Var q,y,z:Array[Array[String,3],3]=Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    Array("Saab", "5", "2"),
                                                                    Array("Land Rover", "17", "15")
                                                            ),
                                                        Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    2,1
                                                            ),
                                                        Array (
                                                                    Array("Volvo", "22", "18"),
                                                                    Array(1, 5, 7, 12),
                                                                    Array(12.34e-10,12.34E-10, 12.34, 32e+10)
                                                            )

                                                            ;

                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],IntLit(2),IntLit(1)])),AttributeDecl(Instance,VarDecl(Id(z),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[IntLit(1),IntLit(5),IntLit(7),IntLit(12)],[FloatLit(1.234e-09),FloatLit(1.234e-09),FloatLit(12.34),FloatLit(320000000000.0)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 64))


    def test_65(self):
        """More complex program"""
        input = r"""
                    Class Program:sv{
                       Val x,y,$z:Vu=New Vu(),New Yeu(x,x+y,New Hey()),New Tho();
                     }
                     """
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(Vu)),NewExpr(Id(Vu),[]))),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(Vu)),NewExpr(Id(Yeu),[Id(x),BinaryOp(+,Id(x),Id(y)),NewExpr(Id(Hey),[])]))),AttributeDecl(Static,ConstDecl(Id($z),ClassType(Id(Vu)),NewExpr(Id(Tho),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 65))

    # -----------------------Dinh---------------------------

    def test_66(self):
        """intlit"""
        input = """
                    Class Sv:BK{
                        sv(){
                            d.sv(1,0,03,0x34_3,0x0,0b0,0B1);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[MethodDecl(Id(sv),Instance,[],Block([Call(Id(d),Id(sv),[IntLit(1),IntLit(0),IntLit(3),IntLit(835),IntLit(0),IntLit(0),IntLit(1)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 66))

    def test_67(self):
        """boollit"""
        input = """
                    Class Sv:BK{
                        Var a:Boolean=True;
                        Val $b:Boolean=False;
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input, expect, 67))

    def test_68(self):
        """array"""
        input = """
                    Class Sv:BK{
                        Var c:Array[String,2]=Array("dinh","1913114");
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,VarDecl(Id(c),ArrayType(2,StringType),[StringLit(dinh),StringLit(1913114)]))])])"
        self.assertTrue(TestAST.test(input, expect, 68))

    def test_69(self):
        """list_array"""
        input = """
                    Class Sv:BK{
                        Var c:Array[Array[Int,2],2]=Array(Array(1,2),Array(3,4));
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,VarDecl(Id(c),ArrayType(2,ArrayType(2,IntType)),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 69))

    def test_70(self):
        """Class"""
        input = """Class SV{
                    }"""
        expect = "Program([ClassDecl(Id(SV),[])])"
        self.assertTrue(TestAST.test(input,expect,70))

    def test_71(self):
        """Class Parent"""
        input = """Class SV:sv{
                    }"""
        expect = "Program([ClassDecl(Id(SV),Id(sv),[])])"
        self.assertTrue(TestAST.test(input,expect,71))

    def test_72(self):
        """Class"""
        input = """Class SV{
                    }
                    Class BK{
                    }"""
        expect = "Program([ClassDecl(Id(SV),[]),ClassDecl(Id(BK),[])])"
        self.assertTrue(TestAST.test(input,expect,72))
    def test_73(self):
        """Class Parent"""
        input = """Class SV:sv{
                    }
                    Class BK:bk{
                    }"""
        expect = "Program([ClassDecl(Id(SV),Id(sv),[]),ClassDecl(Id(BK),Id(bk),[])])"
        self.assertTrue(TestAST.test(input,expect,73))

    def test_74(self):
        """Mix"""
        input = """Class SV{
                    }
                    Class BK:sv{
                    }"""
        expect = "Program([ClassDecl(Id(SV),[]),ClassDecl(Id(BK),Id(sv),[])])"
        self.assertTrue(TestAST.test(input,expect,74))

    def test_75(self):
        input = """Class SV{
                        Var a,$b,c,d:Int;
                        Val a,$b,$c,d:Array[Int,5_2];
                    }
                    """
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(52,IntType),None)),AttributeDecl(Static,ConstDecl(Id($b),ArrayType(52,IntType),None)),AttributeDecl(Static,ConstDecl(Id($c),ArrayType(52,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(d),ArrayType(52,IntType),None))])])"
        self.assertTrue(TestAST.test(input,expect,75))

    def test_76(self):
        input = """Class SV{
                        Var a,$b,c,d:Int=1,2,3,4;
                        Val a,$b,$c,d:Array[Int,5_2]=Array(1,2,3,4,5),Array(
                            Array("dinh","1913114","BK"),Array("03","46","93"),Array("64","27","Dinh")
                            ),a+b,c+d;
                    }
                    """
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(d),IntType,IntLit(4))),AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(52,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),AttributeDecl(Static,ConstDecl(Id($b),ArrayType(52,IntType),[[StringLit(dinh),StringLit(1913114),StringLit(BK)],[StringLit(03),StringLit(46),StringLit(93)],[StringLit(64),StringLit(27),StringLit(Dinh)]])),AttributeDecl(Static,ConstDecl(Id($c),ArrayType(52,IntType),BinaryOp(+,Id(a),Id(b)))),AttributeDecl(Instance,ConstDecl(Id(d),ArrayType(52,IntType),BinaryOp(+,Id(c),Id(d))))])])"
        self.assertTrue(TestAST.test(input,expect,76))

    def test_77(self):
        input = """Class SV{
                        Var a,$b,c,d:Array[Array[Array[String,3],5],5_2];
                        Val a,$b,$c,d:A=New A(1,2),New A(3,4), New A(5,6), New A(7,8);
                    }
                    """
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(52,ArrayType(5,ArrayType(3,StringType))))),AttributeDecl(Static,VarDecl(Id($b),ArrayType(52,ArrayType(5,ArrayType(3,StringType))))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(52,ArrayType(5,ArrayType(3,StringType))))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(52,ArrayType(5,ArrayType(3,StringType))))),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[IntLit(1),IntLit(2)]))),AttributeDecl(Static,ConstDecl(Id($b),ClassType(Id(A)),NewExpr(Id(A),[IntLit(3),IntLit(4)]))),AttributeDecl(Static,ConstDecl(Id($c),ClassType(Id(A)),NewExpr(Id(A),[IntLit(5),IntLit(6)]))),AttributeDecl(Instance,ConstDecl(Id(d),ClassType(Id(A)),NewExpr(Id(A),[IntLit(7),IntLit(8)])))])])"
        self.assertTrue(TestAST.test(input,expect,77))

    def test_78(self):
        """dec_Type"""
        input = """Class SV{
                        Var a:Int;
                        Val b:Float;
                    }Class BK{
                        Var e:Array[Array[String,3],4];
                        Val f:SV;
                    }
                    Class Sv:BK{
                        Var c:String;
                        Val d:Boolean;
                    }"""
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,None))]),ClassDecl(Id(BK),[AttributeDecl(Instance,VarDecl(Id(e),ArrayType(4,ArrayType(3,StringType)))),AttributeDecl(Instance,ConstDecl(Id(f),ClassType(Id(SV)),NullLiteral()))]),ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,None))])])"
        self.assertTrue(TestAST.test(input,expect,78))

    def test_79(self):
        """EXp0"""
        input = """Class SV{
                        Val a:Boolean="dinh"==."dinh";
                        Var b:String="dinh"+."1913114";
                    }"""
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BinaryOp(==.,StringLit(dinh),StringLit(dinh)))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(+.,StringLit(dinh),StringLit(1913114))))])])"
        self.assertTrue(TestAST.test(input,expect,79))

    def test_80(self):
        """EXp1"""
        input = """Class SV{
                        Var a:Boolean=(a>b) && (c<d) || (a==b) && (e!=d) ||(a>=b) || (c>=d);
                    }"""
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(||,BinaryOp(||,BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(>,Id(a),Id(b)),BinaryOp(<,Id(c),Id(d))),BinaryOp(==,Id(a),Id(b))),BinaryOp(!=,Id(e),Id(d))),BinaryOp(>=,Id(a),Id(b))),BinaryOp(>=,Id(c),Id(d)))))])])"
        self.assertTrue(TestAST.test(input,expect,80))

    def test_81(self):
        """EXp2"""
        input = """Class SV{
                        main(){
                            Return a && b || c && d;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(SV),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(&&,BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)),Id(d)))]))])])"
        self.assertTrue(TestAST.test(input,expect,81))

    def test_82(self):
        """EXp3"""
        input = """Class SV{
                        Var a,b,c:Int=a+b,3-4,d.sv()+d::$d(3,2)-5;
                    }"""
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(-,IntLit(3),IntLit(4)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(-,BinaryOp(+,CallExpr(Id(d),Id(sv),[]),CallExpr(Id(d),Id($d),[IntLit(3),IntLit(2)])),IntLit(5))))])])"
        self.assertTrue(TestAST.test(input,expect,82))

    def test_84(self):
        """EXp4"""
        input = """Class SV{
                        Val a,b:Boolean=!True,!False;
                    }"""
        expect = "Program([ClassDecl(Id(SV),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,UnaryOp(!,BooleanLit(True)))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,UnaryOp(!,BooleanLit(False))))])])"
        self.assertTrue(TestAST.test(input,expect,83))

    def test_84(self):
        """EXp5"""
        input = """
                    Class Sv:BK{
                        Val a,$b,c,$d:Float=-12.,-.0e10,-4.54,65.3;
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,UnaryOp(-,FloatLit(12.0)))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,UnaryOp(-,FloatLit(0.0)))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,UnaryOp(-,FloatLit(4.54)))),AttributeDecl(Static,ConstDecl(Id($d),FloatType,FloatLit(65.3)))])])"
        self.assertTrue(TestAST.test(input,expect,84))

    def test_85(self):
        """Exp6"""
        input = """
                    Class Sv:BK{
                        main(){
                            Val a:Array[Int,3]=Array(1,2,3);
                            Var b,c: Array[Array[String,3],2]=Array(1,2,3),Array(
                                Array("dinh","doan","lan"),Array("dinh","doan","lan"));
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)]),VarDecl(Id(b),ArrayType(2,ArrayType(3,StringType)),[IntLit(1),IntLit(2),IntLit(3)]),VarDecl(Id(c),ArrayType(2,ArrayType(3,StringType)),[[StringLit(dinh),StringLit(doan),StringLit(lan)],[StringLit(dinh),StringLit(doan),StringLit(lan)]])]))])])"
        self.assertTrue(TestAST.test(input,expect,85))

    def test_86(self):
        """Exp7"""
        input = """Class Program{
                        main(){
                            d.dv();
                            Return d.d;
                            Return d.dv();
                        }
                    }
                    """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(d),Id(dv),[]),Return(FieldAccess(Id(d),Id(d))),Return(CallExpr(Id(d),Id(dv),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,86))

    def test_87(self):
        """Exp8"""
        input = """Class Program{
                        main(){
                            d::$dv(1,2,3);
                            Return d::$dv(1,2,3);
                            Return d::$d;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(d),Id($dv),[IntLit(1),IntLit(2),IntLit(3)]),Return(CallExpr(Id(d),Id($dv),[IntLit(1),IntLit(2),IntLit(3)])),Return(FieldAccess(Id(d),Id($d)))]))])])"
        self.assertTrue(TestAST.test(input,expect,87))

    def test_88(self):
        """Exp9"""
        input = """Class Program{
                        Var a:Int;
                        Val b:Float;
                        Main(){
                            a=New d();
                            Return New d(1,2,3);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,None)),MethodDecl(Id(Main),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(d),[])),Return(NewExpr(Id(d),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,88))
    def test_89(self):
        """Exp10"""
        input = """Class Program{
                    main(){
                        Return 1;
                        Return "dinh";
                        Return True;
                        Return a;
                        Return Self;
                        Return Null;
                        Return Array(3,4,5);
                    }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(IntLit(1)),Return(StringLit(dinh)),Return(BooleanLit(True)),Return(Id(a)),Return(Self()),Return(NullLiteral()),Return([IntLit(3),IntLit(4),IntLit(5)])]))])])"
        self.assertTrue(TestAST.test(input,expect,89))

    def test_90(self):
        """Exp11"""
        input = """
                    Class Sv:BK{
                        Var c:String=(-4)+4;
                        Val d:Boolean=(!True) && True;
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+,UnaryOp(-,IntLit(4)),IntLit(4)))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,BinaryOp(&&,UnaryOp(!,BooleanLit(True)),BooleanLit(True))))])])"
        self.assertTrue(TestAST.test(input,expect,90))

    def test_91(self):
        """Exp11"""
        input = """
                    Class Sv:BK{
                        $get(){
                            Var x: Vu;
                            Var z: Vu= New Vu(); 
                            Return;
                            Var x: Int= Self +Self;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Sv),Id(BK),[MethodDecl(Id($get),Static,[],Block([VarDecl(Id(x),ClassType(Id(Vu)),NullLiteral()),VarDecl(Id(z),ClassType(Id(Vu)),NewExpr(Id(Vu),[])),Return(),VarDecl(Id(x),IntType,BinaryOp(+,Self(),Self()))]))])])"
        self.assertTrue(TestAST.test(input,expect,91))

    def test_92(self):
        input = """
               Class Integer{
                   sortArray(a:Array[Int,10]){
                    Var i,j:Int=0,0;
                    Foreach( i In 0 .. list.length-1 ){
                        Foreach(j In 0 .. list.length-i-1){
                            If(list[j] > list[j+1]){
                            array.swap(list[j], list[j+1]);
                        }
                    }
                    }
                    Return a;
                }
                }
               """
        expect = """Program([ClassDecl(Id(Integer),[MethodDecl(Id(sortArray),Instance,[param(Id(a),ArrayType(10,IntType))],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(j),IntType,IntLit(0)),For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(Id(list),Id(length)),IntLit(1)),IntLit(1),Block([For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,FieldAccess(Id(list),Id(length)),Id(i)),IntLit(1)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(list),[Id(j)]),ArrayCell(Id(list),[BinaryOp(+,Id(j),IntLit(1))])),Block([Call(Id(array),Id(swap),[ArrayCell(Id(list),[Id(j)]),ArrayCell(Id(list),[BinaryOp(+,Id(j),IntLit(1))])])]))])])])]),Return(Id(a))]))])])"""
        self.assertTrue(TestAST.test(input,expect,92))

    def test_93(self):
        input = """
           Class Integer{
                giaiThua(n:Int)
                {
                    If (n == 1)
                    {
                        Return 1;
                    }
                    Else{
                        Return n * Integer.giaiThua(n - 1);
                    }

                }
            }
           """
        expect = """Program([ClassDecl(Id(Integer),[MethodDecl(Id(giaiThua),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(IntLit(1))]),Block([Return(BinaryOp(*,Id(n),CallExpr(Id(Integer),Id(giaiThua),[BinaryOp(-,Id(n),IntLit(1))])))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 93))

    def test_94(self):
        input = """
           Class Restaurant{
               Var doanhthu,hoahong: Int;
                Calculator(){
                    If(doanhthu>1000)
                    {
                        self.hoahong=doanhthu*0.05;
                    }
                    Elseif(doanhthu>2000)
                    {
                        self.hoahong=doanhthu*0.1;
                    }
                    Elseif(doanhthu>5000)
                    {
                        self.hoahong=doanhthu*0.3;
                    }
                }
            }
           """
        expect = """Program([ClassDecl(Id(Restaurant),[AttributeDecl(Instance,VarDecl(Id(doanhthu),IntType)),AttributeDecl(Instance,VarDecl(Id(hoahong),IntType)),MethodDecl(Id(Calculator),Instance,[],Block([If(BinaryOp(>,Id(doanhthu),IntLit(1000)),Block([AssignStmt(FieldAccess(Id(self),Id(hoahong)),BinaryOp(*,Id(doanhthu),FloatLit(0.05)))]),If(BinaryOp(>,Id(doanhthu),IntLit(2000)),Block([AssignStmt(FieldAccess(Id(self),Id(hoahong)),BinaryOp(*,Id(doanhthu),FloatLit(0.1)))]),If(BinaryOp(>,Id(doanhthu),IntLit(5000)),Block([AssignStmt(FieldAccess(Id(self),Id(hoahong)),BinaryOp(*,Id(doanhthu),FloatLit(0.3)))]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 94))

    def test_95(self):
        input = """
           Class Integer{
                main(n:Int)
                {
                    Var i,sum:Int=0,0;
                    Foreach(i In 1 .. n)
                    {
                        If(n%i==0)
                        {
                            sum=sum+i;
                        }
                    }
                    Return sum;
                }
            }
           """
        expect = """Program([ClassDecl(Id(Integer),[MethodDecl(Id(main),Instance,[param(Id(n),IntType)],Block([VarDecl(Id(i),IntType,IntLit(0)),VarDecl(Id(sum),IntType,IntLit(0)),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i)))]))])]),Return(Id(sum))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 95))

    def test_96(self):
        input = """
           Class PrintINT{
              PrintEven(){
                   Foreach (i In 1 .. 100 By 2) {
                      If(i%2==0)
                      {
                         Out.printInt(i);
                      }
                  }
              }
            }
           """
        expect = """Program([ClassDecl(Id(PrintINT),[MethodDecl(Id(PrintEven),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Id(Out),Id(printInt),[Id(i)])]))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 96))

    def test_97(self):
        input = """
        Class Operator {
            Val x,y : Int=Array(),1;
            add(){
               X.add(x);
            }
            remove(x,y:Int){
               If(x==y)
               {
                  X.remove(x);
               }
               Else{
                  Break;
               }
            }
            }
        """
        expect = 'Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,[])),AttributeDecl(Instance,ConstDecl(Id(y),IntType,IntLit(1))),MethodDecl(Id(add),Instance,[],Block([Call(Id(X),Id(add),[Id(x)])])),MethodDecl(Id(remove),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([If(BinaryOp(==,Id(x),Id(y)),Block([Call(Id(X),Id(remove),[Id(x)])]),Block([Break]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 97))

    def test_98(self):
        input = """
        Class Operator
        {
            Check()
            {
                Return 2&&2 ;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(Check),Instance,[],Block([Return(BinaryOp(&&,IntLit(2),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 98))

    def test_99(self):
        input = """Class ABC {
            method() {
            Val a : Array[Int,3] = Array(1);
            Foreach(a In 1 .. a By a/2)
            {
               If(a>10)
               {
                  io.Print("A >10");
               }
               Else{
                  Continue;
               }
            }
            }
            }"""
        expect = "Program([ClassDecl(Id(ABC),[MethodDecl(Id(method),Instance,[],Block([ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1)]),For(Id(a),IntLit(1),Id(a),BinaryOp(/,Id(a),IntLit(2)),Block([If(BinaryOp(>,Id(a),IntLit(10)),Block([Call(Id(io),Id(Print),[StringLit(A >10)])]),Block([Continue]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 99))

    def test_100(self):
        input = """
        Class TestOperator
        {
            main()
            {
               a[(a+x.test(2))*b::$abc(3+4)] = a[b[x]] +3*a[4]/3;
            }
        }
        """
        expect = "Program([ClassDecl(Id(TestOperator),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(*,BinaryOp(+,Id(a),CallExpr(Id(x),Id(test),[IntLit(2)])),CallExpr(Id(b),Id($abc),[BinaryOp(+,IntLit(3),IntLit(4))]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[Id(x)])]),BinaryOp(/,BinaryOp(*,IntLit(3),ArrayCell(Id(a),[IntLit(4)])),IntLit(3))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 100))








