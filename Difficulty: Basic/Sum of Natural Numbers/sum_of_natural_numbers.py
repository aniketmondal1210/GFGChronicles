class Solution:
    def findSum(self, n):
        # code here
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum
