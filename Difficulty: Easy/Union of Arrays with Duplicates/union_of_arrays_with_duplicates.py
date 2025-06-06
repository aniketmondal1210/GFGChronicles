#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        set_a = set(a)
        set_b = set(b)
        union_set = set_a.union(set_b)
        return len(union_set)

#{
  # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]

        ob = Solution()
        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends
