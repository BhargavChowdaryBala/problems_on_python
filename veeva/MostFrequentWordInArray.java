import java.util.HashMap;
import java.util.Scanner;

public class MostFrequentWordInArray {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String arr[]=s.split(" ");
        int n=arr.length;
        HashMap<String,Integer> hm=new HashMap<>();
        for(String x:arr)
        {
            hm.put(x,hm.getOrDefault(x,0)+1);
        }
        String res="";
        int max=Integer.MIN_VALUE;
        for(int i=n-1;i>=0;i--)
        {
            if(hm.get(arr[i])>=max)
            {
                res=arr[i];
            }

        }
        System.out.println(res);
    }
    
}
