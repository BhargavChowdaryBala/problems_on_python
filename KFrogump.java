
public class KFrogump {
    public static void main(String[] args) {
        int arr[] = {30, 20, 50, 10, 40};
        int n = arr.length;
        int k = 3;

        int dp[] = new int[n];
        dp[0] = 0;

        for (int i = 1; i < n; i++) {
            int min = Integer.MAX_VALUE;

            for (int j = i - 1; j >= 0 && j >= i - k; j--) {
                int jump = dp[j] + Math.abs(arr[i] - arr[j]);
                min = Math.min(min, jump);
            }

            dp[i] = min;
        }

        System.out.println(dp[n - 1]);
    }
}




