package module3;

public class Teacher extends Person {
    private String teacherId;

    public Teacher(String name, int age, String teacherId) {
        super(name, age);
        this.teacherId = teacherId;
    }

    public String getTeacherId() {
        return teacherId;
    }

    public void teach() {
        System.out.println("Teacher " + getName() + " is teaching.");
    }
}
