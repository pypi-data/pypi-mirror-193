from collections import deque

class MaxQueue:
    '''
    在队列的基础上增加max_value函数，用于计算当前队列中的最大值
    '''

    def __init__(self):
        self.queue=deque()
        self.candidates=deque()

    def max_value(self) -> int:
        '''
        返回当前队列中的最大值
        '''
        if not self.queue:
            return -1
        else:
            return self.candidates[0]


    def push(self, value: int) -> None:
        '''
        将value加入到队尾
        '''
        self.queue.append(value)
        while self.candidates and self.candidates[-1]<value:
            self.candidates.pop()
        self.candidates.append(value)

    def pop(self) -> int:
        '''
        删除队首元素，并将其返回
        '''
        if not self.queue:
            return -1
        else:
            item=self.queue.popleft()
            if item==self.candidates[0]:
                self.candidates.popleft()
            return item
            

