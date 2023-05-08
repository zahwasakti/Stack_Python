# deklarasi function
def IsEmpty():
    if len(stack) == 0:
        print(True)
    else:
        print(False)

max_stack = 6

# deklarasi list
stack = []

"""
1.
Bila dilakukan PUSH 3 elemen kedalam stack
kemudian di PUSH lagi 2 elemen
dan di POP 3 elemen.
Maka dimana posisi Top of Stack?
"""

# PUSH 3 elemen kedalam stack
print("-----PUSH 3 elemen kedalam stack-----")
# Elemen ke-1 
stack.append(1)

print("\nElemen masuk -> '1'")
print("data sekarang", stack)

# Elemen ke-2 
stack.append(2)

print("\nElemen masuk -> '2'")
print("data sekarang", stack)

# Elemen ke-3 
stack.append(3)
print("\nElemen masuk -> '3'")
print("data sekarang", stack)


# PUSH 2 elemen pada stack
print("\n-----PUSH 2 elemen pada stack-----")
# Elemen ke-4
stack.append(4)

print("\nElemen masuk -> '4'")
print("data sekarang", stack)

# Elemen ke-5 
stack.append(5)
print("\nElemen masuk -> '5'")
print("data sekarang", stack)

# POP 3 elemen
print("\n-----POP 3 elemen kedalam stack-----")

keluar1=stack.pop()

print("\nElemen keluar ->", keluar1 )
print("data sekarang", stack)

keluar2=stack.pop()

print("\nElemen keluar ->", keluar2 )
print("data sekarang", stack)

keluar3=stack.pop()

print("\nElemen keluar ->", keluar3 )
print("data sekarang", stack)

# Posisi Top of Stack
print("\n-------Posisi Top of Stack-------")
top_of_stack = stack[-1]
print("Posisi Top of Stack =", top_of_stack)
print("Jumlah Stack =", len(stack))
print("Max Stack = ", max_stack)




"""
2.
IsEmpty pada kondisi terkahir adalah
"""
print("\nKondisi Terakhir:")
print(stack)

# IsEmpty pada kondisi terakhir
print("\nIsEmpty pada kondisi terakhir:")
IsEmpty()


"""
3.
Berapa elemen yang harus di PUSH
untuk mencapai kokndisi penuh
Top of Stack = max_stack
"""

print("\n----Top of Stack = max_stack----")

print("Jumlah Stack saat ini =", len(stack))
print("Max Stack = ", max_stack)

# melakukan PUSH elemen agar kondisi Top of Stack = max_stack
stack.append(3)

print("\nElemen masuk -> '3'")
print("data sekarang", stack)

stack.append(4)

print("\nElemen masuk -> '4'")
print("data sekarang", stack)

stack.append(5)

print("\nElemen masuk -> '5'")
print("data sekarang", stack)

stack.append(6)

print("\nElemen masuk -> '6'")
print("data sekarang", stack)

print("\nJumlah Stack saat ini =", len(stack))
print("Max Stack = ", max_stack)


"""
4.
Berapa elemen yang harus di POP
untuk mencapai kondisi
IsEmpty = True
"""

# melakukan POP pada elemen di dalam stack[]
print("\n----POP----")

pop1=stack.pop()

print("\nElemen keluar ->", pop1 )
print("data sekarang", stack)

pop2=stack.pop()

print("\nElemen keluar ->", pop2 )
print("data sekarang", stack)

pop3=stack.pop()

print("\nElemen keluar ->", pop3 )
print("data sekarang", stack)

pop4=stack.pop()

print("\nElemen keluar ->", pop4 )
print("data sekarang", stack)

pop5=stack.pop()

print("\nElemen keluar ->", pop5 )
print("data sekarang", stack)

pop6=stack.pop()

print("\nElemen keluar ->", pop6 )
print("data sekarang", stack)


# mengecek IsEmpty stack[]
print("\nIsEmpty pada kondisi terakhir:")
IsEmpty()


