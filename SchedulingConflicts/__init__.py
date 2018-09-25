def main():
    courseSchedules = {}
    coursesList = {}
    
    with open("courses.txt") as text_file:
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