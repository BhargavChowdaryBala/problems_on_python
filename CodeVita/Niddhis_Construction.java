package CodeVita;
import java.util.*;
public class Niddhis_Construction {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
        int b[]=new int[n];
        String dir[]=new String[n];
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
            b[i]=sc.nextInt();
            dir[i]=sc.next();
        }
        int target=sc.nextInt();
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(a[i]>a[j] || (a[i]==a[j] && b[i]>b[j]))
                {
                    int temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;

                    temp=b[i];
                    b[i]=b[j];
                    b[j]=temp;
                    String s=dir[i];
                    dir[i]=dir[j];
                    dir[j]=s;
                }
            }
        }
         int x[]=new int[51];
        int y[]=new int[51];
        boolean present[]=new boolean[51];
        present[1]=true;
        x[1]=0;
        y[1]=0;
        for(int i=0;i<n;i++) 
        {
            int old=a[i];
            int nw=b[i];
            int nx=x[old];
            int ny=y[old];
            if (dir[i].equals("top"))
                ny++;
            else if (dir[i].equals("down"))
                ny--;
            else if (dir[i].equals("left"))
                nx--;
            else if (dir[i].equals("right"))
                nx++;
            for (int j=1;j<=50;j++) {
                if (present[j] && x[j] == nx && y[j]==ny) {
                    present[j]=false;
                    break;
                }
            }
            x[nw] = nx;
            y[nw] = ny;
            present[nw] = true;
        }
        int up=-1;
        int down=-1;
        int left=-1;
        int right=-1;
        for (int i=1;i<= 50; i++) 
            {
            if (!present[i]|| i == target)
                continue;
            if (x[i] ==x[target] && y[i] == y[target] + 1)
                up =i;
            else if (x[i]==x[target] && y[i] == y[target] - 1)
                down=i;
            else if (x[i] == x[target] - 1 && y[i] == y[target])
                left= i;
            else if (x[i] == x[target] + 1 && y[i] == y[target])
                right = i;
        }
        System.out.println(up+" "+down+" "+left+" "+right);
    }
    
}
