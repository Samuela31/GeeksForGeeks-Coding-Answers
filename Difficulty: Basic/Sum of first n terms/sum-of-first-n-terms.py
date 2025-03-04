#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        s=0
        def rec(n,s):
            if n<1:
                #print(s)
                return s
            s+=n**3
            return rec(n-1,s)
            
        return rec(n,s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends