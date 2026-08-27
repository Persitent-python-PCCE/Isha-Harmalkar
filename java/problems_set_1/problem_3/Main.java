import java.util.HashMap;
import java.util.Map;

class Main {
    public static void main(String args[])
    {
        String s = "programming";
        int maxCount = 0;
        int secondMaxCount = 0;
        char res = 'a';
        int n = s.length();

          HashMap<Character, Integer> hashMap = new HashMap<>();

        for(int i = 0; i < n; i++)

        {
            char c = s.charAt(i);
            int charExist = hashMap.getOrDefault(c, 0);

            if (charExist != 0)
            {
                int curCount = hashMap.get(c);
                curCount += 1;
                hashMap.put(c, curCount);
            }
            else{
                hashMap.put(c, 1);

            }



            


        }

  /*       for (Map.Entry<Character, Integer> entry : hashMap.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
 */

        for(int i = 0; i < n; i ++)
        {
            int curCount = hashMap.get(s.charAt(i));

            if(curCount > maxCount)
            {
                secondMaxCount = maxCount;
                res = s.charAt(i);
                maxCount = curCount;
            }
        }

       System.out.println("The second most frequest character is: "+ res);


    }
}