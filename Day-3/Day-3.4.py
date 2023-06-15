#Exercício para calcular valor de uma pizza
# S = 15
# M = 20
# L = 25
# Peppersoni = +2 pra pequena e + 3 pra média/grande
# Queijo = +1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill +=3
    if extra_cheese == 'Y':
        bill += 1

print(f'Your final bill is: ${bill}.')