

class Main {
    public static void main(String[] args)
    {
        String s = "aaabbccccd";
        String res = "";
        int n = s.length();
        res += s.charAt(0);
        res += "1";
        //res = a1
        //a
        

        for(int i = 1; i < n; i++)
        {   //System.out.println("At index" +i + "res currently: " + res );
            char curChar = s.charAt(i);
            char prevChar = s.charAt( i - 1);
            if  (curChar == prevChar)
            {
               int resLen = res.length();
               char lastCountChar =  res.charAt(resLen - 1);
               int lastCountInt  = Character.getNumericValue(lastCountChar) + 1;
               //System.out.println("the count is incremented befoer conv? :" + lastCountInt);

               //char newCount = Integer.parseInt(String.valueOf(lastCountInt));
               char newCount = Character.forDigit(lastCountInt, 10);
               //System.out.println("the count is incremented? :" + newCount);
               res = res.substring(0, resLen -1  );
               res += newCount;
            



                
  

            }

            else{
                res += s.charAt(i);
                res += "1";
                
            }
            
        }

        System.out.println("Res is :" + res);

    }
}