# 单项循环链表
# 定义节点
class Node(object):
     """单链表的节点"""
     def __init__(self, data):
        # 储存数据元素
        self.data = data

        # 储存下一个节点的位置
        self.next = None

class CircleLinkedList(object):
    """双向循环链表"""
    def __init__(self, node=None):
        """双向链表的头指针"""
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """获取列表长度"""
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
                count += 1
        print("链表的长度为:{}".format(count))
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur.next != self.__head:
            print("链表内元素:{}".format(cur.data))
            # 游标向右移动
            cur = cur.next
        print("链表内元素:{}".format(cur.data))


    def add(self, data):
        """头插法"""
        # 在头部创建一个新节点
        # 1.创建一个新节点
        # 2.将新指针指向之前的头节点所对应的链接域
        # 3.将头指针指向新节点的链接域
        node = Node(data)

        if self.is_empty():
            self.__head = node
            node.next = node

        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node


    def append(self, data):
        """尾插法"""
        # 1.创建一个新节点
        # 2.将旧尾节点指向新节点对应的链接部
        # 3.新节点的链接部指向空节点None
        node = Node(data)

        if self.is_empty():
            self.__head = node
            node.next = node

        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, data):
        """在指定位置插入元素"""
        if pos <= 0:
            # 头部插入
            self.add(data)
        elif pos >= self.length():
            # 尾部插入
            self.append(data)
        else:
            node = Node(data)
            # 计数
            count = 0
            # 游标
            cur = self.__head
            while count < (pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, data):
        """删除节点"""
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur != self.__head:
            # 查询待删除的节点
            if cur.data == data:
                # 1.待删除的节点就是头节点
                if cur == self.__head:
                    # rear为游标指向的最后一个结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = cur.next

                # 2.待删除的节点是普通节点
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 最后一个结点还没有进行比较
        # 最后一个结点需要删除
        if cur.data == data:
            # 退出循环了，如果cur还是指向head说明就只要一个元素
            if cur == self.__head:
                #只有一个结点
                self.__head = None
            else:
                #链表有多个结点
                pre.next = self.__head

    def search(self, data):
        """查找节点是否存在"""
        cur = self.__head
        while cur != self.__head:
            if cur.data == data:
                print("查询{}成功".format(data))
                return "查询结果为:{}".format(True)
            else:
                cur = cur.next

        if cur.data == data:
            print("查询{}成功".format(data))
            return "查询结果为:{}".format(True)
        else:
            return "查询结果为:{}".format(False)

if __name__ == '__main__':
    li = CircleLinkedList()
    li.add("a")
    li.add(2)
    li.append(3)
    li.insert(2, 4)
    li.length()
    li.travel()
    li.search(3)
    li.remove(2)
    print("链表长度为:{}".format(li.length()))
    li.travel()
    print(li.search(3))

