from antlr4 import *
from ExprLexer import ExprLexer
import sys

entrada = "10-4"
archivo = sys.argv[1] if len(sys.argv) > 1 else "prueba.txt"
input_stream = FileStream(archivo)

#lexer = ExprLexer(InputStream(input("?")))
#lexer = ExprLexer(InputStream(entrada))
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)



for token in tokens.tokens:
    tipo = "EOF" if token.type == Token.EOF else lexer.symbolicNames[token.type]
    print("Texto: ", token.text, " Tipo: ", tipo)
