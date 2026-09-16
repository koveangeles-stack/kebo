class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__("Glass")
        self.capacity = capacity


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(100),
            Beaker(100),
            Beaker(250),
            Beaker(250),
            Beaker(500)
        ]


tray = Tray()

print("Number of beakers:", len(tray.beakers))

del tray
