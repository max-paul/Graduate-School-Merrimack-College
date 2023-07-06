package module3;

import java.util.ArrayList;
import java.util.List;

public class Course {
    private String courseId;
    private String name;
    private List<Student> students;
    private Teacher teacher;

    public Course(String courseId, String name, Teacher teacher) {
        this.courseId = courseId;
        this.name = name;
        this.teacher = teacher;
        students = new ArrayList<>();
    }

    public void enrollStudent(Student student) {
        students.add(student);
        System.out.println("Student " + student.getName() + " enrolled in the course " + name + ".");
    }

    public void printStudents() {
        System.out.println("Students enrolled in the course " + name + ":");
        for (Student student : students) {
            System.out.println(" - " + student.getName());
        }
    }

    public void conductLecture() {
        System.out.println("Teacher " + teacher.getName() + " is conducting a lecture for the course " + name + ".");
    }
}
