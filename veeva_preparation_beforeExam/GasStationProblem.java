class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
       int start=0,curramount=0,totalgas=0,totalcost=0;

       for(int i=0;i<gas.length;i++)
       {
        totalgas+=gas[i];
        totalcost+=cost[i];
        curramount += gas[i]-cost[i];
        if(curramount<0)
        {
            start=i+1;
            curramount=0;
        }
       }




       
       if(totalcost>totalgas) return -1;
       return start;

        
        
    }
}