import java.util.*;
class Solution {
    public boolean checkSub(int i, int j, String[][] park, int mat){
        for(int k = i; k < i + mat; k++){
            for(int q = j; q < j + mat; q++){
                if(k >= 0 && k < park.length && q >= 0 && q < park[0].length){
                    if(!park[k][q].equals("-1")){
                        return false;
                    }   
                } else {
                    return false;
                }
            }
        }
        return true;
    }
    
    public boolean checkAll(int mat, String[][] park){
        for(int i = 0; i <= park.length - mat; i++){
            for(int j = 0; j <= park[0].length - mat; j++){
                if(checkSub(i, j, park, mat)){
                    return true;
                }
            }
        }
        return false;
    }
    
    public int solution(int[] mats, String[][] park) {
        Arrays.sort(mats);
        int answer = -1;

        for(int mat : mats){
            if(checkAll(mat, park)){
                answer = mat;
            } else {
                break;
            }
        }
        return answer;
    }
}
