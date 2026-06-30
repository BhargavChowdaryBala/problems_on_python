import java.util.HashMap;
import java.util.Scanner;

public class FirstNonRepeatingCharacter {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();

        int n=s.length();
        HashMap<Character,Integer> hm=new HashMap<>();
        for(int i=0;i<n;i++)
        {
            char ch=s.charAt(i);
            hm.put(ch,hm.getOrDefault(ch,0)+1);
        }
        boolean temp=false;
        for(int i=0;i<n;i++)
        {
            if(hm.get(s.charAt(i))==1)
            {
                System.out.println(s.charAt(i));
                temp=true;
                break;
            }
        }
        if(!temp)
            System.out.println("-1");

    }
    
}
