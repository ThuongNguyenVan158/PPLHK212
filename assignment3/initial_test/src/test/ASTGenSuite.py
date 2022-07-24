import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_AST5(self):
        input = """Class Rectangle {
        Var x:Int=4[2.3];
    }"""
        expect = "Program([ClassDecl(Id(ABC),Id(DEF),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),FloatType),param(Id(f),FloatType),param(Id(g),FloatType)],Block([VarDecl(Id(b),ClassType(Id(A)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(A)),None),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 304))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   