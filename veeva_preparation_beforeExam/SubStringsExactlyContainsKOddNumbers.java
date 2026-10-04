import java.util.HashMap;
import java.util.Scanner;

class SubStringExactlyContainsKOddNumbers
{
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);

        int n=5;
        int k=3;
        int arr[]={1,1,2,1,1};
        int res=Atmostk(arr, n, k)-Atmostk(arr, n, k-1);
        System.out.println(res);

    }

    static int Atmostk(int[] arr,int n,int k)
    {

        int l=0;
        int count=0;
        int oddcount=0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]%2 !=0)
            {
                oddcount++;

            }
            while(oddcount> k)
            {
                if(arr[l]%2 !=0) oddcount--;
                    l++;    
            }
            count += i-l+1;
        }



        
        return count;
    }
}