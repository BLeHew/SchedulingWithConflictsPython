class Semester:

    def __init__(self, semnum):
        self.semnum = semnum
        self.semcourses = {}

    def addcourse(self, course):
        self.semcourses[course.name] = course

        if len(self.semcourses) == self.rightamountofdays():
            self.assigndays()

    def canaddmoredays(self):
        return len(self.semcourses) < self.rightamountofdays()

    def hasrightamountofdays(self):
        return len(self.semcourses) == self.rightamountofdays()

    def hastoomanydays(self):
        return len(self.semcourses) > self.rightamountofdays()

    def assigndays(self):
        numtries = 1
        coursestocheck = set()
        daystaken = set()
        for cname, course in self.semcourses.items():
            if course.getschedule()[0][-1] == 'O':
                course.day = 'O'
            elif len(course.getschedule()[0]) == 1:
                if course.getschedule()[0][0] in daystaken:
                    course.day = '-'
                else:
                    daystaken.add(course.getschedule()[0][0])
                    course.day = course.getschedule()[0][0]
            else:
                numtries *= len(course.getschedule())
                coursestocheck.add(cname)
        if len(coursestocheck) == 0:
            return

        while len(daystaken) < self.rightamountofdays() and numtries > 0:
            for course in coursestocheck:
                for i in self.semcourses[course].getschedule():
                    for j in i:
                        if j not in daystaken:
                            daystaken.add(j)
                            self.semcourses[course].day = j
                            break
                        else:
                            self.semcourses[course].day = '-'
            numtries -= 1

    def remove(self, course):
        del self.semcourses[course]
        
        if len(self.semcourses) == self.rightamountofdays():
            self.assigndays()
        
    def rightamountofdays(self):
        if self.semnum % 3 == 0 or (self.semnum + 2) % 3 == 0:
            return 3
        else:
            return 2 