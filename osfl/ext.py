import re

class System:
    def output(self, text):
        print(text)
    
    def input(self, _):
        input("Press Enter to exit...")

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def tokenize(code):
    tokens = re.findall(r'\bimport\b|\bsystem\b|\bsys\b|\boutput\b|\binput\b|\w+|[();]', code)
    return tokens

def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        if tokens[i] == 'import' and tokens[i + 1] == 'system':
            ast.append(('import_system',))
            i += 3
        elif tokens[i] == 'sys' and tokens[i + 1] == '=' and tokens[i + 2] == 'system' and tokens[i + 3] == '(' and tokens[i + 4] == ')':
            ast.append(('create_system',))
            i += 6
        elif tokens[i] == 'sys' and tokens[i + 1] == '.' and tokens[i + 2] == 'output':
            ast.append(('output', tokens[i + 4]))
            i += 6
        elif tokens[i] == 'sys' and tokens[i + 1] == '.' and tokens[i + 2] == 'input':
            ast.append(('input', tokens[i + 4]))
            i += 6
        else:
            i += 1
    return ast

def evaluate(ast):
    env = {}
    for node in ast:
        if node[0] == 'import_system':
            env['system'] = System
        elif node[0] == 'create_system':
            env['sys'] = System()
        elif node[0] == 'output':
            env['sys'].output(node[1])
        elif node[0] == 'input':
            env['sys'].input(node[1])

def run_file(filename):
    if not filename.endswith('.osfl'):
        raise ValueError("Invalid file type. Expected a .osfl file")
    
    code = read_file(filename)
    tokens = tokenize(code)
    ast = parse(tokens)
    evaluate(ast)

run_file("main.osfl")
