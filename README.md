## Installation

TODO: publish to pip

`pip install mystify`

### Human readable, diffable and reviewable notebook format

The Myst `ContentManager` provides you with a way to save notebooks in a format that's easier to operate with git.

To do so, first generate the jupyter config file following the directions [here](https://jupyter-notebook.readthedocs.io/en/stable/config.html#config-file-and-command-line-options) - `jupyter notebook --generate-config`

To enable the content manager, then add the following line to your `jupyter_notebook_config.py`

```
c.NotebookApp.contents_manager_class = 'mystify.myst_contents_manager.MystContentsManager'
```

To convert your existing notebooks into `mystify` format use `jupyter nbconvert` tool.

```
jupyter nbconvert --to mystify your_notebook.ipynb
```
