#author sahaj Singh
import random
with open("50-states") as outFile:
    dit = dict()
    l = list()
    data = outFile.read()
    data2 = data.split('\n')
    for i in data2:
        key,val = i.split(',')
        dit[key.strip()] = val.strip()
#print(dit)
for i in dit.values():
    l.append(i)
s = random.choice(l)
t = input('What is the name of city of ' + s)
if dit[t] == s:

    print("correct")
else:
    print('wrong')






Gary = {
  "name": "Gary",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
Alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
Tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
students = (Gary, Alice, Tyler)
for i in Gary.values():
    print(i)
print()
for i in Alice.values():
    print(i)
print()
for i in Tyler.values():
    print(i)

print()

num = (1,2,3)
def average(numbers):
     total = float(sum(numbers))
     average = total / len(numbers)
     return average

print('Average of list is:', average(num))


def get_average(di):
    for i,k in di.items():
        homework = list()
        quizzes = list()
        tests = list()
        count = 0
        su = 0
        if i == 'homework':
            for s in k:
                homework.append(s)
                homework2 = sum(homework) / len(homework)

        elif i == 'quizzes':
            for s in k:
                quizzes.append(s)
                quizzes2 = sum(quizzes) / len(quizzes)
        elif i == 'tests':
            for s in k:
                tests.append(s)
                tests2 = sum(tests) / len(tests)
    avg = (homework2 * .10) + (quizzes2 * .30) + (tests2 * .60)
    return avg
print('Alice\'s average is' , get_average(Alice))






#problem

students = (Gary, Alice, Tyler)
def get_class_average(students):
    results = list()
    results.append(get_average(Gary))
    results.append(get_average(Alice))
    results.append(get_average(Tyler))
    avg = average(results)
    return avg
print('class average is', get_class_average(students))






