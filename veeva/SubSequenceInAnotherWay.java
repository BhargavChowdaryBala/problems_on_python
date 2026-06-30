
import java.util.*;


public class SubSequenceInAnotherWay {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        System.out.println("Enter sequence");
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter subsequence");
        int k=sc.nextInt();
        int[] sub=new int[k];
        for(int i=0;i<k;i++)
        {
            sub[i]=sc.nextInt();
        }
        boolean temp=false;
        int j=0;
        for(int i=0;i<n;i++)
        {
            if(j==k)
                break;
            if(arr[i]==sub[j])
            {
                j++;
            }
        }
        if(j==k)
        {
            System.out.println("true");

        }
        else
            System.out.println("false");

    }
    
}
