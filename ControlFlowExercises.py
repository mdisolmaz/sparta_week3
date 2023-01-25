#print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x1 = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x1[0:5])


#print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x2 = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
# for i in x2:
#     if i % 2==0:
#         print(i)
#     else:
#         pass

#print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x3 = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
# for i in x3[0:5]:
#     if i % 2==0:
#         print(i)
#     else:
#         pass

# -------------------------------------------------------------------------------------- #

#print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names1 = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

# first_letters = [name.split()[0][0] for name in names1]
# print(first_letters)




#print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names2 = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

# first_spaces=[]
# for name in names2:
#     first_spaces.append(name.index(" "))
# print(first_spaces)



#print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names3 = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
# first_last_letters = [name[0] + name.split()[-1][-1] for name in names3]
# print(first_last_letters)


# -------------------------------------------------------------------------------------- #

#print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

# A3a:
new_list = []
for x in list_of_lists:
    if len(set(x)) == len(x):
        new_list.append(x)
print(new_list)


# result = [lst for lst in list_of_lists if len(set(lst)) == len(lst)]
# print(result)

# -------------------------------------------------------------------------------------- #

#print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
while True:
    user_input = input("Please enter a number greater than 100: ")
    if int(user_input) >= 100:
        print(" you have entered : ", user_input, " thank you ")
        break
    else:
        print("Invalid input, please enter a valid number greater than 100")


#print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

while True:
    user_input = input("Please enter a number greater than 100: ")
    if int(user_input) >= 100:
        is_prime = True
        for i in range(2, int(user_input)):
            if int(user_input) % i == 0:
                is_prime = False
        if is_prime:
            print("You entered: ", user_input," It is prime number")
        else:
            print("You entered: ", user_input," It is not a prime number")
        break
    else:
        print("Invalid input, please enter a valid number greater than 100")






