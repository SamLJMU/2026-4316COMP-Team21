from collections.abc import Callable

class Visualisation:
    def __init__(self, message: str, function: Callable):
        self.message = message
        self._function = function

    def run(self):
        self._function()