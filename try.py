# deklarasi function
def push(list, data):
    if len(list) <= 6:
        list.append(data)
        print("elemen masuk -->", data)
        print("data saat ini", list, "\n")
    else:
        print("Stack Penuh")

def pop(list):
    if len(list) == 0:
        print("Stack sudah kosong")
    else:
        keluar=list.pop()
        print("elemen keluar -->", keluar)
        print("data saat ini", list, "\n")

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
push(stack, 1)

# Elemen ke-2 
push(stack, 2)

# Elemen ke-3 
push(stack, 3)


# PUSH 2 elemen pada stack
print("\n-----PUSH 2 elemen pada stack-----")
# Elemen ke-4
push(stack, 4)

# Elemen ke-5 
push(stack, 5)

# POP 3 elemen
print("\n-----POP 3 elemen kedalam stack-----")

# pop ke-1
pop(stack)
# pop ke-2
pop(stack)
# pop ke-3
pop(stack)


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
# melakukan PUSH elemen agar kondisi Top of Stack = max_stack
print("Jumlah Stack saat ini =", len(stack))
print("Max Stack = ", max_stack)

# elemen ke-1
push(stack, 3)

# elemen ke-2
push(stack, 4)

# elemen ke-3
push(stack, 5)

# elemen ke-4
push(stack, 6)


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

# POP elemen ke-1
pop(stack)
# POP elemen ke-2
pop(stack)
# POP elemen ke-3
pop(stack)
# POP elemen ke-4
pop(stack)
# POP elemen ke-5
pop(stack)
# POP elemen ke-6
pop(stack)


# mengecek IsEmpty stack[]
print("\nIsEmpty pada kondisi terakhir:")
IsEmpty()


