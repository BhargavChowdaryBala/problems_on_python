import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SplitString {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        String s=sc.next();
        String arr[]=s.split(",");
        List<List<String>> res=new ArrayList<>();

        for(int i=0;i<arr.length;)
        {
            List<String> temp=new ArrayList<>();
            temp.add(arr[i]);
            temp.add(arr[++i]);
            i++;
            res.add(temp);
        }
        for(List<String> arr1:res)
        {
            System.out.print("["+arr1.get(0) + "," +arr1.get(1)+"]");
            System.out.println();
        }
    }
    
}
