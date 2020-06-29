## Installation

TODO: publish to pip

`pip install mystify`

### Human readable, diffable and reviewable notebook format

Our `ContentManager` provides you with a way to save notebooks in format that's easier to operate with git.

To enable, add this line to your `jupyter_notebook_config.py`

```
c.NotebookApp.contents_manager_class = 'mystify.markdown_contents_manager.MarkdownContentsManager'
```

To convert your existing notebooks into `mystify` format use `jupyter nbconvert` tool.

```
jupyter nbconvert --to mystify your_notebook.ipynb
```