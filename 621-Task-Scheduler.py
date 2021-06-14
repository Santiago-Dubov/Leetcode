from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks: return 0
        
        counter = Counter(tasks)
        
        x = max(counter.values())
        y = sum([1 for i in counter.values() if i == x])
        
        return max((n+1)*(x-1) + y, len(tasks))