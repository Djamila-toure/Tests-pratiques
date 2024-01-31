def compute_JoinPoint(s1, s2):
    while s1 != s2:
        s1a = str(s1)
        s2a = str(s2)
        somme1 = 0
        somme2 = 0
        for i in s1a:
            somme1 += int(i)
        for i in s2a:
            somme2 += int(i)

        s1 += somme1
        s2 += somme2
    print(s1, s2)


compute_JoinPoint(471, 480)