#import pdb; pdb.set_trace()
w=int()
z=str()
k=str()

n=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_')

a=int(input("digite de qual base queres converter: "))
b=int(input("digite para qual base queres converter: "))

#outras bases para decimal
if b==10:
    y = str(input("digite o numero: "))
    for i in range(len(y)):
        if y[-(i + 1)] != "0":
            for j in n:
                if j == y[-(i + 1)]:
                    break
                k = k + j
            w = w + (len(k) * (a ** i))
            k=""
    print(w)

#base  decimal para outras bases
elif a==10:
    y = int(input("digite o numero: "))
    while y > 0:
        z=(n[(y % b)] + z)
        y=(y // b)
    print(z)

#outras bases para outras bases
else:
    y = str(input("digite o numero: "))
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