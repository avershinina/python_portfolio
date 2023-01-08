class Solution:
    def romanToInt(self,s: str) -> int:
        # Dict with all roman number values.
        r_letters = {'I':1,'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}

        total = 0
        prev_char = None
        for c in reversed(s):
            if c == 'I' and prev_char == 'V':
                total -= 1
            elif c == 'I' and prev_char == 'X':
                total -= 1
            elif c == 'X' and prev_char == 'L':
                total -= 10
            elif c == 'X' and prev_char == 'C':
                total -= 10
            elif c == 'C' and prev_char == 'D':
                total -= 100
            elif c == 'C' and prev_char == 'M':
                total -= 100
            else:
                total += r_letters[c]
            prev_char = c
        
        return total

    def runningSum(self, nums: List[int]) -> List[int]:

        total_nums = len(nums)
        res = []
        res.append(nums[0])
        
        for n in range(2,total_nums+1):
            res.append(sum(nums[:n]))
            
        return res
    
    def pivotIndex(self, nums: List[int]) -> int:
        """ Given an array of integers nums, calculate the pivot index of this array.
        The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
        If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
        Return the leftmost pivot index. If no such index exists, return -1.
        """

        for i in range(len(nums)):

            right_nums = sum(nums[i+1:])
            left_nums = sum(nums[:i])

            if right_nums == left_nums:
                return i
            else:
                return -1
            
            
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
        Example: s = "egg", t = "add" -> True
        """
        
        # This code is not efficient because it calls the index() function twice for each character in the strings s and t. 
        # The index() function has a time complexity of O(n) because it needs to search through the entire string 
        # to find the index of the given character. 
        # Therefore, the time complexity of this code is O(n^2) because it calls index() twice for each character in the strings.
        
        
        # strings of different length can not be isomorphic
        if len(s) == len(t): 


            # Use index to collect indexes of letters
            for l in s:
                s_idxs.append(s.index(l))

            for l in t:
                t_idxs.append(t.index(l))


            # compare indexes
            if s_idxs == t_idxs:
                return True
            else:
                return False
        
        # If the length of s and t is not equal then return False
        else:
            return False
        
        
    def isSubsequence(self, s: str, t: str) -> bool:
        """Given two strings s and t, 
        return true if s is a subsequence of t, or false otherwise.
        A subsequence of a string is a new string 
        that is formed from the original string by deleting some 
        (can be none) of the characters 
        without disturbing the relative positions 
        of the remaining characters. 
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        
        s_pointer = 0
        t_pointer = 0

        my_substr = []

        while s_pointer < len(s) and t_pointer < len(t):

            if s_pointer == t_pointer:
                my_substr.append(s[s_pointer])
                s_pointer = s_pointer + 1
                t_pointer = t_pointer + 1
            else:
                t_pointer = t_pointer + 1
                
        if my_substr == list(s):
            return True
        else:
            return False


## Test roman to integers
s1='III'
s2='LVIII'
s3 = "CCCXLI"

S=Solution()
answer = S.romanToInt(s=s3)
print(answer)

## Test runningSum


## Test
s1=[1,2,3,4]
s2=[1,1,1,1,1]
s3 =[3,1,2,10,1]

S=Solution()
answer = S.romanToInt(s=s3)
print(answer)
