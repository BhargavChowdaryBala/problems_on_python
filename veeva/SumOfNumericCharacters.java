import java.util.Scanner;

public class SumOfNumericCharacters {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        int sum=0;
        for(int i=0;i<s.length();i++)
        {
            if(Character.isDigit(s.charAt(i)))
            {
                int j=i;
                StringBuilder sb=new StringBuilder();
                while(j<s.length() && Character.isDigit(s.charAt(j)))
                {
                    sb.append(s.charAt(j));
                    j++;

                }
                i=j-1;
                String sb1=sb.toString();
                sum=sum+Integer.valueOf(sb1);
            }
        }
        System.out.println(sum);
    }
    
}
