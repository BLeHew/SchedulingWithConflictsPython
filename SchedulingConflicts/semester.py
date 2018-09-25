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