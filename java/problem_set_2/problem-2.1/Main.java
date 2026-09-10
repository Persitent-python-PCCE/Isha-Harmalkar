import java.util.HashSet;
import java.util.Set;

class Main{
    public static void main(String[] args){
        Set <String> setA = new HashSet<>(Set.of("apple", "banana", "cherry", "date"));
        Set <String> setB = new HashSet<>(Set.of("banana", "date", "fig", "grape"));
        Set <String> res = new HashSet<>(setA);
        res.addAll(setB);

        //now we have union in res
        //System.out.println("Union: "+ res);

        Set<String> intersection = new HashSet<>(setA);

        //System.out.println("Intersection: " +  intersection);
        intersection.retainAll(setB);

        res.removeAll(intersection);

        
        System.out.println(res);

        
        
    }
}