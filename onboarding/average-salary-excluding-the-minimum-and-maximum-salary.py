class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        total_of = (total-max(salary)-min(salary))
        return (total_of/(len(salary)-2))