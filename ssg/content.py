from yaml import FullLoader
from yaml import load
import re
from collections.abc import Mapping

class Content(Mapping):
    __delimeter="^(?:-|\+){3}\s*$"
    __regex=re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _,fm,content=__regex.split(string, 2)
        load(fm,"loader"="FullLoader")
        return cls(metadata, content)

    def __init__(self, metadata,content):
        self.data=metadata
        self.data["content"=content]

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if "type" in self.data:
            return self.data["type"]
        else:
            return None

    def settype(self, type):
        self.data["type"]=type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.iter()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data=dict()
        for key, value in self.data.items():
            if key!="content":
                data[key]=value
        return str(data)
