import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_AST1(self):
        input = """Class Program {
        }"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestChecker.test(input, expect, 300))

    def test_AST2(self):
        input = """Class Program  {
             Var numOfShape : Int = 1;
            A(x,y : Int){}
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(numOfShape),IntType,IntLit(5)))])])"

        self.assertTrue(TestChecker.test(input, expect, 301))

    def test_AST3(self):
        input = """Class main {
             Val $numOfShape : Int = 2;
            Val immuAttribute : Int =3;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Static,ConstDecl(Id($numOfShape),ClassType(Id(A)),None)),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),ClassType(Id(B)),None))])])"
        self.assertTrue(TestChecker.test(input, expect, 302))
    