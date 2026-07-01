import java.util.Arrays;
import java.util.Scanner;

public class Kruskals {
    static int parent[];
    static int find(int i){
        if (parent[i]==i){
            return i;
        }
        return find(parent[i]);
    }
    static void union(int i,int j){
        int i1=find(i);
        int j1=find(j);
        if(i1!=j1){
            parent[i1]=j1;
        }
    }

    static int krushkalMst(int v,int[][] edges)
    {
        parent=new int[v];
        for(int i=0;i<v;i++)
        {
            parent[i]=i;
        }
        Arrays.sort(edges,(a,b)->a[2]-b[2]);
        int cost=0;
        int count=0;
        for(int i=0;i<edges.length;i++)
        {
            int x=edges[i][0];
            int y=edges[i][1];
            int w=edges[i][2];
            int x1=find(x);
            int y1=find(y);
            if(x1!=y1)
            {
                union(x,y);
                cost=cost+w;
                count++;
                if(count==v-1)
                    break;
            }
        }
        return cost;
    }
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        System.out.println("Enter no of vertices");
        int v=sc.nextInt();
        int m=sc.nextInt();
        int edges[][]=new int[m][3];
        for(int i=0;i<m;i++)
        {
            edges[i][0]=sc.nextInt();
            edges[i][1]=sc.nextInt();
            edges[i][2]=sc.nextInt();

        }
        int ans=krushkalMst(v,edges);
        System.out.println(ans);

        
    }
    
}
