class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        half = len(nums1) // 2
        return (nums1[half] + nums1[~half]) / 2
