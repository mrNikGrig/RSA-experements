e = 5
d = 20069
m = 50621
def encrypt():
    text = input("please enter your massege\n")
    numKode = []
    for i in text:
        numKode.append((ord(i) ** e) % m)
    return numKode

def decrypt():
    i = int(input("enter u code for decryption close u message \"0\"\n"))
    encrMessage = []
    while i!=0:
        encrMessage.append(i)
        i = int(input())
    for i in encrMessage:
        print(chr((i ** d) % m), end="")




cmd = int(input("u want encrypt(0) or decrypt(1)\n"))
if cmd == 0:
    arr = encrypt()
    for i in arr:
        print(i)
elif cmd == 1:
    decrypt()
else:
    print("wrong comand\n")
