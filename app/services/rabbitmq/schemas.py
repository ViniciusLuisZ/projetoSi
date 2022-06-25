from codecs import utf_8_decode, utf_8_encode
import json


class RabbitBody:
    message: object

    def __init__(self, message):
        self.message = message

    def encode(self):
        return utf_8_encode(json.dumps(self.message))[0]

    @staticmethod
    def decode(encoded):
        dicc = json.loads(utf_8_decode(encoded))
        message = dicc
        return RabbitBody(message)
