
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check_char_in_substring( c: str, s:str) -> bool:
            if(len(c)>1):
                for x in range(len(c)):
                    if(c[x] in c[x+1:len(c)]):
                        return False
            if(c in s):
                return True
            else:
                return False    
        i = 0
        j = 1
        maxlen = 1
        if(len(s)==0):
            return 0
        if(len(s)==len(set(s))):
            print(s)
            return len(s)
        
        while(j <= len(s)):
            st = s[i:j]
            if(check_char_in_substring(st,s)):
                if(len(st) > maxlen):
                    maxlen = len(st)
                print(st)
                j=j+1
            else:
                i=i+1
        
        return maxlen

s = Solution()        
print(s.lengthOfLongestSubstring("pwwkew"))            