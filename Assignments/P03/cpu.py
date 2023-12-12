class CPU:
    def __init__(self):
        self.busy = False
        self.runningPCB = None
        self.executionTime = 0

    def incrementExecutionTime(self):
        self.executionTime += 1

    def decrementCurrentProcess(self):
        self.runningPCB.decrementCpuBurst()

    def loadProcess(self, pcb):
        self.runningPCB = pcb

    def KickOff(self):
        if self.runningPCB.getCurrentBurstTime() == 0:
            self.busy = False
            item = self.runningPCB
            self.runningPCB = None
            return item
    def unloadProcess(self):
      
        finishedProcess = self.runningPCB
        self.runningPCB = None
        self.busy = False  # Mark the CPU as not busy
        return finishedProcess
