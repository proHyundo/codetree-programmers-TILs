import java.util.*;

class Solution {
    
    public static long computeTotalTime(int[] diffs, int[] times, long limit, int level) {
        long totalTime = 0;
        int n = diffs.length;
        totalTime += times[0];

        for (int i = 1; i < n; i++) {
            if (diffs[i] <= level) {
                totalTime += times[i];
            } else {
                int mistakes = diffs[i] - level;
                long timeForMistakes = (long) (times[i] + times[i - 1]) * mistakes;
                totalTime += timeForMistakes + times[i];
            }
            if (totalTime > limit) {
                return totalTime;
            }
        }
        return totalTime;
    }
    
    public int solution(int[] diffs, int[] times, long limit) {
        int n = diffs.length;
        int maxDiff = 0;
        for (int diff : diffs) {
            maxDiff = Math.max(maxDiff, diff);
        }

        int low = 1;
        int high = maxDiff + 1;

        while (low < high) {
            int mid = (low + high) / 2;
            long totalTime = computeTotalTime(diffs, times, limit, mid);
            if (totalTime <= limit) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}