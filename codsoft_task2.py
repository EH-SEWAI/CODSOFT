print("Basic Calculator")

a = input("First number: ")
b = input("Second number: ")

try:
    a = float(a)
    b = float(b)
except:
    print("Only numbers allowed.")
    quit()

print("Choose operation (+, -, *, /)")
op = input("Your choice: ")

if op == "+":
    ans = a + b
elif op == "-":
    ans = a - b
elif op == "*":
    ans = a * b
elif op == "/":
    if b == 0:
        print("Divide by zero error.")
        quit()
    ans = a / b
else:
    print("Invalid operation.")
    quit()

print("Answer:", ans)