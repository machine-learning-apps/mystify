#!/bin/sh
pipenv shell
pipenv install
pipenv lock -r > requirement.txt
git add .
git commit -a -m 'updating requirements before building package'
git push
python3 -m pip install --upgrade setuptools wheel
rm -rf dist/
python3 setup.py sdist bdist_wheel
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*