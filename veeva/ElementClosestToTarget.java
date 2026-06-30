import java.util.*;

class ElementClosestToTarget{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter target");
        int k=sc.nextInt();
        int res=0;

        int min=Integer.MAX_VALUE;
        for(int i=0;i<n;i++)
        {

            if(Math.abs(arr[i]-k)<min)
            {
                min=Math.min(Math.abs(arr[i]-k),min);
                res=arr[i];

            }
        }
        System.out.println(res);
    }
}