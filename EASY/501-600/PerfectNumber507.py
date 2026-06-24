class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num % 2 != 0:
        #     return False
        # lol = []
        # result = 0
        # for i in range(1,num // 2 +1):
        #     if num % i == 0:
        #         lol.append(i)

        # for i in lol:
        #     result = result + i
        
        # return result == num

        #time fail
        def is_prime(n):
            if n < 2:
                return False

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False

            return True

        p = 2
        result = 0

        while result < num:
            mersenne = (2 ** p) - 1
            if is_prime(p) and is_prime(mersenne):
                result = (2 ** (p - 1)) * mersenne

                if result == num:
                    return True

            p += 1

        return False




        class Solution:
            def checkPerfectNumber(self, num: int) -> bool:
                if num==1:
                    return False
                count=1
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        count+=i+num//i
                return num==count
        #this solution is best