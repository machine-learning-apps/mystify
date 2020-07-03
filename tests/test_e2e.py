import pytest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mystify import convert


def test_convert_nb_to_myst():
    with open("examples/example_notebook.ipynb") as f:
        model = json.load(f)
        temp_nb = convert.to_myst(model)
    with open("examples/example_notebook.mystnb") as f:
        myst_nb = f.read()
    assert temp_nb == myst_nb


def test_convert_myst_to_nb():
    with open("examples/example_notebook.mystnb") as f:
        myst_nb = f.read()
    myst_model = convert.to_model(myst_nb)
    with open("examples/example_notebook.ipynb") as f:
        ipynb_model = json.load(f)
    assert myst_model == ipynb_model
