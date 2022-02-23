echo "Building Lexer and Parser"

call antlr4 D96.g4 -o antlr_test

echo "Generating Java Class files"

call javac ./antlr_test/*.java -d ./

echo "Drawing Parse Tree"

call grun D96 %1 -f ./test.txt -%2