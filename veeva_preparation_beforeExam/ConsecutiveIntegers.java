public class ConsecutiveIntegers {
    public static void main(String[] args) {
        String s="abcd123efgh456";
        int sum=0;
        int c=0;






        
        for(int i=0;i<s.length();i++)
        {
            char ch=s.charAt(i);
            if(Character.isDigit(ch))
            {
                StringBuilder sb=new StringBuilder();
                while(i<s.length() && Character.isDigit(s.charAt(i)))
                {
                    sb.append(s.charAt(i));
                    i++;
                    
                }
                sum +=Integer.valueOf(sb.toString());
                c++;
            }
        }
        
        System.out.println("sum : "+sum);
        System.out.println("avg is :" +sum/c );
    }
    
}
