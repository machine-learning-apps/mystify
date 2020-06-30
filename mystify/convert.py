import json
import yaml
import re
from myst_parser.main import default_parser


def to_myst(model):
    pass


def _parse_cell(cell):
    cell_meta = yaml.load(cell[0].content)
    for cell_section in cell[1:]:
        if cell_section.info == "{source}":
            cell_meta["source"] = re.findall("\n", cell_section.content)
        
        from IPython import embed; embed()
    return cell_meta


def _split_sections(tokens):
    sections = {"cells": []}
    append_to_cell = None
    for token in tokens:
        if token.type == 'fence' and token.info == '{metadata}':
            # Metadata yaml block
            sections['metadata'] = yaml.load(token.content)
        if append_to_cell is not None:
            append_to_cell.append(token)
        if token.type == 'myst_line_comment' and token.content == 'cell':
            append_to_cell = []
        if token.type == 'myst_line_comment' and token.content == 'endcell':
            sections['cells'].append(_parse_cell(append_to_cell))
            append_to_cell = None
    return sections


def to_model(myst):
    md = default_parser("docutils")
    tokens = md.parse(myst)
    sections = _split_sections(tokens)

