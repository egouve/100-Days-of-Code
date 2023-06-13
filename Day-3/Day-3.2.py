#Exercício 3.2 pede que calcule o IMC de uma pessoa de acordo com peso e altura, e retorne sua situação

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
IMC = (round(weight/height**2))
if IMC <= 18.5:
    print(f"Your BMI is {IMC}, you are underweight.")
elif IMC <= 25:
    print(f"Your BMI is {IMC}, you have a normal weight.")
elif IMC <= 30:
    print(f"Your BMI is {IMC}, you are slightly overweight.")
elif IMC <= 35:
    print(f"Your BMI is {IMC}, you are obese.")
elif IMC > 35:
    print(f"Your BMI is {IMC}, you are clinically obese.")

