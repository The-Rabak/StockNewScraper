import re

from classes.validators.baseValidator import BaseValidator

class urlValidator(BaseValidator):
    def __init__(self, url):
        self.url = url.lower()

    def validate(self):
        if err := self.validate_url():
            return err
        return True

    def validate_url(self):
        url_regex = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")

        if not url_regex.search(self.url):
            return self.get_url_err_str()
        return None

    def get_url_err_str(self):
        return "please enter a valid url"