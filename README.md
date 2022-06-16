# json2ast
### The JSON to Python AST converter you never knew you needed

<br/>

### Description
This package is meant to work in the opposite direction of the `ast2json` package which takes a Python AST object as input and produces a JSON structure as output. The one function, `json2ast` expects a Python dictionary created by `ast2json` and returns a replication of the AST objects used to create that dictionary.

### Example

```
import ast
from ast2json import ast2json
from json2ast import json2ast

tree = ast.parse(open("test_scripts/test0.py").read())
json_tree = ast2json(tree)

ast_tree = json2ast(json_tree)
```