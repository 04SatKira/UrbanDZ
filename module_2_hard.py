import random
def stone():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    stone_number = random.choice (numbers)
    return stone_number
stone_number = stone()
print ('Камень №:', stone_number)
print ('------------------------------')
input ('Нажмите "+" для генерации шифра:')
set=[]
for i in range (1, 20):
    for j in range (1, 20):
        if stone_number % (i + j) == 0 and i != j:
            set.append(i)
            set.append(j)
print ('------------------------------')
for i in range (0, len(set),2):
    for j in range (i+2, len(set),2):
        if set[i] == set[j + 1] and set[i +1] == set[j]:
            set.pop(j)
            set.pop(j)
            break
result = ''.join(str(item) for item in set)
print('Слишком древний шифр:', result)
