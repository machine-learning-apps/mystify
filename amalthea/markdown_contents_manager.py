from notebook.services.contents.largefilemanager import LargeFileManager


class MarkdownContentsManager(LargeFileManager):
    def save(self, model, path=''):
        # this is where we put formatting code
        return super(MarkdownContentsManager, self).save(model, path)