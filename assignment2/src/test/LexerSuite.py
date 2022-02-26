import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_valid_ident1(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
            A $ID _id _id1 k19ID 89_id
                """,
            "A,$ID,_id,_id1,k19ID,89,_id,<EOF>",
            101
        ))

    def test_valid_ident2(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
            $id char_id float_id _ string_id classId
                """,
            "$id,char_id,float_id,_,string_id,classId,<EOF>",
            102
        ))

    def test_valid_ident3(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
            $a$1 ab$c a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
            _ _abc _123 _abc123 _abc_123 _123_abc
            __ ____ ____123____
            abc ABC aBC Abc _ABC __ABc __123ABc
            hdad_adsajdk_hf__T_
                """,

            "$a,$1,ab,$c,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,hdad_adsajdk_hf__T_,<EOF>",
            103
        ))

    def test_valid_ident4(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
            abcfgh ABC aBC __abcd __123
            KK1 __abc___________________d ABC___1 AC90
                """,

            "abcfgh,ABC,aBC,__abcd,__123,KK1,__abc___________________d,ABC___1,AC90,<EOF>",
            104
        ))

    def test_invalid_ident0(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
            _acb_@12
                """,
            "_acb_,Error Token @",
            105
        ))

    def test_invalid_ident1(self):
        """Test Invalid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
            id+1 id&1
                """,
            "id,+,1,id,Error Token &",
            106
        ))

    def test_invalid_ident2(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.test(
            """
            123abc$ 123_ab$
            _123
                """,
            "123,abc,Error Token $",
            107
        ))

    def test_comment0(self):
        """Test Comment"""
        self.assertTrue(TestLexer.test(
            """
            ##  comment 1
            # ,comment##
                """, "<EOF>", 108
        ))

    def test_comment1(self):
        """ Test Comment """
        self.assertTrue(TestLexer.test(
            """
            ## Comment with multiple lines
            #,# Hello comments
                This is block comment
            ##
                """,
            "<EOF>",
            109
        ))

    def test_comment2(self):
        """ Test Comment """
        self.assertTrue(TestLexer.test(
            """
            ## My name is Thuong.
            ** It is easier to do in editors that do not automatically indent the second
            ** through last lines of the comment one space from the first.
            ** It is also used in Holub's book, in rule 31.
            *//#/## 123
            ##
                """,
            "123,Error Token #",
            110
        ))

    def test_block_comment3(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
            #####***************************
                Test ##
            \***************************/
                """,

            "Error Token #",
            111
        ))

    def test_comment4(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is a line comment
            /* Comment with multiple lines
                Hello comments
            */####
            /*
                Comment multiple lines
            */
            /* nest comments
                # inline comment
            # inline comment
            */
            ##
                """,
            "<EOF>",
            112
        ))

    def test_comment5(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## This is the style #recommended by Holub for C and C++.
            * It is demonstrated in ''Enough Rope'', in rule 29.
            */
            # This is inline comment
            #
            /**/
            /*                          */
            ## This is comment
                """,

            "This,is,comment,<EOF>",
            113
        ))

    def test_comment6(self):
        """ Test Comment """
        self.assertTrue(TestLexer.test(
            """
            ## // /b/r/n */ */##
            /*/**/ */
            # This is ##comment
                """,

            "/,*,/,*,*,/,*,/,Error Token #",
            114
        ))

    def test_comment7(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
            ## ####  This is a line comment so /* has no meaning here##
                """,
            "<EOF>",
            115
        ))

    def test_comment8(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            # inline comment \b \t
                is multiple lines
            # inline comment
            """,

            "Error Token #",
            116
        ))

    def test_comment9(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            ##!/usr/bin/env python3
            /# -*- coding: UTF-8 -*-
                """,

            "Error Token #",
            117
        ))

    def test_comment10(self):
        """ Test Comments """
        self.assertTrue(TestLexer.test(
            """
            ####?##
                """,

            "Error Token ?",
            118
        ))

    def test_valid_int_lit0(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
            0b1001_10123 0xA123.e101
                """,

            "0b1001101,23,0xA123,.e101,<EOF>",
            119
        ))

    def test_valid_int_lit1(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
            0 1 2 3 4 123 123456789 00001 0x1230x12010b01
                """,

            "0,1,2,3,4,123,123456789,00,00,1,0x1230,x12010b01,<EOF>",
            120
        ))

    def test_valid_int_lit2(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
            0x00013210x1A 00000031231 000312312 
            00312 0 123 132 012 1 2 3 8912
            0000000000000000000000000000000001 12218 0b10
            09132 321 00000000000000000000000000000000000000000001
                """,

            "0x0,00,13210,x1A,00,00,00,31231,00,0312312,00,312,0,123,132,012,1,2,3,8912,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,01,12218,0b10,0,9132,321,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,01,<EOF>",
            121
        ))

    def test_invalid_int_lit2(self):
        """ Test Invalid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
            0x00 0X89ABC 0xffffff
            0xABC 0X2132
            0B2
                """,
            "0x0,0,0X89ABC,0,xffffff,0xABC,0X2132,0,B2,<EOF>",
            122
        ))

    def test_bool_lit(self):
        """ Test Boolean Literal """
        self.assertTrue(TestLexer.test(
            """
            True and False
                """,
            "True,and,False,<EOF>",
            123
        ))

    def test_invalid_bool_lit(self):
        """ Test Invalid Boolean Literal """
        self.assertTrue(TestLexer.test(
            """
            TRUE True TRue TRUe falSe
            falSE FAlse FAlsE
            truE False FAlSE
                """,
            "TRUE,True,TRue,TRUe,falSe,falSE,FAlse,FAlsE,truE,False,FAlSE,<EOF>",
            124
        ))

    def test_float_lit1(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.test(
            """
            9.0 .e 12e8 1. 0.33E-3 128e+42
                """,

            "9.0,.,e,12e8,1.,0.33E-3,128e+42,<EOF>",
            125
        ))

    def test_float_lit2(self):
        """ Test Float  """
        self.assertTrue(TestLexer.test(
            """
            00001.1101010101000
            0e-432
            000000001e-542400
            000313121.e00031321132
                """,

            "00,00,1.1101010101000,0e-432,00,00,00,00,1e-542400,00,0313121,.e00031321132,<EOF>",
            126
        ))

    def test_invalid_float_lit1(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.test(
            """
            1e 123e e123 e-132 -e123 123e1
            1.e3 .e10
                """,

            "1,e,123,e,e123,e,-,132,-,e123,123e1,1.e3,.e10,<EOF>",
            127
        ))

    def test_string_lit1(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.test(
            """
            ""
            "String"
            " n"
            "?'""
            "-"
            "//"
            "Mulitiple Characters"
                """,

            """,String, n,?'",-,//,Mulitiple Characters,<EOF>""",
            128
        ))

    def test_invalid_string1(self):
        """ Test Invalid String Literal """
        self.assertTrue(TestLexer.test(
            """
            ""
            "string"
            'string'
            "string'
            'string"
            """,

            """,string,Error Token '""",
            129
        ))

    def test_mix_lit(self):
        """ Test Mix Literal """
        self.assertTrue(TestLexer.test(
            """
            ""
            12 32.43 43.E12 4e-1 true "False" "'"false "012" 1.32 1.
            "String"
            """,

            """,12,32.43,43.E12,4e-1,true,False,'"false ,012,Unclosed String:  1.32 1.""",
            130
        ))

    def test_unclose_string0(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            """
            " This is my code
            """,
            "Unclosed String:  This is my code",
            131
        ))

    def test_unclosestring_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
            "line1
                line2
            "
                """,

            """Unclosed String: line1""",
            132
        ))

    def test_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
            "\"abc
                """,

            ",abc,<EOF>",
            133
        ))

    def test_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
            string = "string          '
            "a = 4   +5
            g = 9"
                """,

            """string,=,Illegal Escape In String: string          '
