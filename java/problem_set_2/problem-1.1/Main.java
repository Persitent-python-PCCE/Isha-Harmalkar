import java.util.List;
import java.util.ArrayList;

class Main{
    public static void main(String args[]){

        int[] nums = {4, 7, 2, 9, 6, 3, 8, 1};
        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();
        

        for(int i = 0; i < nums.length; i++)
        {
            //odd -> move it forward
            if((nums[i] % 2) == 1)
            {
                odd.add(nums[i]);

            }else{
                even.add(nums[i]);
            }
        }


        List<Integer> res = new ArrayList<>(even);
        res.addAll(odd);

        System.out.println(res);

    }
}