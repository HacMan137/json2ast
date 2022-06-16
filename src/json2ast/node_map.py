import ast
NODE_MAP = {
    "Constant": {
        "node": ast.Constant,
        "args": ["value"]
    },
    "FormattedValue": {
        "node": ast.FormattedValue,
        "args": ["value, conversion, format_spec"]
    },
    "JointedStr": {
        "node": ast.JoinedStr,
        "args": ["values"]
    },
    "List": {
        "node": ast.List,
        "args": ["elts, ctx"]
    },
    "Tuple": {
        "node": ast.Tuple,
        "args": ["elts", "ctx"]
    },
    "Set": {
        "node": ast.Set,
        "args": ["elts"]
    },
    "Dict": {
        "node": ast.Dict,
        "args": ["keys", "values"]
    },
    "Name": {
        "node": ast.Name,
        "args": ["id", "ctx"]
    },
    "Load": {
        "node": ast.Load,
        "args": []
    },
    "Store": {
        "node": ast.Store,
        "args": []
    },
    "Del": {
        "node": ast.Del,
        "args": []
    },
    "Starred": {
        "node": ast.Starred,
        "args": ['value, ctx']
    },
    "Expr": {
        "node": ast.Expr,
        "args": ["value"]
    },
    "UnaryOp": {
        "node": ast.UnaryOp,
        "args": ["op, operand"]
    },
    "UAdd": {
        "node": ast.UAdd,
        "args": []
    },
    "USub": {
        "node": ast.USub,
        "args": []
    },
    "Not": {
        "node": ast.Not,
        "args": []
    },
    "Invert": {
        "node": ast.Invert,
        "args": []
    },
    "BinOp": {
        "node": ast.BinOp,
        "args": ["left", "op", "right"]
    },
    "Add": {
        "node": ast.Add,
        "args": []
    },
    "Sub": {
        "node": ast.Sub,
        "args": []
    },
    "Mult": {
        "node": ast.Mult,
        "args": []
    },
    "Div": {
        "node": ast.Div,
        "args": []
    },
    "FloorDiv": {
        "node": ast.FloorDiv,
        "args": []
    },
    "Mod": {
        "node": ast.Mod,
        "args": []
    },
    "Pow": {
        "node": ast.Pow,
        "args": []
    },
    "LShift": {
        "node": ast.LShift,
        "args": []
    },
    "RShift": {
        "node": ast.RShift,
        "args": []
    },
    "BitOr": {
        "node": ast.BitOr,
        "args": []
    },
    "BitXor": {
        "node": ast.BitXor,
        "args": []
    },
    "BitAnd": {
        "node": ast.BitAnd,
        "args": []
    },
    "MatMult": {
        "node": ast.MatMult,
        "args": []
    },
    "BoolOp": {
        "node": ast.BoolOp,
        "args": ["op, values"]
    },
    "And": {
        "node": ast.And,
        "args": []
    },
    "Or": {
        "node": ast.Or,
        "args": []
    },
    "Compare": {
        "node": ast.Compare,
        "args": ["left", "ops", "comparators"]
    },
    "Eq": {
        "node": ast.Eq,
        "args": []
    },
    "NotEq": {
        "node": ast.NotEq,
        "args": []
    },
    "Lt": {
        "node": ast.Lt,
        "args": []
    },
    "LtE": {
        "node": ast.LtE,
        "args": [],
    },
    "Gt": {
        "node": ast.Gt,
        "args": [],
    },
    "GtE": {
        "node": ast.GtE,
        "args": [],
    },
    "Is": {
        "node": ast.Is,
        "args": [],
    },
    "IsNot": {
        "node": ast.IsNot,
        "args": [],
    },
    "In": {
        "node": ast.In,
        "args": [],
    },
    "NotIn": {
        "node": ast.NotIn,
        "args": [],
    },
    "Call": {
        "node": ast.Call,
        "args": ["func", "args", "keywords", "starargs", "kwargs"]
    },
    "keyword": {
        "node": ast.keyword,
        "args": ["arg", "value"]
    },
    "IfExp": {
        "node": ast.IfExp,
        "args": ["test", "body", "orelse"]
    },
    "Attribute": {
        "node": ast.Attribute,
        "args": ["value", "attr", "ctx"]
    },
    "NamedExpr": {
        "node": ast.NamedExpr,
        "args": ["target", "value"]
    },
    "Subscript": {
        "node": ast.Subscript,
        "args": ["value", "slice", "ctx"]
    },
    "Slice": {
        "node": ast.Slice,
        "args": ["lower", "upper", "step"]
    },
    "ListComp": {
        "node": ast.ListComp,
        "args": ["elt", "generators"]
    },
    "SetComp": {
        "node": ast.SetComp,
        "args": ["elt", "generators"]
    },
    "GeneratorExp": {
        "node": ast.GeneratorExp,
        "args": ["elt", "generators"]
    },
    "DictComp": {
        "node": ast.DictComp,
        "args": ["key", "value", "generators"]
    },
    "comprehension": {
        "node": ast.comprehension,
        "args": ["target", "iter", "ifs", "is_async"]
    },
    "Assign": {
        "node": ast.Assign,
        "args": ["targets", "value", "type_comment"]
    },
    "AnnAssign": {
        "node": ast.AnnAssign,
        "args": ["target", "annotation", "value", "simple"]
    },
    "AugAssign": {
        "node": ast.AugAssign,
        "args": ["target", "op", "value"]
    },
    "Raise": {
        "node": ast.Raise,
        "args": ["exc", "cause"]
    },
    "Assert": {
        "node": ast.Assert,
        "args": ["test", "msg"]
    },
    "Delete": {
        "node": ast.Delete,
        "args": ["targets"]
    },
    "Pass": {
        "node": ast.Pass,
        "args": []
    },
    "Import": {
        "node": ast.Import,
        "args": ["names"],
    },
    "ImportFrom": {
        "node": ast.ImportFrom,
        "args": ["module", "names", "level"]
    },
    "alias": {
        "node": ast.alias,
        "args": ["name", "asname"]
    },
    "If": {
        "node": ast.If,
        "args": ["test", "body", "orelse"]
    },
    "For": {
        "node": ast.For,
        "args": ["target", "iter", "body", "orelse", "type_comment"]
    },
    "While": {
        "node": ast.While,
        "args": ["test", "body", "orelse"]
    },
    "Break": {
        "node": ast.Break,
        "args": []
    },
    "Continue": {
        "node": ast.Continue,
        "args": []
    },
    "Try": {
        "node": ast.Try,
        "args": ["body", "handlers", "orelse", "finalbody"]
    },
    "ExceptHandler": {
        "node": ast.ExceptHandler,
        "args": ["type", "name", "body"]
    },
    "With": {
        "node": ast.With,
        "args": ["items", "body", "type_comment"]
    },
    "withitem": {
        "node": ast.withitem,
        "args": ["context_expr", "optional_vars"]
    },
    "Match": {
        "node": ast.Match,
        "args": ["subject", "cases"]
    },
    "match_case": {
        "node": ast.match_case,
        "args": ["pattern", "guard", "body"]
    },
    "MatchValue": {
        "node": ast.MatchValue,
        "args": ["value"]
    },
    "MatchSingleton": {
        "node": ast.MatchSingleton,
        "args": ["value"]
    },
    "MatchSequence": {
        "node": ast.MatchSequence,
        "args": ["patterns"],
    },
    "MatchStar": {
        "node": ast.MatchStar,
        "args": ["name"],
    },
    "MatchMapping": {
        "node": ast.MatchMapping,
        "args": ["keys", "patterns", "rest"]
    },
    "MatchClass": {
        "node": ast.MatchClass,
        "args": ["cls", "patterns", "kwd_attrs", "kwd_patterns"]
    },
    "MatchAs": {
        "node": ast.MatchAs,
        "args": ["pattern", "name"]
    },
    "MatchOr": {
        "node": ast.MatchOr,
        "args": ["patterns"]
    },
    "FunctionDef": {
        "node": ast.FunctionDef,
        "args": ["name", "args", "body", "decorator_list", "returns", "type_comment"]
    },
    "Lambda": {
        "node": ast.Lambda,
        "args": ["args", "body"]
    },
    "arguments": {
        "node": ast.arguments,
        "args": ["posonlyargs", "args", "vararg", "kwonlyargs", "kw_defaults", "kwarg", "defaults"]
    },
    "arg": {
        "node": ast.arg,
        "args": ["arg", "annotation", "type_comment"]
    },
    "Return": {
        "node": ast.Return,
        "args": ["value"]
    },
    "Yield": {
        "node": ast.Yield,
        "args": ["value"]
    },
    "YieldFrom": {
        "node": ast.YieldFrom,
        "args": ["value"]
    },
    "Global": {
        "node": ast.Global,
        "args": ["names"]
    },
    "Nonlocal": {
        "node": ast.Nonlocal,
        "args": ["names"]
    },
    "ClassDef": {
        "node": ast.ClassDef,
        "args": ["name", "bases", "keywords", "starargs", "kwargs", "body", "decorator_list"]
    },
    "AsyncFunctionDef": {
        "node": ast.AsyncFunctionDef,
        "args": ["name", "args", "body", "decorator_list", "returns", "type_comment"]
    },
    "AsyncFor": {
        "node": ast.AsyncFor,
        "args": ["target", "iter", "body", "orelse", "type_comment"]
    },
    "AsyncWith": {
        "node": ast.AsyncWith,
        "args": ["items", "body", "type_comment"]
    },
    # Top Level Nodes
    "Module": {
        "node": ast.Module,
        "args": ["body"]
    },
    "Expression": {
        "node": ast.Expression,
        "args": ["body"]
    },
}