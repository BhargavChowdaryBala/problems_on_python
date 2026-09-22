public class Matrix {
    public static void main(String[] args) {
        int arr[][] = {
            {1, 5, 6}, 
            {2, 6, 3}, 
            {6, 8, 1}
        }; 




        
        int max=Integer.MIN_VALUE;
        int sum=0;
        for(int i=1;i<arr.length;i++)
        {
            if(sum==0 && arr[i][0] <arr[i-1][1])
            {
                sum+=arr[i][2]+arr[i-1][2];
            }
           else if(arr[i][0] <arr[i-1][1]) sum+=arr[i][2];
        }
        if(sum==0)
        {
            for(int i=0;i<arr.length;i++)
            {


                
                if(arr[i][2]>sum) sum=arr[i][2];
            }
        }
        System.out.println(sum);
    }
    
}
