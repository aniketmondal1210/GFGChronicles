#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    num = 1
    # Loop to jump in powers of 2
    while(x>=num*num):
        ##Your code here
        
        print (num**2 , end = " ")
        num += 1
        ##Your code here


#{ 
 # Driver Code Starts.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
# } Driver Code Ends