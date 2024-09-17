class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health;
        int attackCursor = 0;
        int healStack = 0;
        for(int i = 1; i <= attacks[attacks.length-1][0]; i++){
            if(i == attacks[attackCursor][0]){ //  공격 받아야 함
                answer -= attacks[attackCursor][1];
                attackCursor++;
                healStack = 0;
                if(answer <= 0) return -1;
            }else{ // 회복 가능
                answer = Math.min(health, answer + bandage[1]); // 초당 회복
                healStack++;
                if(healStack == bandage[0]) {
                    answer = Math.min(health, answer + bandage[2]);
                    healStack = 0;
                }
            }
            // System.out.println(answer);
        }
        return answer;
    }
}