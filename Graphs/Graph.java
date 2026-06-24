

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;
public class Graph{
    int M[][],n;
    Graph(int n){
        this.n=n;
        M=new int [n][n];
    }
    public void addEdge(int u,int v){
        M[u][v]=1;
        M[v][u]=1;
    }
    public void display(){
        for(int r[]: M){
            for (int x:r){
                System.out.print(x+" ");
            }
            System.out.println();
        }
    }
    public void dfs(int s,boolean visited[],List<Integer> res)
    {
        res.add(s);
        visited[s]=true;
        for(int i=0;i<n;i++)
        {
            if(M[s][i]==1 && !visited[i] )
            {
                dfs(i, visited, res);
            }

        }

    }
    public ArrayList<Integer> dfs_without_recursion(int s,boolean visited[],List<Integer> res)
    {
        Stack<Integer> st=new Stack<>();
        st.push(s);
        visited[s]=true;
        while(!st.isEmpty())
        {
            int st1=st.pop();
            res.add(st1);
            for(int i=0;i<n;i++)
            {
                if(M[s][i]==1 && !visited[i] )
                {
                    st.push(i);
                    visited[i]=true;
                }
            }
        }
        return res;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println(" Enter no.of vertices");
        int n = sc.nextInt();
        Graph g = new Graph(n);
        while (true) {
            System.out.println("Enter u and v values : ");
            int x = sc.nextInt();
            int y = sc.nextInt();
            g.addEdge(x, y);
            System.out.print("Enter -1");
            int val = sc.nextInt();
            if (val == -1){
                break;
            }
        }
        ArrayList<Integer> res=new ArrayList<>();
        System.out.println("Enter start index");
        int s=sc.nextInt();
        boolean visited[]=new boolean[n];
        res=g.dfs_without_recursion(s, visited, res);
        System.out.println(res);
        sc.close();
    }
}