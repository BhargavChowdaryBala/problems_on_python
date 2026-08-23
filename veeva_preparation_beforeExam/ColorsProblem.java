import java.util.*;
public class ColorsProblem {

    public static void main(String[] args) {
        String s="red,blue   ,yellow,green123,#12red,green,red";
        String arr[]=s.split(",");
        HashMap<String,Integer> hm=new HashMap<>();
        for(String ch:arr)
        {
            ch=ch.replaceAll("[^a-zA-Z]", " ");
            ch=ch.strip();
            hm.put(ch,hm.getOrDefault(ch, 0)+1);
        }
        for(String ch:hm.keySet())
        {
            System.out.println(ch + ":"+hm.get(ch));
        }


    }
    
}
