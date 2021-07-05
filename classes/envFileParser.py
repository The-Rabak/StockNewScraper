import os

class EnvFileParser():

    env_file_dict = dict()
    env_file_path = '.env'

    def __init__(self):
        self.parse_env_file()

    def parse_env_file(self):
        if os.path.isfile(self.env_file_path):
            with open(self.env_file_path) as f:
                while line := f.readline():
                    env_arr = line.split("=")
                    if len(env_arr) == 2:
                        self.env_file_dict[env_arr[0].strip()] = env_arr[1].strip()

    def get_value(self, key):
        return self.env_file_dict.get(key, None)
