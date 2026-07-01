import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class TopologicalSortUsingDFS {
    

    public static ArrayList<Integer> toplogicalSort(ArrayList<ArrayList<Integer>> arr,int n)
    {
        boolean visited[]=new boolean[n];
        Stack<Integer> st=new Stack<>();
        ArrayList<Integer> arr1=new ArrayList<>();
        for(int i=n-1;i>=0;i--)
        {
            if(!visited[i])
            {
                dfs(i,visited,arr,st);
            }
        }
        while (!st.isEmpty()) {
            arr1.add(st.pop());
            
        }
        return arr1;
    }
    public static void dfs(int s,boolean[] visited,ArrayList<ArrayList<Integer>> arr,Stack<Integer> st)
    {
        visited[s]=true;
        for(int x:arr.get(s))
        {
            if(!visited[x])
                dfs(x,visited,arr,st);
        }
        st.push(s);


    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter no of elements");
        int n=sc.nextInt();
        System.out.println("Enter no of edgess");
        int k=sc.nextInt();
        ArrayList<ArrayList<Integer>> arr=new ArrayList<>();
        for (int i = 0; i < n; i++) 
        {
            arr.add(new ArrayList<>());
        }
        
        System.out.println("Enter edges u and v:");
        for (int i = 0; i < k; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            arr.get(u).add(v); 
        }
        ArrayList<Integer> res=toplogicalSort(arr,n);
        for(int x:res)
        {
            System.out.print(x);
        }
    }
}

