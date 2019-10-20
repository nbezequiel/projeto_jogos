import os
import json

class PropertiesReader():

    @classmethod
    def get_paths(cls):
        folder = "../properties/"
        cls._paths = [os.path.join(folder, file_path) for file_path in os.listdir(folder)]
        return cls._paths
    
    @classmethod
    def get_files(cls):
        cls._paths = cls.get_paths()
        cls._files = {file.replace(".json","").replace("../properties/",""): open(file, "r+") for file in cls._paths}
        return cls._files

    @classmethod
    def cast_files_to_json(cls):
        cls._files = cls.get_files()
        cls._files_as_json = {}
        cls._files_as_json =  {name:json.load(file) for name,file in cls._files.items()}
       
        return cls._files_as_json

    def __init__(self):
        self._files = self.cast_files_to_json()



