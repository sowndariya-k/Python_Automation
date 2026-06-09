from configparser import ConfigParser
import os

config = ConfigParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.ini")

config.read(CONFIG_PATH)

def get_config(section, key):
    return config.get(section, key)