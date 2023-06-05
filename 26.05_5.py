et_tvery = []
for tiv in range(2, 10000):
    bajanararner = []
    for b in range(1, tiv//2 + 1):
        if tiv % b == 0:
            bajanararner.append(b)
    if sum(bajanararner) == tiv:
            et_tvery.append(tiv)
for tiv in et_tvery:
    print(tiv)

