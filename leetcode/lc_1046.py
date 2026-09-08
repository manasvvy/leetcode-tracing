class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)

        while len(stones) > 1:
            y = stones.pop(0)
            x = stones.pop(0)

            if x != y:
                stones.append(y - x)
                stones.sort(reverse=True)

        return stones[0] if stones else 0
