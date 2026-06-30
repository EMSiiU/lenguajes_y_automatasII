from antlr4 import *
from ExprLexer import ExprLexer

lexer = ExprLexer(InputStream(input("?")))

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)



for token in tokens.tokens:
    print("Texto: ", token.text, " Tipo: ", lexer.symbolicNames[token.type])