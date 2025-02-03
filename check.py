#*********************************************
#1.BINARY TO ANY
# A.Binary to hexadecimal
# def binary_to_hexadecimal(binary_num):
#     # Check if the input contains only '0' and '1'
#     if not all(char in '01' for char in binary_num):
#         return "Invalid binary number! Please enter only 0s and 1s."
#     decimal_num=int(binary_num, 2)
#     hexal_num="{:x}".format(decimal_num)
#     hexal_num=list(hexal_num)
#     for i in range(len(hexal_num)):
#         if not hexal_num[i].isnumeric():
#             hexal_num[i]=hexal_num[i].upper()
#     hexal_num=''.join(hexal_num)
#     return hexal_num
# binary_num = input("Enter a binary number: ")
# hexal_num = binary_to_hexadecimal(binary_num)
# print(f"hexadecimal equivalent: {hexal_num}")

# B.Binary to octal
# def binary_to_octal(binary_num):
#     # Check if the input contains only '0' and '1'
#     if not all(char in '01' for char in binary_num):
#         return "Invalid binary number! Please enter only 0s and 1s."
    
#     decimal_num=int(binary_num, 2)
#     octal_num="{:o}".format(decimal_num)
#     return octal_num
# binary_num = input("Enter a binary number: ")
# octal_num = binary_to_octal(binary_num)
# print(f"octal equivalent: {octal_num}")

# C.Binary to decimal 
# def binary_to_decimal(binary_num):
#     # Check if the input contains only '0' and '1'
#     if not all(char in '01' for char in binary_num):
#         return "Invalid binary number! Please enter only 0s and 1s."

n=int(input())
alpha=input()
word=input()
if all(char in word for char in alpha):
    print("YES")
else:
    print("NO")
#     return int(binary_num, 2)
# # Example usage
# binary_num = input("Enter a binary number: ")
# decimal_num = binary_to_decimal(binary_num)
# print(f"Decimal equivalent: {decimal_num}")

#2.HEXADECIMAL TO ANY
#A.Hexadecimal to decimal
# def hexadecimal_to_decimal(decimal_num):
#     # Check if the input contains only '0-F'
#     decimal_num=str(decimal_num)
#     if not all(char in '0123456789ABCDEFabcdef' for char in decimal_num):
#         return "Invalid hexadecimal number! Please enter only include 0-F digits."
#     return int(decimal_num, 16)
# hexa_num = input("Enter a octal number: ")
# decimal_num = hexadecimal_to_decimal(hexa_num)
# print(f"Decimal equivalent: {decimal_num}")

#B.Hexadecimal to binary
# def hexadecimal_to_binary(hexal_num):
#     # Check if the input contains only '0-F'
#     hexal_num=str(hexal_num)
#     if not all(char in '0123456789ABCDEFabcdef' for char in hexal_num):
#         return "Invalid hexadecimal number! Please enter only include 0-F digits."
#     decimal_num=int(hexal_num, 16)
#     binary_num= "{:b}".format(decimal_num)
#     return binary_num
# hexa_num = input("Enter a hexadecimal number: ")
# binary_num = hexadecimal_to_binary(hexa_num)
# print(f"Decimal equivalent: {binary_num}")

# C. Hexadecimal to octal
# def hexadecimal_to_binary(hexal_num):
#     # Check if the input contains only '0-F'
#     hexal_num=str(hexal_num)
#     if not all(char in '0123456789ABCDEFabcdef' for char in hexal_num):
#         return "Invalid hexadecimal number! Please enter only include 0-F digits."
#     decimal_num=int(hexal_num, 16)
#     octal_num= "{:o}".format(decimal_num)
#     return octal_num
# hexa_num = input("Enter a hexadecimal number: ")
# octal_num = hexadecimal_to_binary(hexa_num)
# print(f"Decimal equivalent: {octal_num}")

#3.OCTAL TO ANY
#A. Octal to decimal
# def octal_to_decimal(octal_num):
#     # Check if the input contains only '0-7'
#     if not all(char in '01234567' for char in octal_num):
#         return "Invalid octal number! Please enter only include 0-8 digits."
#     return int(octal_num, 8)
# octal_num = input("Enter a octal number: ")
# decimal_num = octal_to_decimal(octal_num)
# print(f"Decimal equivalent: {decimal_num}")

# B. Octal to binary
# def octal_to_binary(octal_num):
#     # Check if the input contains only '0-8'
#     if not all(char in '01234567' for char in octal_num):
#         return "Invalid octal number! Please enter only include 0-7 digits."
#     decimal_num=int(octal_num, 8)
#     binary= "{:b}".format(decimal_num)
#     return binary
# octal_num = input("Enter a octal number: ")
# binary_num = octal_to_binary(octal_num)
# print(f"binary equivalent: {binary_num}")

# C. Octal to hexadecimal
# def octal_to_hexadecimal(octal_num):
#     # Check if the input contains only '0-8'
#     if not all(char in '01234567' for char in octal_num):
#         return "Invalid octal number! Please enter only include 0-7 digits."
#     decimal_num=int(octal_num, 8)
#     hexal_num="{:x}".format(decimal_num)
#     hexal_num=list(hexal_num)
#     for i in range(len(hexal_num)):
#         if not hexal_num[i].isnumeric():
#             hexal_num[i]=hexal_num[i].upper()
#     hexal_num=''.join(hexal_num)
#     return hexal_num
# octal_num = input("Enter a octal number: ")
# hexal_num = octal_to_hexadecimal(octal_num)
# print(f"Hexadecimal equivalent: {hexal_num}")

