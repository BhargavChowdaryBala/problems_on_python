import java.util.*; 

public class check_BipartiteGraph { 
    static boolean isBipartite(List<List<Integer>> g, int n) { 
        int color[] = new int[n]; 
        for(int i = 0; i < n; i++) { 
            color[i] = -1; 
        } 
        for(int i = 0; i < n; i++) { 
            if(color[i] == -1) { 
                if(dfs(g, i, 0, color) == false) return false; 
            } 
        } 
        return true; 
    } 

    static boolean dfs(List<List<Integer>> g, int s, int col, int color[]) { 
        color[s] = col; 
        for(int x : g.get(s)) { 
            if(color[x] == -1) { 
                if(dfs(g, x, 1 - col, color) == false) return false; 
            } else if(color[x] == col) return false; 
        } 
        return true; 
    } 

    static void addEdge(List<List<Integer>> adj, int u, int v) { 
        adj.get(u).add(v); 
        adj.get(v).add(u); 
    } 

    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        
        System.out.println("Enter number of vertices:");
        int n = sc.nextInt(); 
        
        List<List<Integer>> g = new ArrayList<>(); 
        for (int i = 0; i < n; i++) g.add(new ArrayList<>()); 
        
        System.out.println("Enter number of edges:"); 
        int k = sc.nextInt(); 
       
        System.out.println("Enter all adges u,v");
        for(int i = 0; i < k; i++) { 
            int u = sc.nextInt(); 
            int v = sc.nextInt(); 
            addEdge(g, u, v); 
        } 
        
        System.out.println("Is Bipartite: " + isBipartite(g, n)); 
        sc.close();
    } 
}
