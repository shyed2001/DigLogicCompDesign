# def check_sign(value):
#     if value >= 0:
#         S = 0  # positive number
#     else:
#         S = 1  # negative number
#     return S

# # Prompt user for input
# value = float(input("Enter a float value: "))

# # Check the sign bit
# sign_bit = check_sign(value)
# if sign_bit==1:
#   print("The value of the number is negative, Sign bit (S): S= ", sign_bit)
  
# else:
#   print("The value of the number is positive, Sign bit (S): S= ", sign_bit)
  

# In this code, the input() function is used to prompt the user to enter a float value. The entered value is then converted to a float using float() function. The check_sign() function is called with the provided value to determine the sign bit (S), which is then printed to the console.

# Now, when you run the code, it will ask you to enter a float value, and based on the input, it will determine the sign bit and display it on the screen.

# def check_sign(value):
#     if value >= 0:
#         S = 0  # positive number
#     else:
#         S = 1  # negative number
#     return S

# def check_mantissa(value, i):
#     m = value / i  # calculate m
#     M = m - 1  # calculate M as m-1
#     return M

# # Prompt user for input
# value = float(input("Enter a float value: "))

# # Check the sign bit
# sign_bit = check_sign(value)

# # Initialize Mantissa (M) with a default value
# M = 0

# # Check if value falls between any two numbers
# for n in range(11):  # Check up to 2^10 = 1024
#     i = 2 ** n
#     if i < value < (i + 1):
#         M = check_mantissa(value, i)
#         break

# # Print the sign bit and mantissa
# print("Sign bit (S):", sign_bit)
# print("Mantissa (M):", M)

# import tkinter as tk
# import sys

# # Prompt user for input
# value = float(input("Enter a float value: "))

# # Define the range of numbers (powers of 2)
# # number_range = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
# number_range = []

# for i in range(12):
#     number_range.append(2 ** i)
# # Initialize variables
# print(number_range)


# i = 1

# # Check if value falls between any two numbers
# for num in number_range:
#     if i < value < num:
#         break
#     i = num
# print('value is between', i, 'and', num)

# # Calculate m
# m = value / i
# M = 0 # Initialize mantissa (M) with a default value
# # Print i and m
# print(" Dividing the value:", value) 
# print("by", i)
# print("We get m=1.M:", m)
# M = m-1
# print(" So Decimal value of Mantissa (M):", M)

# decimal_value = M
# binary_mantissa = ""

# while decimal_value != 0:
#     decimal_value *= 2
#     print(decimal_value)
#     integer_part = int(decimal_value)
#     binary_mantissa += str(integer_part)
#     decimal_value -= integer_part



# E=0
# print(" Binary value of M is = ",binary_mantissa)
# print("For Single Precision 32 bit, Exponent (E) = 0<E<255")
# print("For Double Precision (double)  64 bit, Exponent (E) = 0<E<2047")
# print("value=(−1)S×1.M×2E−127 , 0<E<255")
# print("value = (-1)^sign * (1 + mantissa) * 2^(exponent - bias)")

#####################################################################################################################################################################################


# import tkinter as tk
# import sys

# # Redirect stdout to a custom Text widget
# class OutputRedirector:
#     def __init__(self, text_widget):
#         self.text_widget = text_widget

#     def write(self, text):
#         self.text_widget.insert("end", text)
#         self.text_widget.see("end")  # Scroll to the end

# # Create a new window
# window = tk.Tk()
# window.title("Python Output")

# # Create a Text widget to display the output
# output_text = tk.Text(window, height=20, width=80)
# output_text.pack()

# # Redirect stdout to the Text widget
# sys.stdout = OutputRedirector(output_text)

# # Function to handle button click
# def calculate():
#     # Get the value entered by the user
#     value = float(value_entry.get())
     
#     # Define the range of numbers (powers of 2)
#     number_range = []

#     for i in range(12):
#         number_range.append(2 ** i)

#     # Initialize variables
#     i = 1

#     # Check if value falls between any two numbers
#     for num in number_range:
#         if i < value < num:
#             break
#         i = num

#     # Calculate m
#     m = value / i
#     M = m - 1

#     # Print i, m, and M
#     print("Value is between", i, "and", num)
#     print("Dividing the value:", value)
#     print("by", i)
#     print("We get m=1.M:", m)
#     print("So Decimal value of Mantissa (M):", M)

