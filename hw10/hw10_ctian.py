from collections import defaultdict
from prettytable import PrettyTable
import os


class Repository:
    def __init__(self, path):
        self.p_student = os.path.join(path, 'students.txt')
        self.p_instructor = os.path.join(path, 'instructors.txt')
        self.p_grade = os.path.join(path, 'grades.txt')
        self.p_major = os.path.join(path,'majors.txt')
        self.students = {}
        self.instructors = {}
        self.majors = {}

    def file_reader(self, path, num_fields=3, sep='\t', header=False):
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't open {path}")
        else:
            with fp:
                
                for index, line in enumerate(fp,1):
                    sp_line = line.strip().split(sep)
                    if len(sp_line) != num_fields:
                        raise ValueError(
                            f"{path} has {len(sp_line)} fields on line {index} but except {num_fields}")
                    else:
                        if header == True:
                            header = False
                            continue
                        else:
                            yield sp_line

    def read_student(self):
        for CWID, tName, tMajor in self.file_reader(self.p_student, 3, '\t', False):
            self.students[CWID] = Student(CWID, tName, tMajor)

    def read_instructor(self):
        for CWID, tName, tDepartment in self.file_reader(self.p_instructor, 3, '\t', False):
            self.instructors[CWID] = Instructor(CWID, tName, tDepartment)

    def read_grades(self):
        for CWID, tCouse, tLetterGrade, tinstructor in self.file_reader(self.p_grade, 4, '\t', False):
            if CWID in self.students.keys():
                self.students[CWID].dict_course_grade(tCouse, tLetterGrade)

            if tinstructor in self.instructors.keys():
                self.instructors[tinstructor].dict_course_num(tCouse)
    
    def read_major(self):
        for major,tflag,tcourse in self.file_reader(self.p_major,3,'\t',False):
            self.majors[major] = Major(major)
        for major,tflag,tcourse in self.file_reader(self.p_major,3,'\t',False):
            self.majors[major].add_tflag[tflag].append(tcourse)
        

    def student_summary(self):
        pt = PrettyTable(field_names=['CWID','Name','Completed Courses'])
        for c_student in self.students.values():
            for cwid,name,cc in c_student.prettytable():
                pt.add_row([cwid, name, cc ])
        print(pt)
        return pt
    
    def instructor_summary(self):
        pt = PrettyTable(field_names=['CWID','Name','Dept','Course','Students'])
        for c_instructors in self.instructors.values():
            for CWID,Name,Dept,Course,Students in c_instructors.prettytable():
                pt.add_row([CWID,Name,Dept,Course,Students])
        print(pt)
        return pt

    def major_summary(self):
        pt = PrettyTable(field_names=['Dept','Required','Electives'])
        for dept in self.majors.values():
            for i,j,e in dept.prettytable():
                pt.add_row([i,j,e])
        print(pt)
            

class Student:
    def __init__(self, CWID, tName, tMajor):
        self.CWID = CWID
        self.tName = tName
        self.tMajor = tMajor
        self.course_grade = defaultdict(str)

    def dict_course_grade(self, course, grade):
        self.course_grade[course] = grade

    def prettytable(self):
        yield self.CWID, self.tName, sorted(list(self.course_grade))

    def remain(self, course):
        if self.course_grade[course] not in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            return course



class Instructor:
    def __init__(self, CWID, tName, tDepartment):
        self.CWID = CWID
        self.tName = tName
        self.tDepartment = tDepartment
        self.course_num = defaultdict(int)

    def dict_course_num(self, course):
        self.course_num[course] += 1
    
    def prettytable(self):
        for tCourse,tStudents in self.course_num.items():
            yield self.CWID, self.tName, self.tDepartment,tCourse ,tStudents


class Major:
    def __init__(self,major):
        self.major = major
        self.add_tflag = defaultdict(list)

    def add_major(self, tflag, tcourse):
        self.add_tflag[tflag].append(tcourse)

    def prettytable(self):
        yield self.major, self.add_tflag['R'], self.add_tflag['E']

def main(path):
    dd = Repository(path)
    dd.read_student()
    dd.read_instructor()
    dd.read_grades()
    dd.read_major()
    dd.student_summary()
    dd.instructor_summary()
    dd.major_summary()

   

if __name__ == "__main__":
    path = '/Users/TC/iCloudDrive/Desktop/ssw810/hw10'
    path_mac = '/Users/chengtian/Desktop/ssw810/hw10'
    main(path_mac)

