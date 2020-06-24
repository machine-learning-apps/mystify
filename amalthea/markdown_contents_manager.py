from notebook.services.contents.largefilemanager import LargeFileManager


class MarkdownContentsManager(LargeFileManager):
    def save(self, model, path=''):
        self.log.debug("Converting into amalthea markdown")
        # this is where we put model to markdown code
        # maybe we can use pre_save hooks (https://github.com/jupyter/notebook/blob/master/notebook/services/contents/manager.py#L86)
        return super(MarkdownContentsManager, self).save(model, path)

    def get(self, path, content=True, type=None, format=None):
        # This is markdown to model
        return super(MarkdownContentsManager, self).get(path, content, type, format)
