import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

class Student {

    int rollNumber;
    String name;
    int marks;
    double cgpa;

    Student(int rollNumber, String name, int marks, double cgpa) {
        this.rollNumber = rollNumber;
        this.name = name;
        this.marks = marks;
        this.cgpa = cgpa;
    }

    @Override
    public String toString() {
        return "Roll Number = " + rollNumber +
               ", Name = " + name +
               ", Marks = " + marks +
               ", CGPA = " + cgpa;
    }
}

public class DetailsOfStudentsUsingBranch{

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        HashMap<String, List<Student>> studentsByBranch = new HashMap<>();

        List<Student> cse = new ArrayList<>();

        cse.add(new Student(101, "Bhargav", 920, 9.2));
        cse.add(new Student(102, "Rahul", 850, 8.5));
        cse.add(new Student(103, "Kiran", 780, 7.8));

        studentsByBranch.put("CSE", cse);

        List<Student> ece = new ArrayList<>();

        ece.add(new Student(201, "Arjun", 880, 8.8));
        ece.add(new Student(202, "Ravi", 760, 7.6));
        ece.add(new Student(203, "Anil", 950, 9.5));

        studentsByBranch.put("ECE", ece);

        List<Student> eee = new ArrayList<>();

        eee.add(new Student(301, "Sai", 810, 8.1));
        eee.add(new Student(302, "Vikas", 890, 8.9));

        studentsByBranch.put("EEE", eee);

        String branch=sc.next();

            System.out.println("Branch: " + branch);

            List<Student> students = studentsByBranch.get(branch);

            for (Student student : students) {
                System.out.println(student);
            }

            System.out.println();
        
    }
}