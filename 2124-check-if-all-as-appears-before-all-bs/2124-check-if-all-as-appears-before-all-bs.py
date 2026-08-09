class Solution:
    def checkString(self, s: str) -> bool:
        seen_b=False
        for ch in s:
            if seen_b and ch=="a":
                return False
            if ch=="b":
                seen_b=True    
        return True        