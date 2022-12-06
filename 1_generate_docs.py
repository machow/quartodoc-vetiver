import sys

from pathlib import Path
from quartodoc import get_object, MdRenderer
from griffe.loader import GriffeLoader
from griffe.docstrings.parsers import Parser, parse

# this could also be collected using static analysis
import vetiver

root = Path(sys.argv[0]).parent

renderer = MdRenderer(header_level=1)

p = root / "api"
p.mkdir(exist_ok=True)

for name in ['write_app', 'compute_metrics']:
    f_obj = get_object("vetiver", name)
    p_func = p / f"{name}.md"
    p_func.write_text(renderer.to_md(f_obj))
