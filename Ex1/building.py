class Building:
    def __init__(self, minFloor: int, maxFloor: int):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = []         # list of elevators in building

    def add_elevator(self, elevator):
        self.elevators.append(elevator)
