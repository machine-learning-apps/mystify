# Amalthea

Amalthea (5th moon of Jupyter) is collection of plugins and tools that will improve experience of using Jupyter notebooks with GitHub.

## Installation

TODO: publish to pip

`pip install amalthea`

### Human readable, diffable and reviewable notebook format

Our `ContentManager` provides you with a way to save notebooks in format that's easier to operate with git.

To enable, add this line to your `jupyter_notebook_config.py`

```
c.NotebookApp.contents_manager_class = 'amalthea.markdown_contents_manager.MarkdownContentsManager'
```

To convert your existing notebooks into `amalthea` format use `jupyter nbconvert` tool.

```
jupyter nbconvert --to amalthea your_notebook.ipynb
```
