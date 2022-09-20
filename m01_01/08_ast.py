import ast


with open('code_exm.py') as f:
    code = f.read()
    print(code)
    tree = ast.parse(code)
    print(tree)
    dump_tree = ast.dump(tree)
    print(dump_tree)
    res = compile(tree, '<stdin>', mode='exec')
    print(res)
    exec(res)
