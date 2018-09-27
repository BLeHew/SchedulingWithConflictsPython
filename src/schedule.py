from semester import Semester
from course import Course
import random
import time


class Schedule(object):
    sems = []
    courseswithconflicts = set()

    CONSCONFLICT = .99
    DAYCONFLICT = .9999
    NOCONFLICT = 1.000001
    DOMAINCONFLICT = 0

    def __init__(self, courseslist, courseconstraints):
        self.assignsemesters(courseslist)
        self.schedprint()
        self.checkconflicts(courseslist, courseconstraints)
        t0 = time.time()
        self.solve(courseslist, courseconstraints)
        t1 = time.time() - t0
        print("Took: ", t1)
        self.schedprint()

    def getnonfullsemesters(self):
        nonfull = []

        for i in range(0, len(self.sems) - 1):
            if self.sems[i].canaddmoredays():
                nonfull.append(i)

        return nonfull

    def assignsemesters(self, courseslist):

        for i in range(0, 11):
            i = Semester(i)
            self.sems.append(i)

        random.seed(2)

        for course in courseslist.values():
            nextsem = random.randint(0, len(self.sems) - 1)
            course.semtaken = nextsem
            self.sems[nextsem].addcourse(course)

            if self.sems[nextsem].hasrightamountofdays:
                self.getdaysfromsemester(self.sems[nextsem], courseslist)

    def checkconflicts(self, courseslist, courseconstraints):
        self.courseswithconflicts.clear()

        for coursename, course in courseslist.items():
            if coursename in courseconstraints:
                for rhscourse, constrainttype in courseconstraints[coursename].items():
                    if constrainttype == "<":
                        if course.fitness.semfitness[10] > 0:
                            course.fitness.semfitness[10] *= 0
                        if courseslist[rhscourse].fitness.semfitness[0] > 0:
                            courseslist[rhscourse].fitness.semfitness[0] *= 0

                        if course.semtaken >= courseslist[rhscourse].semtaken:
                            self.courseswithconflicts.add(coursename)
                            self.courseswithconflicts.add(rhscourse)
                            course.fitness.update(course.semtaken, self.CONSCONFLICT)
                            courseslist[rhscourse].fitness.update(courseslist[rhscourse].semtaken, self.CONSCONFLICT)
                    else:
                        if course.semtaken > courseslist[rhscourse].semtaken:
                            self.courseswithconflicts.add(coursename)
                            self.courseswithconflicts.add(rhscourse)
                            course.fitness.update(course.semtaken, self.CONSCONFLICT)
                            courseslist[rhscourse].fitness.update(courseslist[rhscourse].semtaken, self.CONSCONFLICT)

            if self.sems[course.semtaken].hastoomanydays():
                self.courseswithconflicts.add(coursename)
                course.fitness.update(course.semtaken, self.DAYCONFLICT)
            if course.day == '-':
                self.courseswithconflicts.add(coursename)
                course.fitness.update(course.semtaken, self.DAYCONFLICT)
            if course not in self.courseswithconflicts:
                course.fitness.update(course.semtaken, self.NOCONFLICT)

    def getdaysfromsemester(self, semester, courseslist):
        for k, v in semester.semcourses.items():
            courseslist[k].day = v.day
            courseslist[k].semtaken = v.semtaken

    def changesem(self, course, newsem,  courseslist):
        self.sems[courseslist[course].semtaken].remove(course)
        if self.sems[courseslist[course].semtaken].hasrightamountofdays:
            self.getdaysfromsemester(self.sems[courseslist[course].semtaken], courseslist)

        self.sems[newsem].addcourse(courseslist[course])
        courseslist[course].semtaken = newsem

        if self.sems[newsem].hasrightamountofdays():
            self.getdaysfromsemester(self.sems[newsem], courseslist)

    def schedprint(self):
        i = 0
        for s in self.sems:
            print(i, end=" ")
            for c in s.semcourses.values():
                print(c.name + "\t" + c.day, end="\t")
            print()
            i += 1
        print()

    def solve(self, courseslist, courseconstraints):
        i = 1
        while len(self.courseswithconflicts) > 0:
            if i % 10000 == 0:
                self.schedprint()
                for c in self.courseswithconflicts:
                    print(c, end=" ")
                    for j in courseslist[c].fitness.semfitness:
                        print(j, " ", end="")
                    print()
            for c in self.courseswithconflicts:
                self.changesem(c, courseslist.get(c).fitness.getbestnonfullsemester(self.getnonfullsemesters()), courseslist)
            self.checkconflicts(courseslist, courseconstraints)
            i += 1

