# -*- coding: utf-8 -*-
def make_multiset(l):
    return {x : l.count(x) for x in set(l)}

def ordered_dict(d):
    return sorted(d.items())

def reversed_dict(d):
    return { d[k] : k for k in d }

def unique_objects(l):
    unique = []
    [unique.append(i) for i in l if all((not i is k for k in unique))]
    return len(unique)
    #return len(set([id(x) for x in l]))
