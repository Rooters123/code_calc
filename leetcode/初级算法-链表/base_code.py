# encoding = utf-8
class Node(object):
    """链表的节点"""
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLink(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        # 链表是否为空
        return self._head == None
    def length(self):
        # 链表长度
        if self.is_empty():
            return 0
        cursor = self._head
        count = 1
        while cursor.next != None:
            count += 1
            cursor = cursor.next
        return count


    def travel(self):
        # 遍历整个链表
        cursor = self._head
        pre = None
        while cursor != None:
            print(cursor.item)
            pre = cursor
            cursor = cursor.next
    def prepend(self,item):
        # 链表头部添加元素
        nd = Node(item)
        nd.next = self._head
        self._head = nd

    def append(self,item):
        # 链表尾部添加元素
        """尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos, item):

        # 指定位置添加元素
        if pos <= 0:
            self.prepend(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cursor = self._head
            nd = Node(item)
            while count + 1 < pos :
                cursor = cursor.next
                count += 1
            nd.next = cursor.next
            cursor.next = nd

    def remove(self,item):
        # 删除节点
        cursor = self._head
        pre = None
        while cursor != None:
            if cursor.item == item:
                if not pre:
                    self._head = None
                else:
                    pre.next = cursor.next
                break
            else:
                pre = cursor
                cursor = cursor.next

    def search(self,item):
        # 查找节点是否存在

        cursor = self._head
        count = 0
        while cursor:
            if item == cursor.item:
                return count
            else:
                cursor = cursor.next
        return -1



if __name__ == "__main__":
    ll = SingleLink()
    ll.append(5)
    ll.prepend(5)
    ll.prepend(5)
    ll.prepend(5)
    ll.insert(1,4)
    ll.travel()
    # print(ll.length())

