

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        int answer = 0;

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
        List<String> target = Arrays.asList(reader.readLine().split(""));

        for(int i = 0; i < N-1; i++){
            List<String> compare = Arrays.asList(reader.readLine().split(""));
            List<String> temp_target = new ArrayList<>(target);
            int diff_cnt = 0;

            for(String c : compare){
                if(temp_target.contains(c)){
                    temp_target.remove(c);
                }else{
                    diff_cnt++;
                }
            }

            if(diff_cnt < 2 && temp_target.size() < 2){
                answer++;
            }

        }

        System.out.println(answer);
    }
}
