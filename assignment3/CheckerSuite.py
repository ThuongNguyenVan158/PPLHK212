import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_AST0(self):
        input = """
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){
                Return 1;
            }
          
                
        }"""
        expect = "Type Mismatch In Statement: ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(numOfShape),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(x),IntType,BinaryOp(+,FieldAccess(Self(),Id(numOfShape)),IntLit(1)))),MethodDecl(Id(x),Instance,[],Block([VarDecl(Id(x),IntType,IntLit(1)),Return(IntLit(1)),Block([Return(IntLit(2))])])),MethodDecl(Id(main),Static,[],Block([Return(IntLit(1))]))])"
        self.assertTrue(TestChecker.test(input, expect, 300))
  
    def test_AST1(self):
        input = """
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(x: Int){
                Return;
            }  
        }"""
        expect = "No Entry Point"

        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_AST2(self):
        input = """
        Class main : A  {
            Var numOfShape : Int = 1;
            Var num1 : Int = Self.numOfShape;
            Var num2 : Int = Self.numOfShape + Self.num1;
            Val x: Int = 1;
            Val y: Float = 1.2 + Self.x;
            Var num3 : Int = numOfShape + Self.num3;
            A(a,b : Int){
                Var x: Int = 1;
                Var y: Int =x;
                Return x+y*a;
                }
        }
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){

            }
          
                
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 302))
    def test_AST3(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
            Var num1 : Int = Self.numOfShape;
            Var num2 : Int = Self.numOfShape + Self.num1;
            Val x: Int = 1;
            Val y: Int = 1.2 + Self.x;
            Var num3 : Int = numOfShape + Self.num3;
            A(a,b : Int){
                Var x: Int = 1;
                Var y: Int =x;
                Return x+y*a;
                }
        }
        Class Program : main{
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){

            }
          
                
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,BinaryOp(+,FloatLit(1.2),FieldAccess(Self(),Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 303))
    def test_AST4(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
        }
        Class Program{
            main(){
                Var x: main = New main(1);
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Method: Contructor"
        self.assertTrue(TestChecker.test(input, expect, 304))
    def test_AST5(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape1;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Attribute: numOfShape1"
        self.assertTrue(TestChecker.test(input, expect, 305))
    def test_AST6(self):
        input = """
        Class main {
            Var numOfShape : Boolean = 1;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(numOfShape),BoolType,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 306))
    def test_AST7(self):
        input = """
        Class main {
            Var numOfShape : Boolean = True;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),FloatType,FieldAccess(Id(x),Id(numOfShape)))"
        self.assertTrue(TestChecker.test(input, expect, 307))
    def test_AST8(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape;
                Var y : Int = numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 308))
    def test_AST9(self):
        input = """
        Class main {
            Var numOfShape : Float = 1;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Int = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,FieldAccess(Id(x),Id(numOfShape)))"
        self.assertTrue(TestChecker.test(input, expect, 309))
    def test_AST10(self):
        input = """
        Class main {
            Var numOfShape : Float = 1;
        }
        Class Program{
            main(){
               
                Var z: Int = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input, expect, 310))
    def test_AST11(self):
        input = """
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){
                Var x :Int = 1*2 + True;
                Return;
            }
          
                
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 311))
  
    def test_AST12(self):
        input = """
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            Val x : Int = 1;
            main(x: Int){
                Return;
            }  
        }"""
        expect = "Redeclared Attribute: x"

        self.assertTrue(TestChecker.test(input, expect, 312))

    def test_AST13(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
            Var num1 : Int = Self.numOfShape;
            Var num2 : Int = Self.numOfShape + Self.num1;
            Val x: Int = 1;
            Val y: Float = 1.2 + Self.x;
            Var num3 : Int = numOfShape + Self.num3;
            A(a,b : Int){
                Var x: Int = 1;
                Var y: Int =x;
                Return x+y*a;
                }
        }
        Class Program {
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){
                Return;
            }
          
                
        }
        """
        expect = "Undeclared Identifier: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 313))
    def test_AST14(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
            Var num1 : Int = Self.numOfShape;
            Var num2 : Int = Self.numOfShape + Self.num1;
            Val x: Int = 1;
            Val y: Int = 1.2 * Self.x;
            Var num3 : Int = numOfShape + Self.num3;
            A(a,b : Int){
                Var x: Int = 1;
                Var y: Int =x;
                Return x+y*a;
                }
        }
        Class Program : main{
            Val numOfShape : Int = 1;
            Val x : Int = Self.numOfShape + 1;
            x(){
                Var x: Int =1;
                Return 1;
                {
                Return 2;
                }
            }
            main(){

            }
          
                
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,BinaryOp(*,FloatLit(1.2),FieldAccess(Self(),Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 314))
    def test_AST15(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
        }
        Class Program{
            main(){
                Val x: main = New main(1);
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Illegal Constant Expression: NewExpr(Id(main),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 315))
    def test_AST16(self):
        input = """
        Class main {
            Val numOfShape : Int;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape1;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 316))
    def test_AST17(self):
        input = """
        Class main {
            Var numOfShape : Boolean = 1;
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(numOfShape),BoolType,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 317))
    def test_AST18(self):
        input = """
        Class main {
            Val numOfShape : Boolean = True;
            Contructor(x: Int){
                Self.numOfShape = False;
            }
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Float = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(numOfShape)),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 318))
    def test_AST19(self):
        input = """
        Class main {
            Var numOfShape : Int = 1;
            Contructor(x: Int){
                Self.numOfShape = 1;
            }
        }
        Class Program{
            main(){
                Var x: main = New main(1);
                Var z: Boolean = x.numOfShape;
                Var y : Int = numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Method: Contructor"
        self.assertTrue(TestChecker.test(input, expect, 319))
    def test_AST20(self):
        input = """
        Class main {
            Var numOfShape : Float = 1;
            Contructor(){
                Self.numOfShape = "a";
            }
        }
        Class Program{
            main(){
                Var x: main = New main();
                Var z: Int = x.numOfShape;
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(numOfShape)),StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 320))
    def test_AST21(self):
        input = """
        Class main {
            Var numOfShape : Float = 1;
        }
        Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 321))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 322))

    def test_AST24(self):
        
        input = '''
        Class Test {
           
                
        }
              Class Program{
            main(){
               
                Var z: Int = 1;
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input, expect, 323))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 324))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Method: int"
        self.assertTrue(TestChecker.test(input, expect, 325))

    def test_AST27(self):
        
        input = '''
        Class Test {
            main()
            {
                a = New Exp(1,2,4);
                Self.print(i);
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Class: Exp"
        self.assertTrue(TestChecker.test(input, expect, 326))

    def test_AST28(self):
        
        input = '''
        Class A{}
        Class Program {
            main()
            {
                Var i : Int;
                i = 8;
                A.printf("Factorial of the number is ", i, A.factorial(i));
                Return 0;
            }
            factorial(i : Int)
            {
                If(i < 2)
                {
                    Return 1;
                }
                Return i * A.factorial(i - 1);
                }
            }
        '''
        expect = "Undeclared Method: printf"
        self.assertTrue(TestChecker.test(input, expect, 327))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Identifier: flag"
        self.assertTrue(TestChecker.test(input, expect, 328))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Class: Other"
        self.assertTrue(TestChecker.test(input, expect, 329))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 330))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 331))

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
                    Test.Compare("a", "b");
                    Return 0;
                }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Illegal Member Access: Call(Id(Test),Id(Compare),[StringLit(a),StringLit(b)])"
        self.assertTrue(TestChecker.test(input, expect, 332))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 333))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 334))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 335))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([If(IntLit(1),Block([Return(IntLit(1))]))]))]))]))"
        self.assertTrue(TestChecker.test(input, expect, 336))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 337))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 338))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 339))

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
        }
        '''
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 340))

    def test_AST42(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1/2+3/4+5/6+7/8+8/9;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 341))

    def test_AST43(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1.1 || 2.2;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Expression: BinaryOp(||,FloatLit(1.1),FloatLit(2.2))"
        self.assertTrue(TestChecker.test(input, expect, 342))

    def test_AST44(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1>=2;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 343))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 344))

    def test_AST46(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return -1/-2;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 345))

    def test_AST47(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return -1+-2+1.1+-1.2;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 346))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 347))

    def test_AST49(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                Return 1.0e10/1.2e10;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 348))

    def test_AST50(self):
        
        input = '''
        Class Operator
        {
            main()
            {
                a[(3+x.foo(2))/5*3-25] = a[b[2]] +3*a[4]/3;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        '''
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 349))

    def test_AST51(self):
        input = """
        Class Maim {
             main(){
                Val a : A =New A("Hello world");
                a.boo()[2] = b.boo[a.boo() +3];
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Illegal Constant Expression: NewExpr(Id(A),[StringLit(Hello world)])"

        self.assertTrue(TestChecker.test(input, expect, 350))

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
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 351))

    def test_AST53(self):
        input = """Class Detructor {
             Var a : Float = 1.1;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 352))

    def test_AST54(self):
        input = """
        Class A{}
        Class Clf {
             Var a,b : Int;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 353))

    def test_AST55(self):
        input = """
        Class main {
            Var a,b: Array[Array[Int,3], 2];
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 354))

    def test_AST56(self):
        input = """Class main {
            Var $a,b: Int =1,2;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 355))

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
           
            main()
            {
                a = (Triangle :: $getArea()) * (Triangle :: $getCircle());
            }
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input, expect, 356))

    def test_AST58(self):
        input = """
        Class XXX { }
        Class main {
        }
        Class YYY : zzz{

        }
        Class Program{
            main(){

            }
        }
        """
        expect = "Undeclared Class: zzz"
        self.assertTrue(TestChecker.test(input, expect, 357))

    def test_AST59(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var $a,b: Int=1,2;
            Var $a, b : Float=1.1e+1,2.2e+2;
            Var a,b : Int=1, 3;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Attribute: $a"
        self.assertTrue(TestChecker.test(input, expect, 358))

    def test_AST60(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var a,b : Int=2,1;
            Var a,b : Int=1,2;
            Var a : XXX;
            method(){}
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 359))

    def test_AST61(self):
        input = """
        Class XXX { }
        Class main : XXX {
            Var a: Boolean = True;
            Var a,b : Int=1,1;
            method(a,b: A; a: B){
                Return Null;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 360))

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
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 361))

    def test_AST63(self):
        input = """
        Class Shape:Shape {
            Val $numOfShape,numOfShape: Int=1,2;
            Var x: Float;
            $getNumOfShape() {
                Return hey::$numOfShape;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: hey"
        self.assertTrue(TestChecker.test(input, expect, 362))

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
            
            ##
            method1(a : Int; a,b: Int){
                Return a;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 363))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        ##"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 364))

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
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 365))

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
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 366))

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
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 367))

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
        expect = "Undeclared Class: sv"
        self.assertTrue(TestChecker.test(input, expect, 368))

    def test_AST70(self):
        input = """
        Class Program:sv{
            Var q,$s,c:String= "My", " name" ,"is Thuong";
            }
        """
        expect = "Undeclared Class: sv"
        self.assertTrue(TestChecker.test(input, expect, 369))

    def test_AST71(self):
        input = """
        Class Test {
                main(){
                    A.call("alo");
                }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 370))

    def test_AST72(self):
        input = """
        Class Test {
            main()
            {
            Var A, B, temp : Test = New A(), New B(), New C();

            Other.prVarf("Please enter the 1st number : ");
            }
            }
                  Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 371))

    def test_AST73(self):
        input = """
        Class Test {
            main(){
                a = Other.b() + Other.c() + Other.d();
                Other.prVar(a);
                a = a / Other.sum(a,b) + Other.sub(a,b);
                }

        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: Other"
        self.assertTrue(TestChecker.test(input, expect, 372))

    def test_AST74(self):
        input = """
        Class Test {
            main(){
                Return "abc"+."cde";
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 373))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Method: mainVar"
        self.assertTrue(TestChecker.test(input, expect, 374))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: io"
        self.assertTrue(TestChecker.test(input, expect, 375))

    def test_AST77(self):
        input = """
        Class Operator
        {
            main()
            {
                Return ((1>=2));
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 376))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }

        """
        expect = "Undeclared Method: Contructor"
        self.assertTrue(TestChecker.test(input, expect, 377))

    def test_AST79(self):
        input = """
        Class Test {
            print(x: Int)
            {
                A.x();
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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 378))

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
                  Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 379))

    def test_AST81(self):
        input = """
        Class main{
            method(){
            array[3][2]=2*3;
            a=array[3][3];
            a=a.sinhvien()[3];
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: array"
        self.assertTrue(TestChecker.test(input, expect, 380))

    def test_AST82(self):
        input = """
        Class BK {
            Val $static: Int = 23;
            Var a,b,c: Float = 58.5,3,6;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 381))

    def test_AST83(self):
        input = """
        Class SinhVien {
            getTBTL(id:Int;name:String){
                If((Self.id==id)&&(Self.name==name)){Return Self.TBTL;}
                Elseif((Self.id==id)&&(Self.name!=name)){Return 0;}
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Attribute: id"
        self.assertTrue(TestChecker.test(input, expect, 382))

    def test_AST84(self):
        input = """
        Class SinhVien {
            getTBTL(id:Int;name:String){
                a=b+c;
                c=2*3;
                b=3/4;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 383))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 384))

    def test_AST86(self):
        input = """
        Class Ulities{
           findMax(){
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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: list"
        self.assertTrue(TestChecker.test(input, expect, 385))

    def test_AST87(self):
        input = """
        Class A {
            methodA(a,b:Array[Int,5];c:Int) {
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 386))

    def test_AST88(self):
        input = """
        Class A {
            methodA() {
                Var _: Int=0x12A_F;
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),IntType,StringLit(x.numOfShape))"
        self.assertTrue(TestChecker.test(input, expect, 387))

    def test_AST89(self):
        input = """
        Class Shape {
            $getNumOfShape() {
                a[1][2] = b[3][4] - c[3][4][5];
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test_AST90(self):
        input = """
        Class Program{
            main(){
                Foreach (x In 1+3 .. 8/2 By 3){
                Foreach (i In 1 .. 100 By 2) {
                }
                }
            }
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 389))

    def test_AST91(self):
        input = """
        Class LinkList{
            
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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: length"
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test_AS92(self):
        input = """
        Class Operator
        {
            Var a,sum: Int=0,1;
            main(){
               Foreach( a In 1 .. 100 ){
                    If (sum==2) {Break;}
                    Else {sum = sum+a;}
                }
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 391))

    def test_AST93(self):
        input = """
        Class Integer{
            gcd(a:Int){
            If ((a == 0) || (b == 0)){
            Return a + b;
            }
            }
            }
                  Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 392))

    def test_AST94(self):
        input = """
        Class Integer{
            Var a: Array[Int,5]=Array(2,6,9,7,5);
            findMax(){
           
            Foreach(i In 0 .. 10 By 1){
                If(a[i]<min) {
                    min=a[i];
                }
            }
            Return min;
           }
    }
          Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 393))

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
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,ArrayType(3,StringType)),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 394))

    def test_AST96(self):
        input = """
        Class Shape {
            Var width,length:Array[Array[Int,2],2] = Array(Array(5,6), Array(2*3,4*6)), Array(Array(2,3),Array(a&&b));
            $getNumOfShape() {
                If(width[1][2]*length[12][2]>10)
                {
                    Foreach (x In 5 .. 2) {
                    
                    }
                }
            }
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 395))

    def test_AST97(self):
        input = """
        Class AVL {
            $root(Node: Int; Left: Int;Right:Int){
                Foreach (i In 1 .. 3 By 1) {
                    Left[i]=Left[0];
                }
            }
            }
                  Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 396))

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
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input, expect, 397))

    def test_AST99(self):
        input = """Class SinhVien {
            Var test: Int = (a==b);
            Var test1,test: Int = (3!=2), a>=b;
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Redeclared Attribute: test"
        self.assertTrue(TestChecker.test(input, expect, 398))

    def test_AST100(self):
        input = """
        Class SinhVien:BK {
            Var test: Boolean = !True;
            Var test1: String = "abc";
        }
              Class Program{
            main(){
               
                Var z: Int = "x.numOfShape";
                Var y : Int = x.numOfShape + 1;
            }
        }
        """
        expect = "Undeclared Class: BK"
        self.assertTrue(TestChecker.test(input, expect, 399))
