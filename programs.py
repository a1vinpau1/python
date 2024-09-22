# list and tuple conversion
# x = ("apple", "banana", "kiwi")
# y = list(x)
# y.append("orange")
# y.insert(1, "cherry")
# x = tuple(y)
# print(x, y)


# write a Python program to swap first and last element of the list
# list_1 = [1, 2, 3, 4, 5, 6]
# last_element = list_1.pop()
# first_element = list_1.pop(0)
# list_1.insert(0, last_element)
# last_position = len(list_1)
# list_1.insert(last_position, first_element)
# print(list_1)
# or
# list_1[0], list_1[-1] = list_1[-1], list_1[0]
# print(list_1)


# write a python program  detect a number is even or odd
# number_entered = int(input("Enter a number: "))
# if number_entered  % 2 == 0:
#     print(number_entered, "is an even number.")
# else:
#     print(number_entered, "is an odd number.")


# write  a python program to check whether an alphabet is a vowel or consonant
# vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
# entered_letter = input("Enter an alphabet: ")
# if entered_letter in vowels:
#     print(entered_letter, "is a vowel.")
# else:
#     print(entered_letter, "is not a vowel.")


# write  a python program  to sum two integers. However, if the sum is between 15 and 20 it will return 20
# number_1, number_2 = int(input("Enter the first number: ")), int(input("Enter the second number: "))
# sum = number_1 + number_2
# if sum > 15 and sum <= 20:
#     sum = 20
# print("Sum =", sum)


# Write a Python program to display the first and last colors from the following list
# color_list = ("Blue", "Green", "Black", "White", "Orange")
# first_element = color_list[0]
# last_element = color_list[-1]
# print(color_list)
# print(first_element, "is the first color.", last_element, "is the last color.")


# Write a Python program to append a list to the second list
# list_1 = [1, 2, 3, 4, 5]
# list_2 = [6, 7, 8, 9, 10]
# for element in list_2:
#     list_1.append(element)
# print(list_1)


# Write a Python program to check if a list is empty or not
# list_1 = [1, 2]
# if len(list_1) == 0:
#     print("List is empty.")
# else:
#     print(list_1, "is not empty.")


# find largest among 3 numbers
# num_1, num_2, num_3 = int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(input("Enter the third number: "))
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1, "is the largest number.")
# elif num_2 > num_1 and num_2 > num_3:
#     print(num_2, "is the largest number.")
# else:
#     print(num_3, "is the largest number.")


# Reversing a number
# num = int(input("Enter a number: "))
# rev = 0
# while 0 < num:
#     temp = num % 10
#     rev = rev * 10 + temp
#     num = num // 10
# print(rev)


# prime number
# num = int(input("Enter a number: "))
# is_prime = True
# for value in range(2, num):
#     if num % value == 0:
#         is_prime = False
# if is_prime:
#     print("It is a prime number.")
# else:
#     print("It is not a prime number.")


# pattern
# *
# **
# ***
# ****
# *****
# i = 1
# while i <= 5:
#     print("*" * i)
#     i+=1


# pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()
    
    
# pattern
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(1, rows_num+1):
#         print(j, end=" ")
#     print()


# pattern
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(1, rows_num+1):
#         print(i, end=" ")
#     print()


# pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# pattern
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(i, rows_num+1):
#         print(i, end=" ")
#     print()


# pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# rows_num = 5
# for i in range(rows_num, 0, -1):
#     for j in range(i):
#         print(i, end= " ")
#     print()


# pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(i):
#         print("*", end = " ")
#     print()


# pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()


# pattern
#    *
#   * *
#  * * *
# * * * *
# rows_num = 4
# for i in range(1, rows_num+1):
#     print(" "* (rows_num-i), end = "")
#     for j in range(i):
#         print("*", end = " ")
#     print()


# pattern
# A B C D E
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y
# rows_num = 5
# ascii_num = 65
# inc_num = 0
# for i in range(rows_num):
#     for j in range(rows_num):
#         print(chr(ascii_num + inc_num), end = " ")
#         inc_num += 1
#     print()


# pattern
# A A A A A
# B B B B B 
# C C C C C
# D D D D D
# E E E E E
# rows_num = 5
# ascii_num = 65
# inc_num = 0
# for i in range(rows_num):
#     for j in range(rows_num):
#         print(chr(ascii_num + inc_num), end = " ")
#     inc_num += 1
#     print()


# pattern
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# rows_num = 5
# ascii_num = 65
# for i in range(rows_num):
#     for j in range(rows_num):
#         print(chr(ascii_num + j), end = " ")
#     print()


# pattern
# A
# A B
# A B C 
# A B C D
# A B C D E
# rows_num = 5
# ascii_num = 65
# for i in range(rows_num):
#     for j in range(i+1):
#         print(chr(ascii_num + j), end = " ")
#     print()


# factorial using function
# input_num = int(input("Enter a number: "))
# def fact(input):
#     factorial_result = 1
#     for i in range(1, input+1):
#         factorial_result *= i
#     return factorial_result
# output_result = fact(input_num)
# print("Factorial =", output_result)


# pattern
# * * * *
#  * * *
#   * *
#    *
# rows_num = 4
# for i in range(rows_num, 0, -1):
#     print(" "* (rows_num-i), end = "")
#     for j in range(i):
#         print("*", end= " ")
#     print()


# pattern
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
# rows_num = 4
# for i in range(1, rows_num+1):
#     print(" "* (rows_num-i), end = "")
#     for j in range(i):
#         print("*", end = " ")
#     print()
# for i in range(rows_num-1, 0, -1):
#     print(" "* (rows_num-i), end = "")
#     for j in range(i):
#         print("*", end= " ")
#     print()


# anagram
# word_1 = input("Enter the first word: ").lower()
# word_2 = input("Enter the second word: ").lower()
# if len(word_1) == len(word_2):
#     if sorted(word_1) == sorted(word_2):
#         print("The word is anagram")
#     else:
#         print("The word is not anagram")
# else:
#     print("Length of both strings should be same.")


# Pattern
# 0
# 0  1
# 0  2  4
# 0  3  6  9
# 0  4  8  12  16
# 0  5  10  15  20  25
# rows_num = 6
# for i in range(rows_num):
#     if i != 0:
#         for j in range(0, i*i+1, i):
#             print(j, end="  ")
#         print()
#     else:
#         print(i, end="  ")
#         print()


# fibonacci
# first = 0 
# second = 1
# fib = int(input("Enter the length of the series: "))
# for i in range(fib):
#     third = first + second
#     print(first, end = " ")
#     first = second
#     second = third

