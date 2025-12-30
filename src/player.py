from dataclasses import dataclass, field

@dataclass
class PLayer:
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    properties: list = field(default_factory = list)

    def move(self, steps: int):
        old_position = self.position
        self.position = (self.position + steps) % 40

        # Passed 'Go' logic
        if self.position < old_position:
            # Collect $200 for passing Go
            self.money += 200
            print(f"{self.name} collected $200 for passing Go!")

    def pay(self, amount: int, recipient = None):
        self.money -= amount
        if recipient:
            recipient.money += amount

    def receive(self, amount: int):
        self.money += amount