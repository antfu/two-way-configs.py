import pytest
import biconfigs

change_count = 0
def test_list():
    global change_count

    def onchanged(list):
        global change_count
        change_count += 1

    orginal_list = ['orginal_vale', 2]
    l = biconfigs.Bilist(orginal_list, onchanged=onchanged)

    assert len(orginal_list) == len(l)

    for i in range(len(orginal_list)):
        assert l[i] == orginal_list[i]

    # Should not fire changed till now
    assert change_count == 0

    l.clear()
    assert len(l) == 0
    l.append(123)
    l.insert(0, 'insert-0')
    l.reverse()
    l[1] = 'reversed'
    l.remove(123)
    l.pop()
    l.append('value')
    del(l[0])

    assert change_count == 9

    assert len(l) == 0

changed_count = 0
def test_with():
    global changed_count
    changed_count = 0
    def onchanged(obj):
        global changed_count
        changed_count += 1

    l = biconfigs.Bilist([1, 2], onchanged=onchanged)

    assert changed_count == 0

    l.append(3)
    l.append(4)
    assert changed_count == 2

    with l:
        for i in range(5,10):
            l.append(i)

    assert changed_count == 3

def test_nested():
    nested_dict1 = {'key1':'value1'}
    nested_list1 = ['nested_list', 2, 3]
    orginal_list = [nested_dict1, nested_list1]
    l = biconfigs.Bilist(orginal_list)

    assert isinstance(l[0], biconfigs.Bidict)
    assert isinstance(l[1], biconfigs.Bilist)

    for k in nested_dict1.keys():
        assert l[0][k] == nested_dict1[k]

    for i in range(len(nested_list1)):
        assert l[1][i] == nested_list1[i]

    l.clear()
    l.append([])
    l.append({})
    assert isinstance(l[0], biconfigs.Bilist)
    assert isinstance(l[1], biconfigs.Bidict)
