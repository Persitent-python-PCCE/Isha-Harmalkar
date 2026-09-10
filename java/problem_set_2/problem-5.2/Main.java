import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Main{
    public static void main(String[] args) {
        List<Integer> nums = List.of(2, 3, 4, 5, 6, 7, 8, 9, 10, 11);

        Map<Boolean, List<Integer>> partioned = nums.stream()
                .collect(Collectors.partitioningBy(Main:: isPrime));
        

        List<Integer> primes = partioned.get(true);
        List<Integer> nonPrimes = partioned.get(false);

        System.out.print("Primes: " + primes);
        System.out.print("Non Primes: " + nonPrimes);
        
        
    }

    public static boolean isPrime(int n) {
        if(n <= 1) return false;

        for(int i = 2; i <= Math.sqrt(n); i++){
            if(n % i == 0) return false;
        }

        return true;
        
    }
}