#     decimal_value = M
#     binary_mantissa = ""
#     counter = 0
#     while decimal_value != 0:
#         decimal_value *= 2
#         if counter < 5:
#              print(decimal_value)
#              counter+=1
#         integer_part = int(decimal_value)
#         binary_mantissa += str(integer_part)
#         decimal_value -= integer_part

#     # Print binary representation of M
#     print("Binary value of M is:", binary_mantissa)

#     # Rest of the code...
    
# # Create an entry field for the float value
# value_label = tk.Label(window, text="Enter a float value:")
# value_label.pack()

# value_entry = tk.Entry(window)
# value_entry.pack()

# # Create a button to trigger the calculation
# calculate_button = tk.Button(window, text="Calculate", command=calculate)
# calculate_button.pack()

# # Run the event loop to display the window
# window.mainloop()


import tkinter as tk
import sys

# Redirect stdout to a custom Text widget
class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)
        self.text_widget.see("end")  # Scroll to the end

# Create a new window
window = tk.Tk()
window.title("Python Output")

# Create a Text widget to display the output
output_text = tk.Text(window, height=30, width=100)
output_text.pack()

# Redirect stdout to the Text widget
sys.stdout = OutputRedirector(output_text)

# Function to handle button click
def calculate():
    # Get the value entered by the user
    value = float(value_entry.get())

    def check_sign(value):
        if value >= 0:
            S = 0  # positive number
        else:
            S = 1  # negative number
        return S

    # Check the sign bit
    sign_bit = check_sign(value)
    if sign_bit == 1:
        print("The value of the number is negative, Sign bit (S): S =", sign_bit)
    else:
        print("The value of the number is positive, Sign bit (S): S =", sign_bit)

    value = -1*value if sign_bit == 1 else value
    
    # Define the range of numbers (powers of 2)
    number_range = []

    for i in range(12):
        number_range.append(2 ** i)

    # Initialize variables
    i = 1

    # Check if value falls between any two numbers
    for num in number_range:
        if i < value < num:
            break
        i = num

    # Calculate m
    m = value / i
    M = m - 1

    # Print i, m, and M
    print("Value is between", i, "and", num)
    print("Dividing the value:", value)
    print("by", i)
    print("We get m=1.M:", m)
    print("So Decimal value of Mantissa (M):", M)

    decimal_value = M
    binary_mantissa = ""
    counter = 0
    while decimal_value != 0:
        decimal_value *= 2
        if counter < 5:
            print(decimal_value)
            counter += 1
        integer_part = int(decimal_value)
        binary_mantissa += str(integer_part)
        decimal_value -= integer_part

    # Print binary representation of M
    
    print("For Single Precision take 23 bit only")

    print("Binary value of M is:", binary_mantissa)
    
    E=0
   
    print("For Single Precision 32 bit, Exponent (E) = 0<E<255")

    print("value=(−1)^S×1.M×2^E−127 , 0<E<255")
    print("value = (-1)^sign * (1 + mantissa) * 2^(exponent - bias or biasing exponent)")
    
    import math

    k = math.log2(i)
    print(int(k))
    
    E32=int(k)+127
    print("For Single precision E-127 = ",int(k))
    print("For", i,"= 2^",int(k))
    print("For Single precision E in decimal is ",E32)
    
    print("For Single precision E in binary is ")
    binaryE32 = bin(E32)
    binaryE32 = binaryE32[2:]
    print(binaryE32)
    
    print("For Double Precision (double) 64 bit, Exponent (E) = 0<E<2047")
    
    E64=int(k)+1023
    print("For Single precision E-1023= ",int(k))
    print("For Double precision E in decimal is ",E64)
    print("For Double precision E in binary is ")
    binaryE64 = bin(E64)
    binaryE64 = binaryE64[2:]
    print(binaryE64)  
    print(" For Double precision Binary value of M is = ",binary_mantissa)
    print("For Double Precision take 52 bit only")
    print("For Single Precision ", sign_bit, binaryE32, binary_mantissa)
    print("For Double Precision ", sign_bit, binaryE64, binary_mantissa)
    
    
# Create an entry field for the float value
value_label = tk.Label(window, text="Enter a float value:")
value_label.pack()

value_entry = tk.Entry(window)
value_entry.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Run the event loop to display the window
window.mainloop()
