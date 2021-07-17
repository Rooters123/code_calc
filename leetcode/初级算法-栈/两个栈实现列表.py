# encoding = utf-8
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def addItem(self,item):
        # 装在stack1的最下面
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(item)

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1
    def deletItem(self):
        if not self.stack1:
            return -1
        return self.stack1.pop()