"""Reset completed exercise modules while preserving prompts and signatures."""

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXERCISE_FILES = (
    "exercises/python/topic_01_arrays_and_strings/arrays_strings.py",
    "exercises/python/topic_02_hash_maps_and_sets/hash_maps_sets.py",
    "exercises/python/topic_03_two_pointers/two_pointers.py",
    "exercises/python/topic_04_sliding_window/sliding_window.py",
    "exercises/python/checkpoint_01_mixed_foundations/mixed_foundations.py",
)


def reset_function(function):
    """Keep a function's prompt and replace its implementation with a stub."""
    body = []

    if (
        function.body
        and isinstance(function.body[0], ast.Expr)
        and isinstance(function.body[0].value, ast.Constant)
        and isinstance(function.body[0].value.value, str)
    ):
        body.append(function.body[0])

    body.append(ast.Raise(exc=ast.Name(id="NotImplementedError", ctx=ast.Load())))
    function.body = body


def reset_file(relative_path):
    path = ROOT / relative_path
    tree = ast.parse(path.read_text(encoding="utf-8"))

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            reset_function(node)

    ast.fix_missing_locations(tree)
    path.write_text(ast.unparse(tree) + "\n", encoding="utf-8")


def main():
    for relative_path in EXERCISE_FILES:
        reset_file(relative_path)


if __name__ == "__main__":
    main()
