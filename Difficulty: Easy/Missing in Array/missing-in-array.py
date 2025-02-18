#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        currsum=sum(arr)
        n=len(arr)+1 #add 1 because one number missing
        actualsum=(n*(n+1))//2
        ans= actualsum-currsum
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends