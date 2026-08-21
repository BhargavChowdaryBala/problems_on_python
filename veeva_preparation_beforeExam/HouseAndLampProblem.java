import java.util.Scanner;

public class HouseAndLampProblem {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int hs=sc.nextInt();
        int ls=sc.nextInt();
        
        int h[]=new int[hs];
        int l[]=new int[ls];
        System.out.println("Enter indexes of houses");
        for(int i=0;i<hs;i++)
        {
            h[i]=sc.nextInt();
        }
        System.out.println("Enter indexes of lamps");
        for(int i=0;i<ls;i++)
        {
            l[i]=sc.nextInt();
        }
        int max1=Integer.MIN_VALUE;

        for(int i=0;i<h.length;i++)
        {
            int min=Integer.MAX_VALUE;
            for(int j=0;j<l.length;j++)
            {
                if(Math.abs(l[j]-h[i]) < min) min=Math.abs(l[j]-h[i]);
            }
            if(min>max1) max1=min;
        }
        System.out.println("range of lamp is "+max1);
    }
    
}
