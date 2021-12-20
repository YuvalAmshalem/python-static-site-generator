from pathlib import Path
from typing import List
import shutil

class Parser:
    def __init__(self):
        extensions=list[str]

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source:Path, dest:Path):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path= self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path,dest / path.relative_to(source))

class ResourceParser(Parser):
    extensions=['.jpg','.png','.gif','.html']

    def parse(self, path: Path, source:Path, dest:Path):
        super().copy(path,source,dest)
