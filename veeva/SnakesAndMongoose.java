import java.util.*;
import java.lang.*;
import java.io.*;

class SnakesAndMongoose
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t!=0)
		{
		    t--;
		    String s1=sc.next();
		    char arr[]=s1.toCharArray();
		    int s=0;
		    int m=0;
		    for(char ch:arr)
		    {
		        if(ch=='s') s++;
		        else m++;
		    }
		    
		    for(int i=0;i<arr.length;i++)
		    {
		        if(arr[i]=='m')
		        {
		            if( i-1>=0 && arr[i-1]=='s')
		            {
		                s--;
		                arr[i-1]='*';
		            }
		            else if(i+1<arr.length && arr[i+1]=='s')
		            {
		                s--;
		                arr[i+1]='*';
		            }
		        }
		    }
		    if(s==m) System.out.println("tie");
		    else if(m>s) System.out.println("mongooses");
		    else System.out.println("snakes");
		}

	}
}
