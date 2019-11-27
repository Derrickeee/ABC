import configparser


class DiskParameter:
    def __init__(self, filename):
        Config = configparser.ConfigParser()
        Config.read(str(filename))
        self.cylinders = Config.getint('diskq1', 'cylinders')
        self.previous = Config.getint('diskq1', 'previous')
        self.current = Config.getint('diskq1', 'current')
        self.sequence = Config.get('diskq1', 'sequence')
        self.sequence = self.sequence.split(",")
        seq = []
        for i in self.sequence:
            seq.append(int(i))
        self.sequence = seq

    def getCylinders(self):
        return self.cylinders

    def getPrevious(self):
        return self.previous

    def getCurrent(self):
        return self.current

    def getSequence(self):
        return self.sequence
