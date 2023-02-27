# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:07:58 2023

@author: William Denny
"""
from numpy import argsort
import matplotlib.pyplot as plt

# format the file to be read
# Task 1:
paper_dict = {}
with open('SciencePaper.txt', 'r',errors = 'ignore') as file:
    for line in file:
        config = line.upper().replace(',','').replace('"','').replace('.','')\
        .replace('~', '').replace('(','').replace(')','').replace('?','')\
        .replace('-','').split()
        for word in config:
            try:
                paper_dict[word] += 1
            except:
                paper_dict[word] = 1

print('There are', len(paper_dict),'unique words in the file')

# Task 2:
keys = list(paper_dict.keys())
values = list(paper_dict.values())
sorted_val_ind = argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_val_ind}

freq_words = list(sorted_dict.keys())

print('The 10 most frequent words are:')
count = 1
while count < 11:
    print(freq_words[len(freq_words) - count])
    count += 1

# Task 3:
print('Summerfelt appears', paper_dict['SUMMERFELT'], 'times')
print('wastewater appears', paper_dict['WASTEWATER'], 'times')
print('greenhouse appears', paper_dict['GREENHOUSE'], 'times')
print('salmon appears', paper_dict['SALMON'], 'times')

# Task 4:
flip_dict = {}
for word,count in paper_dict.items():
    try:
        flip_dict[count].append(word)
    except:
        flip_dict[count] = [word]

print('The words that appear only once are:', flip_dict[1],'\n')
print('The words that appear only twice are:', flip_dict[2],'\n')
print('The words that appear only 5 times are:', flip_dict[5],'\n')
print('The words that appear only 10 times are:', flip_dict[10],'\n')

#task 5:
avg_len = [sum([len(word) for word in value]) / len(value) for value in flip_dict.values()]
appearances = list(flip_dict.keys())
plt.bar(appearances, avg_len)

