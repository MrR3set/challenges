class RingBuffer:
    def __init__(self,maxCapacity):
        self.maxCapacity = maxCapacity
        self.storage = []
        self.old = 0
        
    def insert(self,value):
        if len(self.storage) < self.maxCapacity:
            self.storage.append(value)
        else:
            self.storage.pop(self.old)
            self.storage.insert(self.old,value)
            self.old+=1
            if self.old >= self.maxCapacity:
                self.old = 0

    def __str__(self):
        return f'{self.storage}'
