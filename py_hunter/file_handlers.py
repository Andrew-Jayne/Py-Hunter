from ast import parse
from pathlib import Path

from py_hunter.code_visitor import HunterNodeVisitor
from py_hunter.constructs import HunterStyleCheck


def analyze_file(
    filepath: Path,
    *,
    disallow_lambda: bool = False,
    disallow_logic_in_match: bool = False,
) -> list[HunterStyleCheck]:
    """Analyze a single Python file for style violations."""
    source = filepath.read_text(encoding="utf-8")
    tree = parse(source, filename=str(filepath))
    ## some kind of try except needs to go here to tell you a file is not valid
    finder = HunterNodeVisitor(
        filename=str(filepath),
        disallow_lambda=disallow_lambda,
        disallow_logic_in_match=disallow_logic_in_match,
    )
    return list(finder.visit(tree))
