import yaml
import os
import glob
import re


class YamlLoader(object):
    """
      you defined any yaml file in directory
      this class load all yaml file and use for Variant(string or number(integer)) in python grammer
      ## argument
      - dir_name => parent directory you put yaml file
      - extension => target extension(default = yml)
      - dir_symbol => decided to symbol for serach path
    """
    def __init__(self, dir_name, extension='.yml', dir_symbol=':'):
        """initializer setting"""
        self.is_exist_dir = True
        if os.path.exists(dir_name) == False:
            self.is_exist_dir = False
        self.extension = extension
        self.variant = self.load_all_yaml(dir_name, dir_symbol=dir_symbol)

    def load_all_yaml(self, target_dir, dir_symbol):
        """load all yaml file and convert dictionary type"""
        yaml_list = dict()
        target_files = list()
        for root, dirs, files in os.walk(target_dir):
            yml_file = [os.path.join(root, f) for f in files if self.extension in f]
            target_files.extend(yml_file)

        for file_path in target_files:
            f = open(file_path, "r+")
            data = yaml.load(f)
            key_array = file_path.split("/")
            if len(key_array) > 2:
                key_name = key_array[len(key_array) - 2] + dir_symbol + key_array[len(key_array) -1]
            else:
                key_name = key_array[len(key_array) - 1]
            yaml_list[key_name.replace(self.extension, "")] = data
        return yaml_list

    def yaml(self, path, attribute_symbol="@"):
        """find in dictionary(convert yaml), uses argument path """
        variant = self.variant
        attribute = False
        if self.is_exist_dir == False:
            return "not found dir"
        target_path = path.split(".")
        for key in target_path:
            if attribute_symbol in key:
                attribute = key[key.find(attribute_symbol)+1::]
                key = key[:key.find(attribute_symbol)]
            if key not in variant.keys():
                return "not found"
            variant = variant[key]
            if attribute:
                variant = variant.replace('{'+ attribute_symbol +'}', attribute)
        return variant

def sample():
    yml = YamlLoader("yml")
    aaa = "oooo"
    print(yml.yaml(f'test.foo.bar@{aaa}'))
    print(yml.yaml(f'test.foo.tmp'))
    print(yml.yaml(f'test.foo.ymd@{aaa}'))
    print(yml.yaml(f'test:utils.util.hello@{aaa}'))
if __name__=='__main__':
    sample()
