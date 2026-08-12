class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        k=2
        d={}
        for r in range(len(fruits)):
            ch=fruits[r]
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
            while len(d)>k:
                lval=fruits[l]
                d[lval]-=1
                if d[lval]==0:
                    d.pop(lval)
                l+=1 
            ans=max(ans,r-l+1)   
        return ans             