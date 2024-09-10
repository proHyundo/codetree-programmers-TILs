import java.util.*;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        String[] varr = video_len.split(":");
        int i_video_len = Integer.parseInt(varr[0]) * 60 + Integer.parseInt(varr[1]);
        String[] parr = pos.split(":");
        int i_pos = Integer.parseInt(parr[0]) * 60 + Integer.parseInt(parr[1]);
        String[] sarr = op_start.split(":");
        int i_start = Integer.parseInt(sarr[0]) * 60 + Integer.parseInt(sarr[1]);
        String[] earr = op_end.split(":");
        int i_end = Integer.parseInt(earr[0]) * 60 + Integer.parseInt(earr[1]);
        
        
        for(int i = 0; i < commands.length; i++){
            // 현재 위치가 오프닝이라면 건너뛰기
            if(i_pos >= i_start && i_pos <= i_end) i_pos = i_end;
            
            // 명령어 수행
            if(commands[i].equals("next")){
                // 최대 끝 까지
                i_pos = Math.min(i_video_len, i_pos + 10);
            }else{
                i_pos = Math.max(0, i_pos - 10);
            }
        }
        // 명령어 끝낸 위치가 오프닝 이라면 건너뛰기
        if(i_pos >= i_start && i_pos <= i_end) i_pos = i_end;
        
        String miniute = ((int) i_pos / 60) + "";
        String seconds = i_pos % 60 + "";
        
        if(miniute.length() == 1) miniute = "0" + miniute;
        if(seconds.length() == 1) seconds = "0" + seconds;
        
        
        return miniute + ":" + seconds;
    }
}