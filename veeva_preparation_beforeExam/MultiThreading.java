/**
 * MultiThreading
 */
class Counter{
    int n;
    public synchronized void inc()
    {
        n++;
    }
}
public class MultiThreading  {
    public static void main(String[] args) throws Exception{

        Counter c=new Counter();
        Thread t1=new Thread(()->{
            for(int i=0;i<100;i++)
                c.inc();;
        });
         Thread t2=new Thread(()->{
            for(int i=0;i<100;i++)
                c.inc();
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(" counter is "+ c.n);
    }

    
}