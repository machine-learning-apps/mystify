# pylint: disable=protected-access,missing-function-docstring, missing-class-docstring, missing-module-docstring
# -*- coding: utf-8 -*-
import pytest
import json
from mystify import convert


def test_convert_nb_to_myst(self):
    with open("examples/example_notebook.ipynb") as f:
        model = json.load(f)
        temp_nb = convert.to_myst(model)
    with open("examples/example_notebook.mystnb") as f:
        myst_nb = f.read()
    self.assertEquals(temp_nb, myst_nb)


def test_convert_myst_to_nb(self):
    with open("examples/example_notebook.mystnb") as f:
        myst_nb = f.read()
    myst_model = convert.to_model(myst_nb)
    with open("examples/example_notebook.ipynb") as f:
        ipynb_model = json.load(f)
    self.assertEquals(myst_model, ipynb_model)

