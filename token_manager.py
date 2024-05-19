import random

chars: list[str] = []

chars.extend([chr(code) for code in [45, 46, 95, 126]])
chars.extend([chr(code) for code in range(48, 58)])
chars.extend([chr(code) for code in range(65, 91)])
chars.extend([chr(code) for code in range(97, 123)])

size = 60


class Token:

    def __init__(self, size: int):
        self.size = size

    def generate(self):
        token: str = ""
        for _ in range(size):
            token += random.choice(chars)
        return token
