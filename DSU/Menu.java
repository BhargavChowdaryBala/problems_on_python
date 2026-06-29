import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

class DSU_Menu {
    int n;
    int parent[];
    HashMap<Integer,ArrayList<Integer>> hm=new HashMap<>();

    DSU_Menu(int n){
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
    int friendshipgrps()
    {
        HashSet<Integer> hs=new HashSet<>();
        for(int i=0;i<n;i++)
        {
            hs.add(find(i));
        }
        return hs.size();
    }
    void ElementsInAllGrp()
    {
        for(int i=0;i<n;i++)
        {
            int par=find(i);
            
            if(!hm.containsKey(par))
            {
                ArrayList<Integer> arr=new ArrayList<>();
                arr.add(i);
                hm.put(par,arr);

            }
            else{
                ArrayList<Integer> arr=hm.get(par);
                arr.add(i);
                hm.put(par,arr);
            }
        }
        for(int i:hm.keySet())
        {
            System.out.println(i + " : " + hm.get(i));
        }
    }
    void ElementsInParticularGrp(int key)
    {
        System.out.println("Elements in grp"+key+"are : "+hm.get(key));
    }
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        DSU_Menu obj = new DSU_Menu(n);
        while (true) {
            System.out.println("1.Add Friend Ship ! : ");
            System.out.println("2.Execute Query ! : ");
            System.out.println("3.How many Friendships groups : ");
            System.out.println("4.Persons in each group : ");
            System.out.println("5.Persons in particular group : ");
            System.out.println("6.Exit...");
            int ch = sc.nextInt();
            switch (ch) {
                case 1:
                    int a = sc.nextInt();
                    int b = sc.nextInt();
                    obj.union(a,b);
                    break;
                case 2:
                    int i = sc.nextInt();
                    int j = sc.nextInt();
                    int res = obj.find(i);
                    int res1=obj.find(i);
                    if (res==j||res1==i){
                        System.out.println("Friends..");
                    }
                    else{
                        System.out.println("Not Friends..");
                    }
                    break;
                case 3:
                    int res2=obj.friendshipgrps();
                    System.out.println("No of friendship  grps"+res2);
                    break;
                case 4:
                    obj.ElementsInAllGrp();;
                    break;
                case 5:
                    System.out.println("Enter the key of particular grp");

                    int a=sc.nextInt();
                    obj.ElementsInParticularGrp(a);
                    break;
                case 6:
                    System.exit(0);
                default:
                    break;
            }
        }

    }
    
}