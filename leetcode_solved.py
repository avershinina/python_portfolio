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

        for i in range(len(nums)):

            right_nums = sum(nums[i+1:])
            left_nums = sum(nums[:i])

            if right_nums == left_nums:
                return i
            else:
                return -1


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
