#User function Template for python3
import math 
class Solution:
    def isPrime (self, n):
        # Initialize a counter variable to
        # count the number of factors.
        cnt = 0
    
        # Loop through numbers from 1
        # to the square root of n.
        for i in range(1, int(math.sqrt(n)) + 1):
            # If n is divisible by i
            # without any remainder.
            if n % i == 0:
                # Increment the counter.
                cnt = cnt + 1
    
                # If n is not a perfect square,
                # count its reciprocal factor.
                if n // i != i:
                    cnt = cnt + 1
    
        # If the number of
        # factors is exactly 2.
        if cnt == 2:
             # Return true, indicating
             # that the number is prime.
            return 1
        # If the number of
        # factors is not 2.
        else: 
            # Return false, indicating
            # that the number is not prime.
            return 0





#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends