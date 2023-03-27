print("***********************************************")
print("*** Welcome to your calculator              ***\n*** please press a number between 1 and 6 ? ***")
print("***********************************************")
number_input =input("press 1 for addition \npress 2 for subtracring \npress 3 for multiplying \npress 4 for dividing \npress 5 for remainder \npress 6 for exponentiation \n")
num_1 = int(input("Enter the first number \n"))
num_2 = int(input("Enter the second number \n"))

if number_input == "1":
    print("The sum is " + str(num_1 + num_2))
elif number_input == "2":
    print("The difference is " + str(num_1 - num_2))
elif number_input == "3":
    print("The product is " + str(num_1 * num_2))
elif number_input == "4":
    print("The division is " + str(num_1 / num_2))
elif number_input == "5":
    print("The remainder is " + str(num_1 % num_2))
elif number_input == "6":
    print("The exponent is " + str(num_1 ** num_2))
else:
    print("sorry, operation not found... \nplease choose operations between 1 and 6!!!")