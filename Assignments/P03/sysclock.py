class SysClock:
    # Using a class attribute for shared state to implement the Singleton pattern.
    _shared_state = {}

    def __init__(self):
        # Ensuring that all instances share the same state.
        self.__dict__ = self._shared_state

        # Initialize the clock if it hasn't been already.
        if 'clock' not in self.__dict__:
            self.clock = 0

    def increment(self):
        """
        Increments the system clock by one unit.
        """
        self.clock += 1

    def getClock(self):
        """
        Returns the current value of the system clock.
        """
        return self.clock

    # Optionally, if you ever need to reset the clock
    def resetClock(self):
        """
        Resets the system clock back to zero.
        This might be useful for certain types of simulation scenarios.
        """
        self.clock = 0
