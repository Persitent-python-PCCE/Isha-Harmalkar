import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main{
    
    public static void main(String[] args){
       List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7));
       int k = 3;
       int n = list.size();

       k = k % n;

       List<Integer> res = new ArrayList<>();
       res.addAll(list.subList(n - k, n));
       res.addAll(list.subList(0, n - k));

       System.out.println(res);




    }
}