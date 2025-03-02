#User function Template for python3
import math

class Solution:
    def sumOfDivisors(self, n):
        if n == 1:
            return 1
    
        total_sum = 1  # Sum of divisors
        for i in range(2, n + 1):
            sum_i = 0  # Sum of divisors for i
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    sum_i += j
                    if j != i // j:  # Avoid adding square roots twice (e.g., j=3 for i=9)
                        sum_i += i // j
            total_sum += sum_i
    
        return total_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends