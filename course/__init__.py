import random
class Course:
    def __init__(self,name):
        self.name = name
    def setSem(self,semester):
        self.semester = semester

        
class Semester:
    def __init__(self,semNum):
        self.semNum = semNum
    def add(self,course, courseSchedule):
        self.schedules[course] = courseSchedule
        
        if len(self.schedules) == self.rightAmountOfDays(self) :
            self.assignDays(self)
    
    def assignDays(self):
        numTries = 1;
        coursesToCheck = set()
        daysTaken = set()
        for k,v in self.schedules.items() :
            if v.getDays(self.semNum)[-1] == 'O' :
                self.assignedDays[k] = 'O'
            elif len(v.getDays(self.semNum)) == 1 :
                if v.getDays(self.semNum)[0] in self.assignedDays :
                    self.assignedDays[k] = '-'
                else :
                    daysTaken.add(v.getDays(self.semNum)[0])
                    self.assignedDays[k] = v.getDays(self.semNum)[0]
            else :
                numTries *= len(v)
                coursesToCheck.add(k.name)
        
        if len(coursesToCheck) == 0 :
            return   
        
        while len(daysTaken) < self.rightAmountofDays(self) and numTries > 0 :
            for course in coursesToCheck :
                for i in range(len(self.schedules[course].getDays(self.semNum))) :
                    d = self.schedules[course].getDays(self.semNum)[i]
                    
                    if not d in daysTaken :
                        daysTaken.add(d)
                        self.assignedDays[course] = d
                        break
                    
                    self.assignedDays[course] = '-'
                    
                numTries -= 1
    
    def remove(self,course):
        del self.schedules[course] 
        self.assignedDays.clear()
        
        if len(self.schedules == self.rightAmountOfDays()):
            self.assignDays()
        
    def rightAmountOfDays(self):
        if self.semNum % 3 == 0 or (self.semNum + 2) % 3 == 0 :
            return 3
        else :
            return 2 
class CourseSchedule:
    def __init__(self,fallDays,springDays,summerDays):
        self.fallDays = fallDays
        self.springDays = springDays
        self.summerDays = summerDays
    
    def getDays(self,semTaken):
        if semTaken % 3 == 0:
            return self.fallDays
        if semTaken + 2 % 3 == 0:
            return self.springDays
        if semTaken + 1 % 3 == 0:
            return self.summerDays
        

def main():
    courseSchedules = {}
    coursesList = {}
    
    with open("course.txt") as text_file:
        contents = text_file.readlines()[1: ]        
        
        for line in contents:
            data = line.split()
            courseSchedules[''.join(data[:1])] = [data[1:2],data[2:3],data[3:4]]
            coursesList[''.join(data[:1])] = Course(''.join(data[:1]))
    
    courseConstraints = {}
    
    with open("constraints.txt") as text_file:
        contents = text_file.readlines()[1: ]  
        
        for line in contents:
            data = line.split()
            lhsCourse = ''.join(data[:1])
            consType = ''.join(data[1:2])
            rhsCourse = ''.join(data[2:3])
            
            if not lhsCourse in courseConstraints:
                courseConstraints[lhsCourse] = {rhsCourse : consType}
            
            courseConstraints[lhsCourse][rhsCourse] = consType
                
    assignSemesters(courseSchedules,courseConstraints,coursesList)    

def assignSemesters(courseSchedules, courseConstraints,coursesList): 
    sems = []
      
    for i in range(11):
        sems[i] = Semester(i)
    
    for k,v in coursesList : 
        semester = random.randint(0,12)
        setSemTaken()
        
        
def setSemTaken(course, semester, sems):
    
main()  
             
            
        