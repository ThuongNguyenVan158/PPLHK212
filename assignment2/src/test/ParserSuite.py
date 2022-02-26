import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Test program"""
        input = """
        Class ABC { 
            Var $1d : Int = 0;
            ABC(){
                Return d;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        """Test program"""
        input = """class ABC : B{ }"""
        expect = "Error on line 1 col 0: class"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_program3(self):
        """Test program """
        input = '''
        Class A {
            Val x,y : Int;
            Mul(){
                Return Self.x + Self.y;
            }
            main(){
            
            }
        }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_program4(self):
        """Test attbute decalre """
        input = '''
        Class Desk {
            Val length,width: Int = 0,0,0;
            getArea() {
                Return Self.length* Self.width;
                };
            
            Desk(length : Float,width: Float){
            Self.length = length;
            Self.width = width;
            }
        }
            '''
        expect = 'Error on line 3 col 39: ,'
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_program5(self):
        """Test Contructor """
        input = '''
        Class Desk {
            Val length,width: Int = 0,0;
            getArea() {
                Return Self.length* Self.width;
                }
            
            Contructor(length : Int;width: Int){
            Self.length = length;
            Self.width = width;
            }
        }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_program6(self):
        """Test program """
        input = '''
        Class Shape{
           
        }
        Class Triangle : Shape {
            Val $len,$width : Int = 0,0;
            getArea(){
                {
                    
                }
                Return Self.length*Self.width / 2;
            }
        }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_program7(self):
        """Test Program """
        input = '''
        Class A{
            Val str: String = "My name is Thuong";
            $SayHello()
            {
                Return "Nice to meet you" + Self.str ;
            }
        }
        Class B: A {
           main(){
            Val x : A = New A();
            x::$SayHello();
        }}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_program8(self):
        """Test Program """
        input = '''
        Class A{
            Val a, b, c: Int;
            Var x, y, z : Float;
            Var g, h, y : String;
            Test(){}
            Var x, y, z: String;
            Var q, w,e : float = 12.,.12e1,.123E0;
            Val a: Int = 0b01;
        ##Have one comment in here hihi##
        }
        '''
        expect = 'Error on line 9 col 28: 1'
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_program9(self):
        """Test Program """
        input = '''
        Class Example {
            Val arr : Array[Int,1];
            Test(){
               Self.arr[0] = 1;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_program10(self):
        """Test Program """
        input = '''
        Class Example {
            A(){
            Var r,s : Int = 000;
        }
        }
        '''
        expect = 'Error on line 4 col 30: 0'
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_program11(self):
        """Test Program """
        input = '''
        Class Example {
            Test(){
                If (flag== False) {{}}
                Elseif(1) {}
                Elseif((3*2)+1) {}
                Else{{}}
            }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_program12(self):
        """Test Staments Program """
        input = '''
        Class Example {
            Test(){
                Foreach(i In 1+1 .. 100+1) {
                    x=x+x==x;
                }
                }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_program13(self):
        """Test Program """
        input = '''
        Class Myself {
            Val firstName: String = "Nguyen"; 
            Val lastName : String = "Van Thuong";  
            Var age : Int = 20+1;        

            fullname() {

            }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_program14(self):
        """Test Program """
        input = '''
        ## Class Myself {
            Val firstName: String = "Nguyen"; 
            Val lastName : String = "Van Thuong";  
            Var age : Int = 20+1;        

            fullname() {

            }
        }
        };##
        '''
        expect = 'Error on line 12 col 8: <EOF>'
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_program15(self):
        """Test Program """
        input = '''
        Class Myself {
           Class A: Myself{
               
           }
        }
        '''
        expect = 'Error on line 3 col 11: Class'
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_program16(self):
        """Test Program """
        input = '''
        Class Test {
            abc(){
                a.abc();
            }
            abc(){
                abc = abc();
            }
            abc(){
                x=abc()*abc();
            }
        }
        '''
        expect = 'Error on line 7 col 25: ('
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_program17(self):
        """Test must't declare static variable in method """
        input = '''
        Class Test {
            ABC(c: Float){
                Var $s: Int =0;
                S=1;
            }
        }
        '''
        expect = 'Error on line 4 col 20: $s'
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_program18(self):
        """Test Program """
        input = '''
        Class Test {
            main(){}
            Return y;
        }

}
        '''
        expect = 'Error on line 4 col 12: Return'
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_program19(self):
        """Test Program """
        input = '''
        Class Test {
            Testfunc (x: Float)
            {
                Return  x*x*x+x*2 ;
            }
            main()
            {
                Var i : Int = 1;
                Return Testfunc(i);
            }
        }
        '''
        expect = 'Error on line 10 col 31: ('
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_program20(self):
        """Test Program """
        input = '''
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

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_program21(self):
        """Test Program """
        input = '''
        Class Test {
           Var b : Array[Array[Int,1],100];
           Self.b[0][1] = 100;
        }

        '''
        expect = 'Error on line 4 col 11: Self'
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_program22(self):
        """Test Program """
        input = '''
         Class Test {
           Var b : Array[Array[Int,1],100];
           Set(){
           Self.b[0][1] = 100;
           }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_program23(self):
        """Test Program """
        input = '''
        Class Test {
            Val x: Int = y;
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_program24(self):
        """Test Program """
        input = '''
        Class Test {
            Val x: Int = y,z,y;
        }
        '''
        expect = 'Error on line 3 col 26: ,'
        self.assertTrue(TestParser.test(input, expect, 224))
############### invalid ##################

    def test_program25(self):
        """Test Program """
        input = '''
        Class Test {
            Val x,y,z,t: Int = y,z,y;
        }
        '''
        expect = 'Error on line 3 col 36: ;'
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_invalid_program26(self):
        """Test Program """
        input = '''
        Class Test {
            print(x: Int)
            {
                x();
            }
            main()
            {
                Val x: Int= 100+1;
                Foreach( h In 1 .. x+1 by x-1)
                {
                    If(x%2 == 0)
                    {
                        print(x);
                    }
                    else Continue;
                }
            }
        }

        '''
        expect = 'Error on line 5 col 17: ('
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_program27(self):
        """Test Program """
        input = '''
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


        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_program28(self):
        """Test Program """
        input = '''
        '''
        expect = 'Error on line 2 col 8: <EOF>'
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_invalid_program29(self):
        """Test Program """
        input = '''
            Class main(){
                
            }
        '''
        expect = 'Error on line 2 col 22: ('
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_program30(self):
        """Test Program """
        input = '''
        Class Shape{
           
        }
        Class Triangle : Shape {
            Val $len,$width, height : Int = 0,0, exp;
            getArea(){
                {
                    Return Self.length*Self.width* height;
                }
                
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_program31(self):
        """Test Program """
        input = '''
        Class Test {
            main([]: A) {}
        }

        '''
        expect = 'Error on line 3 col 17: ['
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_program32(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                    If abc {a=c;}
                    Else {c=d};
                }
        }

        '''
        expect = 'Error on line 4 col 23: abc'
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_program33(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                    foreach true;
                }
        }

        '''
        expect = 'Error on line 4 col 28: true'
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_program34(self):
        """Test Program """
        input = '''
        Class Test {
           main()
              {
                  Class A{};
              }
        }

        '''
        expect = 'Error on line 5 col 18: Class'
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_program35(self):
        """Test Program """
        input = '''
        Class Test {
            $Var : Int = check() {
                    If (IsaFunc()) Return false;
                    Return peek() == 1;
                }
        }

        '''
        expect = 'Error on line 3 col 17: :'
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_program36(self):
        """Test Program """
        input = '''
         Class Test {
            Val $Var : Int = check() {
                    If (IsaFunc()) Return false;
                    Return peek() == 1;
                }
        }

        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_program37(self):
        """Test Program """
        input = '''
        Class Test {
            Val $Var : Int = check() 
            Void()
            {
                    If (IsaFunc()) Return false;
                    Return peek() == 1;
            }
        }

        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_program38(self):
        """Test Program """
        input = '''
         Class Test {
            Val $Var : Int = check() ;
            Void()
            {
                    If (IsaFunc()) {Return false;}
                    Return peek() == 1;
            }
        }
        }
}

        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_program39(self):
        """Test Program """
        input = '''
         Class Test {
            Val $Var : Int = check() ;
            Void()
            {
                If (IsaFunc()&&a) {Return false;}
                Return peek() == 1;
            }
        }
        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_program40(self):
        """Test Program """
        input = '''
         Class Test {
            Val $Var : Int = check() + 1 ;
            Void()
            {
                If (IsaFunc()==.1) {Return false;}
                Return peek() == 1;
            }
        }

        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_program41(self):
        """Test Program """
        input = '''
       Class Test {
            Val $Var : Int = check()New A();
        }

        '''
        expect = 'Error on line 3 col 34: ('
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_program42(self):
        """Test Program """
        input = '''
        Class Test {
            Val $Var : Int = New A();
            a= $Var+1;
        }


        '''
        expect = 'Error on line 4 col 13: ='
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_program43(self):
        """Test Program """
        input = '''
        Class Test {
            Val $Var : Int = New A();
            Void()
            {
            a= $Var+1;
            }
        }
        '''
        expect = 'Error on line 6 col 15: $Var'
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_program44(self):
        """Test Program """
        input = '''
         Class Test {
            Val $Var : Int = New A();
            Void()
            {
            ##a= $Var+1;##
            Return $Var;
            }
        }

        '''
        expect = 'Error on line 7 col 19: $Var'
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_program45(self):
        """Test Program """
        input = '''
        Class Test {
            Val $Var : Int = New A();
            Void()
            {
            ##a= $Var+1;
            Return $Var;
            }
        }
        '''
        expect = '#'
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_program46(self):
        """Test Program """
        input = '''
        ##Class Test {
            maVarest(){};
        }##

        '''
        expect = 'Error on line 6 col 8: <EOF>'
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_program47(self):
        """Test Program """
        input = '''
        Class Test {
                main(){
                    Var a: Int;
                    a = Continue + 1;
                };
        }

        '''
        expect = 'Error on line 5 col 24: Continue'
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_program48(self):
        """Test Program """
        input = '''
        Class Test {
                main(){
                    a = a + 1;
                }
                main(){
                    a = void + 1;
                }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_program49(self):
        """Test Program """
        input = '''
        Class Test {
            main ()
            {
                a = !(a && b || c);
                e = a / b *c / (10 * c % d) && !(1) || (1) / 2;
                (b)[3] = a && b;
                !(b) = 3;
                b!= a || b;
            }
        }

        '''
        expect = 'Error on line 9 col 26: ;'
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_program50(self):
        """Test Program """
        input = '''
        Class Test {
            main ()
            {
                a = !(a && b || c);
                e = a / b *c / (10 * c % d) && !(1) || (1) / 2;
                (b)[3] = a && b;
                (b) = 3;
                b!= a || b;
            }
        }

        '''
        expect = 'Error on line 9 col 26: ;'
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_program51(self):
        """Test Program """
        input = '''
        Class Test {
            main ()
            {
                Var a : Array[Array[Int,1],1];
                a = [2]b;
            }
        }

        '''
        expect = 'Error on line 6 col 20: ['
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_program52(self):
        """Test Program """
        input = '''
        Class Test {
                {}
        }

        '''
        expect = 'Error on line 3 col 16: {'
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_program53(self):
        """Test Program """
        input = '''
         Class Test {
            main ()
            {
                a = (!(a && b || c) && c + x);
                b!= a || b;
            }
        }
        '''
        expect = 'Error on line 6 col 26: ;'
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_program54(self):
        """Test Program """
        input = '''
        Class Test {
                main(){
                    Self.call("alo");
                }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_program55(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                a.call("alo"};
            }
        }

        '''
        expect = 'Error on line 4 col 28: }'
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_program56(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                a.$call("alo");
            }
        }

        '''
        expect = 'Error on line 4 col 18: $call'
        self.assertTrue(TestParser.test(input, expect, 256))
################# valid ###########

    def test_program57(self):
        """Test Program """
        input = '''
          Class Test {
            main(){
                a::$call("alo");
            }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_program58(self):
        """Test Program """
        input = '''
        Class Test {
            main()
            {
            Var A, B, temp : Test = New A(), New B(), New C(),;

            Other.prVarf("Please enter the 1st number : ");
            Other.scanf("%d",A);
            Other.prVarf("\\nPlease enter the 2nd number : ");
            Other.scanf("%d",B);

            Other.prVarf("\\nBefore swapping:\\n");
            Other.prVarf("A - %d \\nB - %d", A, B);

            temp = A;
            A = B;
            B = temp;

            Other.prVarf("\\nAfter swapping:\\n");
            Other.prVarf("A - %d \\nB - %d", A, B);

            Return 0;
            }

        }

        '''
        expect = 'Error on line 5 col 61: ,'
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_program59(self):
        """Test Program """
        input = '''
        Class Test {
            main()
            {
            Var A, B, temp : Test = New A(), New B(), New C();

            Other.prVarf("Please enter the 1st number : ");
            Other.scanf("%d",A);
            Other.prVarf("\\nPlease enter the 2nd number : ");
            Other.scanf("%d",B);
            Return 0;
            }

        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_program60(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                Elseif(1){}
            }
        }

        '''
        expect = 'Error on line 4 col 16: Elseif'
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_program61(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                a = Other.b() + Other.c() + Other.d();
                Other.prVar(a);
                a = a / Other.sum(a,b) + Other.sub(a,b);
                }

        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_program62(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                Return 1+2;
            }

        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_program63(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                Return a.$X(1);
            }

        }

        '''
        expect = 'Error on line 4 col 25: $X'
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_program64(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                Return "abc"+."cde";
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_program65(self):
        """Test Program """
        input = '''
        Class Test {
            main(){
                Return "abc"+."cde" + a::X(1,1);
            }
        }

        '''
        expect = 'Error on line 4 col 41: X'
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_program66(self):
        """Test Program """
        input = '''
         Class Test {
            main(){
                Return "abc"+."cde" + a::$X(1;1);
            }
        }

        '''
        expect = 'Error on line 4 col 45: ;'
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_program67(self):
        """Test Program """
        input = '''
        Class sinhvien
        {
            Val masinhvien, ten, quequan : Int;
            Var tuoi : Int;
            Var diemtoan, diemly, diemhoa: Int;
            di(){};
            dung(){};
            ngoi(){};
            hoctap(){};
        }

        '''
        expect = 'Error on line 7 col 18: ;'
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_program68(self):
        """Test Program """
        input = '''
        Class CallbackHell
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_program69(self):
        """Test Program """
        input = '''
        Class CallbackHell
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
                Else {Return 1;
                {
                  {
                      x=1;
                  }  
                }
                }
                
            }
        }
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_program70(self):
        """Test Program """
        input = '''
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

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_program71(self):
        """Test Program """
        input = '''
        Class Shape {
            Var length,width : Float;
            Var getArea() {}
            Shape(length,width: Float){
                Self.length = length;
                Self.width = width;
            }
        }
        Class Rectangle :Shape {
            getArea(){
                Return Self.length*Self.width;
            }
        }
        '''
        expect = 'Error on line 4 col 23: ('
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_program72(self):
        """Test Program """
        input = '''
        Class Shape {
            Var length,width;
           getArea() {x::1;}
            Shape(length,width){
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
        expect = 'Error on line 3 col 28: ;'
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_program73(self):
        """Test Program """
        input = '''
        Class Parent {
            Var p: Int = X();
        }
        Class Child : Parent {
            Var c;
        }

        '''
        expect = 'Error on line 3 col 26: ('
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_program74(self):
        """Test Program """
        input = '''
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

        Class Car : Vehicle, FourWheeler
        {
        }

        '''
        expect = 'Error on line 18 col 27: ,'
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_program75(self):
        """Test Program """
        input = '''
        Class Vehicle
        {
            Vehicle()
            {
                io.writeVarLn("Self is a Vehicle");
            }
        }

        Class FourWheeler : Vehicle
        {
            FourWheeler()
            {
                io.writeVarLn("Self is a 4 wheeler Vehicle");
            }
        }

        Class Car : FourWheeler
        {
            Car()
            {
                io.writeVarLn("Self is a car");
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_program76(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return 1+2/3*4;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_program77(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return ((1>=2));
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_program78(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return -1;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_program79(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return -1/-2;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_program80(self):
        """Test Program """
        input = '''
    Class Operator
    {
        main()
        {
            Return -1+-2+1.1+-1.2;
        }
    }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_program81(self):
        """Test Program """
        input = '''
        Class Operator
        {
            Var a=0: Int;
            main
            {
                Foreach() i In 1 .. 100 ){
                    If (i==2) {Break;}
                    Else {a = a++}
                }
            }
        }

        '''
        expect = 'Error on line 4 col 17: ='
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_program82(self):
        """Test Program """
        input = '''
         Class Operator
        {
            Var a: Int;
            main
            {
                Foreach( i In 1 .. 100 ){
                    If (i==2) {Break;}
                    Else {a = a++}
                }
            }
        }
        '''
        expect = 'Error on line 6 col 12: {'
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_program83(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return 1.0e10/1.2e10;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_program84(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                a[(3+x.foo(2))/5*3-25] = a[b[2]] +3*a[4]/3;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_program85(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return (((1+(1))));
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_program86(self):
        """Test Program """
        input = '''
        Class Operator
        {
            $main()
            {
                Return Other.prVar("Self is result").x;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_program87(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return Other.prVar("Self is result").prVar1("Self is result1").prVar2("Self is result2");
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_program88(self):
        """Test Program """
        input = '''
        Class A{
            $1Id(){
                Return 1&&2||1*5;
            }
            Self::$1Id();
        }
        '''
        expect = 'Error on line 6 col 12: Self'
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_program89(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return ;
            }
        }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_program90(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return && ;
            }
        }

        '''
        expect = 'Error on line 6 col 23: &&'
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_program91(self):
        """Test Program """
        input = '''
        Class Operator
        {
            main()
            {
                Return &&2 ;
            }
        }

        '''
        expect = 'Error on line 6 col 23: &&'
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
        Class Operator
        {
            main()
            {
                Return Null;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
        Class Shape {
            Var $length,$width: Int;
            getArea() {}
            Shape(length:Int;width:Int){
                Self.length = "length";
                Self.width = width;
            }
        }
        Class Rectangle : Shape {
            getArea(){
            Return Self.length*Self.width;
            }
        }
        Class Triangle : Shape {
            getArea(){
            Return Self.length*Self.width / 2;
            }
        }
        Class Example2 {
            main(){
            s = New Rectangle(3,4);
            (b.coo().d.ass()).o();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
        Class ID {
            Var total: Int=0;
           Val name: String= Null;
            Contructor(){
                Self.name=Null;
            }
            Contructor(name: String){
                Self.name=name;
                ID.total = ID.total +1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
        Class ID {
            ID(name:String){
                Self.name=name;
                ID.total = ID.total.X() +1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
        Class ID {
            ID(name:String){
                Self.name=name;
                name = New New();
                ID.total = ID.total.X() +1;
            }
        }
        """
        expect = "Error on line 5 col 27: New"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
        Class array {
            element() = { };
        }
        """
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
        Class array {
            main(){
                Return true;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """
        Class array {
            main(){
                Return True&&false;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
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
        Class Example2 {
            main(){
            s = New Rectangle(3,4);
            io.writeVarLn(s.getArea());
            s = New Triangle(3,4);
            io.writeVarLn(s.getArea());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))