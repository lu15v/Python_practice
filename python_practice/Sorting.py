import csv


def bubblesort(list):
    for word in range(len(list)-1, 0, -1):
        for i in range(word):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

file = open('words.csv', 'r')
reader = csv.reader(file)
for word in reader:
    print(word)
