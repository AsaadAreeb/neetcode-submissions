class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counts = {}
        for number in nums:
            if number not in Counts:
                Counts[number] = 0
            Counts[number] += 1
        SortedCounts = sorted(Counts.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in SortedCounts[:k]]
