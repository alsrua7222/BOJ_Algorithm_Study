import time

class Times:
    def __init__(self) -> None:
        self.start = time.time()
        self.end = None
        self.elapsed = None
        return
    
    def get_start(self) -> float:
        return self.start
    
    def get_end(self) -> float:
        return time.time() - self.start
    
    def getStopwatch(self) -> float:
        return f"{round(self.get_end(), 3)} Second"
