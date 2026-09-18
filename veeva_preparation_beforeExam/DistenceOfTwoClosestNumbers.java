import java.util.*;
public class DistenceOfTwoClosestNumbers {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter n");
        int n=sc.nextInt();

        System.out.println("Enter elments");
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        int min=Integer.MAX_VALUE;
        for(int i=1;i<arr.length;i++)
        {
            if(Math.abs(arr[i]-arr[i-1]) < min) min=Math.abs(arr[i]-arr[i-1]);
        }
        if(min==Integer.MAX_VALUE)
            System.out.println("-1");
        else
        System.out.println(min);

    }
    
}
