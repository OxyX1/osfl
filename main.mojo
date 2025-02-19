import mojo.combined  # Import the single combined file

fn main():
    print("Running Mojo Language")
    
    # Example usage of lexer and AST
    var tokens = mojo.combined.tokenize("print('Hello, world!')")
    var ast = mojo.combined.parse(tokens)
    mojo.combined.evaluate(ast)

main()
