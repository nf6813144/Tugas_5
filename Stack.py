stack=[]

#push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)
print("stack setelah push: ", stack)

elemen=stack.pop()
print("elemen yang di pop pertama:", elemen)
print("stack setelah pop kedua :", stack)

elemen=stack.pop()
print("elemen yang di pop kedua:", elemen)
print("stack setelah pop:", stack)

if stack:
    print("elemen teratas:", stack[-1])
else:
    print("stack kosong")
