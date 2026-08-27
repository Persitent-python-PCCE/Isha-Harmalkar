import java.util.HashSet;
import java.util.Set;


public class Main{
    public static void main(String[] args) {
        int[] nums = {100, 4, 200, 1, 3, 2};
        Set<Integer> mySet = new HashSet<>();
        int res = 0;

        int n = nums.length;
        for(int i = 0; i < n; i++)
        {
            mySet.add(nums[i]);
            
        }

        for(int i = 0; i < n; i++)
        {
            int curNum = nums[i];
            int cur = 1;

            while (mySet.contains(curNum + 1))
            {
                curNum = curNum + 1;
                cur += 1;
            }

            res = Math.max(res, cur);

        }

        System.out.println("The longest sequesnce is: " + res);


        

        




    }
}