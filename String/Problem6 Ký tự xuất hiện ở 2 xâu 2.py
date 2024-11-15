if __name__ == '__main__':
    s1 = input()
    s2 = input()
    set_S1 = set(s1)
    set_S2 = set(s2)
    unique_S1 = set_S1.difference(set_S2)
    unique_S2 = set_S2.difference(set_S1)
    print(''.join(sorted(unique_S1)))
    print(''.join(sorted(unique_S2)))
