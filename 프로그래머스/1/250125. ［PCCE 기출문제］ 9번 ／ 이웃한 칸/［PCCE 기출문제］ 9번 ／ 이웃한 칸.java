class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        String target = board[h][w];
        int[] dxs = {0,1,0,-1};
        int[] dys = {1,0,-1,0};
        
        for (int i = 0; i < 4; i++){
            int nx = h + dxs[i];
            int ny = w + dys[i];
            if(nx >= 0 && nx < board.length && ny >= 0 && ny < board.length){
                if(board[nx][ny].equals(target)) answer++;
            }
        }
        return answer;
    }
}