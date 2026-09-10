import java.util.HashMap;
import java.util.Map;

class Main{
    public static void main(String[] args){
        String text = "the cat the dog the cat sat";
        Map <String, Integer> hashMap = new HashMap<>();

        String[] strs = text.split(" ");
        int mostFreqCount = 0;
        String mostFreqName = "";


        for(int i = 0; i < strs.length; i++)
        {

           int val = 0;
           String key = strs[i];

           if(hashMap.containsKey(key))
           {
                val = hashMap.get(key) + 1;
                hashMap.put(key, val);
           }
           else{
            val = 1;
            hashMap.put(strs[i], val);

           }

           if (val > mostFreqCount){
            
            mostFreqCount = val;
            mostFreqName = key;
           } 
           if(val == mostFreqCount){
            if(key.compareTo(mostFreqName) < 0){
                mostFreqName = key;
            }
           }



        }

        for(Map.Entry<String, Integer> entry: hashMap.entrySet()){
            System.out.println(entry.getKey() + "=" + entry.getValue());
        }

        System.out.print("Most Frequent: " + mostFreqName + "(" + mostFreqCount + ")");

    }
}