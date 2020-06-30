import json
import yaml
import re
from myst_parser.main import default_parser


def to_myst(model):
    pass


def _parse_code_output(cell_section):
    out = {}
    out['output_type'] = cell_section.info.split(" ")[1]
    if out['output_type'] == 'stream':
        out['text'] = cell_section.content.splitlines(True)
        out['name'] = 'stdout'
    return out


def _parse_cell(cell):
    cell_meta = yaml.load(cell[0].content)
    if not "metadata" in cell_meta:
        cell_meta["metadata"] = {}
    for cell_section in cell[1:]:
        if cell_section.info == "{source}":
            cell_meta["source"] = cell_section.content.splitlines(True)
            cell_meta["source"][-1] = cell_meta["source"][-1].strip()
        if cell_section.info.startswith("{output}"):
            out = _parse_code_output(cell_section)
            if 'outputs' not in cell_meta:
                cell_meta['outputs'] = []
            cell_meta['outputs'].append(out)
    return cell_meta


def _split_sections(tokens):
    append_to_cell = None
    for token in tokens:
        if token.type == 'fence' and token.info == '{metadata}':
            # Metadata yaml block
            sections = yaml.load(token.content)
            sections["cells"] = []
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
    return sections

