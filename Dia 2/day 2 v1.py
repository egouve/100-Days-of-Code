#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

porcentagem_gorjeta = tip / 100
gorjeta_total = bill * porcentagem_gorjeta
conta_total = bill + gorjeta_total
conta_por_pessoa = conta_total / people
valor = round(conta_por_pessoa, 2)

print(f"Each person should pay: ${valor}")
