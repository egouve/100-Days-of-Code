# Fazer um for loop que descubra qual número, dentro de uma lista, é o maior. Não pode ser usado max

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

pontuacao = 0
for score in student_scores:
  if pontuacao < score:
    pontuacao = score

print(f'A maior pontuação na classe é: {pontuacao}')