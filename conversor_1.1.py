n=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_')

a=int(input("type from wich base you want to convert: "))
b=int(input("type to wich base tou want to convert: "))

def o_t_d(y):
  k=str();w=int()
  for i in range(len(y)):
    for j in n:
      if j == y[-(i + 1)]:
        break
      k = k + j
    w = w + (len(k) * (a ** i))
    k=""
  return(w)

def d_t_o(y):
  z=str()
  while y > 0:
    z=(n[(y % b)] + z)
    y=(y // b)
  return(z)

if b==10:
  print(o_t_d(str(input("type the number: "))))

elif a==10:
  print(d_t_o(int(input("type the number: "))))

else:
  print(d_t_o(o_t_d(str(input("type the number: ")))))
