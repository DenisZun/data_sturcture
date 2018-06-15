# python双向链表
class Node(object):
    """双向链表的节点"""
    def __init__(self, data):
        # data为节点的元素域
        # pre为节点的头链接部
        # next为节点的尾链接部
        self.data = data
        self.pre  = None
        self.next = None

class DoubleLinkedList(object):
    """双向链表"""
    def __init__(self, node=None):
        """双向链表的头指针"""
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # 定义计数
        # 定义游标
        count = 0
        cur = self.__head
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print("链表内元素:{}".format(cur.data))
            cur = cur.next

    def add(self, data):
        # 在头部创建一个新节点
        # 1.创建一个新节点
        # 2.将新节点的next指向旧头节点的pre
        # 3.将旧头节点的pre指向新节点的next
        # 4.头指针指向新节点
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, data):
        """尾插法"""
        # 1.创建一个新节点
        # 2.将旧尾节点next指向新节点pre
        # 3.将新尾节点pre指向旧节点next
        # 4.新节点的链接部指向空节点None
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            cur.pre = cur
            node.next = None

    def insert(self, pos, data):
        """在指定位置插入元素"""
        if pos <= 0:
            # 头部插入
            self.add(data)
        elif pos > self.length()-1:
            # 尾部插入
            self.append(data)
        else:
            node = Node(data)
            # 计数
            count = 0
            # 游标
            cur = self.__head
            while count < (pos - 1):
                cur = cur.next
                count += 1
            node.pre = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def remove(self, data):
        """删除节点"""
        cur = self.__head
        while cur != None:
            # 查询待删除的节点
            if cur.data == data:
                # 1.待删除的节点就是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.pre = None
                # 2.待删除的节点是普通节点
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                return
            else:
                cur = cur.next

    def search(self, data):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.data == data:
                print("查询{}成功".format(data))
                return "查询结果为:{}".format(True)
            cur = cur.next
        return "查询结果为:{}".format(False)

if __name__ == '__main__':
    li = DoubleLinkedList()
    li.add("a")
    li.add(2)
    li.append(3)
    li.insert(2, 4)
    print("链表长度为:{}".format(li.length()))
    li.travel()
    li.remove(2)
    print("链表长度为:{}".format(li.length()))
    li.travel()
    print(li.search(3))



