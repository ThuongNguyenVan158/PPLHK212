import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_AST1(self):
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_AST2(self):
        input = """Class Program  {
             Var numOfShape : Int =5;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(numOfShape),IntType,IntLit(5)))])])"

        self.assertTrue(TestAST.test(input, expect, 301))

    def test_AST3(self):
        input = """Class main {
             Var $numOfShape : Int = 0;
            Var $immuAttribute : Int = 0;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Static,VarDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($immuAttribute),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_AST4(self):
        input = """Class Ex {
            Var my1Var, my2Var : Array[Int, 3] = Array(1,2,3), Array(2,3,4);
        }"""
        expect = "Program([ClassDecl(Id(Ex),[AttributeDecl(Instance,VarDecl(Id(my1Var),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(my2Var),ArrayType(3,IntType),[IntLit(2),IntLit(3),IntLit(4)]))])])"
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_AST5(self):
        input = """Class ABC : DEF{ 
            main(){

            }
            main(a,b,c: Int ; e,f,g : Float){
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(ABC),Id(DEF),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),FloatType),param(Id(f),FloatType),param(Id(g),FloatType)],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_AST6(self):
        input = '''
        Class Example1
        {
            factorial(n : Int){
                If (n == 0) {
                    Return 1;
                }
                Else{
                     Return n * Example1.factorial(n - 1);
                    }
            }
        }
            '''
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(1))]),Block([Return(BinaryOp(*,Id(n),CallExpr(Id(Example1),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_AST7(self):
        input = '''
        Class Example1 {
           factorial(n: Int){
                If (n == 0) {
                    Return 1;
                }
                Else {
                     Return n * Self.factorial(n - 1);
                     }
            }
        }
        Class Example2 : Example1{
            main(){
                Var x : Int = 5;
                io.writeIntLn(Self.factorial(x));
            }
        }
            '''
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(1))]),Block([Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))]))]),ClassDecl(Id(Example2),Id(Example1),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),IntType,IntLit(5)),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_AST8(self):
        input = '''
        Class Shape {
            Var length,width: Int = 2,5;
            $getArea() {
                Return Self.length*Self.width;
            }
            Shape(length,width: Float){
                Self.length = length;
                Self.width = width;
            }
        }
            '''
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(width),IntType,IntLit(5))),MethodDecl(Id($getArea),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))])),MethodDecl(Id(Shape),Instance,[param(Id(length),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))])])"
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_AST9(self):
        input = '''
        Class Rectangle : Shape {
            $getArea(){
                Return Self.length*Self.width;
            }
        }
            '''
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id($getArea),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_AST10(self):
        input = '''
    Class Triangle : Shape {
        getArea(){
            Return Self.length*Self.width / 2;
        }
    }
    Class Program{
        main(arg: String)
        {
            Return 0;
        }
        main()
        {
            Var a: Triangle;
            a.getArea();
        }
    }
            '''
        expect = "Program([ClassDecl(Id(Triangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(arg),StringType)],Block([Return(IntLit(0))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Triangle)),NullLiteral()),Call(Id(a),Id(getArea),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_AST11(self):
        input = '''
            Class Example2 {
                 main(){
                    s = New Rectangle(3,4);
                }
            }
        '''
        expect = "Program([ClassDecl(Id(Example2),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_AST12(self):
        input = '''
            Class Example2 {
                Var a, b, c : Int;
                Var x, y, z : String;
                Var g, h, y : Boolean;
                nty(){
                    Return;
                }
                Var x, y, z : Array[Int, 3];
                Var q, w : Exp1 = New A(), New B();
                Val a : A = New A();
            ##
                =======================================
                Comment here
                =======================================
            ##
            }
        '''
        expect = "Program([ClassDecl(Id(Example2),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(x),StringType)),AttributeDecl(Instance,VarDecl(Id(y),StringType)),AttributeDecl(Instance,VarDecl(Id(z),StringType)),AttributeDecl(Instance,VarDecl(Id(g),BoolType)),AttributeDecl(Instance,VarDecl(Id(h),BoolType)),AttributeDecl(Instance,VarDecl(Id(y),BoolType)),MethodDecl(Id(nty),Instance,[],Block([Return()])),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(z),ArrayType(3,IntType))),AttributeDecl(Instance,VarDecl(Id(q),ClassType(Id(Exp1)),NewExpr(Id(A),[]))),AttributeDecl(Instance,VarDecl(Id(w),ClassType(Id(Exp1)),NewExpr(Id(B),[]))),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_AST13(self):
        input = '''
        Class Example2 {
            test(){
                b[3] = Array(1,2,3);
                a[3+x.foo(2)] = a[b[2]] +3;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Example2),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(ArrayCell(Id(b),[IntLit(3)]),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(2)])]),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_AST14(self):
        input = '''
        Class Example2 {
            test(){
                ## start of declaration part##
                Var r,s : Float ;
                Val a,b : Array[Int,5];
                ## list of statements##
                r=2.0;
                s=r*r*Self.myPI;
                a[0]= s;
                }
        }
        '''
        expect = "Program([ClassDecl(Id(Example2),[MethodDecl(Id(test),Instance,[],Block([VarDecl(Id(r),FloatType),VarDecl(Id(s),FloatType),ConstDecl(Id(a),ArrayType(5,IntType),None),ConstDecl(Id(b),ArrayType(5,IntType),None),AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_AST15(self):
        input = '''
        Class Example2 {
            test(){
                If (flag) {
                    r=2.0;
                    }
                Else{
                    a[0]= s; 
                    }
                }
            }
         '''
        expect = "Program([ClassDecl(Id(Example2),[MethodDecl(Id(test),Instance,[],Block([If(Id(flag),Block([AssignStmt(Id(r),FloatLit(2.0))]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_AST16(self):
        input = '''
        Class Example2 {
            test(){
                Foreach ( i  In 1 .. 100) {
                    io.writeIntLn(i);
                    Intarray[i] = i + 1;
                }
                Foreach (x In 100 .. 0) {
                    io.writeIntLn(x);
                    }
            }
        }
        '''
        expect ="Program([ClassDecl(Id(Example2),[MethodDecl(Id(test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),[Id(i)]),BinaryOp(+,Id(i),IntLit(1)))])]),For(Id(x),IntLit(100),IntLit(0),IntLit(1),Block([Call(Id(io),Id(writeIntLn),[Id(x)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_AST17(self):
        input = '''
        Class Person {
                Val firstName : String = "Thuong"; 
                Val lastName: String = "Thuong";
                Var age: Int = 22;
                fullname() {
                    Return Self.firstName +. Self.lastName;
                }
        }
        '''
        expect ="Program([ClassDecl(Id(Person),[AttributeDecl(Instance,ConstDecl(Id(firstName),StringType,StringLit(Thuong))),AttributeDecl(Instance,ConstDecl(Id(lastName),StringType,StringLit(Thuong))),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(22))),MethodDecl(Id(fullname),Instance,[],Block([Return(BinaryOp(+.,FieldAccess(Self(),Id(firstName)),FieldAccess(Self(),Id(lastName))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_AST18(self):
        
        input = '''
        Class Person {
            Val firstName : String = "Thuong"; 
            Val lastName: String = "Thuong";
            Var age: Int = 22;
            Contructor(fname, lname: String; age : Int)
            {
                Self.firstName = fname;
                Self.lastName = lname;
                Self.age = age;
            }
        }
    '''
        expect ="Program([ClassDecl(Id(Person),[AttributeDecl(Instance,ConstDecl(Id(firstName),StringType,StringLit(Thuong))),AttributeDecl(Instance,ConstDecl(Id(lastName),StringType,StringLit(Thuong))),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(22))),MethodDecl(Id(Contructor),Instance,[param(Id(fname),StringType),param(Id(lname),StringType),param(Id(age),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(firstName)),Id(fname)),AssignStmt(FieldAccess(Self(),Id(lastName)),Id(lname)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))]))])])"
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_AST19(self):
        
        input = '''
     Class Person {
            Val firstName : String = "Thuong"; 
            Val lastName: String = "Thuong";
            Var age: Int = 22;
            c(){
                s = a + b + c * d;
                d = a && b;
                e = !a;
            }
    }
            '''
        expect ="Program([ClassDecl(Id(Person),[AttributeDecl(Instance,ConstDecl(Id(firstName),StringType,StringLit(Thuong))),AttributeDecl(Instance,ConstDecl(Id(lastName),StringType,StringLit(Thuong))),AttributeDecl(Instance,VarDecl(Id(age),IntType,IntLit(22))),MethodDecl(Id(c),Instance,[],Block([AssignStmt(Id(s),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d)))),AssignStmt(Id(d),BinaryOp(&&,Id(a),Id(b))),AssignStmt(Id(e),UnaryOp(!,Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_AST20(self):
        
        input = '''
        Class Test {
            abc(){}
            abc(){}
            abc(){}
            abc(){}
            print(){
                Self.abc();
            }

        }
        '''
        expect ="Program([ClassDecl(Id(Test),[MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(abc),Instance,[],Block([])),MethodDecl(Id(print),Instance,[],Block([Call(Self(),Id(abc),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_AST21(self):
        input = '''
        Class Test {
            abc__bc_ab(c : Int){
            }
            print(a: String){
                a.printf("hello" +. a.toString());
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(abc__bc_ab),Instance,[param(Id(c),IntType)],Block([])),MethodDecl(Id(print),Instance,[param(Id(a),StringType)],Block([Call(Id(a),Id(printf),[BinaryOp(+.,StringLit(hello),CallExpr(Id(a),Id(toString),[]))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_AST22(self):
        
        input = '''
        Class Test {
            square ( x : Int)  
            {
                Var p :Int = 1;
                p = x * x ;
                Return  p;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(square),Instance,[param(Id(x),IntType)],Block([VarDecl(Id(p),IntType,IntLit(1)),AssignStmt(Id(p),BinaryOp(*,Id(x),Id(x))),Return(Id(p))]))])])"
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_AST23(self):
        
        input = '''
        Class Test {
            swap(a,b: Int)
            {
                Var temp: Int = a;
                a = b;
                b= temp;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(swap),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(temp),IntType,Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(temp))]))])])"
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_AST24(self):
        
        input = '''
        Class Test {
            a(abc: ABC){
                Return ABC.__str__();
            }
                
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(a),Instance,[param(Id(abc),ClassType(Id(ABC)))],Block([Return(CallExpr(Id(ABC),Id(__str__),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_AST25(self):
        
        input = '''
        Class Test {
            a(){

            }
            a(a,b,c : Array[Int, 3]; d : Array[Float,3]){

            }
            Var1(a: Int){

            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(a),Instance,[],Block([])),MethodDecl(Id(a),Instance,[param(Id(a),ArrayType(3,IntType)),param(Id(b),ArrayType(3,IntType)),param(Id(c),ArrayType(3,IntType)),param(Id(d),ArrayType(3,FloatType))],Block([])),MethodDecl(Id(Var1),Instance,[param(Id(a),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_AST26(self):
        
        input = '''
        Class Test {
            Convertfloattoint(a: Float){
                Return Self.int(a);
            }
           a(a : Array[Int, 3]; b: Int; c: Array[String, 3]; d: Int){
               Return Null;
           }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Convertfloattoint),Instance,[param(Id(a),FloatType)],Block([Return(CallExpr(Self(),Id(int),[Id(a)]))])),MethodDecl(Id(a),Instance,[param(Id(a),ArrayType(3,IntType)),param(Id(b),IntType),param(Id(c),ArrayType(3,StringType)),param(Id(d),IntType)],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_AST27(self):
        
        input = '''
        Class Test {
            main()
            {
                a = New Exp(1,2,4);
                Self.print(i);
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(Exp),[IntLit(1),IntLit(2),IntLit(4)])),Call(Self(),Id(print),[Id(i)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_AST28(self):
        
        input = '''
        Class Program {
            main()
            {
                Var i : Int;
                i = 8;
                test.printf("Factorial of the number is ", i, test.factorial(i));
                Return 0;
            }
            factorial(i : Int)
            {
                If(i < 2)
                {
                    Return 1;
                }
                Return i * Test.factorial(i - 1);
                }
            }
        '''
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(i),IntType),AssignStmt(Id(i),IntLit(8)),Call(Id(test),Id(printf),[StringLit(Factorial of the number is ),Id(i),CallExpr(Id(test),Id(factorial),[Id(i)])]),Return(IntLit(0))])),MethodDecl(Id(factorial),Instance,[param(Id(i),IntType)],Block([If(BinaryOp(<,Id(i),IntLit(2)),Block([Return(IntLit(1))])),Return(BinaryOp(*,Id(i),CallExpr(Id(Test),Id(factorial),[BinaryOp(-,Id(i),IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_AST29(self):
        
        input = '''
        Class Test {
            main()
            {
                If (flag*fag) 
                    {a=1;
                    }
                Else{
                    If (flag&&flag)
                        {a=2;}
                    Else{
                        If (flag || flag) 
                           { a=3;}
                        Else{
                            Return 0;
                        }
                    }
                }
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(*,Id(flag),Id(fag)),Block([AssignStmt(Id(a),IntLit(1))]),Block([If(BinaryOp(&&,Id(flag),Id(flag)),Block([AssignStmt(Id(a),IntLit(2))]),Block([If(BinaryOp(||,Id(flag),Id(flag)),Block([AssignStmt(Id(a),IntLit(3))]),Block([Return(IntLit(0))]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_AST30(self):
        
        input = '''
        Class Test {
            main(){
                a = Other.b() + Other.c() + Other.d();
                Other.print(a);
                a = a / Other.sum(a,b) + Other.sub(a,b);
                Other.print(a);
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,CallExpr(Id(Other),Id(b),[]),CallExpr(Id(Other),Id(c),[])),CallExpr(Id(Other),Id(d),[]))),Call(Id(Other),Id(print),[Id(a)]),AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),CallExpr(Id(Other),Id(sum),[Id(a),Id(b)])),CallExpr(Id(Other),Id(sub),[Id(a),Id(b)]))),Call(Id(Other),Id(print),[Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_AST31(self):
        input = '''
        Class Test {
            main(){
                If(x<1){
                    a =1;
                }Elseif((x>1) && (x<5) ){
                    a=2;
                }Elseif((x>5) && (x>10) ){
                    a =3.5;
                }Else { 
                    a= 0;
                }
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(<,Id(x),IntLit(1)),Block([AssignStmt(Id(a),IntLit(1))]),If(BinaryOp(&&,BinaryOp(>,Id(x),IntLit(1)),BinaryOp(<,Id(x),IntLit(5))),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(&&,BinaryOp(>,Id(x),IntLit(5)),BinaryOp(>,Id(x),IntLit(10))),Block([AssignStmt(Id(a),FloatLit(3.5))]),Block([AssignStmt(Id(a),IntLit(0))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_AST32(self):
        
        input = '''
        Class Test {
            main(){
                Return True;
            }
            main(arg : Array[String, 3]){
                Return Null;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Return(BooleanLit(True))])),MethodDecl(Id(main),Instance,[param(Id(arg),ArrayType(3,StringType))],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_AST33(self):
        
        input = '''
        Class Test {
            Compare(s1,s2: String){
                Var a: String;
                If(s1 ==. s2)
                {
                    a =s1+.s2;
                }
                Else {
                    a=s2+.s1;
                }
            }
            main(){
                    Self.Compare("a", "b");
                    Return 0;
                }
        }
        '''
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(Compare),Instance,[param(Id(s1),StringType),param(Id(s2),StringType)],Block([VarDecl(Id(a),StringType),If(BinaryOp(==.,Id(s1),Id(s2)),Block([AssignStmt(Id(a),BinaryOp(+.,Id(s1),Id(s2)))]),Block([AssignStmt(Id(a),BinaryOp(+.,Id(s2),Id(s1)))]))])),MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(Compare),[StringLit(a),StringLit(b)]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_AST34(self):
        
        input = '''
        Class Student {
            Val id : Int;  
            Var salary: Int; 
            Val name : String; 
            $getName()
            {
                Return Self.name;
            }
        }
        Class Score : Student{
            Val idScore : Int;
            Run(){
                Student :: $getName();
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Student),[AttributeDecl(Instance,ConstDecl(Id(id),IntType,None)),AttributeDecl(Instance,VarDecl(Id(salary),IntType)),AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),MethodDecl(Id($getName),Static,[],Block([Return(FieldAccess(Self(),Id(name)))]))]),ClassDecl(Id(Score),Id(Student),[AttributeDecl(Instance,ConstDecl(Id(idScore),IntType,None)),MethodDecl(Id(Run),Instance,[],Block([Call(Id(Student),Id($getName),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_AST35(self):
        
        input = '''
        Class Student {
            Val id : Int;  
            Var salary: Int; 
            Val name : String; 
            Contructor(){
                Self.id = 1;
                Self.salary = 1000;
                Self.name = "Thuong";
            }
            Detructor(){

            }
            display() {
                Return Self.print(Self.id + Self.salary +Self.name);
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Student),[AttributeDecl(Instance,ConstDecl(Id(id),IntType,None)),AttributeDecl(Instance,VarDecl(Id(salary),IntType)),AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),MethodDecl(Id(Contructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(id)),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(salary)),IntLit(1000)),AssignStmt(FieldAccess(Self(),Id(name)),StringLit(Thuong))])),MethodDecl(Id(Detructor),Instance,[],Block([])),MethodDecl(Id(display),Instance,[],Block([Return(CallExpr(Self(),Id(print),[BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(id)),FieldAccess(Self(),Id(salary))),FieldAccess(Self(),Id(name)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_AST36(self):
        
        input = '''
        Class sinhvien
        {
            Val masinhvien, ten, quequan : String;
            Var tuoi : Int;
            Var Diem : Array[Float, 11]; 
            di(){
                Foreach(i In 0 .. 10){
                    Self.Print(Self.Diem[i]);
                    }
            }
        }
        '''
        expect = "Program([ClassDecl(Id(sinhvien),[AttributeDecl(Instance,ConstDecl(Id(masinhvien),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(ten),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(quequan),StringType,None)),AttributeDecl(Instance,VarDecl(Id(tuoi),IntType)),AttributeDecl(Instance,VarDecl(Id(Diem),ArrayType(11,FloatType))),MethodDecl(Id(di),Instance,[],Block([For(Id(i),IntLit(0),IntLit(10),IntLit(1),Block([Call(Self(),Id(Print),[ArrayCell(FieldAccess(Self(),Id(Diem)),[Id(i)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_AST37(self):
        
        input = '''
        Class Callback
        {
            main(){
                If(1){
                    If(1){
                        If(1){
                            If(1){
                                Return 1;
                            }
                        }
                    }
                }
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Callback),[MethodDecl(Id(main),Instance,[],Block([If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([Return(IntLit(1))]))]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_AST38(self):
        
        input = '''
        Class CallbackHell
        {
            main(){
                Foreach( i In 1 .. 10){
                    Foreach ( x In i+1 .. 10){
                        If(1){
                            If(1){
                                If(1){
                                    If(1){
                                        Return 1;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        '''
        expect = "Program([ClassDecl(Id(CallbackHell),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([For(Id(x),BinaryOp(+,Id(i),IntLit(1)),IntLit(10),IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([Return(IntLit(1))]))]))]))]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_AST39(self):
        
        input = '''
        Class CallbackHell
        {
            typeString(){
                Return "string";
            }
            typeInt(){
                Return 1;
            }
            typeFloat(){
                Return 1.0;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(CallbackHell),[MethodDecl(Id(typeString),Instance,[],Block([Return(StringLit(string))])),MethodDecl(Id(typeInt),Instance,[],Block([Return(IntLit(1))])),MethodDecl(Id(typeFloat),Instance,[],Block([Return(FloatLit(1.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_AST40(self):
        
        input = '''
        Class Shape {
            Var length,width : Float;
           getArea() {}
            Shape(length,width : Int){
                Self.length = length;
                Self.width = width;
            }
        }
        Class Rectangle : Shape {
            getArea(){
                Return Self.length*Self.width;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getArea),Instance,[],Block([])),MethodDecl(Id(Shape),Instance,[param(Id(length),IntType),param(Id(width),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_AST41(self):
        
        input = '''
        Class Parent {
            Var p : Int;
        }
        Class Child : Parent {
            Var c: Array[Int, 5];
            Contructor()
            {
                Foreach(i In 0 .. 5)
                {
                    Self.c[i] = i*i;
                }
            }
            Detructor(){

            }
            print(){
                Return "Hihi";
            }
        }
        Class Program{
            Var a : Child = New Child();
            main(){

            }
            main(a: Int){
                a.print();
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Parent),[AttributeDecl(Instance,VarDecl(Id(p),IntType))]),ClassDecl(Id(Child),Id(Parent),[AttributeDecl(Instance,VarDecl(Id(c),ArrayType(5,IntType))),MethodDecl(Id(Contructor),Instance,[],Block([For(Id(i),IntLit(0),IntLit(5),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(c)),[Id(i)]),BinaryOp(*,Id(i),Id(i)))])])])),MethodDecl(Id(Detructor),Instance,[],Block([])),MethodDecl(Id(print),Instance,[],Block([Return(StringLit(Hihi))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Child)),NewExpr(Id(Child),[]))),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Call(Id(a),Id(print),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_AST42(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1/2+3/4+5/6+7/8+8/9;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(/,IntLit(1),IntLit(2)),BinaryOp(/,IntLit(3),IntLit(4))),BinaryOp(/,IntLit(5),IntLit(6))),BinaryOp(/,IntLit(7),IntLit(8))),BinaryOp(/,IntLit(8),IntLit(9))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_AST43(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1.1 || 2.2;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(||,FloatLit(1.1),FloatLit(2.2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_AST44(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1>=2;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(>=,IntLit(1),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_AST45(self):
        
        input = '''
        Class Operator
        {
            Var $operand: Int = 2;
            main()
            {
                Return -1*Operator :: $operand;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Static,VarDecl(Id($operand),IntType,IntLit(2))),MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(*,UnaryOp(-,IntLit(1)),FieldAccess(Id(Operator),Id($operand))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_AST46(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return -1/-2;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(/,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_AST47(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return -1+-2+1.1+-1.2;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))),FloatLit(1.1)),UnaryOp(-,FloatLit(1.2))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_AST48(self):
        
        input = '''
        Class Operator
        {
            Var a: Int =0;
            main()
            {
                Foreach ( i In 1 .. 100) {
                    If (i%2 == 0) {
                        Self.print(i);
                        }
                    Else{
                        Continue;
                        }
                }
            }
            print(i : Int)
            {
                Return i.__str__();
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Call(Self(),Id(print),[Id(i)])]),Block([Continue]))])])])),MethodDecl(Id(print),Instance,[param(Id(i),IntType)],Block([Return(CallExpr(Id(i),Id(__str__),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_AST49(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1.0e10/1.2e10;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(/,FloatLit(10000000000.0),FloatLit(12000000000.0)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_AST50(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                a[(3+x.foo(2))/5*3-25] = a[b[2]] +3*a[4]/3;
            }
        }
        '''
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(-,BinaryOp(*,BinaryOp(/,BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)])),IntLit(5)),IntLit(3)),IntLit(25))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(2)])]),BinaryOp(/,BinaryOp(*,IntLit(3),ArrayCell(Id(a),[IntLit(4)])),IntLit(3))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_AST51(self):
        input = """
        Class Maim {
             main(){
                Val a : A =New A("Hello world");
                a.boo()[2] = b.boo[a.boo() +3];
            }
        }
        """
        expect = "Program([ClassDecl(Id(Maim),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[StringLit(Hello world)])),AssignStmt(ArrayCell(CallExpr(Id(a),Id(boo),[]),[IntLit(2)]),ArrayCell(FieldAccess(Id(b),Id(boo)),[BinaryOp(+,CallExpr(Id(a),Id(boo),[]),IntLit(3))]))]))])])"

        self.assertTrue(TestAST.test(input, expect, 350))

    def test_AST52(self):
        input = """
        Class Triangle : Shape {
        Var length, width : Float;
        Var a, $b,$c,d : Float = 1.1,2.2,3.4,4.4;
        getArea(){
                Return Self.length*Self.width / 2;
            }
        $getCircle(){
                Return a*Triangle:: $b*Triangle::$c / 2;
            }
        }
        Class Program{
            main(arg: String)
            {
                Return 0;
            }
            main()
            {
                Var a: Triangle;
                a.getArea();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Triangle),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(1.1))),AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(2.2))),AttributeDecl(Static,VarDecl(Id($c),FloatType,FloatLit(3.4))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(4.4))),MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))])),MethodDecl(Id($getCircle),Static,[],Block([Return(BinaryOp(/,BinaryOp(*,BinaryOp(*,Id(a),FieldAccess(Id(Triangle),Id($b))),FieldAccess(Id(Triangle),Id($c))),IntLit(2)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(arg),StringType)],Block([Return(IntLit(0))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Triangle)),NullLiteral()),Call(Id(a),Id(getArea),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_AST53(self):
        input = """Class Detructor {
             Var a : Float = 1.1;
        }"""
        expect = "Program([ClassDecl(Id(Detructor),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(1.1)))])])"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_AST54(self):
        input = """
        Class Clf {
             Var a,b : A;
        }"""
        expect = "Program([ClassDecl(Id(Clf),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(A)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(A)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_AST55(self):
        input = """
        Class main {
            Var a,b: Array[Array[Int,3], 2];
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(2,ArrayType(3,IntType)))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(2,ArrayType(3,IntType))))])])"
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_AST56(self):
        input = """Class main {
            Var $a,b: Int =1,2;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2)))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_AST57(self):
        input = """
        Class Triangle : Shape {
        Var length, width : Float;
        Var a, $b,$c,d : Float = 1.1,2.2,3.4,4.4;
        $getArea(){
                Return Self.length*Self.width / 2;
            }
        $getCircle(){
                Return a*(Triangle:: $b)*(Triangle::$c) / 2;
            }
        }
        Class Program{
            main(arg: String)
            {
                Return 0;
            }
            main()
            {
                a = (Triangle :: $getArea()) * (Triangle :: $getCircle());
            }
        }
        """
        expect = "Program([ClassDecl(Id(Triangle),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(1.1))),AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(2.2))),AttributeDecl(Static,VarDecl(Id($c),FloatType,FloatLit(3.4))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(4.4))),MethodDecl(Id($getArea),Static,[],Block([Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))])),MethodDecl(Id($getCircle),Static,[],Block([Return(BinaryOp(/,BinaryOp(*,BinaryOp(*,Id(a),FieldAccess(Id(Triangle),Id($b))),FieldAccess(Id(Triangle),Id($c))),IntLit(2)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(arg),StringType)],Block([Return(IntLit(0))])),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(*,CallExpr(Id(Triangle),Id($getArea),[]),CallExpr(Id(Triangle),Id($getCircle),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_AST58(self):
        input = """
        Class XXX { }
        Class main {
        }
        Class YYY{

        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),[]),ClassDecl(Id(YYY),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_AST59(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var $a,b: Int=1,2;
            Var $a, b : Float=1.1e+1,2.2e+2;
            Var a,b : Int=1, 3;
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(11.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(220.0))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(3)))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_AST60(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var a,b : Int=2,1;
            Var a,b : Int=1,2;
            Var a : XXX;
            method(){}
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(XXX)),NullLiteral())),MethodDecl(Id(method),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_AST61(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var a: Boolean = True;
            Var a,b : Int=1,1;
            method(a,b: A; a: B){
                Return Null;
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(1))),MethodDecl(Id(method),Instance,[param(Id(a),ClassType(Id(A))),param(Id(b),ClassType(Id(A))),param(Id(a),ClassType(Id(B)))],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_AST62(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var a: Boolean = True;
            Var a,b : Int=1,1;
            method(a : Int; a,b: Boolean){
                If(True)
                    {
                        Return "It's true";
                    }
                Else {
                        Return "It's not true";
                    }
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(1))),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(a),BoolType),param(Id(b),BoolType)],Block([If(BooleanLit(True),Block([Return(StringLit(It's true))]),Block([Return(StringLit(It's not true))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_AST63(self):
        input = """
        Class Shape:Shape {
            Val $numOfShape,numOfShape: Int=1,2;
            Var x: Float;
            $getNumOfShape() {
                Return hey::$numOfShape;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(hey),Id($numOfShape)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_AST64(self):
        input = """
        Class XXX { }
        Class main : XXX {
            ## Self is a line comment
            /*
                Self is also a comment do nha ^^
            */
            Var a=1,b=2;
            Var a=1.1e+1, b=2.2e+2;
            Var a,b=1;
            method(Var a; Var a,b){
                Var $a=1,b=2;
                Var a=1.1e+1, b=2.2e+2;
                Var a,b;
            }
            ##
            method1(a : Int; a,b: XXX){
                Return a;
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[MethodDecl(Id(method1),Instance,[param(Id(a),IntType),param(Id(a),ClassType(Id(XXX))),param(Id(b),ClassType(Id(XXX)))],Block([Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_AST65(self):
        input = """
        Class XXX { }
        ##Class main : XXX {
            # Self is a line comment
            /*
                Self is also a comment do nha ^^
            */
             Var a=1,b=2;
            Var a=1.1e+1, b=2.2e+2;
            Var a,b=1;
             Var method(Var a; Var a,b){
                Var $a=1,b=2;
                Var a=1.1e+1, b=2.2e+2;
                Var a,b;
                Return a;
            }
             method1(Var a; Var a,b){
                Var $a=1,b=2;
                Return 1;
            }
        }
        ##"""
        expect = "Program([ClassDecl(Id(XXX),[])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_AST66(self):
        input = """
        Class XXX { }
        Class main : XXX {
            ## Self is a line comment
            ##
            Var a: Int=1;
            Var a: Float=1.1e+1;
            Val b: Float =2.2e+2;
            method(a: XXX; a,b: XXX){
                Return a;
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(11.0))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(220.0))),MethodDecl(Id(method),Instance,[param(Id(a),ClassType(Id(XXX))),param(Id(a),ClassType(Id(XXX))),param(Id(b),ClassType(Id(XXX)))],Block([Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_AST67(self):
        input = """
        Class XXX { }
        Class main : XXX {
            ## Self is a line comment
            ##
            
            method1(a: Int;a,b: String){
                Var b : Int=2;
                Self.myPI = 3.14;
                value = x.foo(5);
                l[3] = value / 2;
                r = 2.0;
                s = r*r*Self.myPI;
                Return 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[MethodDecl(Id(method1),Instance,[param(Id(a),IntType),param(Id(a),StringType),param(Id(b),StringType)],Block([VarDecl(Id(b),IntType,IntLit(2)),AssignStmt(FieldAccess(Self(),Id(myPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),[IntLit(3)]),BinaryOp(/,Id(value),IntLit(2))),AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),Return(IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_AST68(self):
        input = """
        Class XXX { }
        Class main : XXX {
            method(a: Int;a,b: String){
                If (flag) {
                    a = b;
                    }
                Else{ a = b+1;}
                Return a;
            }
             method1(a: Int;a,b: String){
                value = x.foo(5);
                l[3] = value / 2;
                r = 2.0;
                s = r*r*Self.myPI;
                Return 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(XXX),[]),ClassDecl(Id(main),Id(XXX),[MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(a),StringType),param(Id(b),StringType)],Block([If(Id(flag),Block([AssignStmt(Id(a),Id(b))]),Block([AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(1)))])),Return(Id(a))])),MethodDecl(Id(method1),Instance,[param(Id(a),IntType),param(Id(a),StringType),param(Id(b),StringType)],Block([AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),[IntLit(3)]),BinaryOp(/,Id(value),IntLit(2))),AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),Return(IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_AST69(self):
        input = """
        Class Program:sv{
            main(){
                    {
                        If(a){}
                        Elseif(b){}
                        Elseif(c){}
                        {
                            a = 1;
                            Return a;
                        }
                    }
                }
            }
       """
        expect = "Program([ClassDecl(Id(Program),Id(sv),[MethodDecl(Id(main),Static,[],Block([Block([If(Id(a),Block([]),If(Id(b),Block([]),If(Id(c),Block([])))),Block([AssignStmt(Id(a),IntLit(1)),Return(Id(a))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_AST70(self):
        input = """
        Class Program:sv{
            Var q,$s,c:String= "My", " name" ,"is Thuong";
            }
        """
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(q),StringType,StringLit(My))),AttributeDecl(Static,VarDecl(Id($s),StringType,StringLit( name))),AttributeDecl(Instance,VarDecl(Id(c),StringType,StringLit(is Thuong)))])])"
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_AST71(self):
        input = """
        Class Test {
                main(){
                    Self.call("alo");
                }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Call(Self(),Id(call),[StringLit(alo)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_AST72(self):
        input = """
        Class Test {
            main()
            {
            Var A, B, temp : Test = New A(), New B(), New C();

            Other.prVarf("Please enter the 1st number : ");
            }
            }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(A),ClassType(Id(Test)),NewExpr(Id(A),[])),VarDecl(Id(B),ClassType(Id(Test)),NewExpr(Id(B),[])),VarDecl(Id(temp),ClassType(Id(Test)),NewExpr(Id(C),[])),Call(Id(Other),Id(prVarf),[StringLit(Please enter the 1st number : )])]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_AST73(self):
        input = """
        Class Test {
            main(){
                a = Other.b() + Other.c() + Other.d();
                Other.prVar(a);
                a = a / Other.sum(a,b) + Other.sub(a,b);
                }

        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,CallExpr(Id(Other),Id(b),[]),CallExpr(Id(Other),Id(c),[])),CallExpr(Id(Other),Id(d),[]))),Call(Id(Other),Id(prVar),[Id(a)]),AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),CallExpr(Id(Other),Id(sum),[Id(a),Id(b)])),CallExpr(Id(Other),Id(sub),[Id(a),Id(b)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_AST74(self):
        input = """
        Class Test {
            main(){
                Return "abc"+."cde";
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(+.,StringLit(abc),StringLit(cde)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_AST75(self):
        input = """
        Class Test
        {
            main(){
                Return "Val";
            }
            mainVar(){
                Return 1;
            }
            mainVar(){
                Return 1.0;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([Return(StringLit(Val))])),MethodDecl(Id(mainVar),Instance,[],Block([Return(IntLit(1))])),MethodDecl(Id(mainVar),Instance,[],Block([Return(FloatLit(1.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_AST76(self):
        input = """
        Class Vehicle
        {
            Vehicle()
            {
                io.writeVarLn("Self is a Vehicle");
            }
        }

        Class FourWheeler
        {
            FourWheeler()
            {
                io.writeVarLn("Self is a 4 wheeler Vehicle");
            }
        }

        Class Car : Vehicle
        {
        }
        """
        expect = "Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(Vehicle),Instance,[],Block([Call(Id(io),Id(writeVarLn),[StringLit(Self is a Vehicle)])]))]),ClassDecl(Id(FourWheeler),[MethodDecl(Id(FourWheeler),Instance,[],Block([Call(Id(io),Id(writeVarLn),[StringLit(Self is a 4 wheeler Vehicle)])]))]),ClassDecl(Id(Car),Id(Vehicle),[])])"
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_AST77(self):
        input = """
        Class Operator
        {
            main()
            {
                Return ((1>=2));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Operator),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(>=,IntLit(1),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_AST78(self):
        input = """
         Class Point {
            Var x,y,z: Int;
            Contructor(x:Int;y:Int;z:Int)
            {
                Self.x = x;
                Self.y = y;
                Self.z = z;
            }
            Sum()
            {
                Return Self.x+Self.y+Self.z;
            }
            main()
            {
                Var b: Point = New Point(1,2,4);
                b.Sum();
                Return 0; 
            }
        }

        """
        expect = "Program([ClassDecl(Id(Point),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Instance,VarDecl(Id(z),IntType)),MethodDecl(Id(Contructor),Instance,[param(Id(x),IntType),param(Id(y),IntType),param(Id(z),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y)),AssignStmt(FieldAccess(Self(),Id(z)),Id(z))])),MethodDecl(Id(Sum),Instance,[],Block([Return(BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y))),FieldAccess(Self(),Id(z))))])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(b),ClassType(Id(Point)),NewExpr(Id(Point),[IntLit(1),IntLit(2),IntLit(4)])),Call(Id(b),Id(Sum),[]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_AST79(self):
        input = """
        Class Test {
            print(x: Int)
            {
                Self.x();
            }
            main()
            {
                Val x: Int= 100+1;
                Foreach( h In 1 .. x+1 By x-1)
                {
                    If(x%2 == 0)
                    {
                        Self.print(x);
                    }
                    Else {Continue;}
                    Break;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(print),Instance,[param(Id(x),IntType)],Block([Call(Self(),Id(x),[])])),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(x),IntType,BinaryOp(+,IntLit(100),IntLit(1))),For(Id(h),IntLit(1),BinaryOp(+,Id(x),IntLit(1)),BinaryOp(-,Id(x),IntLit(1)),Block([If(BinaryOp(==,BinaryOp(%,Id(x),IntLit(2)),IntLit(0)),Block([Call(Self(),Id(print),[Id(x)])]),Block([Continue])),Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_AST80(self):
        input = """
        Class Animal {
            Val $numOfAnimal: Int = 0;
            Val imAttr: Int = 0;
            Var height, weight: Int;
            $getNumOfAnimal() {
            Return Animal::$numOfAnimal;
            }
            }
            Class Elephant: Animal {
            getWeight() {
            Return Self.weight;
            }
            }
        """
        expect = "Program([ClassDecl(Id(Animal),[AttributeDecl(Static,ConstDecl(Id($numOfAnimal),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(imAttr),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(weight),IntType)),MethodDecl(Id($getNumOfAnimal),Static,[],Block([Return(FieldAccess(Id(Animal),Id($numOfAnimal)))]))]),ClassDecl(Id(Elephant),Id(Animal),[MethodDecl(Id(getWeight),Instance,[],Block([Return(FieldAccess(Self(),Id(weight)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_AST81(self):
        input = """
        Class main{
            method(){
            array[3][2]=2*3;
            a=array[3][3];
            a=a.sinhvien()[3];
            }
        }
        """
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(ArrayCell(Id(array),[IntLit(3),IntLit(2)]),BinaryOp(*,IntLit(2),IntLit(3))),AssignStmt(Id(a),ArrayCell(Id(array),[IntLit(3),IntLit(3)])),AssignStmt(Id(a),ArrayCell(CallExpr(Id(a),Id(sinhvien),[]),[IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_AST82(self):
        input = """
        Class BK {
            Val $static: Int = 23;
            Var a,b,c: Float = 58.5,3,6;
        }
        """
        expect = "Program([ClassDecl(Id(BK),[AttributeDecl(Static,ConstDecl(Id($static),IntType,IntLit(23))),AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(58.5))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(6)))])])"
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_AST83(self):
        input = """
        Class SinhVien {
            getTBTL(id:Int;name:String){
                If((Self.id==id)&&(Self.name==name)){Return Self.TBTL;}
                Elseif((Self.id==id)&&(Self.name!=name)){Return 0;}
            }
        }
        """
        expect = "Program([ClassDecl(Id(SinhVien),[MethodDecl(Id(getTBTL),Instance,[param(Id(id),IntType),param(Id(name),StringType)],Block([If(BinaryOp(&&,BinaryOp(==,FieldAccess(Self(),Id(id)),Id(id)),BinaryOp(==,FieldAccess(Self(),Id(name)),Id(name))),Block([Return(FieldAccess(Self(),Id(TBTL)))]),If(BinaryOp(&&,BinaryOp(==,FieldAccess(Self(),Id(id)),Id(id)),BinaryOp(!=,FieldAccess(Self(),Id(name)),Id(name))),Block([Return(IntLit(0))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_AST84(self):
        input = """
        Class SinhVien {
            getTBTL(id:Int;name:String){
                a=b+c;
                c=2*3;
                b=3/4;
            }
        }
        """
        expect = "Program([ClassDecl(Id(SinhVien),[MethodDecl(Id(getTBTL),Instance,[param(Id(id),IntType),param(Id(name),StringType)],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c))),AssignStmt(Id(c),BinaryOp(*,IntLit(2),IntLit(3))),AssignStmt(Id(b),BinaryOp(/,IntLit(3),IntLit(4)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_AST85(self):
        input = """
        Class SinhVien {
            getTBTL(id:Int;name:String){
                Foreach(a In 1 .. 100 By 5)
                {
                    a=2*3;
                    If(a!=0){Return;}
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(SinhVien),[MethodDecl(Id(getTBTL),Instance,[param(Id(id),IntType),param(Id(name),StringType)],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(5),Block([AssignStmt(Id(a),BinaryOp(*,IntLit(2),IntLit(3))),If(BinaryOp(!=,Id(a),IntLit(0)),Block([Return()]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_AST86(self):
        input = """
        Class Ulities{
           findMax(list: Array[Int,10]){
                Var max,max1:Int=list[0], list[0];
                Foreach(i In 0 .. 10 By 1){
                    If(list[i]>max) {
                        max=list[i];
                        max1=max;
                    }
                }
                Return Array(max,max1);
           }
        }
        """
        expect = "Program([ClassDecl(Id(Ulities),[MethodDecl(Id(findMax),Instance,[param(Id(list),ArrayType(10,IntType))],Block([VarDecl(Id(max),IntType,ArrayCell(Id(list),[IntLit(0)])),VarDecl(Id(max1),IntType,ArrayCell(Id(list),[IntLit(0)])),For(Id(i),IntLit(0),IntLit(10),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(list),[Id(i)]),Id(max)),Block([AssignStmt(Id(max),ArrayCell(Id(list),[Id(i)])),AssignStmt(Id(max1),Id(max))]))])]),Return([Id(max),Id(max1)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_AST87(self):
        input = """
        Class A {
            methodA(a,b:Array[Int,5];c:Int) {
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(methodA),Instance,[param(Id(a),ArrayType(5,IntType)),param(Id(b),ArrayType(5,IntType)),param(Id(c),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_AST88(self):
        input = """
        Class A {
            methodA() {
                Var _: Int=0x12A_F;
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(methodA),Instance,[],Block([VarDecl(Id(_),IntType,IntLit(4783))]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_AST89(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                a[1][2] = b[3][4] - c[3][4][5];
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(-,ArrayCell(Id(b),[IntLit(3),IntLit(4)]),ArrayCell(Id(c),[IntLit(3),IntLit(4),IntLit(5)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_AST90(self):
        input = """
        Class Program{
            main(){
                Foreach (x In 1+3 .. 8/2 By 3){
                Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
                }
                }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(3)),BinaryOp(/,IntLit(8),IntLit(2)),IntLit(3),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_AST91(self):
        input = """
        Class LinkList{
            Var head,tail: Node = Null,Null;
            Var length: Int=0;
            append(value:Int){
                If(length==0){
                    Self.head= New Node(value);
                    Self.tail=head;

                } Else{
                    Var temp: Node= Self.tail;
                    Self.tail= New Node(value);
                    temp.nextNode=Self.tail;
                }
                Self.length=Self.length+1;
            }
        }
        """
        expect = "Program([ClassDecl(Id(LinkList),[AttributeDecl(Instance,VarDecl(Id(head),ClassType(Id(Node)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(tail),ClassType(Id(Node)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),MethodDecl(Id(append),Instance,[param(Id(value),IntType)],Block([If(BinaryOp(==,Id(length),IntLit(0)),Block([AssignStmt(FieldAccess(Self(),Id(head)),NewExpr(Id(Node),[Id(value)])),AssignStmt(FieldAccess(Self(),Id(tail)),Id(head))]),Block([VarDecl(Id(temp),ClassType(Id(Node)),FieldAccess(Self(),Id(tail))),AssignStmt(FieldAccess(Self(),Id(tail)),NewExpr(Id(Node),[Id(value)])),AssignStmt(FieldAccess(Id(temp),Id(nextNode)),FieldAccess(Self(),Id(tail)))])),AssignStmt(FieldAccess(Self(),Id(length)),BinaryOp(+,FieldAccess(Self(),Id(length)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_AS92(self):
        input = """
        Class Operator
        {
            Var a,sum: Int=0,New Operator("hien",1230).new;
            main(){
               Foreach( a In 1 .. 100 ){
                    If (sum==2) {Break;}
                    Else {sum = sum+a;}
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(sum),IntType,FieldAccess(NewExpr(Id(Operator),[StringLit(hien),IntLit(1230)]),Id(new)))),MethodDecl(Id(main),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(1),Block([If(BinaryOp(==,Id(sum),IntLit(2)),Block([Break]),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(a)))]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_AST93(self):
        input = """
        Class Integer{
            gcd(a:Int; b:Int){
            If ((a == 0) || (b == 0)){
            Return a + b;
            }
            }
            }
        """
        expect = "Program([ClassDecl(Id(Integer),[MethodDecl(Id(gcd),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(a),IntLit(0)),BinaryOp(==,Id(b),IntLit(0))),Block([Return(BinaryOp(+,Id(a),Id(b)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_AST94(self):
        input = """
        Class Integer{
            Var a: Array[Int,5]=Array(2,6,9,7,5);
            findMax(){
            Var max:Int= a[0];
            Foreach(i In 0 .. 10 By 1){
                If(a[i]<min) {
                    min=a[i];
                }
            }
            Return min;
           }
    }
        """
        expect = "Program([ClassDecl(Id(Integer),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(2),IntLit(6),IntLit(9),IntLit(7),IntLit(5)])),MethodDecl(Id(findMax),Instance,[],Block([VarDecl(Id(max),IntType,ArrayCell(Id(a),[IntLit(0)])),For(Id(i),IntLit(0),IntLit(10),IntLit(1),Block([If(BinaryOp(<,ArrayCell(Id(a),[Id(i)]),Id(min)),Block([AssignStmt(Id(min),ArrayCell(Id(a),[Id(i)]))]))])]),Return(Id(min))]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_AST95(self):
        input = """
        Class ArrayList{
            Val a, b: Array[Array[String,3],2] = Array(1,2,3), Array("$abc", 0x123, 0b101);
            Var c: Int = a[0] + b[0];
            $GETsHAPE(){
                Foreach(i In 1 .. 2){
                    Foreach(j In 1 .. 3){
                    If(a[i][j]>0)
                    {
                        Out.Print("Duong");
                    }
                    Else{
                        Out.Print("am");
                    }
                }
            }
        }
        }
        """
        expect = "Program([ClassDecl(Id(ArrayList),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(2,ArrayType(3,StringType)),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(2,ArrayType(3,StringType)),[StringLit($abc),IntLit(291),IntLit(5)])),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(b),[IntLit(0)])))),MethodDecl(Id($GETsHAPE),Static,[],Block([For(Id(i),IntLit(1),IntLit(2),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(3),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(a),[Id(i),Id(j)]),IntLit(0)),Block([Call(Id(Out),Id(Print),[StringLit(Duong)])]),Block([Call(Id(Out),Id(Print),[StringLit(am)])]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_AST96(self):
        input = """
        Class Shape {
            Var width,length:Array[Array[Int,2],2] = Array(Array(5,6), Array(2*3,4*6)), Array(Array(2,3),Array(a&&b));
            $getNumOfShape() {
                If(width[1][2]*length[12][2]>10)
                {
                    Foreach (x In 5 .. 2) {
                    Out.printInt(a[x]);
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(width),ArrayType(2,ArrayType(2,IntType)),[[IntLit(5),IntLit(6)],[BinaryOp(*,IntLit(2),IntLit(3)),BinaryOp(*,IntLit(4),IntLit(6))]])),AttributeDecl(Instance,VarDecl(Id(length),ArrayType(2,ArrayType(2,IntType)),[[IntLit(2),IntLit(3)],[BinaryOp(&&,Id(a),Id(b))]])),MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(>,BinaryOp(*,ArrayCell(Id(width),[IntLit(1),IntLit(2)]),ArrayCell(Id(length),[IntLit(12),IntLit(2)])),IntLit(10)),Block([For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[Id(x)])])])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_AST97(self):
        input = """
        Class AVL {
            $root(Node: Int; Left: Int;Right:Int){
                Foreach (i In 1 .. 3 By 1) {
                    Left[i]=Left[0];
                }
            }
            }"""
        expect = "Program([ClassDecl(Id(AVL),[MethodDecl(Id($root),Static,[param(Id(Node),IntType),param(Id(Left),IntType),param(Id(Right),IntType)],Block([For(Id(i),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(Id(Left),[Id(i)]),ArrayCell(Id(Left),[IntLit(0)]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_AST98(self):
        input = """
        Class Shape {
           Contructor(){}
        }
        Class Rectangle : Shape {
           getArea(){
            x.b[2] = x.m()[3];
            }
        }
        Class Triangle : Shape {
            getArea(){
            Return Self.length*Self.width / 2;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Contructor),Instance,[],Block([]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),[IntLit(2)]),ArrayCell(CallExpr(Id(x),Id(m),[]),[IntLit(3)]))]))]),ClassDecl(Id(Triangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_AST99(self):
        input = """Class SinhVien {
            Var test: Int = (a==b);
            Var test1,test: Int = (3!=2), a>=b;
        }"""
        expect = "Program([ClassDecl(Id(SinhVien),[AttributeDecl(Instance,VarDecl(Id(test),IntType,BinaryOp(==,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(test1),IntType,BinaryOp(!=,IntLit(3),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(test),IntType,BinaryOp(>=,Id(a),Id(b))))])])"
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_AST100(self):
        input = """
        Class SinhVien:BK {
            Var test: Boolean = !(3==2)||(2==3)&&(2==2);
            Var test1: String = "abc";
        }"""
        expect = "Program([ClassDecl(Id(SinhVien),Id(BK),[AttributeDecl(Instance,VarDecl(Id(test),BoolType,BinaryOp(&&,BinaryOp(||,UnaryOp(!,BinaryOp(==,IntLit(3),IntLit(2))),BinaryOp(==,IntLit(2),IntLit(3))),BinaryOp(==,IntLit(2),IntLit(2))))),AttributeDecl(Instance,VarDecl(Id(test1),StringType,StringLit(abc)))])])"
        self.assertTrue(TestAST.test(input, expect, 399))
