'''
init file for json2ast module
'''
from json2ast.node_map import NODE_MAP
from typing import Dict, Any

class UnKnownNodeException(Exception):
    pass

class MissingArgumentException(Exception):
    pass

def resolveArgument(arg: Any):
    if type(arg) == list:
        retlist = []
        for item in arg:
            retlist.append(resolveArgument(item))
        return retlist
    elif type(arg) == dict and "_type" in arg:
        return resolveNode(arg)
    
    return arg

def resolveNode(node: Dict):
    if "_type" not in node:
        return None
    
    node_type = node['_type']

    if node_type not in NODE_MAP:
        raise UnKnownNodeException(f"Unknown node type: {node_type}")

    args = {}

    # Organize necessary args in the proper order
    '''
    for arg in NODE_MAP[node_type]["args"]:
        try:
            args[arg] = node[arg]
        except KeyError:
            args[arg] = None
    '''
    
    # Iterate over arguments and resolve any child nodes that we find
    for arg in node:
        args[arg] = resolveArgument(node[arg])

    # Create node with properly resolved arguments
    return NODE_MAP[node_type]["node"](**args)

def json2ast(data: Dict):
    return resolveNode(data)