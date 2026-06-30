import java.util.*;

public class FloodFillAlgorithm {
    public static int[][] floodfill(int[][] img,int sc,int sr,int newcol)
    {
        if(img[sr][sc]==newcol)
            return img;
        int m=img.length;
        int n=img[0].length;
        int oldcol=img[sr][sc];
        dfs(img,sr,sc,m,n,oldcol,newcol);
        return img;
    }
    public static void dfs(int[][] img,int x ,int y,int m,int n,int oldcol,int newcol)
    {
        if(x<0 || y<0 || x>=m || y>=n || img[x][y]!=oldcol)
            return;
        img[x][y]=newcol;
        dfs(img,x+1,y,m,n,oldcol,newcol);
        dfs(img,x-1,y,m,n,oldcol,newcol);
        dfs(img,x,y+1,m,n,oldcol,newcol);
        dfs(img,x,y-1,m,n,oldcol,newcol);
    }
    public static void main(String args[])
    {
        Scanner sc1=new Scanner(System.in);
        System.out.println("Enter no of rows");
        int n=sc1.nextInt();
        System.out.println("Enter no of columns");
        int m=sc1.nextInt();
        System.out.println("Enter elements");
        int img[][]=new int[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                img[i][j]=sc1.nextInt();
            }
        }
        System.out.println("Enter source row");
        int sr=sc1.nextInt();
        System.out.println("Enter source colunm");
        int sc=sc1.nextInt();
        System.out.println("Enter new color");
        int newcolor=sc1.nextInt();
        int[][] res=floodfill( img, sc,sr,newcolor);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                System.out.print(res[i][j]);
            }
            System.out.println("");
        }

    }
    
}
