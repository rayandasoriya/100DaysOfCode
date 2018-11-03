class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int count = 0;
        int i = 0;
        while(i<n-2&&nums[i]==0)i++;
        for(int k=n-1; k>1; k--){
            int r = k-1;
            int l = i;
            while(l<r){
                while(l<r&&nums[l]+nums[r]<=nums[k])l++;
                count += r-l;
                r--;
        }
        }
        return count;
}
};
