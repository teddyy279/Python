if __name__ == '__main__':
    s = input()
    t = input()
    set1 = set(s)
    set2 = set(t)
    giao = set1.intersection(set2)
    hop = set1.union(set2)
    print(''.join(sorted(giao)))
    print(''.join(sorted(hop)))
