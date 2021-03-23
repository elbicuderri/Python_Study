class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted([*nums1, *nums2])
        L = len(nums3)
        if L == 0:
            return 0.0000
        
        elif L % 2 == 1:
            return nums3[L // 2]
        
        else:
            return (nums3[(L//2) - 1] + nums3[(L//2)]) / 2.0