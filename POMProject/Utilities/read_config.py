from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


class ReadConfig:

    @staticmethod
    def get_browser():
        return config.get("basic info", "browser")

    @staticmethod
    def get_url():
        return config.get("basic info", "url")

    @staticmethod
    def get_email():
        return config.get("login credential", "email")

    @staticmethod
    def get_password():
        return config.get("login credential", "password")

    @staticmethod
    def get_valid_search_term():
        return config.get("search term", "validterm")

    @staticmethod
    def get_invalid_search_term():
        return config.get("search term", "invalidterm")