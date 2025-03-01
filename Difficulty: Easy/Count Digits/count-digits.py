#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        if n<10:
            return 1 #2 divides 2, 9 divides 9, single digit nums divide itself
            
        cnt=0
        num=n
        
        while num>0:
            rem=num%10
            if rem!=0 and n%rem==0: #cant divide by 0
                cnt+=1
                
            num=num//10
            
        return cnt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends