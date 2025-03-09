#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	ans=[]
    	def rec(N):
        	if N==1 or N==0:
        	    return 1
        	return N*rec(N-1)
        	
    	for i in range(1,n+1):
    	    f=rec(i)
    	    #print(f)
    	    if f<=n:
    	        ans.append(f)
    	    else:
    	        break
    	return ans
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends