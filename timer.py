import time

class Timer:
    def __init__(self) -> None:
        self.start_time: int = 0

    def start(self) -> None:
        '''Starts the timer'''
        self.start_time: float = time.time()

    def stop(self) -> float:
        '''Stops the timer.
        Returns time in seconds with two decimals'''
        return round((time.time() - self.start_time), 2)
