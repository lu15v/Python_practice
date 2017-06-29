#A little program that reads a csv file and then orders the rows in ascending order
#Using the algorithm of bubblesort.

import csv


def bubblesort(list):
    for word in range(len(list)-1, 0, -1):
        for i in range(word):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

with open('words.csv') as i:
    reader = csv.reader(i, delimiter=',')
    iList = list(reader)[0]
    bubblesort(iList)
    print(iList)
