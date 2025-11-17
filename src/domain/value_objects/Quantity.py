class Quantity:
    def __init__(self, value: int):
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self.value = value
