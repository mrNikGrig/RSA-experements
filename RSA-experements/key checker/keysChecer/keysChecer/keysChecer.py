keys = [5, 173, 247,
        11, 21191, 47053,
        5, 20069, 50621,
        5, 30917, 51983,
        5, 42317, 53357,
        3, 53515, 80851,
        3, 115795, 174541]
for i in range(6):
    e = keys[0 + (3*i)]
    d = keys[1 + (3*i)]
    m = keys[2 + (3*i)]
    for i in range(300):
        ei = (i ** e) % m
        di = (ei ** d) % m
        if (di != i):
            print('error keys:')
            print(e)
            print(d)
            print(m)
            break
print("complit")