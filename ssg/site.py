import Path from pathlib

class Site:
    def __init__(self, source, dest):
        self.source=Path(source)
        self.dest=Path(dest)

    def create_dir(self, path):
        directory="{0}/{1}".format(self.dest,Path.relative_to(self.source))
        directory.mkdir(parents=True,exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if Path.isdir(path):
                self.create_dir(path)
