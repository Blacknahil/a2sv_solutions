class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        min_time=0
        tasks.sort(reverse=True)
        processorTime.sort()
        tasks_pos=0
        for processor in processorTime:
            for _ in range(4):
                min_time=max(min_time,processor + tasks[tasks_pos])
                tasks_pos+=1
        return min_time

        