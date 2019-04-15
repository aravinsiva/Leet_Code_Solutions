from numpy import *
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        final=[]
        
        while(i<len(nums1) and j<len(nums2)):
            
            if(nums1[i]<=nums2[j]):
                final.append(nums1[i])
                i+=1
                
                
            elif(nums1[i]>nums2[j]):
                final.append(nums2[j])
                j+=1
                
        
        for x in range(i,len(nums1)):
            final.append(nums1[x])
            i+=1
        
        for y in range (j,len(nums2)):
            final.append(nums2[y])
            j+=1
            
        return (float(median(final)))
        
        