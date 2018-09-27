from semester import Semester
from course import Course
from schedule import Schedule
import random


def main():
    courseslist = {}
    courseconstraints = {}

    with open("courses.txt") as text_file:
        contents = text_file.readlines()[1:]

        for line in contents:
            data = line.split()
            courseslist[''.join(data[:1])] = Course(''.join(data[:1]), -1, data[1:2], data[2:3], data[3:4])

    with open("constraints.txt") as text_file:
        contents = text_file.readlines()[1:]

        for line in contents:
            data = line.split()
            lhsCourse = ''.join(data[:1])
            consType = ''.join(data[1:2])
            rhsCourse = ''.join(data[2:3])

            if lhsCourse not in courseconstraints:
                courseconstraints[lhsCourse] = {rhsCourse: consType}

            courseconstraints[lhsCourse][rhsCourse] = consType

    s = Schedule(courseslist, courseconstraints)



main()
