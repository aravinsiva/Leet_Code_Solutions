import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int current=0;
        int max=0;
        
        Hashtable<Integer,Character> table= new Hashtable<Integer,Character>(); 
    
        
       for (int i=0; i<s.length();i++){
           for (int j=i; j<s.length();j++){
              if (table.contains(s.charAt(j))){
                  break;
              }
                current++;
                  table.put(j,s.charAt(j));
           }
                   
          if (current>=max)
            max=current;
           current=0;
        table=new Hashtable<Integer,Character>();  
       }
       
         
        
        return max;
}
}