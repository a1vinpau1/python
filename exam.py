# # pattern
# rows_num = 5
# for i in range(1, rows_num+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# # palindrome
# num = int(input("Enter a number: "))
# str_num = str(num)
# str_rev_num = str_num[::-1]
# rev_num = int(str_rev_num)
# if num == rev_num:
#     print("The number is palindrome.")
# else:
#     print("The number is not palindrome.")


# num_1 = input("Enter a number to reverse : ") 
# print("Reverse of the number :", num_1[::-1])


# num = 5
# for i in range(1, 11):
#     value = num * i
#     print(num, "*", i, "=", value)


# rows = 5
# for i in range(1, rows+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# import numpy as np
# import matplotlib.pyplot as plt
# t = np.linspace(0,2*np.pi, 1000)
# x = 16*np.sin(t)**3
# y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
# plt.plot(x, y, color='red')
# plt.axis('equal')
# plt.axis('off')
# plt.fill(x, y, color='red')

# encoded_string ="49462049204b4e4f57204c4f56452049542049532042454341555345204f4620594f55"
# message = bytes.fromhex(encoded_string).decode('utf-8')

# plt.text(0, -20, message, color='blue', fontsize=17, fontweight='bold', ha='center')

# plt.show()



# rows = 4
# for i in range(rows):
#     for j in range(1, rows+1):
#         print("*", end=" ")
#     print()




    

# def check_prime(num):
#     if num == 1:
#         return False
#     elif num == 2 or num == 3:
#         return True
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True


# def next_prime(num):
#     new = False
#     while not new:
#         num += 1
#         new = check_prime(num)
#     if new:
#         print(num)


# num = int(input("Number ?= "))
# result = check_prime(num)


# if result:
#     print("Prime")
#     next_prime(num)    
# else:
#     print("Not Prime")




s = 'caberqiitefg'
vowels = 'aeiou'
k = 5
num_vowels = 0

for i in range(k):
    if s[i] in vowels:
        num_vowels +=1 
print(num_vowels)