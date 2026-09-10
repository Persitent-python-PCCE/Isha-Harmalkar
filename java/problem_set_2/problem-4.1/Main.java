import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

class Main{
    public static void main(String[] args) {
        String stream = "aabcbc";
        Queue<Character> q = new ArrayDeque<>();

        Map<Character, Integer> hashMap = new HashMap<>();

        for(int i = 0; i < stream.length(); i++){
            if(hashMap.containsKey(stream.charAt(i))){
                hashMap.put(stream.charAt(i), hashMap.get(stream.charAt(i)) + 1);
            

                //remove from q
                q.remove(stream.charAt(i));
                

            }else{
                hashMap.put(stream.charAt(i), 1);
                q.offer(stream.charAt(i));

            }

            if(!q.isEmpty()){
                System.out.print(q.peek() + " ");

            }
            else{
                System.out.print("#" + " ");
            }
        }


    }
}