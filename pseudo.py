# Pseudo Quote Generator (Rus version w/ english comments)
# You can download Russian version with russian comments and English version with English comments from my github account (under development)

# This code works on Linux OS (Arch Linux)

# Repo Link: https://github.com/OnePixeLBoiii/SomeGenMechanics
# Author: OnePixeLBoiii

# Commentary: This program will not work without these files: "part1.txt", "part2.txt", "part3.txt".
# Also, you can customize these files, or add new files.

# Version : 0.0.1
# Date : 13-08-2020
# License: GNU License

# Code starts here

# Import "Random" Module
import random
# Open files with quotes
f1 = open('part1.txt')
f2 = open('part2.txt')
f3 = open('part3.txt')

#Get only 1 line
lines_f_f_1 = f1.read().splitlines()
# Random string from f1
line1 = random.choice(lines_f_f_1)

#Get only 1 line
lines_f_f_2 = f2.read().splitlines()
# Random string from f2
line2 = random.choice(lines_f_f_2)

#Get only 1 line
lines_f_f_3 = f3.read().splitlines()
# Random string from f3
line3 = random.choice(lines_f_f_3)

# Output
print("Цитата дня:")
print(line1, line2, line3)

# Code ends here
