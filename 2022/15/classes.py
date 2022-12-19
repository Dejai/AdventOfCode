
class Sensor:

    def __init__(self, line):

        self.Row = None
        self.Col = None
        self.Beacon = Beacon(line)

    def __repr__(self):
        return "{0}".format(row)


class Beacon:

    def __init__(self, line):
