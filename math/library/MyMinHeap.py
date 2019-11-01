import copy
import unittest

# 使用 list 实现 最小堆 （优先队列）
# Note：
# 堆与二叉排序树：
# 堆是为了实现排序的数据结构
# 堆的父节点小于（最小堆）其左右子节点，且堆通常是完全二叉树
# 二叉排序树是为了实现查找的数据结构
# 二叉排序树中父节点大于左节点小于右节点


class MyHeap(object):
    def __init__(self, obj_list=None):
        super().__init__()
        self.Nodes = []

        if obj_list:
            # for obj in obj_list:
            #     self.Push(obj)
            self.Nodes = copy.deepcopy(obj_list)
            self.__Sort()

    # parent = (i+1)//2-1
    # left_child = i*2+1
    # right_child = i*2+2
    def Push(self, obj):
        self.Nodes.append(obj)
        index = self.GetSize()-1
        while index > 0:
            iparent = (index+1)//2-1
            if self.Nodes[iparent] > self.Nodes[index]:
                self.Nodes[index], self.Nodes[iparent] = self.Nodes[iparent], self.Nodes[index]
                index = iparent
            else:
                break

    def Pop(self):
        if self.IsEmpty():
            return None
        obj = self.Nodes[0]
        self.Nodes[0] = self.Nodes[-1]
        self.Nodes.pop()  # size - 1
        self._FallDown(0)
        return obj

    def IsEmpty(self):
        return False if self.Nodes else True

    def GetSize(self):
        return len(self.Nodes)

    def _FallDown(self, index=0):
        max_index = self.GetSize()-1
        while index*2+1 <= max_index:
            child_index = index*2+1
            if child_index < max_index and self.Nodes[child_index] > self.Nodes[child_index+1]:
                child_index = child_index+1
            if self.Nodes[child_index] < self.Nodes[index]:
                self.Nodes[child_index], self.Nodes[index] = self.Nodes[index], self.Nodes[child_index]
                index = child_index
            else:
                break

    def __Sort(self):
        max_index = self.GetSize()
        for i in range(max_index//2,-1,-1):
            self._FallDown(i)
        pass
    

class TestMyHeap(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.array = [3,4,2,7,8,13,9,33,12,1]

    def assert_MinHeap(self, heap):
        lenth = heap.GetSize()
        for i in range((lenth-1)//2):
            if i*2+1 < lenth:
                self.assertTrue(heap.Nodes[i] < heap.Nodes[i*2+1])
            if i*2+2 < lenth:
                self.assertTrue(heap.Nodes[i] < heap.Nodes[i*2+2])
    def test_init(self):
        l1 = self.array
        lenth = len(l1)
        a = MyHeap(l1)
        self.assertEqual(lenth, a.GetSize())
        self.assert_MinHeap(a)

    def test_empty(self):
        a = MyHeap()
        self.assertTrue(a.IsEmpty())
        a.Push(3)
        self.assertFalse(a.IsEmpty())
        a.Pop()
        self.assertTrue(a.IsEmpty())

    def test_pop(self):
        l1 = self.array
        l2 = sorted(l1)
        a = MyHeap(l1)
        for n in l2:
            self.assertEqual(n, a.Pop())
            self.assert_MinHeap(a)

    def test_push(self):
        l1 = self.array
        a = MyHeap()
        for n in l1:
            a.Push(n)
            self.assert_MinHeap(a)


if __name__ == '__main__':
    unittest.main()