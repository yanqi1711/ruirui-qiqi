package 搜索算法;

// 给定一个长度为 n 的非降序数组和一个非负数整数 k ，要求统计 k 在数组中出现的次数
public class GetNumberOfK {
    /**
     * 数字在升序数组中出现的次数
     */
    public int GetNumberOfK (int[] nums, int k) {

        return this.biSearch(nums, k + 0.5) - this.biSearch(nums, k - 0.5);
    }

    private int biSearch(int[] data, double k) {
        int left = 0;
        int right = data.length - 1;
        while(left <= right) {
            int mid = right - (right - left) / 2;
            if (data[mid] > k) {
                right = mid - 1;
            } else if (data[mid] < k) {
                left = mid + 1;
            }
        }
        return left;
    }
}
