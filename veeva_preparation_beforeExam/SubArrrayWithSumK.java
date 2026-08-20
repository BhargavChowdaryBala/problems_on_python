
public class SubArrrayWithSumK {
    public static void main(String[] args) {
        int k=3;
    int arr[]={1,2,3,-5,1};
    int c=0;
    int s=0;
    int j=0,i=0;
    while(i<arr.length)
    {
        s=s+arr[i];
        while(s>k)
        {
            s -=arr[j];
            j++;
        }
        if(s==k)c++;
        i++;
        

    }
    System.out.println(c);
    }
}
