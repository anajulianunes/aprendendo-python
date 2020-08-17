import random
a1 = str(input('Type the first student: '))
a2 = str(input('Type de second student: '))
a3 = str(input('Type de third student: '))
a4 = str(input('Type de fourth student: '))
students = [a1, a2, a3, a4]
random.shuffle(students)
print('A ordem é {}'.format(students))


