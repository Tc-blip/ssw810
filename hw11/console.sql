SELECT i.CWID, i.Name, i.Dept, g.Course, count(g.Student_CWID) as Student from HW11_instructors i
    left join HW11_grades g on i.CWID = g.Instructor_CWID group by g.Course;