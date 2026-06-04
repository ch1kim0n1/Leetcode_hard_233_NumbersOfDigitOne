class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1

        while place <= n:
            lower = n % place
            current = (n // place) % 10
            higher = n // (place * 10)

            if current == 0:
                count += higher * place
            elif current == 1:
                count += higher * place + lower + 1
            else:
                count += (higher + 1) * place

            place *= 10

        return count
