#{
  # Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    # Your code here
    s.add(element)
    
    
# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Your code here
    s.discard(element)
    
    
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    # Your code here
    return sum(s)



# {
  # Driver Code Starts.

# Driver Code
def main():
    # Testcase input
    testcase = int(input())

    # looping through testcases
    while testcase > 0:
        query = int(input())
        st = {int(x) for x in input().split()}

        while query > 0:
            q = input().split()

            if q[0] == 'i':
                element = int(q[1])
                insert(st, element)
                for i in sorted(st):
                    print(i, end=' ')
                print()

            if q[0] == 'r':
                element = int(q[1])
                remove_from_set(st, element)
                for i in sorted(st):
                    print(i, end=' ')
                print()

            if q[0] == 's':
                print(sum_set(st))

            query -= 1

        testcase -= 1
        print("~")

if __name__ == '__main__':
    main()
# Driver Code Ends
