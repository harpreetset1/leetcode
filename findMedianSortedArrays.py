

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        merged = []
        num1_ctr=0
        num2_ctr = 0
        for i in range(nums1_len+nums2_len):
            #print(nums1[num1_ctr],nums2[num2_ctr])
            if(num1_ctr < nums1_len and  num2_ctr < nums2_len):
                if(nums1[num1_ctr]< nums2[num2_ctr]):
                    merged.append(nums1[num1_ctr])
                    num1_ctr = num1_ctr+1
                else:
                    merged.append(nums2[num2_ctr])
                    num2_ctr=num2_ctr+1
            elif(num1_ctr>=nums1_len and num2_ctr < nums2_len):
                merged.append(nums2[num2_ctr])
                num2_ctr=num2_ctr+1
            elif(num2_ctr>=nums2_len and num1_ctr < nums1_len):
                merged.append(nums1[num1_ctr])
                num1_ctr=num1_ctr+1
            #print(num1_ctr,nums1[num1_ctr],num2_ctr,nums2[num2_ctr])    
        median = 0.0
        mid_pt = int(len(merged)/2)
        if(len(merged)%2 ==1):
            median = merged[mid_pt]
        else:    
            median = (merged[mid_pt-1]+merged[mid_pt])/2
        #print(mid_pt,median, merged)            
        return median

s = Solution()        
print(s.findMedianSortedArrays([1,2],[ 1,3,4,5]))            