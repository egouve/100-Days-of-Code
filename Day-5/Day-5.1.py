# Exercício para descobrir a média de altura dos alunos usando o for loop. Proibido usar sum() e len()

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

altura = 0
for altura_estudante in student_heights:
    altura += altura_estudante

media = round(altura / (n+1))

print(media)