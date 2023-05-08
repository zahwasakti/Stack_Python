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
stack.append("a")

print("\nElemen masuk -> 'a'")
print("data sekarang", stack)

# Elemen ke-2 
stack.append("b")

print("\nElemen masuk -> 'b'")
print("data sekarang", stack)

# Elemen ke-3 
stack.append("c")
print("\nElemen masuk -> 'c'")
print("data sekarang", stack)


# PUSH 2 elemen kedalam stack
print("\n-----PUSH 2 elemen kedalam stack-----")
# Elemen ke-4
stack.append("d")

print("\nElemen masuk -> 'd'")
print("data sekarang", stack)

# Elemen ke-5 
stack.append("e")
print("\nElemen masuk -> 'e'")
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
stack.append('f')

print("\nElemen masuk -> 'f'")
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

keluar1=stack.pop()

print("\nElemen keluar ->", keluar1 )
print("data sekarang", stack)

keluar2=stack.pop()

print("\nElemen keluar ->", keluar2 )
print("data sekarang", stack)

keluar3=stack.pop()

print("\nElemen keluar ->", keluar3 )
print("data sekarang", stack)

keluar4=stack.pop()

print("\nElemen keluar ->", keluar4 )
print("data sekarang", stack)

keluar5=stack.pop()

print("\nElemen keluar ->", keluar5 )
print("data sekarang", stack)

keluar6=stack.pop()

print("\nElemen keluar ->", keluar6 )
print("data sekarang", stack)

# mengecek IsEmpty stack[]
print("\nIsEmpty pada kondisi terakhir:")
IsEmpty()


