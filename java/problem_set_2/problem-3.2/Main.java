import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Main{
    public static void main(String[] args){

        String[] words = {"listen", "silent", "enlist", "google", "gogole", "cat", "act"};

        Map<List<Integer>, List<String>> hashMap = new HashMap<>();

        for(int i = 0; i < words.length; i++){
            List<Integer> count = new ArrayList<>(getCount(words[i]));
            

            if(hashMap.containsKey(count)){
                hashMap.get(count).add(words[i]);

            }else{
                List<String> newList = new ArrayList<>(List.of(words[i]));
                hashMap.put(count, newList);
            }
        }

        hashMap.forEach((key, list) -> {
            System.out.println(list);
        });






    }

    public static List<Integer> getCount(String s)
    {

        List<Integer> count = new ArrayList<>(Collections.nCopies(26, 0));

        for(int i = 0; i < s.length(); i++){

            int index = s.charAt(i) - 'a';
            int val = count.get(index) + 1;
            count.set(index, val);
        }


   
        return count;


    }
}