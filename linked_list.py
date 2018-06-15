# 链表
# 定义节点
class Node(object):
     """单链表的节点"""
     def __init__(self, data):
        # 储存数据元素
        self.data = data

        # 储存下一个节点的位置
        self.next = None



class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # 定义计数
        count = 0
        # 定义游标
        cur = self.__head
        while cur != None:
            # print("链表内元素:[{}]".format(cur.data))
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
        """头插法"""
        # 在头部创建一个新节点
        # 1.创建一个新节点
        # 2.将新指针指向之前的头节点所对应的链接域
        # 3.将头指针指向新节点的链接域
        node = Node(data)
        node.next = self.__head
        self.__head = node


    def append(self, data):
        """尾插法"""
        # 1.创建一个新节点
        # 2.将旧尾节点指向新节点对应的链接部
        # 3.新节点的链接部指向空节点None
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.next = None

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
        cur = self.__head
        pre = None
        while cur != None:
            # 查询待删除的节点
            if cur.data == data:
                # 1.待删除的节点就是头节点
                if cur == self.__head:
                    self.__head = cur.next
                # 2.待删除的节点是普通节点
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
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
    li = SingleLinkList()
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