from semester import Semester
from course import CourseSchedule
import random


class Schedule(object):
    sems = [Semester]
    courseswithconflicts = set()

    CONSCONFLICT = .999
    DAYCONFLICT = .999999
    NOCONFLICT = 1.000001
    DOMAINCONFLICT = 0

    def __init__(self, courseslist, courseschedules, courseconstraints):
        self.makesems()
        self.assignsemesters(courseslist, courseschedules)
        self.schedprint(courseslist)
        #self.checkconflicts(courseslist, courseconstraints)
        #self.solve(courseslist, courseconstraints, courseschedules)
        #self.schedprint(courseslist)

    def getnonfullsemesters(self):
        nonfull = []

        for i in range(0, len(self.sems)):
            if self.sems[i].canaddmoredays():
                nonfull.append(i)

        return nonfull

    def assignsemesters(self, courseslist, courseschedules):
        for course in courseslist.values():
            #nextsem = random.randint(0, len(self.sems))
            nextsem = 5
            course.semtaken = nextsem
            self.sems[nextsem].add(course, courseschedules.get(course))
            if self.sems[nextsem].hasrightamountofdays:
                self.getdaysfromsemester(self.sems[nextsem], courseslist)

    def checkconflicts(self, courseslist, courseconstraints):
        self.courseswithconflicts.clear()

        for coursename, course in courseslist.items():
            if course in courseconstraints:
                for rhscourse, constrainttype in courseconstraints[course].items():
                    if constrainttype == "<":
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
            if course.day == '-':
                self.courseswithconflicts.add(coursename)
            if course not in self.courseswithconflicts:
                course.fitness.update(course.semtaken, self.NOCONFLICT)

    def getdaysfromsemester(self, semester, courseslist):

        for k, v in semester.assigneddays.items():
            courseslist[k].day = v

    def changesem(self, course,newsem,  courseslist, courseschedules):
        self.sems[course.semtaken].remove(course)
        if self.sems[course.semtaken].hasrightamountofdays:
            self.getdaysfromsemester(course.semtaken, courseslist)

        self.sems[newsem].add(course, courseschedules.get(course))
        courseslist[course].semtaken = newsem

        if self.sems[newsem].hasrightamountofdays():
            self.getdaysfromsemester(newsem, courseslist)

    def makesems(self):
        for i in range(12):
            s = Semester(i)
            self.sems.append(s)

    def schedprint(self, courseslist):
        semoutput = [11]
        output = ""

        for c in courseslist.items():
            semoutput[c.semtaken].append(c.name + "\t" + c.day + "\t")

        for i in range(0, len(self.sems)):
            output.append(i + ". " + semoutput[i])

        print(output)

    def solve(self, courseslist, courseconstraints, courseschedules):
        while len(self.courseswithconflicts) > 0:
            for c in self.courseswithconflicts:
                self.changesem(c, courseslist.get(c).fitness.getbestnonfullsemester(self.getnonfullsemesters()), courseslist, courseschedules)
            self.checkconflicts(courseslist, courseconstraints)
