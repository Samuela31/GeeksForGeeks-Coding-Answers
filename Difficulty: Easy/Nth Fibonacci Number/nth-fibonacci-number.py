
class Solution:
    def nthFibonacci(self, n : int) -> int:
        mod = 1000000007
    
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n==2:
            return 1
        
        a, b = 1, 1
        for i in range(3, n + 1):
            temp=a
            a = b
            b = (temp + b) % mod
        
        return b
        






#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.nthFibonacci(n)

        print(res)

        print("~")

# } Driver Code Ends