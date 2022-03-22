import math
import random
prime_numbers = [211, 223, 227, 229, 233, 347, 503]
'''             8377, 8221, 8269, 8369, 8039, 8377, 8353, 8431, 8423, 8269, 8039, 8209, 8447, 8501, 8273,
                8419, 8231, 8171, 8237, 8237, 8039, 8093, 8243, 8431, 8377, 8081, 8297, 8363, 8069, 8389,
                8429, 8291, 8209, 8167, 8219, 8101, 8317, 8447, 8233, 8123, 8111, 8363, 8039, 8287, 8353,
                8501, 8369, 8101, 8069'''
'''def swap_numbers ():
    arr = []
    arr = input().split()
    size = len(arr) - 1
    for i in range(size):
        rand = random.randint(0, size)
        prime_numbers[i] = arr[rand]'''



for i in range(len(prime_numbers) - 1):
    n = prime_numbers[i] * prime_numbers[i + 1]
    f = (prime_numbers[i] - 1) * (prime_numbers[i+1] - 1)
    e = 2
    #print("part 1 confirm")
    while math.gcd(e, f) != 1:
        e += 1
        if e > f:
            print("error")
    #print("part 2 confirm")
    d = 0
    while (d * e) % f != 1:
        d+=1
    #print("complite")
    print (str(e) + " " + str(d) + " " + str(n))

