class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # O(klogn)
        res = heapq.nsmallest(k, arr, key=lambda e: abs(e - x))
        print(res)
        return sorted(res)
        
        # O(nlogn) - sort
#         res = []
#         start, end, length = 0, len(arr) - 1, len(arr)
    
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if arr[mid] < x:
#                 start = mid
#             else:
#                 end = mid

#         toRight = min(length, k + end)
#         toLeft = max(0, start - k)
#         rangeToSearch = arr[toLeft:toRight]

#         diff = [(abs(e - x), e) for e in rangeToSearch]
#         diff = sorted(diff)
#         diff = diff[:k] ## 前k個tuple

#         for _, x in diff:
#             res.append(x)
#         res = sorted(res) # O(klogk)
#         return res


        # if x <= arr[0]: return arr[:k]
        # if x >= arr[-1]: return arr[-k:]
        # l,r = 0, len(arr)-k
        # while l < r:
        #     m =(l+r)//2
        #     if x-arr[m]> arr[m+k]-x:
        #         l = m + 1
        #     else:
        #         r = m
        # return arr[l:l+k]
