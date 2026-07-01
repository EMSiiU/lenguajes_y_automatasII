from antlr4 import *
from ExprLexer import ExprLexer
import sys

#entrada = "edad = 18"
archivo = sys.argv[1] if len(sys.argv) > 1 else "prueba.txt"
input_stream = FileStream(archivo)

#lexer = ExprLexer(InputStream(input("?")))
#lexer = ExprLexer(InputStream(entrada))
lexer = ExprLexer(input_stream)


tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)



for token in tokens.tokens:
    print("Texto: ", token.text, " Tipo: ", lexer.symbolicNames[token.type])