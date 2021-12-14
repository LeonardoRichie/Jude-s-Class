


class Person():
    def __init__(self, name, address):
        self._name = name
        self._address = address
    
    def getName(self):
        return self._name
    def getAddress(self):
        return self._address
    def setAddress(self, address):
        self._address = address
    def __str__(self):
        return "Student: {}({})".format(self.name, self.address)

class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
    def addCourseGrade(self, course, grade):
        self.__Courses.append(course)
        self.__numCourses = self.__numCourses+1
        self.__grades = int(grade)
    def printGrades(self):
        print (self.__grades)
    def getAverageGrade(self):
        x = sum(self.__grades) / self.__numCourses
        print("The average Grade is {}".format(x))
    def __str__(self):
        return "Student: {}({})".format(self.name, self.address)

class Teacher(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
    def addCourse(self,courses):
        if courses not in self.__courses:
            self.__courses.append(courses)
            self.__numCourses = self.__numCourses + 1
        else:
            print("The course already existed")

    def removeCourse(self,courses):
        if courses in self.__courses:
            self.__courses.remove(courses)
        else:
            print("The course does not exist")


    def __str__(self):
        return "Teacher: {}({})".format(self.name, self.address)