a = int(input("Masukkan tinggi segitiga : "))

#segitiga siku 1
for i in range(1,a+1):
    print(i*"*")
print()
print(30*"=") #pemmbatas
print()
#segitiga siku 2
for i in range(1,a+1):
    print((a-i+1) *"*")
print()
print(30*"=") #pembatas
print()
#segitiga siku 3
for i in range(1,a+1):
    print(((a-i+1)*" ") +(i* "*"))
print()
print(30*"=")    
print()
#segitiga siku 4
for i in range(1,a+1):
    print((i*" ") + (a-i+1) * "*")
print()
print(30*"=")    
print()
#segitiga piramida
for i in range(1,a+1):
    print(((a-i+1)*" ") + (i*"*") + ((i-1)*"*"))
print()
print(30*"=")    
print()
#segitiga piramida 2
for i in range (1,a+1):
    print(((i*" ") + (a-i+1) * "*") + (a-i) *"*")