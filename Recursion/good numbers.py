class Solution:
    mod=10**9 + 7
    @staticmethod
    def pow(base,exponent,mod):
        if exponent == 0:
            return 1
        half = Solution.pow(base,exponent//2,mod)
        half = (half * half )% mod
        if exponent % 2 == 0:
            return half
        else:
            return (half * base) % mod

        
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = (n)//2
        part1 = Solution.pow(5,even,Solution.mod)
        part2 = Solution.pow(4,odd,Solution.mod)
        return (part1 * part2) % Solution.mod
            


