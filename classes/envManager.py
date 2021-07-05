import os

from classes.envFileParser import EnvFileParser

class EnvManager:
    def __init__(self):
        ...

    def get_from_env(self, key):
        if value := os.environ.get(key):
            return value
        envFileParser = EnvFileParser()
        return envFileParser.get_value(key)