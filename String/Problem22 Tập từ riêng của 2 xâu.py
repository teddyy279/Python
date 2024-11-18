if __name__ == '__main__':
    s = input().lower()
    t = input().lower()
    a = set(s.split())
    b = set(t.split())
    unique_words = a.difference(b)
    print(' '.join(sorted(unique_words)))
