import sys

from pathlib import Path
from quartodoc import get_function, MdRenderer
from griffe.loader import GriffeLoader
from griffe.docstrings.parsers import Parser, parse

# this could also be collected using static analysis
import vetiver

root = Path(sys.argv[0]).parent

renderer = MdRenderer(header_level=1)

p = root / "api"
p.mkdir(exist_ok=True)

for name in ['vetiver.write_app', 'vetiver.VetiverModel', 'vetiver.load_pkgs']:
    griffe = GriffeLoader(docstring_parser=Parser("numpy"))
    mod = griffe.load_module("vetiver")

    f_obj = mod._modules_collection[name]
    p_func = p / f"{name}.md"
    p_func.write_text(renderer.to_md(f_obj))
