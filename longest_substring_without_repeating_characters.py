class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        sub_i = 0
        max_len =0
        sub_set = dict()
        sub_str = str()

        for a in s:
            if a in sub_set.keys():
                index = sub_set[a]
                for ii in range(sub_i, index+1, 1):
                    sub_set.pop(s[ii])
                sub_set[a] = i
                sub_i = index + 1
                sub_str = s[sub_i:i+1]
            else :
                sub_set[a] = i
                sub_str += a
                max_len_tmp =len(sub_str)
                if max_len_tmp > max_len:
                    max_len = max_len_tmp
            i += 1

        return max_len


ss=Solution()
print (ss.lengthOfLongestSubstring("abccccaefabchgdefeaaa"))
