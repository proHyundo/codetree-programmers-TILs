class Solution {
    
    public boolean isPossible(int[] wallet, int[] bill){
        if((wallet[0] >= bill[0] && wallet[1] >= bill[1]) ||
          (wallet[0] >= bill[1] && wallet[1] >= bill[0])){
            return true;
        }
        return false;
        
    }
    
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        while(true){
            if(isPossible(wallet, bill)) break;
            // 더 큰 쪽을 접고, answer += 1
            if(bill[0] > bill[1]){
                bill[0] = (int) bill[0] / 2;
            }else{
                bill[1] = (int) bill[1] / 2;
            }
            answer += 1;
        }
        return answer;
    }
}
    