import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        List<Integer> lst = new ArrayList<>();
        
        int before = arr[0];
        lst.add(before);
        
        for(int i = 1; i < arr.length; i++){
            if(arr[i] != before){
                lst.add(arr[i]); 
                before = arr[i];
            }
        }
        
        int[] iarr = new int[lst.size()];
        for(int i = 0; i < lst.size(); i++){
            iarr[i] = lst.get(i);
        }
        return iarr;
        
    }
}