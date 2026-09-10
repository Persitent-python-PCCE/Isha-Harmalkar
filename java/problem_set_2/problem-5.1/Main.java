import java.security.cert.CollectionCertStoreParameters;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collector;
import java.util.stream.Collectors;

class Main{
    record Employee(String name, String dept, int salary){}

    public static void main(String[] args) {
        List<Employee> employees = List.of(
            new Employee("Asha",  "Engineering", 85000),
            new Employee("Ravi",  "Engineering", 92000),
            new Employee("Meera", "Sales",       60000),
            new Employee("John",  "Sales",       72000),
            new Employee("Priya", "HR",          55000)
        );

        Map<String, Optional<Employee>> topEarnerByDept = employees.stream().collect(Collectors.groupingBy(Employee::dept,
            Collectors.maxBy(Comparator.comparingInt(Employee::salary))
        ));


        topEarnerByDept.forEach((dept, optEmp) ->{
            optEmp.ifPresent(emp -> System.out.println(dept + " -> " + emp.name() + emp.salary()));
        });




    }
}