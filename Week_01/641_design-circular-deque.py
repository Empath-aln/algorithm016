# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_q0HxI4xdpENe9oyuJUOi5AsoIq_I92w
"""

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dq = [None] * k    # 初始化队列   
        self.capacity = k   # 队列容量
        self.sz = 0     #队列实际长度
        self.frt = 0    # 头部指针 (0不代表队列中的元素 代表位置)
        self.lst = 0    # 尾部指针
        
        # 代码中比较tricky的一点是，做操作后有些参数（isEmpty, isFull）并未及时更新，但是之后调用时，可以递归更新出来

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        
        if self.isEmpty():
            self.frt = 0
            self.lst = 0
            self.dq[self.frt] = value
            self.sz += 1 
            return True
        if not self.isFull():
            self.frt = (self.frt - 1) % self.capacity
            self.dq[self.frt] = value
            self.sz += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            self.frt = 0
            self.lst = 0
            self.dq[self.lst] = value
            self.sz += 1
            return True
        if not self.isFull():
            self.lst = (self.lst + 1) % self.capacity
            self.dq[self.lst] = value
            self.sz += 1
            return True
        return False

        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.dq[self.frt] = None
            self.frt = (self.frt + 1) % self.capacity
            self.sz -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.dq[self.lst] = None
            self.lst = (self.lst - 1) % self.capacity
            self.sz -= 1
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dq[self.frt]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.dq[self.lst]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.sz == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.sz == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()