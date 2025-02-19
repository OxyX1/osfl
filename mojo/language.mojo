# Token structure
struct Token:
    var type: Str
    var value: Str

# Lexer function
fn tokenize(source: Str) -> [Token]:
    var tokens = []
    for char in source:
        if char.is_alpha():
            tokens.append(Token(type="IDENTIFIER", value=char))
        elif char == "(":
            tokens.append(Token(type="LPAREN", value=char))
        elif char == ")":
            tokens.append(Token(type="RPAREN", value=char))
    return tokens

# AST Node structure
struct ASTNode:
    var type: Str
    var value: Str
    var children: [ASTNode]

# Parsing function
fn parse(tokens: [Token]) -> ASTNode:
    return ASTNode(type="PROGRAM", value="", children=[])

# Evaluation function
fn evaluate(node: ASTNode):
    print("Evaluating AST Node:", node.type)
