class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            val=1
            temp=[]
            for j in range(i+1):
                temp.append(val)   
                val=val*(i-j)//(j+1)
            ans.append(temp) 
        return ans    