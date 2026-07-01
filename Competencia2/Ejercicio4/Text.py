from antlr4 import *
from ExprLexer import ExprLexer

entrada = "if edad > 18"

#lexer = ExprLexer(InputStream(input("?")))
lexer = ExprLexer(InputStream(entrada))

tokens = CommonTokenStream(lexer)
tokens.fill()
print(tokens)



for token in tokens.tokens:
    print("Texto: ", token.text, " Tipo: ", lexer.symbolicNames[token.type])