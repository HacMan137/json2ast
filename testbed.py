import ast
from ast2json import ast2json
from json2ast import json2ast

tree = ast.parse(open("test_scripts/test0.py").read())
json_tree = ast2json(tree)

ast_tree = json2ast(json_tree)

c = compile(ast_tree, "unknown", "exec")

exec(c)