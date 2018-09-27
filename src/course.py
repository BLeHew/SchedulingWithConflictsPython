from fitness import Fitness


class Course:

    def __init__(self, name, semtaken, falldays, springdays, summerdays):
        self.semtaken = semtaken
        self.name = name
        self.falldays = falldays
        self.springdays = springdays
        self.summerdays = summerdays
        self.fitness = Fitness()
        self.day = '-'

    def getschedule(self):
        if self.semtaken % 3 == 0:
            return self.falldays
        if (self.semtaken + 2) % 3 == 0:
            return self.springdays
        if (self.semtaken + 1) % 3 == 0:
            return self.summerdays
      
       