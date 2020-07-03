import pytest
import json
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mystify import convert

a = convert.to_myst((Path.cwd() / "examples" / "example_notebook.ipynb").read_text())
