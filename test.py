name = input("Vad heter du?")
age = int(input("Hur gammal är du?"))

print("Hej ", name)

if age > 48:
    print("Gamling")
else:    
    print("Ungdom")

for i in range(1,age):
    print("Varv ", i)
