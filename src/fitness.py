

class Fitness:

    MAXFITNESS = 30**11

    def __init__(self):
        self.semfitness = [self.MAXFITNESS] * 11

    def update(self, sem, amount):
        self.semfitness[sem] *= amount

    def getbestnonfullsemester(self, nonfullsemesters):
        if len(nonfullsemesters) > 0:
            best = nonfullsemesters[0]
            for i in range(1, len(nonfullsemesters)):
                best = i if self.semfitness[i] > self.semfitness[best] else best
            return best
        else:
            return self.gethealthiestsemester()

    def gethealthiestsemester(self):
        maxat = 0
        for i in range(0, len(self.semfitness)):
            maxat = i if self.semfitness[i] > self.semfitness[maxat] else maxat
        return maxat
