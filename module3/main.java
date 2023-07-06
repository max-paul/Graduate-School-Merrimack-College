package module3;

public class main {
    public static void main(String[] args) {
        // Create a Teacher object
        Teacher teacher = new Teacher("John Doe", 35, "T001");

        // Create two Student objects
        Student student1 = new Student("Alice Smith", 20, "S001");
        Student student2 = new Student("Bob Johnson", 21, "S002");

        // Create a Course object
        Course course = new Course("C001", "Java Programming", teacher);

        // Enroll students in the course
        course.enrollStudent(student1);
        course.enrollStudent(student2);

        // Print the list of enrolled students
        course.printStudents();

        // Conduct a lecture for the course
        course.conductLecture();

        // Students studying and teachers teaching
        student1.study();
        student2.study();
        teacher.teach();
    }
}


