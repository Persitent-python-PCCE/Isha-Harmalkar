import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Main{
    public static void main(String[] args) {
        int n = 5;
        Queue<String> q = new ArrayDeque<>();
        q.offer("1");

        List<String> res = new ArrayList<>();

        while (res.size() < n){
            String cur = q.poll();
            res.add(cur);
            q.offer( cur + "0");
            q.offer(cur + "1");
        }


        System.err.println(res);
    }
}