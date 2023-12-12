class PCB:
    def __init__(self, pid, bursts, at, priority):
        self.pid = pid
        self.priority = priority
        self.arrivalTime = at
        self.bursts = bursts
        self.currBurstIndex = 0  # Tracks the current burst index
        self.readyQueueTime = 0  # Time spent in the ready queue
        self.waitQueueTime = 0   # Time spent in the wait queue
        self.TAT = 0             # Turnaround time

    def decrementCpuBurst(self):
        """
        Decrements the current CPU burst time.
        """
        if self.isCpuBurst():
            self.bursts[self.currBurstIndex] -= 1

    def decrementIoBurst(self):
        """
        Decrements the current IO burst time.
        """
        if self.isIoBurst():
            self.bursts[self.currBurstIndex] -= 1

    def incrementBurstIndex(self):
        """
        Moves to the next burst in the sequence.
        """
        self.currBurstIndex += 2  # Assumes alternating CPU and IO bursts

    def incrementReadyQueueTime(self):
        """
        Increments the time spent in the ready queue.
        """
        self.readyQueueTime += 1

    def incrementWaitQueueTime(self):
        """
        Increments the time spent in the wait queue.
        """
        self.waitQueueTime += 1

    def getCurrentBurstTime(self):
        """
        Returns the current burst time (CPU or IO).
        """
        return self.bursts[self.currBurstIndex]

    def isCpuBurstComplete(self):
        """
        Checks if the current CPU burst is complete.
        """
        return self.isCpuBurst() and self.bursts[self.currBurstIndex] <= 0

    def isIoBurstComplete(self):
        """
        Checks if the current IO burst is complete.
        """
        return self.isIoBurst() and self.bursts[self.currBurstIndex] <= 0

    def hasMoreBursts(self):
        """
        Checks if there are more bursts after the current one.
        """
        return self.currBurstIndex < len(self.bursts) - 1

    def isCpuBurst(self):
        """
        Checks if the current burst is a CPU burst.
        """
        return self.currBurstIndex % 2 == 0

    def isIoBurst(self):
        """
        Checks if the current burst is an IO burst.
        """
        return self.currBurstIndex % 2 != 0
    
    def completeCurrentBurst(self):
        """ Completes the current burst and moves to the next burst index. """
        self.incrementBurstIndex()
