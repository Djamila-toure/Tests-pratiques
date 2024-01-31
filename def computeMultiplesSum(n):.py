def computeMultiplesSum(n):
    liste1 = list(range(1,n))
    mul3 = []
    mul5 = []
    mul7 = []
    for i in liste1:
        if i % 3 == 0:
            mul3.append(i)
        if i % 5 == 0:
            mul5.append(i)
        if i % 7 == 0:
            mul7.append(i)

    liste_total = mul3 + mul5 + mul7
    liste_trie = sorted(liste_total)
    print(liste_trie)
    print(sum(liste_total))


computeMultiplesSum(11)