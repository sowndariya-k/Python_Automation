from configparser import ConfigParser
import os

config = ConfigParser()

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "config.ini")

config.read(config_path)

def get_config(section, key):
    return config.get(section, key)