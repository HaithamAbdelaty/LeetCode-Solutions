# Time:  O(n)
# space: O(1)

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def find_right_from_left(s, first, last, left):
            right, i = last[ord(s[left])-ord('a')], left
            while i <= right:
                if first[ord(s[i])-ord('a')] < left:
                    return -1
                right = max(right, last[ord(s[i])-ord('a')])
                i += 1
            return right
            
        first, last = [float("inf")]*26, [float("-inf")]*26
        for i, c in enumerate(s):
            first[ord(c)-ord('a')] = min(first[ord(c)-ord('a')], i)
            last[ord(c)-ord('a')] = max(last[ord(c)-ord('a')], i)
        result = [""]
        right = float("inf")
        for left, c in enumerate(s):
            if left != first[ord(c)-ord('a')]:
                continue
            new_right = find_right_from_left(s, first, last, left)
            if new_right == -1:
                continue
            if left > right:
                result.append("")
            right = new_right
            result[-1] = s[left:right+1]
        return result
