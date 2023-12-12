class IO:
    def __init__(self) -> None:
        self.busy = False
        self.servingPCB = None

    def decrementCurrentProcess(self):
        """
        Decrements the current IO burst time of the process being served.
        """
        if self.servingPCB is not None:
            self.servingPCB.decrementIoBurst()

    def loadProcess(self, pcb):
        """
        Loads a process onto the IO device.
        """
        self.servingPCB = pcb
        self.busy = True  # Mark the IO device as busy

    def unloadProcess(self):
        """
        Unloads the process from the IO device and returns it.
        """
        if self.servingPCB is not None and self.servingPCB.isIoBurstComplete():
            finished_process = self.servingPCB
            self.servingPCB = None
            self.busy = False  # Mark the IO device as available
            return finished_process
        return None

    def isBusy(self):
        """
        Returns True if the IO device is currently busy.
        """
        return self.busy
