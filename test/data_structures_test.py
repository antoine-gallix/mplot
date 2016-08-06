import context
context.set_path()
from mplot.data_structures import CircularList


def test_clist_create_empty():
    cl = CircularList()
    assert cl == []


def test_clist_create_from_list():
    l = [1, 2, 3]
    cl = CircularList(l)
    assert cl == l


def test_index_wrap():
    cl = CircularList([1, 2, 3])
    assert cl[0] == 1
    assert cl[1] == 2
    assert cl[2] == 3
    assert cl[3] == 1
    assert cl[1000] == 2
    assert cl[-1] == 3
    assert cl[-4] == 3


def test_enumerate():
    l = [1, 2, 3]
    cl = CircularList(l)
    l2 = [0, 0, 0, 0, 0]
    for i, e in cl.enumerate():
        l2[i] += e
    assert l2 == [1, 2, 3, 0, 0]
