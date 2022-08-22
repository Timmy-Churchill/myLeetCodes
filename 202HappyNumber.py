class Solution:
    def isHappy(self, n: int) -> bool:
        pastNumbers = []
        nextNumber = n
        while (nextNumber not in pastNumbers) and (nextNumber != 1):
            listeger = [int(x) for x in str(nextNumber)]
            pastNumbers.append(nextNumber)
            nextNumber = 0
            for number in listeger:
                nextNumber += number ** 2
                
        
        if nextNumber == 1:
            return True   





nineteen = Solution()

print(nineteen.isHappy(19))