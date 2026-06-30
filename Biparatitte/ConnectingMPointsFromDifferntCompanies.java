import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

class EarliesstMovementWhenEveryIneBecomeFriends {
    int n;
    int parent[];
    HashMap<Integer,ArrayList<Integer>> hm=new HashMap<>();

    EarliesstMovementWhenEveryIneBecomeFriends(int n){
        this.n=n;
        parent=new int[n];
        for (int i = 0; i<n;i++){
            parent[i]=i;
        }
    }
    int find(int i){
        if (parent[i]==i){
            return i;
        }
        return find(parent[i]);
    }
    void union(int i,int j){
        int i1=find(i);
        int j1=find(j);
        if(i1!=j1){
            parent[i1]=j1;
        }
    }
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n");
        int n = sc.nextInt();
        System.out.println("Enter m");
        int m=sc.nextInt();
        List<List<Integer>> arr=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            List<Integer> arr1=new ArrayList<>();

            System.out.println("Enter list values");
            System.out.println("Enter u ,v,time values");
            int u=sc.nextInt();
            int v=sc.nextInt();
            int time=sc.nextInt();
            arr1.add(u);
            arr1.add(v);
            arr1.add(time);
            arr.add(arr1);
        }
        Collections.sort(arr,(a,b)->a.get(2)-b.get(2));
        
       

    }
    
}






