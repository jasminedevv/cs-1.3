#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s0 = Set()
        assert s0.keys() == []

        s1 = Set(1)
        assert len(s1.keys()) == 1
        assert s1.length() == 1
        assert s1.size == 1

        s2 = Set(['a', 'b', 'c'])
        assert len(s2.keys()) == 3
        assert s2.length() == 3
        assert s2.size == 3

        s3 = Set(['a', 'a', 'a'])
        assert len(s3.keys()) == 1
        assert s3.length() == 1
        assert s3.size == 1


    def test_contains(self):
        s0 = Set()
        assert s0.contains("anything") is False


    def test_add(self):
        s0 = Set()
        assert s0.contains("anything") is False
        s0.add("something")
        assert s0.contains("something") is True

        s1 = Set([1,2,3])
        assert s1.keys() == [1,2,3]
        s1.add(1)
        assert s1.keys() == [1,2,3]
        s1.add(4)
        assert s1.keys() == [1,2,3,4]


    def test_remove(self):
        s0 = Set()
        assert s0.contains(1) is False
        s0.add(1)
        assert s0.contains(1) is True
        s0.remove(1)
        assert s0.contains(1) is False

        s1 = Set([0.5, 3.4])
        assert s1.contains(0.5) is True
        s1.remove(0.5)
        assert s1.contains(0.5) is False


    def test_union(self):
        s1 = Set([1,2])
        s2 = Set([3,4])
        assert s1.union(s2).keys() == [1,2,3,4]


    def test_intersection(self):
        s1 = Set([1,2])
        s2 = Set([2,3])
        assert s1.intersection(s2).keys() == [2]


    def test_difference(self):
        s1 = Set([1,2])
        s2 = Set([2,3])
        assert s2.difference(s1).keys() == [1,3]


    def test_is_subset(self):
        s0 = Set()
        s1 = Set([1,2])
        s2 = Set([1,2,3,4])
        assert s1.is_subset(s2) == True
        assert s0.is_subset(s1) == True # emptiness is a subset of all things


if __name__ == '__main__':
    unittest.main()