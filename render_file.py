import sys
from myst_parser.main import to_html


infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as inf:
    content = inf.read()

outf = to_html(content)

with open(outfile, "w") as out:
    out.write(outf)
