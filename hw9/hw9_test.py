import unittest
import hw9_ctian
from prettytable import PrettyTable

class H9Test(unittest.TestCase):
    def test_student_summary(self):
        path_mac = '/Users/chengtian/Desktop/810/hw9'
        dd = hw9_ctian.Repository(path_mac)
        dd.read_student()
        dd.read_instructor()
        dd.read_grades()
        dd.student_summary()
        dd.instructor_summary()
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        test_student_summary = []
        test_student_summary.append(('10103', 'Baldwin, C', "['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']"))
        test_student_summary.append(('10115', 'Wyatt, X', "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']"))
        test_student_summary.append(('10172' , 'Forbes, I' ,"['SSW 555', 'SSW 567']"))
        test_student_summary.append(("10175","Erickson, D","['SSW 564', 'SSW 567', 'SSW 687']"))
        test_student_summary.append(("10183", "Chapman, O", "['SSW 689']"))
        test_student_summary.append(("11399", "Cordova, I", "['SSW 540']"))
        test_student_summary.append(("11461", "Wright, U", "['SYS 611', 'SYS 750', 'SYS 800']"))
        test_student_summary.append(("11658", "Kelly, P", "['SSW 540']"))
        test_student_summary.append(("11714", "Morton, A" , "['SYS 611', 'SYS 645']"))
        test_student_summary.append(("11788", "Fuller, E", "['SSW 540']"))  
        for CWID,Name,CC in test_student_summary:
            pt.add_row([CWID, Name, CC])
        self.assertEqual(str(dd.student_summary()), str(pt))

    def test_instructor_summary(self):
        path_mac = '/Users/chengtian/Desktop/810/hw9'
        dd = hw9_ctian.Repository(path_mac)
        dd.read_student()
        dd.read_instructor()
        dd.read_grades()
        dd.student_summary()
        dd.instructor_summary()
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept','Course','Students'])
        test_instructor_summary = []
        test_instructor_summary.append(("98765", 'Einstein, A' , 'SFEN' , 'SSW 567' , '4'))
        test_instructor_summary.append(("98765" , 'Einstein, A' , 'SFEN' , 'SSW 540' , '3'))
        test_instructor_summary.append(("98764" , 'Feynman, R' , 'SFEN' , 'SSW 564', '3'))
        test_instructor_summary.append(("98764" , 'Feynman, R' , 'SFEN' , 'SSW 687' , '3'))
        test_instructor_summary.append(("98764" , 'Feynman, R' , 'SFEN' , 'CS 501' , '1'))
        test_instructor_summary.append(("98764" , 'Feynman, R' , 'SFEN' , 'CS 545' , '1'))
        test_instructor_summary.append(("98763" , 'Newton, I' , 'SFEN' , 'SSW 555' , '1'))
        test_instructor_summary.append(("98763" , 'Newton, I' , 'SFEN' , 'SSW 689' , '1'))
        test_instructor_summary.append(("98760" , 'Darwin, C' , 'SYEN' , 'SYS 800' , '1'))
        test_instructor_summary.append(("98760" , 'Darwin, C' , 'SYEN' , 'SYS 750' , '1'))
        test_instructor_summary.append(("98760" , 'Darwin, C' , 'SYEN' , 'SYS 611' , '2'))
        test_instructor_summary.append(("98760" , 'Darwin, C' , 'SYEN' , 'SYS 645' , '1'))
        for CWID, Name, Dept, Course, Students in test_instructor_summary:
            pt.add_row([CWID, Name, Dept, Course, Students])

        self.assertEqual(str(dd.instructor_summary()), str(pt))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
