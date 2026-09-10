import java.util.HashSet;
import java.util.Set;

class Main{
    public static void main(String[] args){

        Set<Integer> s1 = new HashSet<>(Set.of(1, 2, 3, 4, 5));
        Set<Integer> s2 = new HashSet<>(Set.of(2, 3, 5, 7));
        Set<Integer> s3 = new HashSet<>(Set.of(2, 3, 5, 9, 11));

        Set<Integer> res = new HashSet<>(s1);
        res.retainAll(s2);
        res.retainAll(s3);

        System.out.println(res);


    }
}