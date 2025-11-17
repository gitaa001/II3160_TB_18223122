class Money:
    def __init__(self, value: int):
        if value < 0:
            raise ValueError("Money cannot be negative")
        self.value = value