""",
            134
        ))

    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
            " abc \n xyz "
            " abc \n\t xyz "
            """,

            r" abc \n xyz , abc \n\t xyz ,<EOF>",
            135
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
            " hello lexer \t \b \n \'"     asdf
            """,

            r" hello lexer \t \b \n \',asdf,<EOF>",
            136
        ))

    def test_escape3(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
            "Backspace  \b"
            "Formfeed   \f"
            "Return     \r"
            "Newline    \n"
            "Tab        \t"
            "Double quote       \""
            "Backslash  \\ "
                """,

            r"""Backspace  \b,Formfeed   \f,Return     \r,Newline    \n,Tab        \t,Illegal Escape In String: Double quote       \"""",

            137
        ))

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r""" Illegal"\a" """,

            r"""Illegal,Illegal Escape In String: \a""",
            138
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
        r"""
            " Hi Hi \c \d "
        """,

            r"""Illegal Escape In String:  Hi Hi \c""",
            139
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
            " Hi Hi \\f \s\d\\f "
                """,

    r"""Illegal Escape In String:  Hi Hi \\f \s""",
            140
        ))

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
            "abc - xyz"
            "abc \ xyz"
                """,

            """abc - xyz,Illegal Escape In String: abc \ """,
            141
        ))

    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
            "abc - xyz"
            "abc \\\fyyz"
                """,

            r"""abc - xyz,abc \\\fyyz,<EOF>""",
            142
        ))

    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
            "abc\mabc"
                """,

            """Illegal Escape In String: abc\m""",
            143
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            r"""
            "\a"
                """,

            r"""Illegal Escape In String: \a""",
            144
        ))

    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            r"""
            "2.dadhsdas743242#$@$^hjsshx\\o\r"
                """,

            r"""2.dadhsdas743242#$@$^hjsshx\\o\r,<EOF>""",
            145
        ))

    def test_illegal9(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
            "&*&(^(\#!\4))"
                """,
            "Illegal Escape In String: &*&(^(\#", 
            146
        ))

    def test_94_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            r"""
            " abc \.  xyz "
            """,

        r"""Illegal Escape In String:  abc \.""",
            147
        ))

    def test_95_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            r""" "abc\fabc" """,
            r"""abc\fabc,<EOF>""", 148))

    def test_96_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
        " abc \n  xyz "
    """,

            """Unclosed String:  abc """,
            149
        ))

    def test_97_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            r"""
        " abc \t  xyz "
    """,

        r""" abc \t  xyz ,<EOF>""",
            150
        ))

    def test_err_tok1(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
    !== != & ^ % $ # ... \
                """,

            r"!=,=,!=,Error Token &",
            151
        ))

    def test_err_tok2(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    a = a ~ 1
                """,

            "a,=,a,Error Token ~",
            152
        ))

    def test_err_tok3(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    'a = 5
                """,

            "Error Token '",
            153
        ))

    def test_err_tok4(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
            abc?
                """,

            "abc,Error Token ?",
            154
        ))

    def test_err_tok5(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "aAajskjkwscsVN hgSVnxx%##a##dajkj",
            "aAajskjkwscsVN,hgSVnxx,%,dajkj,<EOF>",
            155
        ))

    def test_err_tok6(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "*(*)()_+_+)((..)$)",
            "*,(,*,),(,),_,+,_,+,),(,(,..,),Error Token $",
            156
        ))

    def test_err_tok7(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "hakasjdklsajdkla*()*)%!++(+)|*()",
            "hakasjdklsajdkla,*,(,),*,),%,!,+,+,(,+,),Error Token |",
            157
        ))

    def test_err_tok8(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            " ;,[](){}%+-=====*/@asnakncslka&*))(_h",
            ";,,,[,],(,),{,},%,+,-,==,==,=,*,/,Error Token @",
            158
        ))

    def test_keyword(self):
        """ Test Keyword """
        self.assertTrue(TestLexer.test(
            """
            .:.<+..$.a
                """,
            ".,:,.,<,+.,.,Error Token $",
            159
        ))

    def test_invalid_keyword(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.test(
            "BOOLEAN int 1.12INTEGER sTRIng not 12and",
            "BOOLEAN,int,1.12,INTEGER,sTRIng,not,12,and,<EOF>",
            160
        ))

    def test_invalid_keyword2(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.test(
            "BOOLean Int INTeger STRING whiLE If foR Float Void VOID Break BREAK CONtinue CONTINUE True TRUE FALSE",
            "BOOLean,Int,INTeger,STRING,whiLE,If,foR,Float,Void,VOID,Break,BREAK,CONtinue,CONTINUE,True,TRUE,FALSE,<EOF>",
            161
        ))

    def test_operator(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
        r"""
            + - * /  % != == < > <= >= || && ! :: New
            """,

            "+,-,*,/,%,!=,==,<,>,<=,>=,||,&&,!,::,New,<EOF>",
            162
        ))

    def test_invalid_operator2(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            """
            *= /= %=
                """,

            "*,=,/,=,%,=,<EOF>",
            163
        ))

    def test_invalid_operator(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            """
            ++ -- += -= & ^ |
                """,

            "+,+,-,-,+,=,-,=,Error Token &",
            164
        ))

    def test_invalid_operator3(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            " !xyz 45**4290=12 a<>b+2^3 c-=d) x=y",
            "!,xyz,45,*,*,4290,=,12,a,<,>,b,+,2,Error Token ^",
            165
        ))

    def test_invalid_operator4(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "   income+=salary.12*12+month/3",
            "income,+,=,salary,.,12,*,12,+,month,/,3,<EOF>",
            166
        ))

    def test_invalid_operator5(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "   x = (4 + 3i)(2 + 5i)?i^2",
            "x,=,(,4,+,3,i,),(,2,+,5,i,),Error Token ?",
            167
        ))

    def test_invalid_operator6(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "cost = sum((y - h(i))**2)",
            "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>",
            168
        ))

    def test_case_sensitive_keyword(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.test(
            "truE TRUE tRUe",
            "truE,TRUE,tRUe,<EOF>",
            169
        ))

    def test_case_sensitive_keyword2(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.test(
            "false FALse FOR FOr If iF While WHILE contiNue CONTInue Break break",
            "false,FALse,FOR,FOr,If,iF,While,WHILE,contiNue,CONTInue,Break,break,<EOF>",
            170
        ))

    def test_unclose_string(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "38n\"[#Ffs?0ED\"0.\"T`#!7n",
            """38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n""",
            171
        ))

    def test_unclose_string2(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            r"""
            "{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1"
            """,
            r"""Illegal Escape In String: {SRs}\"""",
            172
        ))

    def test_unclose_string3(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            r"""
            "\"o|F&)LqX\"+>X+\"#Fft"
            """,
            r"""Illegal Escape In String: \"""",
            173
        ))

    def test_unclose_string4(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "a+11.2+\"mam.123\" 12 \"%^&",
            """a,+,11.2,+,mam.123,12,Unclosed String: %^&""",
            174
        ))

    def test_operator2(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            "not<>=and>=mod<=-and!=or&&^^",
            "not,<,>=,and,>=,mod,<=,-,and,!=,or,&&,Error Token ^",
            175
        ))

    def test_operator3(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            "+-*/%*()/*//$#",
            "+,-,*,/,%,*,(,),/,*,/,/,Error Token $",
            176
        ))

    def test_operator4(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            """
                a + b = c
                a * b = c ** 2
                a / 2 = 5
                a % 2 = 6
                a # 2 = 0.6
                a && a == 1
                """,
            "a,+,b,=,c,a,*,b,=,c,*,*,2,a,/,2,=,5,a,%,2,=,6,a,Error Token #",
            177
        ))

    def test_random1(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                # \f abc
                /* // */ acc
                a++;
                string a = "a";
                """,
            """Error Token #""",
            178
        ))

    def test_random2(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                for (int a ; b = 2 && c = 2; 2**2)
                break
                """,
            "for,(,int,a,;,b,=,2,&&,c,=,2,;,2,*,*,2,),break,<EOF>",
            179
        ))

    def test_random3(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                int a,b       ,c ,a                   b;
                float a = b (abc).12;
                str abc[] = {1,2,3};
                """,
            "int,a,,,b,,,c,,,a,b,;,float,a,=,b,(,abc,),.,12,;,str,abc,[,],=,{,1,,,2,,,3,},;,<EOF>",
            180
        ))

    def test_full11(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("$no idea", "$no,idea,<EOF>", 181))

    def test_random5(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                INT abc = 12;
                abc = "";
                float = 2.e2
                char = ''
                """,
            """INT,abc,=,12,;,abc,=,,;,float,=,2.e2,char,=,Error Token '""",
            182
        ))

    def test_random6(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            r"""
                "t \{abcd}\\x efg"
                """,
            r"""Illegal Escape In String: t \{""",
            183
        ))

    def test_random7(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
            ## ],],* ae0bc not mod,return,,
            {} < + Qefbe and ; of o366c false array else < > and for J4981 & <> return = for if ..
            (* of break h80bb,or,bfa18 ) W6bd3,float##,<*)
                """,
            ",,<,*,),<EOF>",
            184
        ))

    def test_random8(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
            ## and,<=,return v415f ( division,and,or
            + , or b328b = <= ) G39be ? else break / * = [ Qd057 ] float[] break * >= do >
            (##*## end , b60f1,>=,dd28e , dd3ab,string,of*)
                """,
            "*,Error Token #",
            185
        ))

    def test_random9(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
            ">=<=for of8ae ##*## :=then>="
            ##- + false P4366 ; * , l84bc , > : flaot true [ / while Va93a boolean and integer function - , false
            (* new , Wbffd,),y6349 else w7e53,(,)*##)#
                """,
            ">=<=for of8ae ##*## :=then>=,),Error Token #",
            186
        ))

    def test_random10(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
            ## [,<>,( k6301 with begin,],true
            + - integer N0699 + > then L09e7 >= float > >= , ] <> * eb142 > integer / while boolean procedure false
            (* false for Z2262,do,G9a7c## continue e46e2,+,break*)
                """,
            "continue,e46e2,,,+,,,break,*,),<EOF>",
            187
        ))

    def test_random11(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """ " """"" " " " a""",
            """Unclosed String:    a""",
            188
        ))

    def test_random12(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
        if (flag) {
            a=1;
        else
            a=2;
                """,
            "if,(,flag,),{,a,=,1,;,else,a,=,2,;,<EOF>",

            189
        ))

    def test_complex_program1(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            Float a, b, c;
            Boolean x, y, z;
                ##
                    =======================================
                    Comment here
                    =======================================
                ##
            """,

            """Float,a,,,b,,,c,;,Boolean,x,,,y,,,z,;,<EOF>""",
            190
        ))

    def test_complex_program2(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            class Example1 {
                ##.##
            }
            }
                """,

            "class,Example1,{,},},<EOF>",
            191
        ))

    def test_complex_program3(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            class Shape {
            var $length,$width: Int;
            getArea() {}
            Shape(length::Int,width::Int){
            Self.length = length;
            Self.width = width;
            }
            }
                """,

            "class,Shape,{,var,$length,,,$width,:,Int,;,getArea,(,),{,},Shape,(,length,::,Int,,,width,::,Int,),{,Self,.,length,=,length,;,Self,.,width,=,width,;,},},<EOF>",
            192
        ))

    def test_complex_program4(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            class Rectangle : Shape {
            float getArea(){
            return length*width;
            }
            }
                """,

            "class,Rectangle,:,Shape,{,float,getArea,(,),{,return,length,*,width,;,},},<EOF>",
            193
        ))

    def test_complex_program5(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            class Triangle extends Shape {
            float getArea(){
            ;
            }
            }
                """,

            "class,Triangle,extends,Shape,{,float,getArea,(,),{,;,},},<EOF>",
            194
        ))

    def test_complex_program6(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
            class Example2 {
            main(){
                
            }
            }
            class Example3 : Example2
            {
                
            }
                """,

            "class,Example2,{,main,(,),{,},},class,Example3,:,Example2,{,},<EOF>",
            195
        ))

    def test_complex_program7(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """$class X{
                }""",
            """$class,X,{,},<EOF>""",
            196
        ))

    def test_070(self):
        input = r"""Var a: String ="Hello world \t Hello World " """
        expect = r"""Var,a,:,String,=,Hello world \t Hello World ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_str10(self):
        self.assertTrue(TestLexer.test(r""" "String with newline\nafter newline" """,
                        r"""String with newline\nafter newline,<EOF>""", 198))

    def test_string(self):
        input = r"""a:="Hello world1 \b Hello World1 " """
        expect = r"""a,:,=,Hello world1 \b Hello World1 ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_prog8(self):
        """a full program"""
        input = """class A{x(){ ; }}
        class B : A{void x(){##mt##}}"""
        expect = "class,A,{,x,(,),{,;,},},class,B,:,A,{,void,x,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))