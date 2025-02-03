from django.shortcuts import render

# Create your views here.
def select(request):
    return render(request,'select.html')
def number(request):
    if request.method=='POST':
        action=request.POST.get("action")
        if action=='binary':
            value=int(request.POST['decimal'])
            message= "{:b}".format(value)#changes to binary number
        elif action=='octal':
            value=int(request.POST['decimal'])
            message= "{:o}".format(value)#changes to octal number
        elif action=='hexadecimal':
            value=int(request.POST['decimal'])
            message= "{:x}".format(value)#changes to hexadecimal number
            message=list(message)
            for i in range(len(message)):
                if not message[i].isnumeric():
                    message[i]=message[i].upper()
            message=''.join(message)
        else:
            message="unknown"
        return render(request,"select.html",{"message":message})
    return render(request,"select.html")

def decimal_to_binary(value):
    value=int(value)
    message= "{:b}".format(value)#changes to binary number
    return message
def decimal_to_octal(value):
    value=int(value)
    message= "{:o}".format(value)#changes to octal number
    return message
def decimal_to_hexadecimal(value):
    value=int(value)
    message= "{:x}".format(value)#changes to hexadecimal number
    message=list(message)
    for i in range(len(message)):
        if not message[i].isnumeric():
            message[i]=message[i].upper()
    message=''.join(message)
    return message
def binary_to_decimal(binary_num):
    # Check if the input contains only '0' and '1'
    if not all(char in '01' for char in binary_num):
        return "Invalid binary number! Please enter only 0s and 1s."
    
    return int(binary_num, 2)
def binary_to_octal(binary_num):
    # Check if the input contains only '0' and '1'
    if not all(char in '01' for char in binary_num):
        return "Invalid binary number! Please enter only 0s and 1s."
    
    decimal_num=int(binary_num, 2)
    octal_num="{:o}".format(decimal_num)
    return octal_num
def binary_to_hexadecimal(binary_num):
    # Check if the input contains only '0' and '1'
    if not all(char in '01' for char in binary_num):
        return "Invalid binary number! Please enter only 0s and 1s."
    decimal_num=int(binary_num, 2)
    decimal_num=str(decimal_num)
    hexal_num=decimal_to_hexadecimal(decimal_num)
    return hexal_num
def octal_to_decimal(octal_num):
    # Check if the input contains only '0-7'
    if not all(char in '01234567' for char in octal_num):
        return "Invalid octal number! Please enter only include 0-8 digits."
    return int(octal_num, 8)
def octal_to_binary(octal_num):
    # Check if the input contains only '0-8'
    if not all(char in '01234567' for char in octal_num):
        return "Invalid octal number! Please enter only include 0-7 digits."
    decimal_num=int(octal_num, 8)
    binary= "{:b}".format(decimal_num)
    return binary
def octal_to_hexadecimal(octal_num):
    # Check if the input contains only '0-8'
    if not all(char in '01234567' for char in octal_num):
        return "Invalid octal number! Please enter only include 0-7 digits."
    decimal_num=int(octal_num, 8)
    decimal_num=str(decimal_num)
    hexal_num=decimal_to_hexadecimal(decimal_num)
    return hexal_num
def hexadecimal_to_decimal(decimal_num):
    # Check if the input contains only '0-F'
    decimal_num=str(decimal_num)
    if not all(char in '0123456789ABCDEFabcdef' for char in decimal_num):
        return "Invalid hexadecimal number! Please enter only include 0-F digits."
    return int(decimal_num, 16)
def hexadecimal_to_binary(hexal_num):
    # Check if the input contains only '0-F'
    hexal_num=str(hexal_num)
    if not all(char in '0123456789ABCDEFabcdef' for char in hexal_num):
        return "Invalid hexadecimal number! Please enter only include 0-F digits."
    decimal_num=int(hexal_num, 16)
    binary_num= "{:b}".format(decimal_num)
    return binary_num
def hexadecimal_to_octal(hexal_num):
    # Check if the input contains only '0-F'
    hexal_num=str(hexal_num)
    if not all(char in '0123456789ABCDEFabcdef' for char in hexal_num):
        return "Invalid hexadecimal number! Please enter only include 0-F digits."
    decimal_num=int(hexal_num, 16)
    octal_num= "{:o}".format(decimal_num)
    return octal_num
def decimal(request):#operation of decimal number
    # Get the selected values from both dropdowns
    num2 = request.POST.get('number-system-2')
    value= request.POST.get('value')
    if num2=="binary":
        if(value.isnumeric()):
            number= decimal_to_binary(value)
            return number
    # You can now perform any logic with the selected values
        return "Invalid input Enter only numbers!"
    if num2=="octal":
        if(value.isnumeric()):
            number= decimal_to_octal(value)
            return number
        return "Invalid input Enter only numbers!"
    if num2=="hexadecimal":
        if(value.isnumeric()):
            number= decimal_to_hexadecimal(value)
            return number
        return "Invalid input Enter only numbers!"
    if(value.isnumeric()):
        return value
    return "Invalid input Enter only numbers!"
def binary(request):#operation of decimal number
    # Get the selected values from both dropdowns
    num2 = request.POST.get('number-system-2')
    value= request.POST.get('value')
    if num2=="decimal":
        number=binary_to_decimal(value)
        return number
    if num2=="octal":
        number=binary_to_octal(value)
        return number
    if num2=="hexadecimal":
       number=binary_to_hexadecimal(value)
       return number
    if not all(char in '01' for char in value):
        return "Invalid binary number! Please enter only 0s and 1s."
    return value
def octal(request):
    num2 = request.POST.get('number-system-2')
    value= request.POST.get('value')
    if num2=="decimal":
        number=octal_to_decimal(value)
        return number
    if num2=="binary":
        number=octal_to_binary(value)
        return number
    if num2=="hexadecimal":
       number=octal_to_hexadecimal(value)
       return number
    if not all(char in '01234567' for char in value):
        return "Invalid octal number! Please enter only include 0-7 digits."
    return value
def hexadecimal(request):
    num2 = request.POST.get('number-system-2')
    value= request.POST.get('value')
    if num2=="decimal":
        number=hexadecimal_to_decimal(value)
        return number
    if num2=="binary":
        number=hexadecimal_to_binary(value)
        return number
    if num2=="octal":
        number=hexadecimal_to_octal(value)
        return number
    if not all(char in '0123456789ABCDEFabcdef' for char in value):
        return "Invalid hexadecimal number! Please enter only include 0-F digits."
    message=list(value)
    for i in range(len(message)):
        if not message[i].isnumeric():
            message[i]=message[i].upper()
    message=''.join(message)
    return message
def numbers(request):
    if request.method == 'POST':
       num1 = request.POST.get('number-system-1')
       num2 = request.POST.get('number-system-2')
       if num1=="decimal": 
            return render(request,'select.html',{'number':decimal(request),'from_system':num1,'to_system':num2})
       if num1=="binary":
           return render(request,'select.html',{'number':binary(request),'from_system':num1,'to_system':num2})
       if num1=="octal":
           return render(request,'select.html',{'number':octal(request),'from_system':num1,'to_system':num2})
       if num1=="hexadecimal":
           return render(request,'select.html',{'number':hexadecimal(request),'from_system':num1,'to_system':num2})