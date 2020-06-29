import json

def to_myst(model):
    pass

def to_model(myst):
    pass

def code_convert(cell):
    # convert to myst markdown here
    """
        % cell
      ---
      cell_type: code
      execution_count: 1
      ---
      ```python
      print("fbddddoo")
      ```

      foo
      % endcell
    """

    pass

def markdown_convert(cell):
    # convert to myst markdown
    """
    % cell
    ---
    cell_type: markdown
    ---
    testtest
    --------

    *test* of markdown2
    % endcell
    """
    pass

def format_metadata():
    # format metadata
    pass
