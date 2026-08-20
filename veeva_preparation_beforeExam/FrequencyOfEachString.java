import java.util.HashMap;
public class FrequencyOfEachString {

    public static void main(String[] args) {
        String s="Hello This is Index This is land of sacred rivers and rivers flow from west to east";

        String arr[]=s.split(" ");
        HashMap<String,Integer> hm=new HashMap<>();
        for(String x:arr)
        {
            hm.put(x,hm.getOrDefault(x, 0)+1);
        }

        for(String x:hm.keySet())
        {
            System.out.println( x + ":"+ hm.get(x));
        }

    }
    
}
