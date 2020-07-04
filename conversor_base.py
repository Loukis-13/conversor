w=int()
z=str()
k=str()

#base 64 utilized by Youtube
#can be increased or modified without needing to modify the rest of the code
n=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_')

a=int(input("type from wich base you want to convert: "))
b=int(input("type to wich base tou want to convert: "))

#others bases to decimal base
if b==10:
    y = str(input("type the number: "))
    for i in range(len(y)):
        if y[-(i + 1)] != "0":
            for j in n:
                if j == y[-(i + 1)]:
                    break
                k = k + j
            w = w + (len(k) * (a ** i))
            k=""
    print(w)

#decimal base to others bases
elif a==10:
    y = int(input("type the number: "))
    while y > 0:
        z=(n[(y % b)] + z)
        y=(y // b)
    print(z)

#any base to any base
else:
    y = str(input("type the number: "))
    for i in range(len(y)):
        if y[-(i + 1)] != "0":
            for j in n:
                if j == y[-(i + 1)]:
                    break
                k = k + j
            w = w + (len(k) * (a ** i))
            k=""

    while w > 0:
        z=(str(w % b) + z)
        w=(w // b)
    print(z)
