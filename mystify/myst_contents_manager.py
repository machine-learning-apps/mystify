import yaml
from jinja2 import Template
from notebook.services.contents.largefilemanager import LargeFileManager


NOTEBOOK_TPL = """
<!--
amalthea:
  type: notebook
  metadata:
{{ notebook_metadata | indent(4) }}
-->
{% for cell in cells %}
<!--
cell:
  type: {{ cell.cell_type }}
  execution_count: 1
-->

{% if cell.cell_type == 'code' %}
```
{{ cell.source }}
```
{% for out in cell.outputs %}
{% if out.output_type == 'stream' %}
{{ out.text }}
{% elif out.output_type == 'display_data' %}
<img src="data:image/png;base64,{{out.data['image/png']}}">
{% endif %}
{% endfor %}

{% elif cell.cell_type == 'markdown' %}
{{ cell.source }}
{% endif %}
{% endfor %}
"""


class MystContentsManager(LargeFileManager):
    def save(self, model, path=''):
        # maybe we can use pre_save hooks (https://github.com/jupyter/notebook/blob/master/notebook/services/contents/manager.py#L86)
        self.log.debug("Converting into Myst markdown")
        return super(MystContentsManager, self).save(model, path)

    def get(self, path, content=True, type=None, format=None):
        # This is markdown to model
        self.log.debug("Opening Myst markdown")
        return super(MystContentsManager, self).get(path, content, type, format)
