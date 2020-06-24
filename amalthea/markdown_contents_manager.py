from notebook.services.contents.largefilemanager import LargeFileManager


class MarkdownContentsManager(LargeFileManager):
    def save(self, model, path=''):
        from ipdb import set_trace; set_trace()
        return super(MarkdownContentsManager, self).save(model, path)