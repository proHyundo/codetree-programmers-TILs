class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int min_a = 0;
        int min_b = 0;
        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] > sizes[i][1]){
                min_a = Math.max(min_a, sizes[i][0]);
                min_b = Math.max(min_b, sizes[i][1]);
            }else{
                min_a = Math.max(min_a, sizes[i][1]);
                min_b = Math.max(min_b, sizes[i][0]);
            }   
        }
        return min_a * min_b;
    }
}