class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        set1 = set(arr)
        arr1 = list(set1)
        arr1.sort()
        if len(arr1) <= 1:
            return -1
        else:
            return arr1[-2]
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends