class Queue:
    def __init__(self, queueType=None):
        self.queue = []
        self.queueType = queueType

    def __str__(self):
        return ",".join([str(pcb.pid) for pcb in self.queue])

    def addPCB(self, pcb):
        """
        Adds a PCB to the queue.
        """
        self.queue.append(pcb)

    def removePCB(self):
        """
        Removes and returns the first PCB from the queue.
        """
        return self.queue.pop(0) if self.queue else None

    def decrement(self):
        """
        Iterates over the queue and decrements the appropriate burst time
        for each PCB.
        """
        for pcb in self.queue:
            if self.queueType == 'IO':
                pcb.decrementIoBurst()
            elif self.queueType == 'CPU':
                pcb.decrementCpuBurst()

    def increment(self, what='waittime'):
        """
        Iterates over the queue and increments the appropriate waiting time
        for each PCB.
        """
        if what == 'waittime':
            for pcb in self.queue:
                pcb.incrementWaitQueueTime()
        elif what == 'runtime':
            for pcb in self.queue:
                pcb.incrementReadyQueueTime()

    def isEmpty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.queue) == 0

    def peek(self):
        """
        Returns the first PCB in the queue without removing it.
        """
        return self.queue[0] if self.queue else None
