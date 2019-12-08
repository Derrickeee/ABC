from algorithm import DiskParameter


class diskOptimization:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1.ini")
        # self.dp = DiskParameter.DiskParameter("diskq2.ini")
        self.generateAnalysis()

    def printSequence(self, name, location):
        curr = 0
        prev = self.dp.getCurrent()
        total = 0
        working1 = ""
        working2 = ""
        order = ""

        for i in location:
            curr = i
            total += abs(prev - curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev - curr)) + "+"
            prev = i

        working1 = working1[0:-1]
        working2 = working2[0:-1]
        #First Come First Served Order
        order = str(self.dp.getCurrent()) + ", " + str(location)[1:-1]
        print(name + "\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")

    def arrangeSSTF(self, curr, seq):
        temp = seq[:]
        sstf = []
        temp2 = temp[:]

        num = curr
        for i in temp:
            minimum = max(seq)
            num2 = num
            for ii in temp2:
                dist = abs(num2 - ii)
                if dist < minimum:
                    num = ii
                    minimum = dist
            temp2.remove(num)
            sstf.append(num)
        return sstf

    def arrangescan(self, curr, seq):
        temp = seq[:]
        greater = [track for track in temp if track > curr]
        identical = [track for track in temp if track == curr]
        smaller = [track for track in temp if track < curr]
        greater = sorted(greater)
        smaller = sorted(smaller, reverse=True)
        additional = [self.dp.getCylinders() - 1]
        scan = []
        if identical:
            for track in identical:
                scan.append(track)
        order = []
        if greater and smaller and additional:
            if curr > self.dp.getPrevious():
                order = [greater, additional, smaller]
            else:
                additional = [0]
                order = [smaller, additional, greater]
        elif greater and additional and not smaller:
            order = [greater, additional]
        elif smaller and not greater:
            additional = [0]
            order = [smaller, additional]
        for sublist in order:
            for nextTrack in sublist:
                scan.append(nextTrack)
        return scan


    def arrangelook(self, curr, seq):
        temp = seq[:]
        greater = [track for track in temp if track > curr]
        identical = [track for track in temp if track == curr]
        smaller = [track for track in temp if track < curr]
        greater = sorted(greater)
        smaller = sorted(smaller, reverse=True)
        look = []
        #adds current position to order
        if identical:
            for track in identical:
                look.append(track)
        order = []
        if greater and smaller:
            #the order of access depends on the direction of the disk head movement: from previous request served versus the current request serving
            if curr > self.dp.getPrevious():
                #merges the two lists
                order = [greater, smaller]
            else:
                order = [smaller, greater]
        elif greater and not smaller:
            order = [greater]
        elif smaller and not greater:
            order = [smaller]
            #appends the numbers from the list to the order of access
        for sublist in order:
            for nextTrack in sublist:
                look.append(nextTrack)
        return look

    def arrangeclook(self, curr, seq):
        temp = seq[:]
        greater = [track for track in temp if track > curr]
        identical = [track for track in temp if track == curr]
        smaller = [track for track in temp if track < curr]
        greater = sorted(greater)
        smaller = sorted(smaller)
        clook = []
        if identical:
            for track in identical:
                clook.append(track)
        order = []
        #only one direction
        if greater and smaller:
            order = [greater, smaller]
        elif greater and not smaller:
            order = [greater]
        elif smaller and not greater:
            order = [smaller]
        for sublist in order:
            for nextTrack in sublist:
                clook.append(nextTrack)
        return clook
    
    def generateFCFS(self):
        seq = self.dp.getSequence()
        self.printSequence("FCFS", seq)

    def generateSSTF(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        self.printSequence("SSTF", self.arrangeSSTF(curr, seq))

    def generateScan(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        self.printSequence("Scan", self.arrangescan(curr, seq))


    def generatelook(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        self.printSequence("Look", self.arrangelook(curr, seq))

    def generateclook(self):
        seq = self.dp.getSequence()
        curr = self.dp.getCurrent()
        self.printSequence("C-Look", self.arrangeclook(curr, seq))

    def generateAnalysis(self):
        self.generateFCFS()
        self.generateSSTF()
        self.generateScan()
        self.generatelook()
        self.generateclook()
